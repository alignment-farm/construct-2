"""Inspect saved records and replay SQL, without inference or training.

Run with uv run --no-project python scripts/review-weight-continuation.py.
Requires the published study checkout and the two pinned databases in
.cache/weight-continuation-review (hashes are checked before querying).
Outputs JSON; does not write to the ancillary repository.
"""
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import runpy
import sqlite3
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT.parent / "ancillary-studies/weight-consolidation"
CONT = STUDY / "continuation"
EVIDENCE = CONT / "evidence"
FINAL = EVIDENCE / "db-06"
CACHE = ROOT / ".cache/weight-continuation-review"
REVISION = "80c17dbfb63116cd35ab5faf23f527178fec3e5b"


def read(path):
    return json.loads(path.read_text())


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def events(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"Duplicate JSON key: {key}")
        value[key] = item
    return value


def equivalent(actual, expected, tolerance=0):
    if not isinstance(actual, list) or len(actual) != len(expected):
        return False
    for a, b in zip(actual, expected):
        if len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                if not math.isclose(x, y, rel_tol=0, abs_tol=max(tolerance, 1e-8)):
                    return False
            elif x != y:
                return False
    return True


class Median:
    """Portable equivalent for the native worker's SQLite median aggregate."""
    def __init__(self):
        self.values = []

    def step(self, value):
        if value is not None:
            self.values.append(value)

    def finalize(self):
        return statistics.median(self.values) if self.values else None


assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=STUDY, text=True).strip() == REVISION
assert not subprocess.check_output(["git", "status", "--porcelain"], cwd=STUDY, text=True).strip()
publication = read(CONT / "PUBLICATION.json")
for name, expected_hash in publication["files_sha256"].items():
    assert digest(CONT / name) == expected_hash

connections = {}
for revision in ("before", "after"):
    manifest = read(FINAL / f"database-{revision}.json")
    database = CACHE / manifest["name"]
    assert digest(database) == manifest["sha256"]
    conn = sqlite3.connect(f"file:{database}?mode=ro&immutable=1", uri=True)
    conn.create_aggregate("median", 1, Median)
    runpy.run_path(str(CONT / "workload" / f"views_{revision}.py"))["install"](conn, revision)
    connections[revision] = conn


def execute(query, revision, params=()):
    conn = connections[revision]
    deadline = time.monotonic() + 30
    conn.set_progress_handler(lambda: int(time.monotonic() > deadline), 10000)
    return [list(row) for row in conn.execute(query, params).fetchall()]


totals = Counter()
groups = defaultdict(Counter)
tool_counts = defaultdict(Counter)
rows = {}
oracle_cache = {}
queries_replayed = 0
for path in sorted(EVIDENCE.glob("db-*/runs/*/q*/grade.json")):
    row = read(path)
    work = path.parent / "work"
    trace = events(work / "events.jsonl")
    responses = [event for event in trace if event["kind"] == "model_response"]
    raw = {key: sum(event.get(key, 0) for event in responses) for key in ("prompt_tokens", "completion_tokens")}
    raw["calls"] = len(responses)
    raw["model_seconds"] = sum(event["seconds"] for event in responses)
    for key, value in raw.items():
        if key in row["result"].get("usage", {}):
            assert math.isclose(value, row["result"]["usage"][key], abs_tol=1e-8)
    totals.update(raw)
    totals["tasks"] += 1
    answer_path = work / "answer.json"
    answer = read(answer_path) if answer_path.exists() else {}
    expected = row["grade"]["expected"]
    if path.parts[-5] == "db-06" and row["stage"].startswith(("fresh-", "preserved-")):
        key = row["revision"], row["id"]
        if key not in oracle_cache:
            oracle_cache[key] = execute(row["grade"]["reference_sql"], row["revision"])
        assert equivalent(oracle_cache[key], expected)
        if answer:
            replay = execute(answer["query"], row["revision"], answer.get("params", {}))
            assert equivalent(replay, answer["rows"])
            queries_replayed += 1
    correct = equivalent(answer.get("rows"), expected, row["grade"]["tolerance"])
    complete = correct and row["result"]["status"] == "succeeded"
    assert correct == row["grade"]["result_correct"]
    assert complete == row["grade"]["complete"]
    for artifact in row["result"].get("artifacts", []):
        assert digest(work / artifact["name"]) == artifact["sha256"]
    group = path.parts[-5] + "/" + row["stage"]
    groups[group].update(raw)
    groups[group].update(tasks=1, complete=int(complete), correct_artifact=int(correct))
    for response in responses:
        text = response["text"].strip()
        if text.startswith("```json\n") and text.endswith("```"):
            text = text[8:-3].strip()
        try:
            action = json.loads(text, object_pairs_hook=unique_object)
            name = action.get("tool", "unknown")
        except (ValueError, AttributeError):
            name = "malformed-action"
        tool_counts[group][name] += 1
    rows[group, row["id"]] = row

