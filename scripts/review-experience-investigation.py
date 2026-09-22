"""Replay frozen pilot artifacts without model inference or training.

Run with uv from the root. The study clone and reconstructed workspaces stay
in ignored .cache; the review report is tracked in sources/.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / ".cache/experience-investigation-review/study"
REVISION = "47e5b284cf520bc89b0411ae2f0bf40e8cef046a"
OUT = ROOT / "sources/2026-09-21-experience-investigation-review/replay.json"


def read_json(path):
    return json.loads(path.read_text())


def read_rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute(workspace, payload):
    proc = subprocess.run(
        [sys.executable, "etl_pipeline.py", "--execute"], cwd=workspace,
        input=json.dumps(payload), text=True, capture_output=True, timeout=20,
    )
    return {"returncode": proc.returncode, "actual": json.loads(proc.stdout)}


def main():
    revision = subprocess.check_output(
        ["git", "-C", str(STUDY), "rev-parse", "HEAD"], text=True
    ).strip()
    assert revision == REVISION
    assert not subprocess.check_output(
        ["git", "-C", str(STUDY), "status", "--porcelain"], text=True
    ).strip()
    # These imported modules contain the frozen workload and evaluators, no ML
    # imports or top-level experiment execution. Direct execution is limited to
    # reconstructed copies of the small, inspected ETL program.
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(STUDY / "scripts"))
    from workload import write_workspace
    from runtime import parse_action
    from evaluate import run_public, run_hidden
    from evaluate_diagnostic import evaluate
    from teacher_transfer import branch_source

    evidence = STUDY / "evidence/pilot-01"
    report = {
        "date": "2026-09-21", "study_revision": revision,
        "scope": "Frozen-action/source replay; no model inference or training",
        "runs": {},
    }
    with tempfile.TemporaryDirectory(prefix="replay-", dir=STUDY.parent) as temp:
        temp = Path(temp)
        for name in ["ordinary-agent", "learned-agent", "diagnostic-base-agent", "diagnostic-adapter-agent"]:
            diagnostic = name.startswith("diagnostic")
            workspace = temp / name
            if diagnostic:
                write_workspace(workspace, "dev-filter-fresh", history=evidence / "initial-transfer-workspace/history")
            else:
                shutil.copytree(evidence / "initial-transfer-workspace", workspace)
            rows = read_rows(evidence / name / "events.jsonl")
            models = [row for row in rows if row["kind"] == "model"]
            tools = [row for row in rows if row["kind"] == "tool"]
            assert len(models) == len(tools)
            for model, tool in zip(models, tools):
                parsed, _ = parse_action(model["raw"])
                assert parsed == model["action"] == tool["action"]
                if parsed and parsed["action"] == "edit" and tool["result"]["ok"]:
                    source = (workspace / "etl_pipeline.py").read_text()
                    assert source.count(parsed["old"]) == 1
                    (workspace / "etl_pipeline.py").write_text(source.replace(parsed["old"], parsed["new"], 1))
            summary = read_json(evidence / name / "summary.json")
            assert digest(workspace / "etl_pipeline.py") == summary["workspace_source_hash"]
            public = run_public(workspace)
            item = {
                "source_hash": digest(workspace / "etl_pipeline.py"),
                "matches_recorded_final_hash": True,
                "public_passed": public["passed"], "public_detail": public["stderr"],
                "model_calls": len(models),
                "prompt_tokens": sum(row["prompt_tokens"] for row in models),
                "reported_completion_tokens": sum(row["completion_tokens"] for row in models),
                "reported_episode_seconds": summary["seconds"],
                "invalid_actions": sum(row["action"] is None for row in models),
                "responses_at_384_chunk_cap": sum(row["completion_tokens"] == 384 for row in models),
                "successful_edits": sum(bool(row["action"] and row["action"]["action"] == "edit" and row["result"]["ok"]) for row in tools),
                "history_results": [row["result"] for row in tools if row["action"] and row["action"]["action"] == "history_search"],
                "probe_results": [row["result"] for row in tools if row["action"] and row["action"]["action"] == "probe"],
            }
            if diagnostic:
                item["original_diagnostic"] = evaluate(workspace)
                # The task explicitly requires boolean true. These extra cases
                # examine the submitted repair; they do not alter original scores.
                additional = []
                for expression in ["1", '"nonempty"']:
                    payload = {"pipeline": {"steps": [{"op": "filter", "where": expression}]}, "dataset": [{"id": 1}]}
                    result = execute(workspace, payload)
                    expected = {"status": "ok", "data": [], "metrics": {"rows_in": 1, "rows_out": 0}}
                    additional.append({"expression": expression, **result, "expected": expected, "passed": result["returncode"] == 0 and result["actual"] == expected})
                item["root_boolean_contract_checks"] = additional
            else:
                item["hidden"] = run_hidden(workspace, evidence / "examiner")
                item["hidden_passed"] = sum(case["passed"] for case in item["hidden"])
            if name == "ordinary-agent":
                raw = models[-1]["raw"]
                decoder = json.JSONDecoder()
                first, end = decoder.raw_decode(raw)
                second, _ = decoder.raw_decode(raw[end:].lstrip())
                item["last_response_actions"] = [first["action"], second["action"]]
                item["parser_selected"] = models[-1]["action"]["action"]
                item["ignored_edit_old_text_occurrences"] = (workspace / "etl_pipeline.py").read_text().count(first["old"])
            report["runs"][name] = item

        teacher = temp / "teacher"
        write_workspace(teacher, "transfer-branch")
        (teacher / "etl_pipeline.py").write_text(branch_source())
        assert digest(teacher / "etl_pipeline.py") == read_json(evidence / "teacher-transfer/report.json")["source_hash"]
        teacher_public = run_public(teacher)
        teacher_hidden = run_hidden(teacher, evidence / "examiner")
        report["teacher"] = {"source_hash": digest(teacher / "etl_pipeline.py"), "public_passed": teacher_public["passed"], "hidden_passed": sum(case["passed"] for case in teacher_hidden), "hidden": teacher_hidden}

        reference = temp / "unchanged-reference"
        write_workspace(reference, "transfer-branch")
        report["reference_boolean_contract_checks"] = [execute(reference, {"pipeline": {"steps": [{"op": "filter", "where": expr}]}, "dataset": [{"id": 1}]}) for expr in ["1", '"nonempty"']]

    training = read_rows(evidence / "acquisition/training.jsonl")
    report["training"] = {
        "rows": len(training),
        "trajectories": sorted({row["id"].rsplit("-", 1)[0] for row in training}),
        "origin": "scripted researcher-authored actions, not learner rollouts",
        "history_files": sorted(path.name for path in (evidence / "initial-transfer-workspace/history").iterdir()),
    }
    report["known_four_episode_totals"] = {
        field: sum(run[field] for run in report["runs"].values())
        for field in ["model_calls", "prompt_tokens", "reported_completion_tokens", "reported_episode_seconds"]
    }
    inspected = ["AGENTS.md", "README.md", "PROMPT.md", "protocol/pilot-v1.md", "pyproject.toml", "uv.lock"]
    inspected += [str(path.relative_to(STUDY)) for path in sorted((STUDY / "scripts").glob("*.py"))]
    inspected += [str(path.relative_to(STUDY)) for path in sorted(evidence.rglob("*")) if path.is_file()]
    report["artifact_sha256"] = {name: digest(STUDY / name) for name in inspected}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"totals": report["known_four_episode_totals"], "outcomes": {name: {key: item.get(key) for key in ["public_passed", "hidden_passed", "successful_edits", "root_boolean_contract_checks"]} for name, item in report["runs"].items()}, "teacher_hidden_passed": report["teacher"]["hidden_passed"]}, indent=2))


if __name__ == "__main__":
    main()
