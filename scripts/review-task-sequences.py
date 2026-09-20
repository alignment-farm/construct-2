# /// script
# requires-python = ">=3.12,<3.13"
# dependencies = [
#   "pytest==8.3.2",
#   "jsonschema==4.21.1",
#   "tree-sitter==0.21.3",
#   "tree-sitter-languages==1.10.2",
# ]
# ///
"""Check published reference assets, without model calls or benchmark training.

Clone gabeorlanski/scb-problems into .cache/task-sequence-review/scb-problems
and check out SCB_PIN before running with `uv run scripts/review-task-sequences.py`.
This directly invokes that separate problem repository's pytest interface; it
does not reproduce the SlopCodeBench Docker runner or paper agent experiments.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import platform
import shlex
import sqlite3
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache/task-sequence-review"
REPO = CACHE / "scb-problems"
OUT = ROOT / "sources/2026-09-20-task-sequences/reference-checks.json"
SCB_PIN = "ef6a9dd13911566b6b01075ca121758c9f7b5c5f"
CL_PIN = "5f8c50eb1e84b2eda2ef4faff757dfc812a0ea26"


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(REPO), *args], text=True).strip()


def main() -> None:
    if git("rev-parse", "HEAD") != SCB_PIN or git("status", "--porcelain", "--untracked-files=no"):
        raise SystemExit("Expected clean tracked files at the recorded problem revision")
    report: dict = {
        "purpose": "Published reference-asset feasibility, not learner evaluation",
        "repository": "https://github.com/gabeorlanski/scb-problems",
        "revision": SCB_PIN,
        "python": sys.version,
        "platform": platform.platform(),
        "packages": {name: importlib.metadata.version(name) for name in
                     ["pytest", "jsonschema", "tree-sitter", "tree-sitter-languages"]},
        "runs": [],
    }
    for problem in ["etl_pipeline", "code_search"]:
        for checkpoint in [3, 4]:
            label = f"{problem}-checkpoint-{checkpoint}"
            junit = CACHE / f"{label}.xml"
            log = CACHE / f"{label}.txt"
            entry = REPO / problem / "solutions" / f"checkpoint_{checkpoint}" / f"{problem}.py"
            tests = [REPO / problem / "tests" / f"test_checkpoint_{i}.py"
                     for i in range(1, checkpoint + 1)]
            command = [sys.executable, "-m", "pytest", *map(str, tests),
                       "--entrypoint", shlex.join([sys.executable, str(entry)]),
                       "--checkpoint", f"checkpoint_{checkpoint}", "-q",
                       "--disable-warnings", f"--junitxml={junit}"]
            started = time.monotonic()
            with log.open("w") as stream:
                result = subprocess.run(command, cwd=REPO, stdout=stream,
                                        stderr=subprocess.STDOUT, timeout=240)
            suites = ET.parse(junit).getroot()
            cases = list(suites.iter("testcase"))
            failures = [{"class": c.get("classname"), "name": c.get("name"),
                         "message": child.get("message")}
                        for c in cases for child in c
                        if child.tag in {"failure", "error"}]
            skipped = sum(c.find("skipped") is not None for c in cases)
            row = {
                "problem": problem, "reference_checkpoint": checkpoint,
                "test_checkpoints": list(range(1, checkpoint + 1)),
                "command": command, "returncode": result.returncode,
                "elapsed_seconds": round(time.monotonic() - started, 3),
                "tests": len(cases), "passed": len(cases) - len(failures) - skipped,
                "skipped": skipped, "failures": failures,
                "log": str(log.relative_to(ROOT)),
                "log_sha256": hashlib.sha256(log.read_bytes()).hexdigest(),
                "junit_sha256": hashlib.sha256(junit.read_bytes()).hexdigest(),
            }
            report["runs"].append(row)
            OUT.write_text(json.dumps(report, indent=2) + "\n")
            print(label, {k: row[k] for k in ["tests", "passed", "skipped", "returncode"]}, flush=True)


def check_database() -> None:
    """Replay selected public queries on the already cached, pinned databases."""
    repo = CACHE / "cl-bench"
    revision = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "-C", str(repo), "status", "--porcelain", "--untracked-files=no"], text=True
    ).strip()
    if revision != CL_PIN or dirty:
        raise SystemExit("Expected clean tracked CL-Bench files at the recorded revision")
    checks: dict = {
        "scope": "Five selected upstream reference SQL queries and stale-column diagnostics; no learner or full CL-Bench runner",
        "sqlite": sqlite3.sqlite_version,
        "grading": "Numeric comparison from task.py: exact integer or max(declared tolerance, 1% of expected float)",
        "queries": [],
    }
    for name, question_file, ids, expected_hash in [
        ("products.db", "questions.json", [9, 12],
         "edf8ee80ff125de0bfd6c37a1d185efa9e3037ce28eb1bd1d32ae0829bd264a6"),
        ("products_drifted.db", "questions_post_drift.json", [101, 103, 105],
         "a53d523f70604be0e4328f3722417895250ac35e1127cc504b609576aee70fad"),
    ]:
        database = ROOT / ".cache/weight-continuation-review" / name
        with database.open("rb") as stream:
            if hashlib.file_digest(stream, "sha256").hexdigest() != expected_hash:
                raise SystemExit(f"Unexpected database content: {name}")
        connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
        try:
            questions = json.loads((repo / "data/database_exploration" / question_file).read_text())
            for question in questions:
                if question["question_id"] not in ids:
                    continue
                deadline = time.monotonic() + 30
                connection.set_progress_handler(lambda: int(time.monotonic() > deadline), 1000)
                value = connection.execute(question["sql"]).fetchone()[0]
                tolerance = (max(question.get("tolerance", 0), abs(question["answer"]) * .01)
                             if question["answer_type"] == "float" else 0)
                row = {
                    "database": name, "question_id": question["question_id"],
                    "answer_type": question["answer_type"], "reference_value": value,
                    "matches_published_answer": abs(value - question["answer"]) <= tolerance,
                    "effective_tolerance": tolerance,
                }
                if "prc_v2" in question["sql"]:
                    stale = connection.execute(question["sql"].replace("prc_v2", "prc")).fetchone()[0]
                    row.update(stale_prc_value=stale,
                               stale_value_accepted=abs(stale - question["answer"]) <= tolerance)
                checks["queries"].append(row)
        finally:
            connection.close()
    target = OUT.with_name("database-checks.json")
    target.write_text(json.dumps(checks, indent=2) + "\n")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["--database-only"]:
        check_database()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Usage: review-task-sequences.py [--database-only]")