reported = read(EVIDENCE / "summary.json")
assert totals["tasks"] == reported["totals"]["task_executions"] == 229
for key in ("prompt_tokens", "completion_tokens", "calls", "model_seconds"):
    assert math.isclose(totals[key], reported["totals"]["usage"][key], abs_tol=1e-8)
for group, values in groups.items():
    saved = reported["groups"][group]
    assert values["tasks"] == saved["n"]
    assert values["complete"] == saved["complete"]
    assert values["correct_artifact"] == saved["correct_artifact"]
    assert tool_counts[group] == saved["tools"], (group, tool_counts[group], saved["tools"])

training = []
for path in sorted(EVIDENCE.glob("db-*/adapter*/manifest.json")):
    manifest = read(path)
    assert digest(path.parent / "adapter.safetensors") == manifest["weights_sha256"]
    updates = [e for e in events(path.parent / "training.jsonl") if e["kind"] == "update"]
    assert len(updates) == manifest["steps"]
    assert manifest["base_unchanged"] and manifest["initial_tensor_digest"] != manifest["final_tensor_digest"]
    training.append({"path": str(path.relative_to(STUDY)), "steps": len(updates), "seconds": manifest["elapsed_seconds"]})
assert len(training) == 4 and sum(r["steps"] for r in training) == 516

states = {p.parent.name: read(p) for p in sorted((FINAL / "states").glob("*/state.json"))}
verified_assets = 0
for name, state in states.items():
    for relative, fingerprint in state["assets"].items():
        assert digest(FINAL / "states" / name / relative) == fingerprint
        verified_assets += 1
for names in (("base0", "adapter0-144"), ("base1", "stale1", "adapter1-228")):
    base = states[names[0]]
    for name in names[1:]:
        for key, fingerprint in base["assets"].items():
            assert states[name]["assets"][key] == fingerprint
        for key in ("guidance", "max_steps", "mode", "environment"):
            assert states[name]["config"][key] == base["config"][key]

data0 = read(FINAL / "training-data0/training.json")
data1 = read(FINAL / "training-data1/training.json")
assert data1[:len(data0)] == data0 and (len(data0), len(data1)) == (24, 38)
for point, data, names in ((0, data0, ("base0", "adapter0-144")), (1, data1, ("base1", "stale1", "adapter1-228"))):
    for name in names:
        history = read(FINAL / "states" / name / "assets/inherited/history.json")
        assert [record for entry in history for record in entry.get("records", [])] == data
targets = Counter(json.loads(row["target"])["tool"] for row in data1)
assert targets == {"submit": 19, "finish": 19}

decision = read(FINAL / "decision.json")
sequence = events(FINAL / "sequence.jsonl")
assert decision["created_time_ns"] < min(e["time_ns"] for e in sequence if e["kind"] == "fresh_started")
assert all(e["decision_sha256"] == digest(FINAL / "decision.json") for e in sequence if e["kind"] == "fresh_started")

case = rows["db-06/fresh-stale1", 112]
q112 = {"question": read(FINAL / "runs/fresh-stale1/q112/task.json")["question"], "reference": case["grade"]["reference_sql"], "reference_result": oracle_cache["after", 112]}
for arm in ("stale1", "adapter1-228"):
    answer = read(FINAL / f"runs/fresh-{arm}/q112/work/answer.json")
    q112[arm] = {"query": answer["query"], "result": execute(answer["query"], "after")}
fixed = q112["adapter1-228"]["query"].replace("GROUP BY a.attr_val", "AND p.price > 0 GROUP BY a.attr_val")
q112["updated_query_with_reference_positive_price_filter"] = {"query": fixed, "result": execute(fixed, "after")}

print(json.dumps({
    "publication": REVISION,
    "scope": "saved-record grading and usage; fresh/preserved SQL replay; no model inference or optimization",
    "sqlite": sqlite3.sqlite_version,
    "median": "Python statistics.median aggregate registered for portable replay",
    "totals": totals,
    "groups": groups,
    "tools": tool_counts,
    "independent_reference_queries": len(oracle_cache),
    "submitted_query_replays": queries_replayed,
    "state_assets_verified": verified_assets,
    "source_rows_in_matched_states": 2 * len(data0) + 3 * len(data1),
    "teaching_action_counts_cumulative": targets,
    "training": training,
    "q112_output_match_caveat": q112,
}, indent=2))
