# Migration and correction-lineage publication review — 17 September 2026

This ledger supports the [root assessment](../../studies/2026-09-17-migration-lineage-findings.md).
It advances procedural-memory-migration from preparation `f7ca4fc` to publication
`5a670d355491a853e32779260bfe73ea09f02f45`, and correction-lineage from `b5853b7`
to `f8ad1e1ce8b9842efa90305c1206b8690578a204`. Both local trees were clean; direct
`git ls-remote origin refs/heads/main` matched each HEAD. No ancillary writes or
new model calls occurred.

## Evidence reviewed

Read both repositories' AGENTS, README/brief, reproduction instructions, latest
publication and Git history. For migration, read the acquisition/calibration/final
protocols, development log, method ledger, experiment, migration, workload,
audit/replay and policy-report code, bank/policy artifacts, manifests and saved
outcomes. For lineage, read the pilot/fresh protocol, prospective maintenance
diagnosis, separately frozen read diagnostic, public methods, runner, analysis,
evaluator checks, saved fixtures, requests, outputs and cost summaries.

Material uncertainties were source acquisition, identical experience access,
policy timing, cost denominators, SQL fixture coverage, acquired versus supplied
lineage, and whether state-repair errors caused subsequent task failures.

- The [root checker](../../scripts/review-migration-lineage.py) independently
  totals raw calls/costs, reconstructs calibration choices, verifies migration's
  370-file evidence manifest and compares reported outcomes with raw responses.
  For lineage it derives expected state from authoritative source text without
  importing the study's fixture/scorer, verifies repair outputs and subsequent
  orders, checks all 96 workload/diagnostic request hashes, and reproduces costs
  over zero, one and two corrections. It checks identical use requests/outputs
  across arms and identical diagnostic requests except for task wording.
  Results: [checks.json](checks.json).
- After reading their code, ran migration's `scripts/audit.py` and `scripts/replay.py`
  with bytecode writes disabled. They checked 216 calls, common source access,
  pinned models, unchanged pre-evaluation policy and matched final tasks, then
  replayed all 108 submissions with each record's committed generator. All passed.
  This is reproduction with the study's verifier, not an independent SQL oracle.
- Reran its inspected supplemental temporal checker: all twenty saved queries
  retain their labels on twelve fixtures each after event IDs are decoupled from
  timestamps. The reference query passes and the max-ID-only mutant fails.
  [temporal-replay.json](temporal-replay.json) is a post-hoc verifier audit, not
  new model evidence or an additional selection set.
- Ran lineage's inspected offline evaluator checks: erasure, omissions, stale
  state, bool/int confusion, independent support and link scoring passed. The
  separate root scoring confirmed all repaired states and the reported 4/6
  complete fresh episodes per arm. No aggregate results were silently repaired.

To reproduce root accounting, with both studies checked out at the full revisions
above: `uv run python scripts/review-migration-lineage.py`. An optional argument
sets the ancillary parent directory. The script only reads and emits JSON.

## Focused public follow-up

The [selection ledger](../2026-09-17-independent-study-selection/README.md) remains
the methods boundary for P37 and P77–P84. Neither ancillary study replicates those
systems. Local observations are distinguished from the author-reported results
below; no author implementation was executed.

**P84 revisited — [model-upgrade memory portability, 2609.05339v1](https://arxiv.org/html/2609.05339v1).**
Revisited Appendix C's paid twenty-probe forecast and the previously inspected
recovery comparison. The paper already addresses early migration signals; it
does not establish that buying those signals improves a deployed choice after
their cost. **Narrows** the local interpretation: successful selection and lower
use cost must be separated from total repayment against unchanged inheritance.
The new local recipient is smaller, not an evaluated upgrade.

**P83 revisited — [StateAuditor, 2608.01619v1](https://arxiv.org/html/2608.01619v1).**
Revisited §§6.3–6.4. Source-grounded auditing has positive author-reported results
and limits, including over-correction; extracting unstated stale premises is a
specific reported bottleneck. **Narrows** the local explanation: correct state
does not guarantee correct behavior, but the local arithmetic wording contrast
does not demonstrate the paper's stale-premise mechanism or replicate its audit.

**P86 — [MemLineage, 2605.14421v1](https://arxiv.org/html/2605.14421v1).**
Read §§3.5, 6.4 and §8's recovery discussion. Exposure tracing and paid semantic
attribution are explicit alternatives; a propagation guarantee depends on edge
recall. The reported microsecond timings concern system primitives, not a complete
LLM attribution budget. Denying an unauthorized action differs from recovering
task utility; authority repair assumes trusted parameter provenance.
**Answers** generic lineage enforcement and **narrows** future value claims to
acquisition, maintenance and complete behavior. It does not answer whether our
acquired semantic support beats rebuilding. The local spurious suggestion link
is not an observed attack or security failure. No architecture is commissioned.

Two supplementary web queries searched procedural migration/calibration costs
and correction/lineage/rebuild costs. MemLineage was the new primary lead followed;
other returned implementation pages/commentaries remain discovery results and
support no claims here. This is a targeted pass, not a coverage or novelty review.
One cached arXiv ID request verifies P86 as v1, published/updated 14 May 2026;
[retrieval.json](retrieval.json) records URL, UTC time, descriptive User-Agent and
hashes for metadata and versioned HTML. No other metadata API/OAI request was
issued in this review. P83/P84 reuse exact versions from the selection ledger.

The public reading and local findings support bounded closure. Further selection
should identify consequential decisions on continuing tasks where competent
unchanged use or cheap rebuilding no longer settle the comparison. They do not
justify extending the latest experiment solely because a broader question remains.
