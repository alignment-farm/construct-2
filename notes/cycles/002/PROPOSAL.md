# Cycle 2 derivative: retaining the conditions for action

2026-09-08 · Development protocol frozen in
[construct-lesson-transfer](../../../../construct-lesson-transfer/README.md) at
`3408022`. This note explains the research choice; the derivative owns the
[executable protocol](../../../../construct-lesson-transfer/notes/PROTOCOL.md),
raw evidence, and [handoff](../../../../construct-lesson-transfer/notes/HANDOFF.md).
The [development return](PILOT.md) records the completed reproduction
and extension, including the stopped first attempt. It parks the larger
construction study and selects a bounded application diagnostic next.

## What the closer reading changed

The question is narrower than whether reflection helps agents. In
[CLIN v1](https://arxiv.org/pdf/2310.10134v1), §3.3, memory consolidation receives
the target task description and selected successful trial memories. Its §4.3
heating failure also shows that retaining an alternative procedure does not
guarantee selecting it appropriately. Construction and application need separate
controls. This motivates freezing a memory before evaluation and offering the
whole representation, removing retrieval as a moving part.

[ERL v2](https://arxiv.org/pdf/2603.24639v2), Figure 8, already requests a trigger
and action when constructing a heuristic. Appendix E's iterative acquisition
improves source performance while reducing held-out performance relative to its
non-iterative version. That comparison motivates fixing acquisition evidence;
it cannot tell us whether representation, exploration, or their interaction
caused the transfer gap. We do not inherit the authors' possible explanations
as established causes.

[S3Gym v1](https://arxiv.org/pdf/2608.31100v1), §§4.4–4.5, explicitly excludes
evaluation trajectories from subsequent history, memory, and training and uses
disjoint exploration/evaluation seeds. It compares three persistence pathways,
including weight training, with self-judged experience in its main setting.
Our derivative adopts the evaluation boundary but tests a different, deliberately
supervised construction question. Comparing weights and text would introduce
optimization and acquisition differences before this question is resolved.

[AutoGuide v2](https://arxiv.org/pdf/2403.08978v2) remains the closest precedent
for context-associated guidelines. Explicit conditions are not our novelty claim.
The proposed contribution is a controlled account of which distinctions survive
compression, what they cost, and whether later actions use them selectively.
The literature review is targeted; it does not establish priority for this design.

## One reproduction, one extension

**A. Reproduce the narrow M2 correction mechanism.** Three fixed chains use
the pinned original runner, prompts, deterministic mint, corpus, and scorer.
The local inference transport and output budget are documented adaptations.
If the first answer is correct, retain the resulting failure to mint rather
than searching for a convenient mistake. This is repeated measurement of one
retraction case; it cannot establish transfer or population rates.

**B. Test whether construction preserves conditional rules under compression.**
In an executable simulator, three service workflows have two preparation
operations followed by finalization. A world's convention determines which
preparation comes first as a function of one observed field. Another observed
field is irrelevant. The conventions vary across worlds, so operation names
and generic advice cannot supply the world's rule.

All writers receive identical compact records from 24 executed, contrastive
experiences per world, with checked corrections for failures. Four construction
policies cross a general versus explicitly conditional instruction with 48 versus
144 stored whitespace words. Controls supply no memory, a competent fixed
strategy, all raw evidence, or the true rule as a diagnostic consumer check.
The word cap is explicitly not a token budget; raw evidence and truth rules
are not cost-matched treatments.

Fresh evaluation has a single-object task and a composed three-object task,
each paired with a version that reverses the relevant condition. The actor
produces a primitive action plan, which is actually executed on private state.
Both members must succeed for paired success. A memorized unconditional order
cannot succeed on both. Full state transitions and malformed outputs are kept.
An independent declarative validator checks the execution outcome.

The primary contrast is paired success with scoped minus general construction
at 48 words. The secondary contrast asks whether this difference is larger
than at 144 words. These estimate construction-policy effects, including
truncation; they do not isolate the effect of editing one phrase in a memory.
Four development worlds establish instrument behavior, with no p-values or
confidence intervals. Independent worlds and their constructed memories,
not individual actor calls, are the future unit of inference.

## What this will and will not resolve

The design can distinguish useful rule content from generic guidance, loss in
construction from failure to consume correct guidance, and compact lessons
from retaining all source evidence. All evaluation field combinations appeared
in the source experiences. New objects and composition therefore measure
bounded reuse of learned relations, not extrapolation to unseen conventions.
The authored simulator's two binary fields are intentionally legible; a ceiling
result would identify an uninformative comparison for this model and fixture.

The agent does not explore to obtain the experience, supply its own truth
labels, revise memory after feedback, retrieve a subset of records, or train
its weights. Those are separate scientific questions. This derivative must
return a scoped finding or an instrument limitation, not expand automatically
into a general agent platform.

The development budget is 360 attempted local requests, including transport
checks, M2, and interrupted attempts. A prospective experiment and its resource
budget will be specified after the pilot. The user will assign that work to
a derivative agent. Cycle 1 continues independently with Grok 4.6; neither its
state nor its next engineering task is part of this setup.
