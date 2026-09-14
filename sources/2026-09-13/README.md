# Acquisition and transfer: focused methods reading

13 September 2026. This reading informs the next investigation under
[S2](../../studies/README.md#next-investigation-procedure-transfer).
It follows the completed procedure-acquisition and neural-memory-depth studies.
It is a targeted methods review, not a systematic search or a novelty finding.

**Status update — 14 September:** This preparation led to a completed local
recipe test and a diagnostic continuation. The first publication is accepted;
the subsequent diagnosis establishes working acquisition and a controlled
routing repair, with transfer limits. See the
[current root assessment](../../studies/README.md#procedure-transfer-acquisition-diagnosis).
The decision and prospective language below preserve the 13 September rationale.

## Closest methods

| Source and reading scope | Method and boundary relevant here |
|---|---|
| **P17. [On-Policy Context Distillation, 2602.12275v1](https://arxiv.org/html/2602.12275v1)** — §3, §§4.2–4.6, Appendices A.3 and B.2 | Trains on student-generated responses using reverse KL against a teacher with additional context. Its comparisons also change the loss and training inputs. Appendix A.3 selects checkpoints by test accuracy; B.2 reports the three best test checkpoints. These selection procedures limit interpretation of the reported test results. |
| **P18. [Procedural Memory Distillation, 2607.01480v1](https://arxiv.org/html/2607.01480v1)** — §§3.1–3.2 and 4.1 | Builds procedural memory from ongoing attempts and feedback, then uses it to condition a teacher supervising the current policy. Online memory/policy co-evolution is central. A small fixed-evidence experiment would omit that mechanism and would not reproduce this paper. |
| **P4. [SEAL, 2506.10943v2](https://arxiv.org/html/2506.10943v2)** — §§3.1–3.2 revisited | Learns the production of adaptation data using performance after updating as the reward. A stronger fixed training target alone does not reproduce its learned writer. |
| **P8. [PERK, 2507.06415v3](https://arxiv.org/html/2507.06415v3)** — §§3.1–3.2 revisited | Meta-learns adapter initialization through an inner context-learning and outer reasoning objective. This is an alternative intervention on acquisition, with a different training and resource commitment. |

These are author-described methods; no implementation or published result was
reproduced in this preparation. P18 was already identified in the acquisition
study's [literature note](../../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-literature.md).
P17 was followed from P18's reference 47. Exact versions above are the ones
read; they are not asserted to be the latest versions.

## Root decision

Prepare [procedure transfer](../../../ancillary-studies/procedure-transfer/README.md)
as a focused investigation of whether an evidence-informed acquisition method
improves new-input behavior beyond the earlier direct-imitation recipe.
Context distillation supplies an existing method to examine. The ancillary
investigator owns its implementation and any narrower causal comparison.

The local evidence motivates the question: the earlier adapter fit its twelve
training calls, yet transferred poorly, and the demonstrations left the
composition rule underdetermined. Those observations do not isolate the
training objective as the cause. S3 likewise motivates attention to interactions
in learning, without establishing a shared mechanism with language-model LoRA.

The new comparison should separate teacher usefulness, evidence sufficiency,
and student transfer. Extra training cases, verifier answers or a supplied rule
change the information available. A method comparison must disclose those
changes and the costs of producing supervision. A causal claim about where
training responses come from additionally needs the loss and supervision held
comparable; otherwise the result concerns the combined method. Prospective
evaluation should use fresh material and a checkpoint rule fixed before seeing
its results. These are implications we draw for the local question.

## Retrieval record

Two sequential arXiv API requests were attempted with a descriptive User-Agent
and at least three seconds between starts. Both returned HTTP 429; no metadata
or discovery results were obtained. The [attempt record](retrieval.json)
preserves the requests and observed errors. Error bodies and Retry-After headers
were not retained by that attempt. No further API request was made. Versioned
HTML was instead read through the web research tool using existing citations
and the paper reference above. This does not establish comprehensive coverage
of adjacent or newer work.
