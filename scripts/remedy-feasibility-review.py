"""Read pinned published artifacts; no training, generation, or source edits."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import string
import subprocess
import tarfile

PINS = {
    "s4": "981719ffcda62fed0913461b50c0e97dbb4c10c8",
    "crag": "de7c2961ae624a1483a138c5798e1f6d0c4fb0e0",
    "adaptive": "0c88670af8707667eb5c1163151bb5ce61b14acb",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def normalize(text):
    text = "".join(c for c in text.lower() if c not in string.punctuation)
    return " ".join(re.sub(r"\b(a|an|the)\b", " ", text).split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in PINS:
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"revisions": PINS, "source_sha256": {}, "scope":
              "Published metric aggregation and static release review; no new model evaluation."}
    for name, pin in PINS.items():
        root = getattr(args, name)
        head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
        assert head == pin, (name, head)

    def read(name, relative):
        data = (getattr(args, name) / relative).read_bytes()
        result["source_sha256"][f"{name}/{relative}"] = digest(data)
        return data

    cells = []
    for seed in range(5):
        prefix = "future-use/analysis/evaluation/"
        expected = json.loads(read("s4", prefix + f"s{seed}-expected.json"))["result"]
        raw = json.loads(read("s4", prefix + f"s{seed}-full_raw.json"))["result"]
        for key in ["data_sha256", "query_sha256"]:
            assert expected[key] == raw[key], (seed, key)
        for task in ["parity2", "parity4", "agree_ab"]:
            cells.append({"seed": seed, "task": task,
                          "ordinary": expected["metrics"]["ordinary"][task],
                          "fitted": expected["metrics"]["fitted"][task],
                          "full_raw": raw["metrics"]["ordinary"][task],
                          "population_irreducible_mse": expected["population_optimal_mse"][task]})
    result["s4"] = {"cells": cells,
                    "fitted_lower_mse_cells": sum(c["fitted"]["mse"] < c["ordinary"]["mse"] for c in cells),
                    "fitted_lower_accuracy_cells": sum(c["fitted"]["accuracy"] < c["ordinary"]["accuracy"] for c in cells),
                    "full_raw_perfect_cells": sum(c["full_raw"]["accuracy"] == 1 for c in cells),
                    "costs": json.loads(read("s4", "future-use/analysis/costs.json"))}

    counts = {}
    for task in ["popqa", "pubqa", "arc_challenge", "bio"]:
        counts[task] = {rel: len(read("crag", f"data/{task}/{rel}").decode().splitlines())
                        for rel in ["sources", "ref/correct", "ref/incorrect", "ref/ambiguous"]}
    result["crag"] = {"cached_line_counts": counts,
                      "limits": "Counts do not establish semantic alignment; no matched action answers or acquisition timing inferred."}
    for rel in ["README.md", "run_crag_inference.sh", "run_knowledge_preparation.sh",
                "scripts/CRAG_Inference.py", "scripts/internal_knowledge_preparation.py",
                "scripts/external_knowledge_preparation.py", "scripts/combined_knowledge_preparation.py",
                "scripts/eval.py"]:
        read("crag", rel)

    # One pre-existing development slice: useful for feasibility, not new generalization evidence.
    blob = read("adaptive", "predictions.tar.gz")
    del blob
    with tarfile.open(args.adaptive / "predictions.tar.gz") as archive:
        members = archive.getnames()
        successes = {}
        ids = None
        gold_reference = None
        selected = {}
        for arm, prefix in [("zero", "nor"), ("single", "oner"), ("multi", "ircot")]:
            choices = [n for n in members if f"/dev_500/{prefix}_qa_flan_t5_xl_nq_" in n
                       and n.rsplit("/", 1)[-1] == "prediction__nq_to_nq__dev_500_subsampled.json"]
            assert len(choices) == 1, choices
            prediction_path = choices[0]
            directory, filename = prediction_path.rsplit("/", 1)

            def member_json(name):
                data = archive.extractfile(name).read()
                result["source_sha256"]["adaptive/archive/" + name] = digest(data)
                return json.loads(data)

            predictions = member_json(prediction_path)
            golds = member_json(directory + "/" + filename.replace("prediction__", "ground_truth__", 1))
            labels = member_json(directory + "/" + filename.replace("prediction__", "zero_single_multi_classification__", 1))
            assert set(predictions) == set(golds)
            if ids is None:
                ids, gold_reference = set(predictions), golds
            assert set(predictions) == ids and golds == gold_reference
            correct = {qid for qid, pred in predictions.items()
                       if any(normalize(pred) == normalize(g) for g in golds[qid])}
            assert correct == set(labels), (arm, "published correctness mismatch")
            successes[arm] = correct
            selected[arm] = prediction_path
        union = set().union(*successes.values())
        result["adaptive"] = {
            "scope": "FLAN-T5-XL, NQ dev_500; recomputed normalized exact match against released aliases.",
            "selected_archive_members": selected, "queries": len(ids),
            "correct_by_arm": {k: len(v) for k, v in successes.items()},
            "oracle_union_correct": len(union), "all_fail": len(ids - union),
            "single_only_vs_multi": len(successes["single"] - successes["multi"]),
            "multi_only_vs_single": len(successes["multi"] - successes["single"]),
            "published_labels_match_recalculation": True,
            "limits": "Full-information retrospective outcomes; no learned selector or same-evidence reader intervention evaluated.",
        }
    for rel in ["README.md", "evaluate.py", "classifier/preprocess/preprocess_utils.py",
                "classifier/preprocess/preprocess_binary_train.py",
                "classifier/preprocess/concat_binary_silver_train.py",
                "classifier/postprocess/postprocess_utils.py"]:
        read("adaptive", rel)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"s4_cells": len(cells), "s4_fitted_lower_mse": result["s4"]["fitted_lower_mse_cells"],
                      "crag_counts": counts, "adaptive": result["adaptive"]}, indent=2))


if __name__ == "__main__":
    main()
