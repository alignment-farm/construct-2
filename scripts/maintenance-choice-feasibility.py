"""Read-only retrospective choice arithmetic; no learner or forecast is run."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", type=Path)
    args = parser.parse_args()
    expected_revision = "3e71eb5f146e6493c60cef26d15d86dedd2249fb"
    revision = subprocess.check_output(
        ["git", "-C", str(args.study), "rev-parse", "HEAD"], text=True
    ).strip()
    assert revision == expected_revision, revision
    runs = {
        401: "state-support-development-v1",
        501: "state-support-final-seed501-v1",
        502: "state-support-final-seed502-v1",
    }
    cells, inputs = [], []
    for seed, run in runs.items():
        path = args.study / "evidence" / run / "responses.jsonl"
        data = path.read_bytes()
        inputs.append({"path": str(path.relative_to(args.study)),
                       "sha256": hashlib.sha256(data).hexdigest()})
        groups = {}
        for line in data.splitlines():
            row = json.loads(line)
            if "--" not in row["state"]:
                continue
            assert row["version"] == 2 and row["repeat"] == 0
            c = row["case"]
            eligible = bool(c["certified"] or
                            (c["channel"], c["priority"]) in
                            {("copper", "fast"), ("violet", "slow")})
            if not eligible:
                expected = f"FAIL SKIP SKIP {c['stock']} HELD"
            elif not c["stock"]:
                expected = "PASS SKIP SKIP 0 WAIT"
            else:
                expected = "PASS RESERVE SHIP 0 SENT"
            complete = row["raw"].strip() == expected
            assert complete == row["scores"]["complete"]
            group = groups.setdefault(row["state"], {})
            key = json.dumps(c, sort_keys=True)
            assert key not in group
            group[key] = complete
        assert len(groups) == 4
        for history in ("novel", "bridged"):
            n, b = groups[history + "--novel"], groups[history + "--bridged"]
            assert n.keys() == b.keys() and len(n) == 192
            cells.append({"seed": seed, "history": history,
                          "novel": sum(n.values()), "bridged": sum(b.values())})
    totals = {a: sum(c[a] for c in cells) for a in ("novel", "bridged")}
    oracle = sum(max(c["novel"], c["bridged"]) for c in cells)
    matched = sum(c[c["history"]] for c in cells)
    assert (totals["novel"], totals["bridged"], oracle, matched) == (888, 825, 912, 912)
    print(json.dumps({"scope": "Retrospective, equally weighted six published states; not independent trials or a held-out policy test",
                      "study_revision": revision, "inputs": inputs,
                      "endpoint_responses_checked": 2304, "cells": cells,
                      "policy_denominator": 1152, "fixed_support_totals": totals,
                      "state_oracle_total": oracle, "history_matching_total": matched,
                      "oracle_gain_over_best_fixed": oracle - max(totals.values()),
                      "oracle_gain_over_history_matching": oracle - matched}, indent=2))


if __name__ == "__main__":
    main()
