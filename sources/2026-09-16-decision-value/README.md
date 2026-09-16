# From forecast accuracy to useful observation

16 September 2026. Focused root reading following the completed placement
assessment, supporting the [maintenance-decision extension](../../notes/MAINTENANCE_DECISIONS.md#when-observation-can-change-the-decision).
No models or author implementations were run. This pass adds two theoretical
precedents and revisits the forecasting methods already mapped.

## Inspected primary methods

| Source | Exact version and scope | Consequence for the root question |
|---|---|---|
| P26 — What Will My Model Forget? | [2402.01865v3](https://arxiv.org/html/2402.01865v3), §2, sequential-refinement discussion and conclusion | Training partitions update examples; evaluation also follows sequential corrections. Thus transfer beyond a single update already has evidence. This is not a controlled comparison of observation value across independently acquired histories. |
| P27 — Low-rank Example Associations | [2406.14026v8](https://arxiv.org/html/2406.14026v8), §§4.2–4.3, Table 4, Appendix A | Offline forecasts require an additional fine-tuning run; online forecasts use measured damage after the first 10% of training. The table includes seed evaluation and matrix completion. Its prose description of online efficiency must not erase those costs. Separate task fine-tunes are distinguished explicitly from continual task learning. |
| **P46 — Smart “Predict, then Optimize”**, Elmachtoub and Grigas | [1710.08005v5](https://arxiv.org/html/1710.08005v5), §2, §3 through §3.1 | Defines decision loss through the realized cost of the chosen solution relative to the optimum. Its illustrative example separates prediction residuals from consequential ordering errors. This answers the broad theoretical premise that forecast accuracy and action quality differ. The inspected formulation assumes a known feasible region, optimization oracle and training cost vectors; it does not supply missing counterfactual outcomes for agent updates. |
| **P47 — Selecting Computations: Theory and Applications**, Hay et al. | [1207.5879v1](https://arxiv.org/html/1207.5879v1), §§1–2 through Definition 6 and its discussion | Formalizes costly observations before choosing an external action. The value of perfect information bounds expected worthwhile computation under its assumptions; one-step observation can stop prematurely when useful information requires several computations. This supplies prior theory for observation value, not an implemented maintenance policy. |

P46's surrogate optimization, consistency proofs and experiments were not audited.
P47's sampling bounds, tree-search experiments and implementations were not
reproduced. Its 2014 listing was discovered but not read; the exact 2012 version
above is the citation boundary. Numerical examples in the root extension are
new teaching constructions, not results from either paper or an ancillary study.

## What changes in research selection

Generic prediction-guided replay, decision-aware prediction and pricing of
observations already have direct precedents. The independent question becomes
more specific: does an affordable observation recover the **relative value of
available maintenance actions** across changed learners? A change in overall
susceptibility may worsen absolute forecasts without changing which support to
use. Conversely, an explicit fallback can make that same information decisive.
These are root deductions under stated assumptions, not a newly established
literature gap.

The next empirical investment should therefore turn on consequential action
differences and the observations that might resolve them. This is scientific
selection, not a prerequisite that a learned method win or another admission
gate. A bounded explanation that a fixed action suffices remains useful progress.
No new phase is commissioned.

## Retrieval and discovery limits

The single arXiv query attempt in [retrieval.json](retrieval.json) returned HTTP
429 and no metadata. It used one connection and a descriptive User-Agent; the
request was not retried. No discovery XML or successful metadata search is claimed.

Supplementary web queries were:

- `decision focused learning prediction accuracy decision regret value information Elmachtoub Grigas smart predict optimize`
- `site.arxiv.org selecting computations theory rational metareasoning Hay Russell Tolpin Shimony`

The first led to P46 and its publisher entry; the second led to P47 and the
author-hosted paper. Supporting methods were read in exact-version primary HTML.
The newer *Decision-Focused Learning: When and Why Traditional Prediction Models
Fail* and *Smart Predict-then-Optimize Method with Dependent Data* received only
search-result screening; no claims from their methods are adopted. Secondary
results supplied discovery leads only. This is a small targeted search with no
comprehensive novelty or coverage claim.

[full-text-retrieval.json](full-text-retrieval.json) records separate HTML cache
downloads, times and hashes (or failures). Web reading supplied the scopes above;
downloading a paper does not imply every section was inspected. Cached paper
mirrors remain temporary; versioned URLs are the durable references.
