# Evidence-use publication review — 17 September 2026

Root review of [evidence-use-under-revision](https://github.com/alignment-farm/evidence-use-under-revision)
at `da1233fdfb26fe6c5daa337a3dbf9f784f34f9f7`. Local and remote HEAD agree;
the ancillary tree is clean. Prior boundary: preparation
`c3667e301fa4b9b62476739cdf9f16331642dbd4`. No ancillary files were changed.

Read AGENTS.md, README/brief, FINDINGS.md, methods, reproduction instructions,
development/order/final protocols, fresh binding review, recipe decision and Git
history. Inspected workload, experiment, runtime and analysis code; reviewed the
publication-v2 cost ledger and the separate audit's scope. The material questions
were score validity, checkpoint selection timing, request/binding separation,
the causal scope of history/order comparisons and the repayment accounting.

## Reproducible checks

From the root:

```sh
uv run python scripts/review-evidence-use.py \
  --study ../ancillary-studies/evidence-use-under-revision \
  --output sources/2026-09-17-evidence-use-review/checks.json
```

The [script](../../scripts/review-evidence-use.py) does not import study code.
[checks.json](checks.json) records exact source hashes, 1,728 rescored primary
responses, 1,280 checked update targets, 80 recorded training-fit scores and 288
checked executable outputs. It verifies run hash manifests, all complete-score
tables, candidate timing sums, full-bank consumption at 256, no exact train/eval
requests, distinct fresh initialization, identical order-diagnostic data and
controls, and unchanged protocols/decision relative to pre-fresh code `8e93219`.
It reconstructs fresh-entity/rebound, changed-answer and unchanged-retention
groups and compares varied 128 with both contextual lessons and base.

The root check's first draft selected the first REQUEST in a lesson prompt,
which belonged to a historical example. That assertion failed; the checker was
corrected to scope REQUEST after CURRENT. The successful rerun changes no raw
evidence and reproduces the published scores. This is the same parsing hazard
the study separately documented during its own analysis development.

These checks reproduce saved-text results and accounting. They do not regenerate
responses, validate model provenance from a new download, retokenize, repeat
gradients, reload adapters or independently measure timing. The study's separate
reload audits remain reported evidence. No new model run was performed.

## Public interpretation

Revisited the exact already-indexed [P57 version, 2410.10796v3](https://arxiv.org/html/2410.10796v3),
especially §§4.3–4.4 and 6. Its methods/results narrow an interpretation of the
later acquisition regression; they do not prove the local mechanism. P54–P59's
other status remains as recorded in the [selection ledger](../2026-09-16-evidence-use/README.md).
This targeted revisit adds no paper and makes no new novelty claim. Independent
public-artifact inspection for executable experience continues separately.

The [root assessment](../../studies/2026-09-17-evidence-use-findings.md) accepts
the bounded phase, assesses EU1–EU3 without rewriting them, and separates a
favorable measured candidate cost from reliable full-cost deployment repayment.
