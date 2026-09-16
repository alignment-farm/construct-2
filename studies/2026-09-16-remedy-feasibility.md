# Remedy choice: bounded feasibility assessment

16 September 2026. The root completed the review selected in
[feedback decisions](../notes/FEEDBACK_DECISIONS.md).
**Do not commission the proposed missing-evidence versus reading-repair comparison
from these artifacts.** S4 explains the distinction but does not supply the two
actions; public retrieval work already supplies generic outcome-based routing.
The remaining comparison would require a materially different workload and
evidence, rather than a straightforward continuation of either.

This closes this feasibility phase on explanatory progress. It neither refutes
AD1 nor closes the broader question. The independent maintenance-decision-transfer
study remains underway as reported by the user; its unpublished work was not
inspected, and no ancillary assignment was changed.

## Scope and provenance

S4's clean local HEAD and remote HEAD both equal the root's accepted boundary,
`981719ffcda62fed0913461b50c0e97dbb4c10c8`. Read its AGENTS.md, README.md,
FUTURE_USE.md commission, third-phase reproduction guide, design, frozen protocol,
latest findings and recent Git history. The sequence runs from commission
`d7ce66e`, through protocol freeze `06570bd`, to that publication. No later
publication was found and no new review boundary is needed.

The material uncertainty was whether aggregate reader improvement and omissions
actually supply competing remedies. Inspecting the runner, per-seed metrics,
access rules and costs resolves that question more directly than repeating model
evaluation. The [source ledger](../sources/2026-09-16-remedy-feasibility/README.md)
records pinned CRAG and Adaptive-RAG author releases, the added literature,
static implementation checks and a reproducible artifact analysis.

## S4: the proposed retrieval action is absent

The 32-event memory has fixed addressing. Every reader receives the queried rows;
unread independent rows cannot recover distinctions lost in those rows. Raw
histories belong to the evaluator and calibration procedure, and are withheld
from alternative readers. Therefore fetching additional rows is not a remedy
for the demonstrated omissions. A raw-record fallback would introduce a retained
archive and change the published access conditions.

The fitted conditional-moment reader is a functioning repair. Across all 15
published evaluation seed × changed-task cells, its MSE is below ordinary
reading. Complete-answer accuracy is slightly lower in three cells, all from
seed 4; MSE improvement must not be described as uniform accuracy improvement.
This is aggregation of published metrics, not fresh evaluation or a paired
per-query selector test. The same histories and query hashes match the full-raw
reference, which is perfect in every cell.

The fitted read uses about 1.05 ms per 8,192-history batch versus 5.02 ms for
ordinary reading, after a 1.18 ms fitted-table construction. Full-raw direct
reading takes about .41 ms. These inherited single-batch measurements exclude
setup, I/O and several other costs; they are not deployment prices. Nonetheless,
there is no measured saving that motivates choosing ordinary decoding on some
queries. The same 512-byte episodic payload holds full raw records, with no
learned weights. Upfront storage choice thus already has a competent explicit
answer in this setting.

S4 can provide explanatory examples and donor artifacts. It does not provide
observed outcomes of retrieving missing evidence versus repairing a reader,
and its diagnostics must not be relabeled as such.

## Public implementations: useful precedents, different comparisons

CRAG's pinned release prepares internal, external and combined contexts before
inference. Its selector reads those files and generates an answer from the
selected context. PopQA has 1,399 rows in each context file and the query file;
this verifies counts, not semantic alignment. There are no released matched
answers for all actions in that inspected tree or acquisition-cost traces from
which to price an online diagnostic. The ARC external file has 1,339 rows versus
1,172 queries; the combination script also contains basic execution defects.
These limit direct reuse, not the paper's reported findings. Rebuilding a full
CRAG pipeline is unnecessary for the current scientific decision.

The sharper search found **P53, Adaptive-RAG**: outcome-derived labels already
train strategy selection, with dataset-derived labels for unresolved examples.
Its training-data ablation demonstrates a quality/work tradeoff, not an
unqualified advantage from outcome labels. This substantially answers the
generic proposal to learn retrieval strategy from prior outcomes.
[Primary paper, §3.2 and Table 4](https://arxiv.org/html/2403.14403v2).

The author release includes all-strategy predictions. On one bounded development
slice (FLAN-T5-XL, 500 NQ questions), the root recomputed normalized exact match
against released aliases and exactly recovered the stored correctness sets:

| Released strategy | Correct / 500 |
|---|---:|
| No retrieval | 67 |
| Single-step retrieval | 165 |
| Multi-step retrieval | 162 |
| Retrospective oracle across the three | 213 |

Single-step alone succeeds on 28 cases that multi-step misses; multi-step succeeds
on 25 that single-step misses. All three fail on 287. Thus competing useful
actions are available in public evidence. These are author-generated development
outputs re-scored locally, not new model results, an achievable selector, or
fresh transfer evidence. The single and multi configurations also differ in
retrieval count (15 versus 6) and iterative computation. They do not isolate
evidence availability from use of the same evidence.

## Research selection

The proposed local continuation is not selected. S4's competent explicit route
resolves its present storage/use comparison; neither CRAG context selection nor
Adaptive-RAG complexity prediction can simply be renamed an AD1 diagnosis study.
A generic outcome-trained router would repeat an established contribution.

The unresolved AD1 comparison remains specific: at a comparable failed decision
point, can accumulated intervention outcomes improve a choice between obtaining
additional evidence and using existing evidence better, beyond a developed rule
with the same observations? A meaningful contribution must separate the evidence
change from reader computation and assess complete quality with acquisition,
selection and execution costs. This is an evidence requirement for that claim,
not a requirement that the root prove a neural advantage before ancillary work.
Bounded workload discovery could be ancillary work if later selected for its
scientific value.

No immediate replacement experiment is recommended by this review. Preserve the
public implementations as reusable leads and the original predictions as written.
Further independent root research can compete on value with this unresolved
candidate; it need not wait for maintenance results or keep extending the latest
local workload.
