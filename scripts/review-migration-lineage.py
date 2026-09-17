"""Read-only root audit of the two pinned publications; no model calls.

Run with uv run python scripts/review-migration-lineage.py [ancillary directory].
Writes JSON to stdout. SQL replay is a separate, inspected ancillary checker.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "ancillary-studies"


def read(path):
    return json.loads(path.read_text())


def enc(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def tokens(call):
    u = call["response"]["usage"]
    assert u["total_tokens"] == u["prompt_tokens"] + u["completion_tokens"]
    return u["total_tokens"]


def parsed(call):
    text = call["response"]["choices"][0]["message"]["content"].strip()
    return json.loads(text.removeprefix("```json").removeprefix("```").removesuffix("```").strip())


def pin(repo, revision):
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip() == revision
    return revision


def migration():
    repo = BASE / "procedural-memory-migration"
    revision = pin(repo, "5a670d355491a853e32779260bfe73ea09f02f45")
    manifest = read(repo / "artifacts/evidence-manifest.json")
    for entry in manifest["files"]:
        data = (repo / entry["path"]).read_bytes()
        assert len(data) == entry["bytes"] and sha(data) == entry["sha256"], entry["path"]
    calls = {}
    outcomes = {}
    for path in (repo / "runs").rglob("*.json"):
        data = read(path)
        if "request" in data:
            calls[path] = data
        if path.name == "outcome.json":
            raw = [read(p) for p in sorted(path.parent.glob("turn-*.json"))]
            assert len(raw) == len(data["events"])
            assert sum(tokens(r) for r in raw) == data["usage"]["total_tokens"]
            assert all(c["response"]["choices"][0]["message"]["content"] == e["content"] for c, e in zip(raw, data["events"]))
            assert data["success"] == data["verification"]["success"]
            outcomes[path] = data
    calibration = [p for p in outcomes if p.parts[-3] == "calibration-v2"]
    policy = read(repo / "artifacts/policy-v2.json")
    for family, recorded in policy["statistics"].items():
        stats = {}
        for arm in ("none", "inherit", "reconstruct"):
            rows = [outcomes[p] for p in calibration if p.parent.name.endswith("-" + arm) and outcomes[p]["task"]["family"] == family]
            assert len(rows) == 2
            stats[arm] = {"successes": sum(r["success"] for r in rows), "tokens": sum(r["usage"]["total_tokens"] for r in rows)}
        assert stats == recorded
        assert min(stats, key=lambda a: (-stats[a]["successes"], stats[a]["tokens"], ["none", "inherit", "reconstruct"].index(a))) == policy["choices"][family]
    setup = sum(tokens(c) for p, c in calls.items() if "reconstruction-v2" in p.parts)
    calibration_cost = sum(tokens(c) for p, c in calls.items() if "calibration-v2" in p.parts)
    report = read(repo / "reports/policy-results.json")
    result = {}
    for arm in ("none", "inherit", "reconstruct", "policy"):
        rows = []
        for seed in range(400, 412):
            none = read(repo / f"runs/evaluation-recipient-v2/{seed}-none/outcome.json")
            selected = policy["choices"][none["task"]["family"]] if arm == "policy" else arm
            rows.append(read(repo / f"runs/evaluation-recipient-v2/{seed}-{selected}/outcome.json"))
        use = sum(r["usage"]["total_tokens"] for r in rows)
        extra = {"none": 0, "inherit": 0, "reconstruct": setup, "policy": setup + calibration_cost}[arm]
        result[arm] = {"tasks": len(rows), "successes": sum(r["success"] for r in rows), "use_tokens": use, "incremental_setup_tokens": extra, "setup_plus_use_tokens": use + extra}
        for key, value in result[arm].items():
            assert value == report["arms"][arm][key]
    phases = {phase: sum(tokens(c) for p, c in calls.items() if p.relative_to(repo / "runs").parts[0] == phase) for phase in sorted({p.relative_to(repo / "runs").parts[0] for p in calls})}
    return {"revision": revision, "manifest_files_verified": len(manifest["files"]), "raw_calls": len(calls), "tokens": sum(tokens(c) for c in calls.values()), "outcomes": len(outcomes), "successes": sum(r["success"] for r in outcomes.values()), "recipient": result, "phase_tokens": phases}


def authority_state(archive):
    """Derive expected state from source text, without study fixture/scorer code."""
    def number(pattern, source):
        return int(re.search(pattern, archive[source]).group(1))
    unit = number(r"tariff (\d+)", "S1") + number(r"add (\d+)", "S2")
    return {"route": re.search(r"route (\w+)", archive["S1"]).group(1),
            "unit_cost": unit, "batch_cost": unit * number(r"batch has (\d+)", "S2"),
            "cold": "not required" not in archive["S1"],
            "escort": "no longer requires escort" not in archive["S1"] or "no longer requires escort" not in archive["S4"],
            "documents": json.loads(re.search(r"documents are (\[.*?\])", archive["S3"]).group(1)),
            "label": re.search(r'label is "(.*?)"', archive["S3"]).group(1),
            "cutoff": number(r"cutoff hour (\d+)", "S5")}


def match(got, expected):
    return isinstance(got, dict) and all(type(got.get(k)) is type(v) and (sorted(got[k]) == sorted(v) if isinstance(v, list) else got[k] == v) for k, v in expected.items())


def lineage():
    repo = BASE / "correction-lineage"
    revision = pin(repo, "f8ad1e1ce8b9842efa90305c1206b8690578a204")
    result = {"revision": revision}
    identities = set()
    all_calls = []
    for phase in ("pilot-v1", "fresh-v1", "read-diagnostic-v1"):
        folder = repo / "evidence" / phase
        calls = {p.stem: read(p) for p in (folder / "calls").glob("*.json")}
        all_calls.extend(calls.values())
        for c in calls.values():
            assert sha(enc(c["request"]).encode()) == c["request_sha256"]
            assert c["response"]["choices"][0]["finish_reason"] == "stop"
            body = json.loads(c["request"]["messages"][1]["content"])
            assert "truth" not in body and "gold_support_candidates" not in body
            identities.add((c["response"]["model"], c["response"].get("system_fingerprint")))
        fixtures = {f["seed"]: f for f in (read(p) for p in folder.glob("fixture-*.json"))}
        for f in fixtures.values():
            archive = dict(f["archive"])
            for index in range(3):
                if index:
                    event = f["events"][index - 1]
                    archive[event["replace"]] = event["text"]
                assert authority_state(archive) == f["truth"][index]
        rows = read(folder / "results.json")
        for row in rows:
            f = fixtures[row["seed"]]
            event = row.get("event", 1)
            archive = dict(f["archive"])
            for change in f["events"][:event]:
                archive[change["replace"]] = change["text"]
            gold = authority_state(archive)
            assert match(row["state"], gold) and set(row["state"]) == set(gold) and row["state_complete"]
            use_tag = f's{row["seed"]}-' + (f'e{event}-{row["arm"]}-use' if "event" in row else row["arm"])
            output = parsed(calls[use_tag])
            assert output == row.get("fresh_output", row.get("output"))
            expected = [{"quantity": q, "total_cost": q * gold["unit_cost"], **{k: v for k, v in gold.items() if k not in ("unit_cost", "batch_cost")}} for q in f["fresh_quantities"]]
            actual = output.get("orders", [])
            ok = len(actual) == len(expected) and all(match(g, e) for g, e in zip(actual, expected))
            assert ok == row["fresh_complete"]
            if "event" in row:
                assert ok == row["complete"]
                before = parsed(calls[f's{row["seed"]}-write']) if event == 1 else next(x["state"] for x in rows if x["seed"] == row["seed"] and x["arm"] == row["arm"] and x["event"] == event - 1)
                assert before == row["before"]
                repair = parsed(calls[use_tag.removesuffix("use") + "repair"])
                assert set(repair) == set(row["targets"])
                assert {**before, **repair} == row["state"]
        summary = {}
        for arm in sorted({r["arm"] for r in rows}):
            selected = [r for r in rows if r["arm"] == arm]
            stats = {"episodes": len(selected), "state_complete": sum(r["state_complete"] for r in selected), "complete": sum(r["fresh_complete"] for r in selected)}
            if phase != "read-diagnostic-v1":
                tags = {t for r in selected for t in r["event_tags"] + r["initial_tags"]}
                stats.update(calls=len(tags), tokens=sum(tokens(calls[t]) for t in tags), fields=sum(len(r["targets"]) for r in selected))
                saved = read(folder / "summary.json")[arm]
                assert stats["complete"] == saved["complete"]
                assert stats["tokens"] == saved["deployment_cost"]["prompt_tokens"] + saved["deployment_cost"]["completion_tokens"]
            summary[arm] = stats
        if phase != "read-diagnostic-v1":
            links = {"true": 0, "spurious": 0, "missing": 0, "route_s6_after_first_correction": []}
            for seed in fixtures:
                acquired = parsed(calls[f"s{seed}-acquire"])
                expected_links = fixtures[seed]["gold_support_candidates"]
                actual_edges = {(key, source) for key, sources in acquired.items() for source in sources}
                gold_edges = {(key, source) for key, sources in expected_links.items() for source in sources}
                links["true"] += len(actual_edges & gold_edges)
                links["spurious"] += len(actual_edges - gold_edges)
                links["missing"] += len(gold_edges - actual_edges)
                if "S6" in parsed(calls[f"s{seed}-e1-selective-maintain"])["route"]:
                    links["route_s6_after_first_correction"].append(seed)
                for event in (1, 2):
                    group = [calls[f"s{seed}-e{event}-{arm}-use"] for arm in summary]
                    assert len({enc(c["request"]) for c in group}) == 1
                    assert len({enc(parsed(c)) for c in group}) == 1
            for arm, stats in summary.items():
                stats["tokens_at_horizons_0_1_2"] = []
                for horizon in (0, 1, 2):
                    tags = {t for r in rows if r["arm"] == arm for t in r["initial_tags"]}
                    tags.update(t for r in rows if r["arm"] == arm and r["event"] <= horizon for t in r["event_tags"])
                    stats["tokens_at_horizons_0_1_2"].append(sum(tokens(calls[t]) for t in tags))
            summary["acquisition_links"] = links
        else:
            for seed in fixtures:
                pair = [json.loads(json.dumps(calls[f"s{seed}-{arm}"]["request"])) for arm in ("original", "explicit")]
                for request in pair:
                    body = json.loads(request["messages"][1]["content"])
                    body.pop("task")
                    request["messages"][1]["content"] = enc(body)
                assert pair[0] == pair[1]
        result[phase] = {"arms": summary, "calls": len(calls), "tokens": sum(tokens(c) for c in calls.values())}
    assert len(identities) == 1
    probe = read(repo / "evidence/capability-probe.json")
    # The probe stores a direct completion response, unlike workload call records.
    probe_tokens = tokens(probe) if "response" in probe else probe["usage"]["total_tokens"]
    result.update(recorded_requests_verified=len(all_calls), identities=sorted(identities), research_calls_including_probe=len(all_calls) + 1, research_tokens_including_probe=sum(tokens(c) for c in all_calls) + probe_tokens)
    return result


if __name__ == "__main__":
    print(json.dumps({"migration": migration(), "lineage": lineage()}, indent=2))
