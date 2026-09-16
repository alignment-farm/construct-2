# Learned access did not repay its cost on a directly addressable collection

16 September 2026. Root assessment of
[memory-placement-under-revision's findings](https://github.com/alignment-farm/memory-placement-under-revision/blob/73b8448572f6c3a1b955eecc8d7611ef7f80b537/FINDINGS.md)
([local](../../ancillary-studies/memory-placement-under-revision/FINDINGS.md)).

**Accept the publication and close this bounded experimental phase.** A functioning
learned reranker improves predictions of relevance scores in stable use and after
content edits. It does not improve complete answers or repay acquisition against
competent account-aware lexical retrieval. This resolves a local placement choice
and separates statistical learning from useful deployment. It does not resolve
the broader useful-lifetime question or test learned storage of document content.

## Publication and review boundary

Reviewed head: `73b8448572f6c3a1b955eecc8d7611ef7f80b537`, matching `origin/main`
and the live remote branch; the study working tree was clean. Evidence is published
at `be3594a`, with fresh execution revisions `661fedf` and `8ce3332` and the protocol
frozen at `bb5d737`. Their roles are documented in the publication.

The root read the findings, frozen protocol, development decisions, cost and
outcome qualifications, aggregate tables, relevant runner/retrieval/analysis code,
and selected raw traces. An independent read-only calculation reparsed the saved
responses and checked all 768 arm results across 128 requests against saved targets.
Correctness, source-support flags, affected-case counts, paired contrasts, score
calls and the reported imputation/historical-mean diagnostics reconcile. Both
study audit records report success. The root did not independently rederive every
target from document text, reload the 24 saved learner states, or rerun models.
Those deeper checks remain reported study evidence.

## What the comparison establishes

Twelve documents contain named-account rules. Every method receives the same
current text and requests. The cheap control uses account names visible in document
IDs and questions, then BM25 ordering; the learned methods receive the same
priorities. This is legitimate workload structure, not privileged gold retrieval.

| Method | Complete three-value answers | Scored query–document pairs |
|---|---:|---:|
| Account-aware lexical retrieval | 127/128 | 0 |
| Full pointwise reranking | 127/128 | 1,536 |
| All acquired observations, without completion | 126/128 | 488 |
| Full current context with actual KV reuse | 124/128 | 0 |
| EARM, retain document identities | 120/128 | 488 |
| EARM, invalidate changed identities | 121/128 | 509 |

The counts pool two acquisition streams and their five separate continuations;
they are not one 128-request deployment or 128 independent learning histories.
Retained EARM has one paired win and eight losses against lexical retrieval, and
one win/seven losses against observed-only. Lexical retrieval supplies sufficient
evidence for every request; its sole failure is truncation. There is no demonstrated
answer-quality benefit for the learned access mechanism to amortize here.

That conclusion follows functioning acquisition and diagnosis. Development
improved a weak raw-BM25 control using visible account identity, compared learner
ranks and repaired the common answer instruction before fresh evaluation. Retained
EARM's missing-score MSE is 0.0987 in stable reuse, versus 0.1363 for a historical
row mean built from the same observations. Under narrow/broad content edits the
corresponding pairs are 0.1007/0.1381 and 0.1133/0.1424. Learned structure predicts
the scorer better in these conditions; convergence alone is not the evidence.
The target remains the model scorer's ratings, not independently labeled relevance.

## Assessment of the prospective expectations

The original [placement expectation](../notes/RESEARCH_DIRECTION.md#b-when-does-a-learned-memory-component-repay-its-cost-before-it-needs-revision)
and [AD3](../notes/ADAPTATION_DECISIONS.md#three-predictions-and-their-possible-failures)
remain unchanged. The finding has different force for their different parts.

| Expectation | Assessment |
|---|---|
| Longer reuse can repay learned-access acquisition relative to competent explicit access. | **Not demonstrated here.** All methods complete stable sequences; EARM saves scoring against full reranking, while lexical retrieval needs none. The two reuse lengths also use different seeds, preventing a causal length comparison. |
| Access experience can survive content changes better than changed evidence needs. | **Supported at the score-prediction level, with limits.** Under changed evidence needs EARM MSE rises to 0.2263, essentially matching the historical mean's 0.2283 and trailing the current-anchor mean's 0.2124. Different query families and cases prevent interpreting this as an isolated causal effect of relevance change. |
| Preserved access experience produces useful quality/cost advantages after revision. | **Weakened in this workload.** The cheap control matches or exceeds aggregate quality throughout. Predictive persistence does not establish useful persistence relative to the alternative. |
| Joint consequential content and evidence changes can be handled. | **Unresolved by this sample.** Neither combined branch contains an answer-changing target. The narrow/broad branches contain ten such requests, which must not be conflated with the combined condition. |

AD1's learned intervention selector and AD2's decision transfer across receiving
learners were not tested. Keeping or invalidating identities are supplied policies;
the system did not learn when to choose between them.

## Why the failures and costs matter

Seven of retained EARM's eight primary failures are truncated outputs under the
common 512-token ceiling; one lacks sufficient retrieved evidence. Some extra
documents prompt longer reasoning about irrelevant account rules. A larger output
budget might change the ranking, but would be a new comparison with additional
cost. The present answer gap cannot be attributed entirely to missing evidence
or to irreversible loss of learned relevance.

There is also one accidentally correct unsupported vector. Preserving the frozen
endpoint gives 120/128; requiring a known sufficient source as a post hoc diagnostic
gives 119/128. On the ten answer-changing requests, retained EARM has nine correct
vectors but only eight with sufficient evidence; invalidation has nine, and all
explicit controls ten. No wrong vector matches the obsolete target. Thus absence
of stale answers is insufficient evidence of successful revision.

Costs reinforce the bounded conclusion. Retention requires 77,142 uncached input
and 32,988 output tokens across scorer and answerer, versus lexical retrieval's
37,002 and 30,519. Its matrix fitting adds about 1.23 seconds; inference dominates
the measured work. Full context actually reuses KV state, so the comparison does
not manufacture a learned advantage by denying caching. Per-arm timings allocate
shared generations from an interleaved experiment and are not independent deployment
benchmarks. No wall-time, monetary or energy crossover follows from them.

## Connection to public research and the root account

The root revisited [EARM v1, §§IV–VIII](https://arxiv.org/html/2608.22767v1).
Its positive evaluation uses conversational memory, a fixed store and a semantic
retrieval comparator. The paper identifies reusable relevance structure, a fixed
scoring schedule and noisy relevance judgments as consequential assumptions.
This local adaptation studies another regime with explicit entity addressing and
revision; it does not refute the published conversational result. The local
observed-only control also ranks all acquired candidates rather than filtering
only the mixed context. This was a focused comparison with an already mapped
source, not a new comprehensive literature search.

The root's enduring directive is unchanged. The result adds a concrete condition
to its hybrid hypothesis: **persistent predictive structure can be learnable
without being worth learning for the current task and available alternatives.**
The choice depends on what work the learned component replaces, and on how the
receiving model uses its outputs. Here direct addressing already solves access,
while context selection also changes the answerer's ability to finish within budget.

The study can stand down with its publication sufficient. The broader question
remains open because only learned access was tested, reuse was short, and there
was no consequential joint-change sample. Those limitations do not by themselves
justify another immediate round. A future placement investigation should earn
priority through a real unresolved access or learning need, drawing on public
positive regimes and competent controls. Extending this corpus until EARM wins
would not answer the root question. Independent root theory and maintenance-decision
work remain available; no follow-up study is commissioned by this assessment.
