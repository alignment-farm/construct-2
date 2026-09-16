# Maintenance-decision transfer publication review

16 September 2026. [Root assessment](../../studies/2026-09-16-maintenance-transfer-findings.md).
Ancillary local and remote HEAD: `be7a508bfea002baceec72f32f7f9d6f73f7861a`.
Read instructions, README/commission, findings, frozen protocol, development
decision, methods, reproduction, relevant implementation and Git history.
The earlier root preparation boundary was `86d00753bf43beaf48dbc0ce4a6f009475eda6eb`.

The study's `scripts/analyze.py` was rerun into a temporary file and exactly
matched `evidence/final-analysis.json`. Its `scripts/verify_phase.py` reproduced
the phase audit except the expected current-Git-revision field. These standard-
library checks verify recorded file hashes, saved scores, selector choices from
permitted panels, predictor freeze, costs and audit ledgers. They do not execute
model training or generation. Temporary outputs were not added as duplicate
publication artifacts.

The root additionally implemented
[review-maintenance-transfer.py](../../scripts/review-maintenance-transfer.py),
without importing the study's scorer. Independently specified canonical outcomes
agree with all 5,856 saved complete-task scores. It checks assessment panel/identity
separation, all twelve fresh endpoint totals, the consequential 701 tie, predictor
identity at the pre-assessment freeze and disjoint prefix-prediction ranges.
It rebuilds the explicit table from 192 checked evidence labels and verifies
all 192 final responses. [verification.json](verification.json) records source
hashes, counts and diagnostic results.

```sh
uv run python scripts/review-maintenance-transfer.py \
  --study ../ancillary-studies/maintenance-decision-transfer \
  --output sources/2026-09-16-maintenance-transfer-review/verification.json
```

The independent text check validates complete outcomes, not every component
score, tokenizer, gradient, checkpoint or optimizer transition. Model reload
and continuation claims remain supported by the ancillary's recorded audits;
they were not repeated by the root. The study and S2 working trees were unchanged.

The study's primary-method contact uses P26/P27/P46/P47 and pinned author code,
as recorded in its `notes/methods.md`; these are inspected methods, not local full
reproductions. Existing root ledgers retain their prior reading scopes. This
review adds no public paper or discovery query and commissions no experiment.
