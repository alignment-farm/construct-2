# Feedback comparison: discovery and primary-method reading

16 September 2026. Root follow-up to the
[memory-feedback reading](../2026-09-16-memory-feedback/README.md), developing
[feedback decisions](../../notes/FEEDBACK_DECISIONS.md). No models or author code
were run; no ancillary publications or unpublished results were inspected.
Method descriptions below are inspected primary text; experimental findings are
author-reported, not independently reproduced. This is targeted discovery, not a
comprehensive review or novelty determination.

## What was read and what it changes

**P49 — [HiMPO, 2606.16285v2](https://arxiv.org/html/2606.16285v2).**
Inspected §3.1–3.3, Appendix A.7, and Appendices E–F; targeted model-role and
intervention passages. Three teacher-forced scoring passes compare successive
memories against a gold answer and filter credit with hindsight. Appendix E
reverts a selected memory to its predecessor, then resumes retrieval and greedy
generation. Reported top-ranked reversion reduces F1 by .030 (95% CI .003–.057);
per-write correlation with behavioral effect is modest (.16). Appendix F perturbs
targets offline, without testing noisy-supervision training. Extra scoring and
cluster-specific timing are not a portable full-cost estimate. **Answers** the
generic proposal to validate memory credit with actual continuation; **narrows**
claims about trustworthy feedback and later decision value.

**P50 — [AttriMem, 2607.21106v3](https://arxiv.org/html/2607.21106v3).**
Inspected §§2.3, 3, 4.1–4.3 and Appendices A–B. A trained memory writer receives
outcome reward plus token attribution. Context ablations score the same generated
answer; a sparse linear surrogate supplies coefficients. Answers are not
regenerated per ablation. The retriever and answer interface remain fixed during
writer training. Tables 2–3 report QA gains and reuse with other answer models.
The 8/16/32-mask schedule adds computation even when masks run in one batch.
**Answers** whether specific attribution can train a useful memory policy in
these settings; **narrows** any claim equating influence on an observed answer
with correctness or marginal complete-task value. Code and scorer accessibility
were not checked.

**P51 — [Credit Without Ground Truth, 2608.19760v2](https://arxiv.org/html/2608.19760v2).**
Inspected §§1–2, targeted §6–7 passages and §9; other appendices remain unread.
ALFWorld replay contrasts repeated factual continuations with policy-supported
alternative actions. Missing alternatives are excluded and counted; zeros depend
on sampling resolution. The paper reports no reliable incremental fidelity for
the audited signals over shuffled controls; judge evidence is inconclusive at
achieved reliability. The training null lacks a validated positive control, and
effective training dose differs. Its scope excludes return-derived estimators.
**Answers** the need for a generic step-credit audit and **redirects** comparison
toward useful decisions with functioning learning, rather than reading all proxy
credit as either causal or useless. This does not contradict P49's different
memory intervention and task. Artifacts were not audited.

**P52 — [Corrective Retrieval Augmented Generation, 2401.15884v3](https://arxiv.org/html/2401.15884v3).**
Inspected §§4.2–4.5, §5.4, §5.7–5.8 and Appendix B.3–B.4. A supervised T5
relevance evaluator and empirical thresholds route to refining retrieved text,
web search, or both. It is event-responsive correction; it does not accumulate
online intervention outcomes. Action ablations and single-action comparisons
report advantages for the combined rule. Table 6 explicitly excludes retrieval
and preprocessing from generation-cost estimates. **Narrows** the AD1 comparator:
a developed relevance-based rule already has a concrete implementation. Learning
retrieval relevance alone would not establish added value from remedy outcomes.

P48's earlier inspected environment probing and P44's delayed memory reward remain
complementary; their previous scope is preserved in the preceding ledger. The
new reading closes the broad feedback-comparison phase by explaining overlap and
selecting remedy discrimination for bounded feasibility work. No experiment is
commissioned; AD1 remains untested locally.

## Discovery and provenance

Broad web discovery began with these queries:

- `site.arxiv.org agent memory counterfactual credit assignment memory reward`
- `site.arxiv.org Self RAG corrective retrieval augmented generation reflection retrieval evaluator`
- `"memory" "counterfactual" "reward" "agent" arxiv credit`

Follow-up discovery identified HiMPO, AttriMem and the executed-replay audit.
Two sequential arXiv API ID queries, over 30 seconds apart, cached metadata with
a descriptive User-Agent. Requests, UTC timestamps, response headers and SHA-256
hashes are in [retrieval.json](retrieval.json) and
[credit-retrieval.json](credit-retrieval.json); raw responses are
[selected-metadata.xml](selected-metadata.xml) and
[credit-metadata.xml](credit-metadata.xml). Primary HTML was read through the web
tool at the exact versions linked above; full texts are not cached here.

The first response also contains Self-RAG **2310.11511v1** and Exact Is Easier:
Credit Assignment for Cooperative LLM Agents **2603.06859v2**. These remain
metadata/abstract discovery leads in this pass, not inspected methods. Older
search results used the C3 title for the latter; the cached versioned metadata
supplies its current title. Reading priority moved to the closer memory-specific
methods and single-agent audit. Their deferral is not evidence against them.
