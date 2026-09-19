# Lesson-acceptance selection — 19 September 2026

The user authorized study preparation after the runtime memory-worker review.
This targeted reading develops the [selected question](../../notes/LESSON_ACCEPTANCE.md),
not a systematic novelty claim. Exact metadata, retrieval time, response headers,
discovery queries and SHA-256 are in [retrieval.json](retrieval.json) and
[metadata.xml](metadata.xml). One arXiv API request retrieved three entries.
No public code, benchmark artifacts or model runs were executed in this pass.

## Inspected methods and consequences

**P48 revisited — [Grounding Agent Memory, 2609.11060v1](https://arxiv.org/html/2609.11060v1).**
Deepened §§3–4, Table 1 and Appendix B.3 beyond the earlier method/prompt reading.
The curator checks and can revise proposed memories using environment tools;
later task execution stays fixed across memory conditions. The drift table reports
70% pass for trajectory-only memory and 73% with probing, distinct from its 39%
stateless baseline. Headline task costs exclude curation and memory-management
calls. **Answers** generic probing-before-writing feasibility; **narrows** this
study to shared-candidate acceptance decisions, strong cheap alternatives and full
cost. Candidate generation/revision can itself change, so this is not an isolated
acceptance-only comparison. Results remain author-reported.

**P94 — [RSIAgent, 2609.15364v1](https://arxiv.org/html/2609.15364v1).**
Read §4.6, §7 and §§8.1–8.3, with abstract framing; no headline benchmark claim
is adopted. An independent verifier inspects task artifacts/environment, while
the actor subsequently distills and reconciles memory. The verifier does not
approve memory wording. Reported case audits include locally accepted mistakes
that become harmful reusable rules. Its target-conditioned practice differs from
unknown future tasks. **Narrows** the study's claim: independently checked task
success does not itself validate the resulting lesson. **Redirects** evaluation
toward scope and later use, without presuming that more verifier calls help.
Code and saved cases remain uninspected.

P92 CHIME and P93 Causal Agent Replay retain their
[previous reading boundaries](../2026-09-19-experience-credit/README.md).
P40 Memory-R1 and P49–P51 likewise remain prior methods, not new entries.

**Discovery lead only:** MemAudit **2605.23723v1** concerns post-hoc auditing of
poisoned memory; only its abstract/metadata were inspected. It is not the different
MEMAUDIT package-oracle paper **2605.02199** found by the same search. Neither
supplies inspected evidence about this study's full-cost acceptance comparison.
Adversarial poisoning is not needed to create the uncertainty under study.

## What is prepared, and what remains for the investigator

The new study starts from source episodes and model-proposed reusable claims,
retaining generation failures and disclosed teaching. Raw experience, cheap
grounded acceptance and optional paid checks are serious alternatives. A fixed,
competent reader makes acceptance effects interpretable. If checking rewrites
lessons or produces new source examples, its contribution and costs remain visible.

Repeated data integration/reporting is a concrete workload lead, not a selected
public benchmark. Existing database artifacts, source fixtures and motivated
analogues are eligible for investigator-led discovery. Complete results and
intended operations should be checked, avoiding accidental output equality.
Natural candidate errors must be observed in development before generalizing
from them; manufactured errors are labeled diagnostics rather than natural rates.

Preparation claims no functioning workload, checker or acceptance policy. The
commission includes bounded discovery and execution, with explanatory closure if
ordinary checking or reuse resolves the setting. No experiment or agent session
is launched by the root. Runtime `09f6683` is locally available but was not
resolvable through GitHub during preparation; the study's owned local clone
avoids depending on a derivative push or altering its active checkout.

## Repository preparation

The private [lesson-acceptance repository](https://github.com/alignment-farm/lesson-acceptance)
is pushed on `main` at `60552288930555806cef042294ea27145753d1d8`. Local and remote
commits match, `main` tracks `origin/main`, and the study working tree is clean.
[preparation.json](preparation.json) records verification and file hashes. The
brief, instructions, source guide and cached metadata are committed; the owned
runtime checkout is ignored and pinned. LA1–LA3 match the root selection note.
Root documentation changes remain uncommitted alongside the prior reviews.
