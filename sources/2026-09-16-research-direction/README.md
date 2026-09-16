# Public research and the next root questions

16 September 2026. Renewed discovery following the user's request that the root
resume independent theory and literature work. Supports the
[direction note](../../notes/RESEARCH_DIRECTION.md). This pass finds substantial
prior answers to several broadly stated next steps; it does not certify the
remaining questions as novel.

## Exact versions and reading scope

P26–P35 extend the [paper map](../../studies/README.md#3-paper-map-what-we-can-build-on).
All experimental results below remain author-reported. No author code or local
model was run; implementation availability was not independently audited.
The later [preparation pass](../2026-09-16-study-preparation/README.md) adds selected
implementation checks and closer workload precedents without changing this
pass's recorded scope.

| ID | Primary source | Scope inspected and reason for inclusion |
|---|---|---|
| P26 | [What Will My Model Forget?, 2402.01865v3](https://arxiv.org/html/2402.01865v3) | §§2–5, especially forecasting splits, sequential refinement, replay comparators and inference-cost accounting. Direct overlap with MR2 and prediction-guided action. |
| P27 | [Demystifying Language Model Forgetting with Low-rank Example Associations, 2406.14026v8](https://arxiv.org/html/2406.14026v8) | §§2–4; Appendix A limitations and D seed evaluation. Sparse measured forgetting, offline/online replay variants, task generalization versus changing learner histories. |
| P28 | [When and Where to Reset Matters for Long-Term Test-Time Adaptation, 2603.03796v1](https://arxiv.org/html/2603.03796v1) | §3.3–3.5, setup/context. Adaptive reset and recovery are established interventions; domain adaptation differs from revising an authoritative rule. |
| P29 | [Cartridges, 2506.06266v3](https://arxiv.org/html/2506.06266v3) | §§2–4, §5 overview, §6 limitations. Reusable trained KV state, serving benefit and expensive preparation; a concrete placement workload. |
| P30 | [Doc-to-LoRA, 2602.15902v1](https://arxiv.org/html/2602.15902v1) | §§2–3, §6 and Appendix C.4. Amortized context-to-adapter generation and its unrelated-query interference boundary. |
| P31 | [Harness the Memory, 2608.15008v1](https://arxiv.org/html/2608.15008v1) | §§2–3, results/discussion overview, Appendices B.2–B.3 and G. Existing substrate comparison, exact adapter/cache definitions, exclusions and implementation deviations. |
| P32 | [Dual-Layer Agentic Memory, 2608.22215v2](https://arxiv.org/html/2608.22215v2) | §§3–5, Tables 1–2. Write routing, consolidation, changed knowledge and the boundary of reported costs. |
| P33 | [The Retriever Should Remember, 2608.22767v1](https://arxiv.org/html/2608.22767v1) | Method description, §§V–VIII, Table I and completion ablation. Learned access to explicit evidence; budget schedule and changing-memory assumptions. |
| P34 | [On the Fragility of Self-Improving Agents, 2608.18066v2](https://arxiv.org/html/2608.18066v2) | §§3.1, 3.3, 4.2; results overview. Text-memory dependence on task order and supplied feedback, complementary to local neural-state dependence. |
| P35 | [Popular Knowledge Propagates More Errors in LLM Knowledge Updating, 2609.08067v1](https://arxiv.org/html/2609.08067v1) | §§4–5.5, conclusion and limitations. Factual connectivity as a preservation signal; controlled substitutions and the popularity proxy limit transfer. |

P26's [ICML proceedings entry](https://proceedings.mlr.press/v235/jin24d.html)
and the Cartridges and Doc-to-LoRA author pages helped discovery. Earlier versions
of P26/P27/P29 were initially opened; the API then identified the versions above,
which supplied the subsequent methods reading. Publication dates and version
updates are separate in the metadata.

One reporting issue matters for interpreting P32: Table 1 pairs 89.77% QA EM
with 32.08% storage, and 90.71% EM with 47.85% storage. Its prose combines the
lower storage value with the higher EM. Use the table's paired configurations;
do not advertise them as one result. The table counts routing inference, not a
complete repayment calculation including the offline probing and SFT pipeline.

## Discovery, provenance and limits

Three broad arXiv API queries returned fifteen entries each, ordered by submission
date: forgetting prediction, parametric/context storage, and adaptive agent memory.
A fourth request obtained metadata for the ten selected papers. All four
requests succeeded. Queries used one connection, a descriptive User-Agent and
at least three seconds between requests. The exact requests, response headers,
timestamps and hashes are in [retrieval.json](retrieval.json); the four XML
responses are retained alongside it.

[screening.json](screening.json) records the 45 returned discovery entries and
the ten selected versions. Discovery entries received title/date screening;
closely relevant abstracts received further attention. Unselected entries are
not full-text assessments. The review cutoff is 16 September 2026, 09:24:46 UTC;
none of the returned entries required exclusion for a later version date.
The selected set also includes older work found through web discovery rather
than only recent API results.

[web-discovery.json](web-discovery.json) records ten supplementary queries,
including targeted follow-up searches. Secondary summaries supplied leads only.
Supporting claims use primary papers. Search-result rankings and snippets are
not archived. Exact-version HTML downloads succeeded for all ten selected papers;
[full-text-retrieval.json](full-text-retrieval.json) records URLs, retrieval times
and hashes. Full texts and extracted reading copies are in a temporary local
cache, not required repository artifacts.

This is a focused current search, not a systematic review. Fifteen results per
discovery query, unpaginated results, terminology choices and selective reference
following leave coverage gaps. The targeted incremental-refresh and sequential
prediction searches supplied no additional source adopted here; that is not
evidence that no such work exists. A paper's own future-work section does not
establish an unoccupied research question. The root's decisions and proposed
expectations are identified separately in the direction note.
