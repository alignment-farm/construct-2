"""Root saved-evidence review; standard library only, no model execution.

Reconstructs declared account obligations independently of the derivative grader.
The policy table is transcribed from its published investigator specification;
this checks implementation/record consistency, not real-world contract truth.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess


TERMS = {
    "Northstar": {"return": (21, 85, 250, False, False), "damage": (9, 100, 0, True, True)},
    "Harbor": {"return": (35, 90, 400, False, False), "damage": (14, 100, 0, False, True)},
    "Juniper": {"return": (18, 80, 150, True, False), "damage": (6, 95, 0, True, False)},
    "Cedar": {"return": (28, 75, 300, False, False), "damage": (11, 100, 50, True, True)},
}


def read(path):
    return json.loads(path.read_text())


def check(runtime):
    stages, failures, verified_files = {}, [], {}
    task_count = 0
    for outcome_path in sorted((runtime / "evidence/milestone-3").glob("attempt-*/runs/*/outcomes.json")):
        totals = Counter()
        for row in read(outcome_path):
            case = row["case"]
            task = case["task"]
            operation = case["plan"]["operation"]
            terms = TERMS[task["account"]][operation]
            if case["phase"] == 2 and task["account"] == "Northstar" and operation == "damage":
                terms = (16, 90, 125, False, True)
            days, percent, fee, shipping, photo = terms
            plan = {
                "operation": operation, "limit_days": days, "credit_percent": percent,
                "fee_cents": fee, "include_shipping": shipping, "photo_required": photo,
                "redact_contact": True,
            }
            assert plan == case["plan"], case["case_id"]
            eligible = task["age_days"] <= days
            credit = max(0, (task["price_cents"] * percent) // 100
                         + (task["shipping_cents"] if shipping else 0) - fee)
            expected = {
                "eligible": eligible, "credit_cents": credit if eligible else 0,
                "photo_required": photo and eligible, "contact": "[redacted]",
                "applied_plan": plan,
            }
            folder = outcome_path.parent / "store" / row["job"]["task_id"]
            artifact_path = folder / "settlement.json"
            artifact = read(artifact_path) if artifact_path.exists() else None
            assert artifact == row["artifact"]
            complete = artifact == expected and row["job"]["status"] == "succeeded"
            assert complete == row["grade"]["complete"]
            assert expected == row["grade"]["expected"]
            totals["tasks"] += 1
            totals["complete"] += complete
            memory_path = folder / "memory/result.json"
            exact_selection = None
            if memory_path.exists():
                memory = read(memory_path)
                exact_selection = sorted(r["id"] for r in memory["delivery"]["evidence"]) == case["memory_ids"]
                totals["exact_selection"] += exact_selection
                events = [json.loads(line) for line in (folder / "memory/events.jsonl").read_text().splitlines()]
                totals["authority_rejections"] += sum(
                    e.get("kind") == "memory_tool_result"
                    and e.get("result", {}).get("error") == "only current authoritative records are usable"
                    for e in events
                )
            if not complete and outcome_path.parent.name in {"final-p2-learned", "schema-learned"}:
                failures.append({"case": case["case_id"], "stage": outcome_path.parent.name,
                                 "exact_selection": exact_selection,
                                 "artifact_present": artifact is not None})
        stages[str(outcome_path.parent.relative_to(runtime / "evidence/milestone-3"))] = dict(totals)
        task_count += totals["tasks"]
        verified_files[str(outcome_path.relative_to(runtime))] = hashlib.sha256(outcome_path.read_bytes()).hexdigest()

    attempt = runtime / "evidence/milestone-3/attempt-03"
    original = read(attempt / "archive-p2.json")
    changed = read(attempt / "address-probe/view.json")
    mapping = read(attempt / "address-probe/plan.json")["mapping"]
    inverse = {new: old for old, new in mapping.items()}
    recovered = []
    for record in changed["records"]:
        recovered.append({**record, "id": inverse[record["id"]],
                          "supersedes": [inverse[x] for x in record["supersedes"]]})
    assert sorted(recovered, key=lambda r: r["id"]) == sorted(original["records"], key=lambda r: r["id"])
    return {
        "kind": "independent root saved-artifact regrading; no inference or training",
        "revision": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=runtime, text=True).strip(),
        "tasks_regraded": task_count, "all_saved_grades_match": True,
        "address_probe_changes_only_ids_and_order": True,
        "stages": stages, "selected_failures": failures, "outcome_file_sha256": verified_files,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = check(args.runtime.resolve())
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "outcome_file_sha256"}, indent=2))
