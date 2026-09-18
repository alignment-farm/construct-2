"""Read-only review of the pinned publication; no model execution or training.

Run: uv run --no-project python scripts/review-weight-consolidation.py
Emits JSON to stdout. Runs the inspected ancillary audits with writes captured in
memory, independently grades public tasks, and replays the deterministic compiler.
"""
import contextlib
import hashlib
import io
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT.parent / "ancillary-studies/weight-consolidation"
RUNTIME = ROOT.parent / "derivatives/construct-runtime"
REVISION = "491c0f8a745f48327f6d095d2c3fa7f07d768b44"
RUNTIME_REVISION = "9ffb10a66180626b80127fb1892b2cf71e39d946"


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def events(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def expected(task):
    """Independent interpretation of the inspected public contract grammar."""
    header, _ = task["contract"].split(". ", 1)
    fields = {}
    for entry in header.removeprefix("Columns: ").split(", "):
        column, meaning = entry.split(" means ")
        fields[meaning] = column
    contract = task["contract"]
    latest = "The highest revision wins per document." in contract
    major = "Amounts are decimal dollars." in contract
    negative = "Credit-kind values must become negative absolute amounts." in contract
    accepted = contract.split("Accept statuses ")[1].split(" only.")[0].split(", ")
    groups = defaultdict(list)
    for row in task["rows"]:
        groups[row[fields["id"]]].append(row)
    answer = {"job": task["job"], "records": [], "quarantine": [], "excluded": []}
    for identity, rows in sorted(groups.items()):
        row = max(rows, key=lambda r: int(r[fields["revision"]])) if latest else rows[0]
        if row[fields["status"]] not in accepted:
            answer["excluded"].append(identity)
        elif row[fields["account"]] not in task["accounts"]:
            answer["quarantine"].append(identity)
        else:
            value = Fraction(str(row[fields["amount"]])) * (100 if major else 1)
            assert value.denominator == 1
            minor = int(value)
            if negative and row[fields["kind"]] == "credit":
                minor = -abs(minor)
            answer["records"].append({"id": identity, "account": task["accounts"][row[fields["account"]]], "minor": minor})
    answer["total_minor"] = sum(row["minor"] for row in answer["records"])
    return answer


for path, revision in ((STUDY, REVISION), (RUNTIME, RUNTIME_REVISION)):
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=path, text=True).strip() == revision
    assert not subprocess.check_output(["git", "status", "--porcelain"], cwd=path, text=True).strip()

sys.path.insert(0, str(RUNTIME / "src"))
from construct_runtime import records
from construct_runtime.environment import load_environment
from construct_runtime.state import resolve_state

captured = {}
original_write = records.write_json
original_argv = sys.argv[:]
records.write_json = lambda path, value: captured.update({str(Path(path).resolve()): json.loads(json.dumps(value))})
try:
    for name in ("pilot-01", "pilot-02", "confirmation-01"):
        folder = STUDY / "evidence" / name
        sys.argv = [str(STUDY / "scripts/audit.py"), str(folder)]
        with contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(sys.argv[0], run_name="__main__")
        assert captured[str(folder / "audit.json")] == read(folder / "audit.json")
    sys.argv = [str(STUDY / "scripts/costs.py"), str(STUDY / "evidence")]
    with contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(sys.argv[0], run_name="__main__")
    assert captured[str(STUDY / "evidence/costs.json")] == read(STUDY / "evidence/costs.json")
finally:
    records.write_json = original_write
    sys.argv = original_argv

