# Continuing-consolidation review — 18 September 2026

Supports the [root assessment](../../studies/2026-09-18-continuing-consolidation-findings.md).
Study boundary: `80c17dbfb63116cd35ab5faf23f527178fec3e5b`, advancing from the
instruction at `8b299bd` and first reviewed publication `491c0f8`. The study
checkout is clean. Construct Runtime remains pinned at
`9ffb10a66180626b80127fb1892b2cf71e39d946`; study-owned wrapper and lower-rate
trainer adaptations are described in its provenance, not changes to that pin.

## Inspection and independent checks

Read study instructions, README, continuing-work brief, Git history, publication,
protocols 03/04, reproduction guide, discovery and resource provenance. Inspected
the environment, normalized views, teaching, controller, audits, frozen states,
raw events and all fresh submitted queries. Selected source-only diagnostics
explain the acquisition development and its limits.

The [root checker](../../scripts/review-weight-continuation.py) independently
regrades 229 saved task executions, recounts raw usage and actions, verifies
publication/state/artifact/adapter hashes, common source access in saved states,
cumulative training records and decision timing. It replays 22 distinct reference
queries and 46 saved fresh/preserved submissions against both hash-verified
databases. [checks.json](checks.json) preserves the results and q112 diagnosis.
All published score and usage counts checked agree.

```sh
uv run --no-project python scripts/review-weight-continuation.py
```

Before running, obtain `products.db` and `products_drifted.db` from the
[pinned dataset](https://huggingface.co/datasets/continual-learning-bench/database-exploration/tree/a0cc57eeb9a54f01c0490a1b46cb705b4e05aa19)
in `.cache/weight-continuation-review/`. The script checks the published SHA-256
values before opening either read-only. This review downloaded that revision;
the large cache is ignored by root Git. Native SQLite version is recorded in
the checks. A Python `statistics.median` aggregate supplies the worker's median
operation on this host. SQL timeout is 30 seconds for replay; worker execution
used 20. This is result reproduction, not latency reproduction.

No model inference, optimizer step or fresh task was run. Training-step counts
and saved weight hashes are verified; unchanged base/changing tensor assertions
are checked as recorded, not independently recomputed by reloading the model.
Source parity is checked in stored assets/records, not through every live worker
interface. The study's full model-dependent audit was not rerun. Controller
isolation and public pretraining contamination are not proven absent by replay.

q112 reproduces an accidental output match by a count-ranked stale query and a
price-ranked updated query missing the reference filter. The root diagnostic
adds that filter to the existing query without model calls. Original grades,
failed runs and ancillary publication remain unchanged.

## Public methods and selection

**P90 — [Continual Learning Bench, 2606.05661v1](https://arxiv.org/html/2606.05661v1).**
Read the continual-learning framing, task criteria (§§3.1–3.2) and database
methods/scoring (Appendix A.4). Methods were inspected; public system results
remain author-reported and were not reproduced. The upstream code revision is
`5f8c50eb1e84b2eda2ef4faff757dfc812a0ea26`; the local study's discovery records
its selected code and instance inspection.

The benchmark already **answers** whether real artifacts with constructed latent
structure and drift can support an inspectable continuing workload. It **narrows**
our comparison: supplying normalized views removes much of the upstream schema
discovery/migration target. It **redirects** the next question toward learned
query composition and evidence use, not a claim of reproducing CL-Bench's
continual-learning mechanism or leaderboard. The three product groups share one
history. This selected methods reading does not establish broad literature coverage.

[metadata.xml](metadata.xml) is copied unchanged from the ancillary's cached
`continuation/sources/arxiv-metadata.xml` at the reviewed publication. It records
the exact P90 version plus BIRD-INTERACT and HarnessForge; copying metadata does
not upgrade the root reading status of the other entries. This review reopened
the versioned primary HTML and made no new arXiv API request.

The [previous P42/P89 reading](../2026-09-17-weight-consolidation-review/README.md)
already identifies corrected learner trajectories and policy/harness alignment.
Those methods narrow a possible teaching comparison; the current traces do not
establish that either method would fix this learner. No new experiment is selected
solely because a paper supplies a plausible technique.
