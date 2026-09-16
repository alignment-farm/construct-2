# Maintenance comparison: feasibility and stronger controls

16 September 2026. Supports the [concrete comparison](../../notes/MAINTENANCE_COMPARISON.md).
This preparation inspects a published workload, checks a public implementation,
and performs read-only retrospective arithmetic. It is not fresh experimental
evidence for a forecast or an autonomous maintenance policy.

## Local review boundary and calculation

The S2 checkout was absent and was cloned using the root's documented helper.
Local HEAD and the inspected remote head both equal
`3e71eb5f146e6493c60cef26d15d86dedd2249fb`; the checkout is clean. This is exactly
the existing [root review boundary](../../studies/2026-09-15-state-support-findings.md).
The five most recent commits record publication, full audit, both fresh crossings
and retained failed readiness checks. There is no newer publication to accept.

Read AGENTS.md, README.md, STATE_SUPPORT.md, FINDINGS-STATE-SUPPORT.md, the fresh
protocol and reproduction guide. Static implementation reading covered
`maintenance_task.py`, `maintenance_explicit.py`, `state_support_experiment.py`
and `state_support_probe_selection.py`, plus dependency declarations. These establish
the finite conditions, explicit reference's privileges, reset boundaries and
possible probe access. The existing probe selector is for audits; it is not an
evaluated maintenance signal.

[retrospective-choice.json](retrospective-choice.json) records input hashes and
the six state-level contrasts. The root's small
[recalculation script](../../scripts/maintenance-choice-feasibility.py) checks
2,304 endpoint records against independently written canonical outputs from the
published rules, reconciles saved complete scores, and checks paired case sets.
It does not reload weights, retokenize outputs, rerun training or repeat the
entire preceding root audit. Reproduce from the root with:

```sh
uv run --no-project python scripts/maintenance-choice-feasibility.py ../ancillary-studies/procedure-retention-and-revision
```

The history-matching rule obtains the same aggregate total as a state oracle,
912/1,152; constant Novel obtains 888. Selection is retrospective, the six states
share three acquisition roots, and one root was selected diagnostic material.
This is a strong comparator to carry forward, not evidence that the rule will
transfer. No tested state has been reserved as fresh material for this new claim.

## Public method contact and correction of an implementation lead

P27 [2406.14026v8](https://arxiv.org/html/2406.14026v8), §§2, 4 and Appendix A,
links [AuCson/low-rank-forgetting](https://github.com/AuCson/low-rank-forgetting).
Its inspected code revision is `1128e1fdc83752f7a7f30a0dbd237afac3b97fc0`.
The earlier [preparation](../2026-09-16-study-preparation/README.md) inspected
`INK-USC/lm-forgetting-prediction-code`, a related implementation lead. That
historical inspection remains valid, but it should not be presented as an audit
of this paper's linked release.

The linked release's README supplies downloadable statistics and describes
multi-GPU model training. `run_matrix_completion.py` exposes some true entries
of a test row, fits a completion model with training rows, and evaluates the
unobserved entries. It supports additive, KNN and factorized alternatives.
The sampling call omits `replace=False`, so the requested count can contain
duplicates. A local adaptation must count unique measurements and any repeated
work; a nominal sample count is not guaranteed distinct coverage. These are
static observations, not a claimed explanation of paper results.

The implementation does not itself provide histories, counterfactual support
outcomes or a prefix-to-endpoint forecaster. Thus it narrows the method choice
without supplying the proposed experiment. P26's sequential-refinement precedent
and P46/P47's decision theory remain as assessed in the
[decision-value review](../2026-09-16-decision-value/README.md).

[implementation-retrieval.json](implementation-retrieval.json) records pinned
URLs and content hashes. No author code was executed, datasets downloaded or
dependencies installed. Paper claims are author-reported; local hardware
feasibility of an adaptation is not established by static inspection.

## Discovery scope

Supplementary web searches were `"forgetting prediction" "continual" "learner"`
and `"predicting forgetting" "sequential" language models`. Results were screened
as leads; none supplied a closer inspected empirical comparison. This does not
establish novelty. Supporting claims use the primary paper and its linked code.
The single targeted arXiv API request succeeded and is recorded in
[retrieval.json](retrieval.json), with a descriptive User-Agent and no concurrent
API clients. [discovery.xml](discovery.xml) contains one result:
[Continually Learned Pavlovian Signalling, 2305.14365v1](https://arxiv.org/abs/2305.14365v1).
Its title and abstract concern adaptive prosthetic feedback and forgetting of
predictions; methods were not inspected and it was not selected as a comparator.
The narrow query plainly does not establish exhaustive literature coverage.

The concrete effect of this reading is to retain simple public completion methods
as comparators while separating full-update sparse evaluation from early-trial
prediction. Local evidence additionally requires a no-probe history rule, which
matches the published state oracle. These findings redirect the proposed first
investment toward testing history-rule transfer rather than immediately training
a more elaborate maintenance selector.
