"""Read-only evidence audit for the first executable-retention publication.

Recalculate answers and costs without importing study code or calling a model.
Writes only the explicitly requested root review output.
"""
import argparse
import ast
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import zipfile


REVISION = "baf4d764cb4e571551a2b69d45751bb7f3281eaf"


def answer(case):
    """Integer-cent reconciliation from the written contract, not study oracle."""
    latest = {}
    for event in sorted(case["data"]["events"], key=lambda e: e["revision"]):
        latest[event["id"]] = event
    effects = defaultdict(int)
    cutoff = case["request"]["cutoff"]
    for event in latest.values():
        if event["status"] == "posted" and event["date"] <= cutoff:
            cents = int(event["amount"].replace(".", ""))
            effects[event["invoice_id"], event["currency"]] += (
                cents if event["kind"] == "refund" else -cents
            )
    rows, totals = [], defaultdict(int)
    for invoice in case["data"]["invoices"]:
        if (invoice["status"] != "open"
                or invoice["customer"] not in case["request"]["customers"]
                or invoice["due"] > cutoff):
            continue
        balance = int(invoice["amount"].replace(".", "")) + effects[
            invoice["id"], invoice["currency"]
        ]
        if balance > 0:
            rows.append(dict(invoice_id=invoice["id"], customer=invoice["customer"],
                             currency=invoice["currency"], outstanding_cents=balance))
            totals[invoice["currency"]] += balance
    rows.sort(key=lambda r: (r["customer"], r["currency"], r["invoice_id"]))
    return {"rows": rows, "totals": dict(totals)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    study = args.study.resolve()
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=study,
                                   text=True).strip() == REVISION
    assert not subprocess.check_output(["git", "status", "--porcelain"],
                                       cwd=study, text=True).strip()
    read = lambda name: json.loads((study / name).read_text())
    digest = lambda data: hashlib.sha256(data).hexdigest()
    manifest = {}
    for line in (study / "evidence/MANIFEST.sha256").read_text().splitlines():
        checksum, name = line.split(maxsplit=1)
        assert digest((study / name).read_bytes()) == checksum, name
        manifest[name] = checksum
    cases = read("evidence/evaluation-inputs.json")
    gold = [answer(c) for c in cases]
    assert gold == read("evidence/evaluation-gold.json")
    by_seed = {c["seed"]: answer(c) for c in cases}
    dev = read("evidence/development.json")
    assert [answer(x["input"]) for x in dev] == [x["expected"] for x in dev]
    checks = {}
    for path in (study / "evidence/checks").glob("*.json"):
        batch = json.loads(path.read_text())
        assert [r["output"] for r in batch["results"]] == [x["expected"] for x in dev]
        checks[path.stem] = batch
    contract = next(ast.literal_eval(node.value) for node in ast.parse(
        (study / "scripts/workload.py").read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "CONTRACT"
                                              for t in node.targets))
    lesson = (study / "evidence/lessons.md").read_text()
    prompts_checked = 0
    for path in (study / "evidence/calls").glob("*/request.json"):
        if not path.parent.name.startswith(("lessons-", "cache-")):
            continue
        request = json.loads(path.read_text())
        assert request["chat_template_kwargs"] == {"enable_thinking": False}
        assert request["max_tokens"] == 4096 and request["temperature"] == 0
        assert len(request["messages"]) == 2
        text = request["messages"][1]["content"]
        prefix = contract + "\nDevelopment checks available to you:\n"
        assert text.startswith(prefix)
        examples, end = json.JSONDecoder().raw_decode(text[len(prefix):])
        assert examples == dev
        tail = text[len(prefix) + end:]
        middle = "\nRetained procedural lessons (source not retained):\n" + lesson
        middle += "\nCurrent request and page interface parameters:\n"
        assert tail.startswith(middle)
        seed = int(path.parent.name.split("-")[1])
        case = next(c for c in cases if c["seed"] == seed)
        assert json.loads(tail[len(middle):]) == {
            "request": case["request"], "page_size": case["page_size"]
        }
        prompts_checked += 1
    assert prompts_checked == 9
    source = (study / "evidence/acquired.py").read_bytes()
    with zipfile.ZipFile(study / "evidence/acquisition-archive.zip") as archive:
        index = json.loads(archive.read("manifest.json"))
        assert archive.read(index["implementation"]) == source
    calls = {}
    generated_sources_matched = 0
    finish_reasons, fingerprints = Counter(), Counter()
    for directory in sorted((study / "evidence/calls").iterdir()):
        responses = [json.loads(p.read_text()) for p in directory.glob("response-*.json")]
        measurements = [json.loads(p.read_text()) for p in directory.glob("measurement-*.json")]
        calls[directory.name] = {
            "model_calls": 1, "transport_attempts": len(measurements),
            "unknown_usage_attempts": sum(not x["success"] for x in measurements),
            "prompt_tokens": sum(x["usage"]["prompt_tokens"] for x in responses),
            "completion_tokens": sum(x["usage"]["completion_tokens"] for x in responses),
            "cached_tokens": sum(x["usage"].get("prompt_tokens_details", {}).get("cached_tokens", 0)
                                 for x in responses),
            "model_wall_seconds": sum(x["wall_seconds"] for x in measurements),
        }
        for response in responses:
            finish_reasons[response["choices"][0]["finish_reason"]] += 1
            fingerprints[response["system_fingerprint"]] += 1
            candidate = study / "evidence/candidates" / (directory.name + ".py")
            if candidate.exists():
                content = response["choices"][0]["message"]["content"]
                blocks = re.findall(r"```(?:python)?\s*\n(.*?)```", content, re.S)
                assert candidate.read_text() == (max(blocks, key=len) if blocks else content)
                generated_sources_matched += 1
    assert generated_sources_matched == 10
    for name, artifact in [("lesson-construction", "lessons-original.md"),
                           ("lesson-repair", "lessons.md")]:
        content = read(f"evidence/calls/{name}/response-0.json")["choices"][0]["message"]["content"]
        assert (study / "evidence" / artifact).read_text() == content
    def aggregate(names):
        return {key: sum(calls[name][key] for name in names)
                for key in next(iter(calls.values()))}
    records = read("evidence/evaluation-records.json")
    assert len(records) == 32
    assert {(r["arm"], r["seed"]) for r in records} == {
        (arm, seed) for arm in ("ready", "archive", "lessons", "cache") for seed in by_seed
    }
    summary = read("results/summary.json")
    for r in records:
        assert not r["repair_name"] and r["initial_execution"] is None
        outputs = r["execution"]["results"]
        expected = by_seed[r["seed"]]
        assert outputs[-1]["output"] == expected and r["success"]
        if r["build_name"]:
            assert len(outputs) == 1
            build = read(f'evidence/builds/{r["build_name"]}.json')
            assert len(build) == 1 and not build[0]["failures"]
            candidate = (study / build[0]["source_path"]).read_bytes()
        else:
            assert [x["output"] for x in outputs[:-1]] == [x["expected"] for x in dev]
            candidate = source if r["arm"] != "cache" else (study / "evidence/cache.py").read_bytes()
        assert digest(candidate) == r["source_sha256"]
    arms = {}
    for arm in ("ready", "archive", "lessons", "cache"):
        rows = [r for r in records if r["arm"] == arm]
        tally = aggregate([name for name in calls if name.startswith(arm + "-")])
        check_reads = sum(len(r["api_calls"]) for name, batch in checks.items()
                          if name.startswith(arm + "-") for r in batch["results"])
        execution_reads = sum(len(out["api_calls"]) for r in rows for out in r["execution"]["results"])
        tally.update(requests=len(rows), successes=sum(r["success"] for r in rows),
                     wall_seconds=sum(r["wall_seconds"] for r in rows),
                     candidate_check_api_calls=check_reads, execution_api_calls=execution_reads,
                     current_api_calls=sum(len(r["execution"]["results"][-1]["api_calls"]) for r in rows))
        for key, value in tally.items():
            assert math.isclose(value, summary["arms"][arm][key], abs_tol=1e-8), (arm, key)
        tally["all_api_reads"] = check_reads + execution_reads
        arms[arm] = tally
    total = aggregate(calls)
    for key, value in total.items():
        assert math.isclose(value, summary["research_model_total"][key], abs_tol=1e-8), key
    selected = {}
    acquisition = calls["acquisition-compact-0"]
    acquisition_check = checks["acquisition-compact-0"]
    for arm, tally in arms.items():
        lesson_calls = ["lesson-construction", "lesson-repair"] if arm in ("lessons", "cache") else []
        lesson = aggregate(lesson_calls)
        selected[arm] = {
            "known_prompt_tokens": acquisition["prompt_tokens"] + lesson["prompt_tokens"] + tally["prompt_tokens"],
            "known_completion_tokens": acquisition["completion_tokens"] + lesson["completion_tokens"] + tally["completion_tokens"],
            "instrumented_wall_seconds": acquisition["model_wall_seconds"] + lesson["model_wall_seconds"]
                + acquisition_check["container_wall_seconds"] + tally["wall_seconds"],
            "api_calls": sum(len(x["api_calls"]) for x in acquisition_check["results"]) + tally["all_api_reads"],
        }
        for key, value in selected[arm].items():
            assert math.isclose(value, read("results/selected-deployment.json")[arm][key], abs_tol=1e-8)
    result = dict(reviewed_revision=REVISION, manifest_files_checked=len(manifest),
                  independently_scored_fresh_requests=len(gold), recorded_current_outcomes_checked=len(records),
                  nonempty_fresh_requests=sum(bool(x["rows"]) for x in gold),
                  candidate_check_batches=len(checks), arms=arms, selected_deployment=selected,
                  reconstruction_prompts_checked=prompts_checked,
                  generated_sources_matched_to_raw_responses=generated_sources_matched,
                  structured_model_ledger=total, finish_reasons=dict(finish_reasons),
                  backend_fingerprints=dict(fingerprints),
                  manifest_sha256=digest((study / "evidence/MANIFEST.sha256").read_bytes()),
                  limits="Saved-evidence rescore and accounting only; no model calls, source execution or timing replication. Capability probes and uninstrumented overhead excluded from structured ledger.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"Verified {len(manifest)} manifest entries, 32 current outcomes, development checks, source identities and raw-response costs.")


if __name__ == "__main__":
    main()
