# Actual task-sequence inspection — 20 September 2026

Supports the [root comparison](../../notes/TASK_SEQUENCE_COMPARISON.md). This
extends the [earlier methods reading](../2026-09-20-continuing-capability/README.md)
with public artifacts and local reference execution. It does not reproduce paper
model results or review a new ancillary publication. No ancillary or derivative
review boundary advances.

## Pinned sources and inspection

| Source | Revision | Inspected boundary |
|---|---|---|
| [SCBench problems](https://github.com/gabeorlanski/scb-problems/tree/ef6a9dd13911566b6b01075ca121758c9f7b5c5f) | `ef6a9dd13911566b6b01075ca121758c9f7b5c5f` | README, Apache-2.0 license, dependencies; ETL/code-search configs, checkpoint 1–4 requirements, test interfaces and selected assertions; reference entry points/dependencies. ETL checkpoint 5 interface and file-query-tool inventory only surveyed. |
| [SlopCodeBench runner](https://github.com/SprocketLab/slop-code-bench/tree/c2a53b46ed7227545951168e1dfeea8a6eec9316) | `c2a53b46ed7227545951168e1dfeea8a6eec9316` | README, instructions, MIT license, checkpoint guide, prompt template, context-reset and prior-test selection code. Not installed or run. |
| [CL-Bench](https://github.com/pgasawa/continual-learning-bench/tree/5f8c50eb1e84b2eda2ef4faff757dfc812a0ea26) | `5f8c50eb1e84b2eda2ef4faff757dfc812a0ea26` | Root/task instructions and READMEs, Apache-2.0 code license; database question files, schedule/variant, prompts, ordering, migration switch, SQL interface and numeric grading. Sparse checkout of the relevant code/data. |
| [Database snapshots](https://huggingface.co/datasets/continual-learning-bench/database-exploration/tree/a0cc57eeb9a54f01c0490a1b46cb705b4e05aa19) | `a0cc57eeb9a54f01c0490a1b46cb705b4e05aa19` | Reused root's previously downloaded files; reverified SHA-256 against the pinned dataset API's LFS metadata. Selected schemas/queries only; no dataset redistribution. Code license is not an assessment of underlying Amazon data terms. |

The exact paper readings remain **P96 `2603.24755v2`** and **P90 `2606.05661v1`**.
The runner is a later September revision; the problem commit is from May. These
pins define this inspection, not a claim to have recovered the paper's execution
environment. [artifact-manifest.json](artifact-manifest.json) records repository
heads, clean tracked status, key file hashes and database sizes/hashes. Large
assets stay in ignored `.cache/`. No new arXiv API request was needed.

## Executed checks

The [review script](../../scripts/review-task-sequences.py) directly invokes the
separate problem repository's pytest interface with explicit entrypoint and
checkpoint arguments. It does not invoke the SlopCodeBench Docker runner.
Minimal dependencies are pinned in the script. Published implementations are
examiner sanity checks, not agent-produced acquisition or demonstrations for
training. All benchmark canaries remain intact in the cached upstream files.

| Reference implementation | Included checkpoint tests | Passed | Local elapsed time |
|---|---|---|---|
| ETL checkpoint 3 | 1–3 | 117/117 | 7.76 s |
| ETL checkpoint 4 | 1–4 | 134/134 | 8.26 s |
| Code search checkpoint 3 | 1–3 | 47/47 | 1.62 s |
| Code search checkpoint 4 | 1–4 | 75/75 | 5.32 s |

[reference-checks.json](reference-checks.json) saves exact commands, platform,
dependency versions, exit statuses and log/JUnit hashes. Counts include repeated
earlier tests and are not independent samples. Times cover local pytest processes,
not installation, acquisition or model inference. No tests were skipped; hidden
reference correctness and test exhaustiveness were not independently proven.

[database-checks.json](database-checks.json) records q9/q12 against the original
database and q101/q103/q105 against the migrated one. All five upstream reference
queries reproduce their answers. A diagnostic changes only `prc_v2` to stale
`prc` in the three post-migration queries. Applying the numeric comparator
inspected in `task.py` accepts q101 (100.85 versus 101.8, tolerance 1.018) and
q105 (24.0 versus 24.5, tolerance 0.5), and rejects q103 (1035 versus 1049,
integer equality). These are SQL/comparator replays, not full framework runs or
agent failures. No benchmark files or published grades were changed.

To reproduce, clone the repositories at the pins above into
`.cache/task-sequence-review/{scb-problems,cl-bench}`. A sparse CL-Bench checkout
needs `src/tasks/database_exploration` and `data/database_exploration`.
Obtain the two pinned database snapshots in `.cache/weight-continuation-review/`.
Then run from the root:

```sh
uv run scripts/review-task-sequences.py
uv run scripts/review-task-sequences.py --database-only
```

The script checks source revisions and database hashes before replay. Generated
reports retain native paths and timing for the inspecting host; a rerun replaces
those reports. SQLite opens the snapshots read-only with bounded query time.

## What this changes

P96's artifacts **answer** whether short inherited-program sequences with runnable
regression checks already exist. They **narrow** feasibility uncertainty to
participant acquisition, feedback adaptation and memory value; no new general
harness is needed to begin. They **redirect** the first pilot toward ETL, with
code search as a complementary setting, rather than selecting the hardest failure.

P90's artifacts **answer** whether the migration examples are available for local
inspection. They **narrow** interpretation of approximate answer success and
corrective feedback. They **redirect** any local reuse toward explicit computation
checks and a declared history/feedback boundary; the inspected task is not already
a maintained-program comparison. Earlier local normalization and exposure remain
reasons to prefer a different first workload.

AgentCL and AgingBench remain methods precedents from the preceding ledger;
their executable assets were not inspected in this pass. No third-party audit
supports these conclusions. Root selection is an inference from the inspected
assets and prior local findings, not an author-reported ranking of these workloads.
