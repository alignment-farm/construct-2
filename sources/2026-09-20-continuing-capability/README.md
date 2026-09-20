# Continuing capability: methods and root selection

20 September 2026. This bounded public-research pass supports
[the root synthesis](../../notes/CONTINUING_CAPABILITY.md). It revisits P88 at v2
and adds P96–P97. Selected methods were inspected in exact-version primary full
texts. Results remain author-reported; no implementation, dataset or model run
was reproduced. This is a comparison of research designs, not benchmark adoption
or a comprehensive novelty audit.

Subsequent [task-sequence inspection](../2026-09-20-task-sequences/README.md)
advances the original methods-only boundary below with pinned public code,
individual instances and reference checks. This entry preserves what was known
at the earlier reading stage.

## P88 revisited: AgentCL, 2606.02461v2

[Primary text](https://arxiv.org/html/2606.02461v2), §§3.1–3.3 and coding-stream
construction in §4.1. The
[earlier ledger](../2026-09-17-runtime-study-selection/README.md) read v1;
this entry records v2 without asserting which claims changed between versions.

**Inspected:** external memory develops from trajectories without ground-truth
guidance for its construction. The design separates a first pass, frozen-memory
repetition, and held-out tasks; coding streams deliberately introduce reusable
subtasks. **Answers:** generic experience-reuse and generalization evaluation
already exists. **Narrows:** second-pass improvement includes exposure to the
task itself and cannot alone establish transfer. **Redirects:** preserve those
distinctions while testing useful experience through actual requirement changes
and competent artifact reuse. The inspected experiment targets non-parametric
memory; it does not settle our weight-allocation comparison.

## P96: SlopCodeBench, 2603.24755v2

[Primary text](https://arxiv.org/html/2603.24755v2), §§2.1–2.4 and §3 overview.
Read the May revision; discovery results also exposed the older March corpus,
whose counts must not be mixed with v2.

**Inspected:** authored requirement sequences carry forward the agent's own
workspace without prior conversational context. Evaluation includes earlier
checkpoint tests; official tests and feedback are hidden. Problems readily solved
in one shot were excluded. **Answers:** consequences of accumulated code under
new requirements already have a direct evaluation precedent. **Narrows:** its
difficulty selection and feedback boundary differ from ordinary maintenance;
complexity/verbosity metrics do not themselves establish future repair cost.
**Redirects:** keep artifact continuity and measure useful revision directly.
This is a candidate task-design source, not an adopted workload or a reason to
select cases merely because current agents fail them.

## P97: Your Agents Are Aging Too, 2605.26302v1

[Primary text](https://arxiv.org/html/2605.26302v1), §§3–5 and Appendix D.3.

**Inspected:** generated temporal dependencies support longitudinal diagnostics.
Oracle retrieval from retained memory and injection of gold facts help separate
access, writing and utilization limits. The appendix's intervention controller
uses benchmark-derived accumulator error and precision signals. **Answers:**
generic lifespan diagnosis and targeted maintenance already have public methods.
**Narrows:** oracle context is a diagnostic privilege; evaluation-derived runtime
signals do not establish an affordable observation in ordinary deployment.
**Redirects:** examine available observations and functioning remedies before
attributing value to a learned chooser. The paper does not establish the local
value of additional experience beyond competent artifact/source reuse.

## Relation to earlier reading and the remaining gap

P87 already combines external memory and parameter learning; P90 provides a
continuing-database setting whose normalization in our local follow-up removed
part of the original discovery target. P91 cautions that unused retrieval does
not by itself identify a defect. The [runtime-study selection](../2026-09-17-runtime-study-selection/README.md),
[continuation review](../2026-09-18-weight-continuation-review/README.md) and
[harness-component reading](../2026-09-18-harness-components/README.md) retain the
inspection boundaries for those sources; this pass did not reproduce their
implementations.

Root inference: compare the value of additional experience at a shared acquired
workspace separately from the whole-policy effect of creating better workspaces
over time. Both can matter. Keep the source archive and competent tools available
when comparing memory allocations, and count whatever investment creates the
advantage. This is a refinement of our local next question, not a claim to have
invented longitudinal learning evaluation.

## Discovery and retrieval boundary

Web discovery covered continuing agent experience, lifelong benchmarks and
iterative software development, then exact titles. Only primary papers above
support the methods assessment. Search results for LifelongAgent-Bench, EvoClaw,
third-party SlopCodeBench audits and commentary were discovery leads, not inspected
evidence or adopted claims. This pass did not inspect benchmark repositories,
individual runnable tasks, licenses or resource feasibility.

One arXiv query API request retrieved metadata for the three base IDs. The returned
entries identify the exact versions read: P88 v2, P96 v2 and P97 v1.
[metadata.xml](metadata.xml) preserves that response; [retrieval.json](retrieval.json)
records the query, versions and content hash. No parallel API client or retry
was used. Scientific notes cite versioned full text rather than mutable aliases.

The immediate root selection is a bounded workload comparison for experience
helping later change. No benchmark, new study, training recipe or derivative
change is commissioned by this reading.
