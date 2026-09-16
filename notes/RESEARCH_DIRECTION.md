# Research selection within Construct-2's fixed direction

16 September 2026. The user asked the root to resume independent scientific work
while ancillary investigations retain ownership of their experiments. This note
reassesses the next questions using a fresh
[public-research review](../sources/2026-09-16-research-direction/README.md).
It originally prepared research choices without commissioning a study. The
[subsequent preparation](#preparation-after-the-users-agreement) below records
the user's agreement and the resulting handoff; preparation launched no model run.
The prior local publications and prospective R, M and MR expectations remain
historical evidence with their original wording.

The [root directive](../README.md) remains unchanged. The useful lifetime of a
learned component is a selected study question within it, not the program's new
direction. Our existing working hypothesis allows models, records and harnesses
to develop together as experience warrants. The subsequent
[adaptation synthesis](ADAPTATION_DECISIONS.md) develops that hypothesis using
additional public research and distinguishes it from any one study's focus.

**Several broad next steps already have public answers.** Forgetting prediction,
prediction-guided replay, amortized context storage, learned memory admission and
learning how to retrieve experience all have concrete methods and evaluations.
Our local results remain useful, but a generic demonstration of one of those
ideas would need to be justified as replication or adaptation. The root should
select consequential unresolved comparisons using both public and local evidence.

## What the reading changes

**Maintenance decisions have closer precedents than our earlier map captured.**
P26 learns example-level forgetting forecasts and uses them in replay, including
sequential error correction. P27 extends empirical association modeling to larger
models and held-out tasks. Its online variant observes damage after an initial
training prefix; its offline variant pays for an extra training run. Thus sparse
probes, forecast utility and their costs are already studied. Our candidate
contribution must concern a specified generalization or decision boundary.
[P26, §§2–5](https://arxiv.org/html/2402.01865v3),
[P27, §4 and Appendix A](https://arxiv.org/html/2406.14026v8).

Adaptive reset also has an implemented precedent in P28, using collapse signals
and selective recovery in visual test-time adaptation. P35 investigates factual
connectivity as a damage signal and selects preservation anchors. Neither a
monitor nor a selected protection set is new by itself. These are method leads,
with different tasks and information access from the local procedural studies.
[P28, §3](https://arxiv.org/html/2603.03796v1),
[P35, §§4–5](https://arxiv.org/html/2609.08067v1).

**Useful placement has positive public demonstrations as well as our local
negative cost results.** P29 trains reusable KV state for repeated queries over
a corpus, reports serving advantages, and discloses substantial preparation cost.
P30 meta-learns context-to-adapter generation, moving work into an earlier training
stage; its unrelated-query probe also finds interference. Neither is equivalent
to our fixed local LoRA recipe. Our absence of demonstrated repayment cannot be
generalized to the absence of useful learned storage.
[P29, §§3–6](https://arxiv.org/html/2506.06266v3),
[P30, §3 and Appendix C.4](https://arxiv.org/html/2602.15902v1).

**Conditional allocation is already an empirical research program.** P31 compares
eleven memory implementations across multiple workloads and finds regime-dependent
tradeoffs. Its exclusions and implementation substitutions matter when importing
a comparison. P32 combines write admission and parametric consolidation, measures
knowledge transitions, and explicitly leaves temporal conflicts and interference
as limitations. These sources narrow what S5 should add; a general substrate
ranking or a two-layer architecture would overlap substantially.
[P31, §§2–5, Appendices B and G](https://arxiv.org/html/2608.15008v1),
[P32, §§3–5](https://arxiv.org/html/2608.22215v2).

**Learning can improve access while the evidence remains explicit.** P33 retains
relevance scores and estimates unscored query–memory relationships. Its evaluated
budget declines on a fixed schedule, and its discussion identifies changing
memory meanings as a threat to reuse. That supplies a concrete alternative to
putting the evidence itself into an adapter.
[P33, §§V–VIII](https://arxiv.org/html/2608.22767v1).

Finally, P34 finds sensitivity to task order and feedback specification in
text-memory agents. Our learned-state dependence therefore belongs beside a
broader history-dependence problem, without establishing a shared cause.
[P34, §§3–4](https://arxiv.org/html/2608.18066v2).

## Connection to the root account

The useful object of study is an agent's maintained capability: retained evidence,
learned behavior, access procedures and the decisions that change them. The
division between explicit and learned memory can occur inside that system.
Evidence can remain explicit while a learned policy improves its use. Conversely,
learned content may still require explicit correction and fallback evidence.

The local findings supply controlled examples of three dependencies: training
value depends on the receiving state; retention is relative to a later query and
reader; maintenance can change the costs and quality that initially justified
learning. Public work supplies broader demonstrations and mechanisms addressing
each. Their combination motivates a more specific placement question:

> Which part of using experience is worth learning, for how long does that learned
> component remain useful, and what must remain available to revise or replace it?

This is a framing for the selected comparisons, not a replacement for the root
directive, a new theorem or an asserted gap across all literature. It preserves
the priority on neural memory and learned policies while allowing the evidence
to favor explicit or combined arrangements.

## Two independent comparisons worth developing

### A. Does a maintenance decision remain useful after the learner changes?

Local S2 shows that a support preference can reverse between learned states.
Public forecasting methods give concrete comparators rather than a reason to
invent a generic damage score. The question is whether a predictor or action
rule calibrated on some histories remains useful on separately acquired and
subsequently revised states, including valid new obligations.

Our prospective expectation is that a fixed mapping from update examples to
damage will sometimes lose usefulness across changed learner histories, and
that a small observation of the current state can recover decision value. A
strong static comparator performing as well, or observation costs consuming
the benefit, would weaken that expectation. This is untested locally and not
claimed to be unexplored publicly.

Any later study should distinguish forecasting before an update from extrapolating
after a paid trial. Its target should include complete new and preserved behavior,
and its decision comparison should include developed fixed support and direct
validation. Skipping an update has a cost when the new obligation remains unmet.
Changing cases while reusing the same acquired history does not test transfer
across histories. The investigator would own the actual protocol and resource
choice. No automatic fifth S2 phase follows from this question.

### B. When does a learned memory component repay its cost before it needs revision?

The immediate root task is workload discovery for repeated use under meaningful
change. A candidate is a versioned operational reference used across many requests:
the same observations support retrieval, a reusable learned representation, or
learned access to retained records. Changes must affect answers or actions; an
append-only history does not by itself impose correction of a previous rule.

Vary reuse between changes, the scope of a change, and the cost of evidence access.
Develop competent explicit retrieval and cached-context controls alongside a
published learned method. A method's original workloads and implementation costs
should guide feasibility; the laboratory need not rebuild its full training regime
merely to demonstrate the architecture again.

Our prospective expectation is a conditional crossover: longer useful reuse can
favor paying an acquisition cost, while frequent consequential revisions can
remove that advantage or favor learning only the access procedure. A published
method's gain on stable corpora is a reason to test this, not a prediction of a
local win. No observed crossover, after functioning acquisition and serious
controls, would also answer the bounded question.

A useful contrast separates **changes in evidence** from **changes in how it is
used**. Our inference is that a learned access policy may remain useful when
record values change but relevance relationships remain stable. When new goals
change those relationships, its accumulated retrieval experience may also need
revision. Crossing those changes would distinguish an advantage of learning
access from the easier explanation that nothing important to the learned
component changed. The public reading motivates this comparison; it does not
establish either outcome or its novelty.

For a fixed sequence of uses, account for preparation, use, revision, checking
and repair. All methods incur their actual costs. Compare complete quality and
cost jointly; reducing them to cost per success can conceal unacceptable failures.
Use native units until a justified conversion is needed. Prior training cost may
be shared across deployments, but its allocation must be stated. Neither setup
nor the potential source of a crossover should rely on withholding accessible
evidence from the explicit comparator.

The root's preferred next preparation is this placement comparison, alongside
development of A as an independent question. Useful placement has received less
direct attention than the recent S2 chain. B does not require A to produce a
successful controller first; fixed maintenance and explicit fallback already
define meaningful alternatives. Learned retrieval under changed memories is a
candidate within B, not an automatically commissioned third project.

## How this changes root work

The root continues theory, public discovery and research selection during local
execution. It reads an ancillary publication to assess the claim and its effect
on the program, extending the evidence review when a material uncertainty calls
for it. A local follow-up competes with other questions on scientific value; its
proximity to the latest result does not give it priority.

Public evidence can settle a root question, supply a method or baseline, suggest
a complementary comparison, or justify a deliberate replication. We should
record which of those happened. A new bibliography alone is insufficient if the
same local assignment would have been issued regardless of what was read.

Here the concrete change is to replace broad invention of forecasting and memory
allocation with comparisons of existing methods under changing histories and
useful lifetimes. The next preparation should choose a workload and closest
published comparator, check remaining overlap and local feasibility, and identify
the result that would change the account. Ancillary methods and execution remain
local. No new review gate, reporting layer or continuous monitoring service is
introduced by this note.

## Preparation after the user's agreement

The user approved these revised preferences. The root then inspected released
methods and a workload, with the record in the
[preparation review](../sources/2026-09-16-study-preparation/README.md).
Further reading found direct precedents for update robustness and operation-cost
comparisons (P36), structured state revision (P37), and learning supersession
(P38). Those broad demonstrations do not need to be recreated as our contribution.

**B was prepared as an independent study:**
[memory-placement-under-revision](https://github.com/alignment-farm/memory-placement-under-revision)
([local brief](../../ancillary-studies/memory-placement-under-revision/README.md)).
Its first implementation lead is EARM's learned access, with a versioned subset
of the released τ-bench document workload. Content storage remains a possible
comparison, subject to bounded feasibility work. This choice makes contact with
learning using a released lightweight method while preserving the distinction
between learned retrieval and neural content. Preparation has not started the
ancillary agent or any experiments.

**A has an independent [comparison note](MAINTENANCE_DECISIONS.md):** hold out
learner histories, distinguish frozen forecasts from paid current-state
observations, and evaluate the action's value against fixed support and direct
validation. It is root scientific development, not a fifth S2 commission.

The common theoretical quantity is the *useful lifetime of the learned component*,
which need not equal the interval between document changes. For a scalar cost
measure and comparable useful quality, a simplified stable-period comparison is:

```text
learned cost  = setup_L + N * use_L + revision_L
explicit cost = setup_E + N * use_E + revision_E
```

If `use_E > use_L`, the corresponding cost crossover is
`N > ((setup_L - setup_E) + (revision_L - revision_E)) / (use_E - use_L)`.
This is accounting, not an empirical prediction. With no per-use saving, reuse
alone cannot rescue a larger initial cost in this simplified model. Real query
mixes, cache warmup, changing quality and repeated revisions require cumulative
measured costs rather than extrapolating a single timing. Count terminal revision
only if it is actually incurred within the compared sequence, and do not count
the same refresh again as the next period's setup.

For learned retrieval, changed values may preserve useful relevance structure;
changed evidence needs may invalidate it. The proposed comparison tests that
conditional distinction. It also allows the cheap explicit method to win. A
maintenance predictor would be valuable only when its information changes an
available action enough to justify its own costs, so B can proceed without A.

## Status after handoff

The user subsequently reported that memory-placement-under-revision was underway.
The root did not inspect its unpublished results for that update. The
[adaptation synthesis](ADAPTATION_DECISIONS.md) now develops independent theory
and predictions while that study owns its execution. Its broader account of
learning what to change does not alter the existing A/B expectations or assign
another experimental phase.

## Assessment after publication

The [16 September placement assessment](../studies/2026-09-16-placement-findings.md)
accepts B's bounded phase: learned score prediction functions, but cheap explicit
access matches or exceeds complete answers without scoring calls. Prediction
quality persists through content edits better than changed evidence needs; that
does not establish useful repayment. Reuse lengths are confounded with seeds,
and the combined branches contain no answer-changing targets. The prospective
expectations above remain unchanged. The broader placement question remains open,
A remains independent, and this assessment commissions no further experiment.

## Independent development after placement

The [decision-value reading](../sources/2026-09-16-decision-value/README.md)
adds established decision-focused and metareasoning theory (P46/P47). The
[maintenance extension](MAINTENANCE_DECISIONS.md#when-observation-can-change-the-decision)
uses it to narrow A: a history change may alter absolute damage forecasts while
leaving the best action unchanged. Useful observation must resolve consequential
action differences relative to competent fixed choices, explicit fallback and
direct validation. Its constructed examples separate information about a learner
from information worth acquiring for a decision.

This selects further root development of action-value transfer, not generic
forecasting or a renewed placement run. AD1–AD3 and their empirical status remain
unchanged. No new ancillary phase or model experiment is commissioned.

**Concrete preparation:** The [maintenance comparison](MAINTENANCE_COMPARISON.md)
now specifies the workload, functioning support choices, observation alternatives
and illustrative resource scope. The [targeted review](../sources/2026-09-16-maintenance-preparation/README.md)
finds that a simple known-history rule matches the aggregate state oracle on
published S2 endpoints. This is retrospective, but redirects the first investment
toward testing history-rule transfer before a larger learned-selector campaign.
An independent bounded comparison is recommended; no new phase is commissioned.

**Subsequent commissioning decision:** Following the user's direction to continue,
the root prepared and published the independent
[maintenance-decision-transfer study](https://github.com/alignment-farm/maintenance-decision-transfer)
([local brief](../../ancillary-studies/maintenance-decision-transfer/README.md)).
The bounded comparison is authorized for ancillary execution. Preparation has not
started the investigator or model runs. This is a new independent question, not
an S2 renewal or a change to the program's directive.