totals = Counter()
stages = {}
confirm_grades = defaultdict(dict)
identities = set()
direct_count = 0
snapshot_files = 0
compile_contract = runpy.run_path(str(STUDY / "workload/compile_contract.py"))["compile_contract"]
reconcile = runpy.run_path(str(STUDY / "workload/transform.py"))["reconcile"]
for name in ("pilot-01", "pilot-02", "confirmation-01"):
    folder = STUDY / "evidence" / name
    cases = read(folder / "controller-cases.json")
    if (folder / "evaluation-cases.json").exists():
        cases += read(folder / "evaluation-cases.json")
    cases = {c["id"]: c for c in cases}
    for case in cases.values():
        assert expected(case["task"]) == case["expected"]
    freeze = folder / "evaluation-freeze.json"
    if freeze.exists():
        for rel, fingerprint in read(freeze)["files"].items():
            base = STUDY if rel.startswith("evidence/") else folder
            assert sha(base / rel) == fingerprint
            snapshot_files += 1
    for path in sorted((folder / "runs").glob("*/*/grade.json")):
        row = read(path)
        work = path.parent / "work"
        case = cases[row["case_id"]]
        task = read(path.parent / "public-task.json")
        assert task == case["task"] and set(task) == {"job", "contract", "rows", "accounts"}
        result = read(work / "result.json")
        assert result == row["result"]
        actual = read(work / "reconciled.json") if (work / "reconciled.json").exists() else {}
        for artifact in result["artifacts"]:
            assert sha(work / artifact["name"]) == artifact["sha256"]
        components = {k: actual.get(k) == v for k, v in expected(task).items()}
        grade = {"complete": result["status"] == "succeeded" and all(components.values()), "components": components}
        assert grade == row["grade"]
        ev = events(work / "events.jsonl")
        calls = [e for e in ev if e["kind"] == "model_response"]
        errors = [e for e in ev if e["kind"] == "tool_result" and "error" in e["result"]]
        usage = {"prompt_tokens": sum(c["prompt_tokens"] for c in calls), "completion_tokens": sum(c["completion_tokens"] for c in calls), "calls": len(calls), "failed_calls": len(errors)}
        for key, value in usage.items():
            assert value == result["usage"][key]
        usage.update(tasks=1, worker_seconds=result["elapsed_seconds"])
        totals.update(usage)
        stage = stages.setdefault(name + "/" + row["stage"], Counter())
        stage.update(usage)
        stage["complete"] += int(grade["complete"])
        if case["changed"]:
            stage["changed_complete"] += int(grade["complete"])
            stage["changed_excluded"] += int(components["excluded"])
        identities.add(next(e["identity"]["base_digest"] for e in ev if e["kind"] == "model_loaded"))
        if name == "confirmation-01" and row["stage"].startswith("evaluation-"):
            confirm_grades[row["state"]][case["id"]] = grade["complete"]
            assert next(e["time_ns"] for e in ev if e["kind"] == "execution_started") > read(freeze)["time_ns"]
            assert not any('"tool":"read_source"' in e.get("text", "").replace(" ", "") for e in calls)
    for path in sorted((folder / "direct-compiler").glob("*/grade.json")):
        case = cases[read(path)["case_id"]]
        replay = reconcile(case["task"], compile_contract(case["task"]["contract"]))
        assert replay == expected(case["task"]) == read(path.parent / "artifact.json")
        direct_count += 1

assert len(identities) == 1
reported = read(STUDY / "evidence/costs.json")
for key, value in totals.items():
    assert math.isclose(value, reported["model_execution_totals"][key], abs_tol=1e-8)
confirmation = STUDY / "evidence/confirmation-01"
training_rows = read(confirmation / "training-data/training.json")
source_reads = 0
with tempfile.TemporaryDirectory(prefix="construct-weight-review-") as temp:
    for state in sorted((confirmation / "states").iterdir()):
        config = resolve_state(state, None)
        environment = load_environment(config)
        workspace = Path(temp) / state.name
        (workspace / "inherited").mkdir(parents=True)
        for i in range(8):
            filename = f"source-{i}.json"
            (workspace / "inherited" / filename).write_bytes(Path(config["inherited_artifacts"][filename]).read_bytes())
        got = []
        for i in range(8):
            for j in range(2):
                action = {"tool": "read_source", "source_id": f"source-{i}", "kind": "training", "index": j}
                got.append(environment.dispatch({}, action, workspace)["record"])
                source_reads += 1
        assert got == training_rows

updates = [e for e in events(STUDY / "evidence/pilot-02/adapter-32/training.jsonl") if e["kind"] == "update"]
training = reported["training"]
assert len(training) == 1 and len(updates) == training[0]["steps"] == 32
assert sum(e["input_tokens"] for e in updates) == training[0]["usage"]["input_tokens"]
assert sum(e["loss_tokens"] for e in updates) == training[0]["usage"]["loss_tokens"]
pairs = Counter()
for case_id, base in confirm_grades["base"].items():
    learned = confirm_grades["adapter-32"][case_id]
    pairs[{(False, False): "both_fail", (False, True): "adapter_only", (True, False): "base_only", (True, True): "both_complete"}[base, learned]] += 1

print(json.dumps({
    "publication_revision": REVISION, "previous_review_boundary": "a9e609a892fb8e34507e20b5fdf9b504c7c93170",
    "runtime_revision": RUNTIME_REVISION,
    "scope": "saved-record analysis and deterministic tool execution; no model inference or training",
    "author_audits_recomputed": 3, "author_cost_ledger_recomputed": True,
    "independent_task_totals": totals, "stages": stages,
    "manual_confirmation_paired_outcomes": pairs, "direct_compiler_replays": direct_count,
    "exact_source_training_rows": len(training_rows), "public_source_tool_reads_verified": source_reads,
    "freeze_snapshot_files_verified": snapshot_files, "single_base_identity": list(identities),
    "training_runs": training,
}, indent=2))
