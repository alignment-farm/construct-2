# Learning what to change

16 September 2026. Root synthesis during ancillary execution. The enduring
[research directive](../README.md) is unchanged: how agents accumulate useful
experience across sessions, and where that experience should live. This note
develops one part of that question; it does not replace it with maintenance,
cost amortization, or learning a controller.

Our working hypothesis already allows a combination of explicit records,
contextual lessons, executable tools, weights and runtime rules. The
[4 September perspective](RESEARCH_PERSPECTIVES.md) discusses learning to use
external state and the joint development of models and harnesses. The present
question is what experience can teach the system about changing that combination.
The [new public-research review](../sources/2026-09-16-adaptation-decisions/README.md)
supplies direct precedents and limits the novelty of broad claims.

## What the local evidence contributes

The local studies establish several dependencies, without establishing that an
agent can learn to diagnose them or choose the remedy.

| Local finding | Implication for deciding what to change |
|---|---|
| S4 distinguishes query-relevant omissions from failures of a reader; some lost raw detail is irrelevant to a later answer. | Better access can help when usable information survives. Reacquisition or a different retention policy is needed when the required information is absent. |
| Procedure-transfer diagnosis repairs routing from identical initial weights while identifier production remains unreliable. | A failed task can contain separable acquisition problems. The observed repair does not establish an acquired diagnostic policy. |
| S2 crosses inherited state and revision support; a support preference reverses between fresh acquisitions. | The receiving learner matters to the value of an update. A rule learned from one history may need a current-state observation. |
| S1's damage-aware replay improves total completed uses but worsens recurrence and adds substantial selection cost. | A plausible signal and better aggregate acquisition do not establish a better maintenance decision. |

These claims come from the existing [program assessment](../studies/README.md#what-the-completed-investigations-change),
[maintenance synthesis](../studies/2026-09-15-maintenance-findings.md) and
[state/support assessment](../studies/2026-09-15-state-support-findings.md).
They do not identify a common internal cause. Our synthesis is an inference:
intervention value depends jointly on retained information, its use, the receiving
state and the currently required behavior. A fixed assignment by information type
alone is unlikely to capture all four.

## What has already been demonstrated publicly

Learning memory operations is established prior work. AgeMem trains coordinated
long- and short-term memory use; Memory-R1 trains memory management and answer-time
selection. Interactive Memory Learning additionally reports continued policy
adaptation across conversational sessions. Its delayed signal is a response-quality
judgment, which must be distinguished from a measured causal benefit of saving a
particular memory. [P39](https://arxiv.org/html/2601.01885v3),
[P40](https://arxiv.org/html/2508.19828v5),
[P44](https://arxiv.org/html/2609.17088v1).

Harness adaptation also has concrete precedents. Life-Harness uses an external
optimizer to improve the interface around a frozen executor. Co-Evolving Harnesses
and Models reports that imitation can hurt an evolved harness while an on-policy
correction recipe helps. HarnessBandit learns which fixed harness to use for a
training update. Together these make compatibility and learned selection existing
research subjects. [P41](https://arxiv.org/html/2605.22166v2),
[P42](https://arxiv.org/html/2609.09134v1),
[P43](https://arxiv.org/html/2609.13739v1).

A broader system choosing among memory, skills, harness and weight changes is
already explicitly proposed in Next-Generation Agentic RL. Its AReaL2.0 prototype
implements the weight-update branch; the full intervention selector remains part
of its proposed architecture. [P45, §§5–6](https://arxiv.org/html/2607.01120v2).
This is direct conceptual overlap, without evidence there that the complete
selector works. The bounded search does not establish its absence elsewhere.

Consequently, our contribution cannot simply be that agents should learn memory
management, that model and harness can co-evolve, or that different failures call
for different changes. The useful question concerns conditions of effectiveness:
what information supports the choice, how it transfers as the system changes,
and whether its benefit survives the cost of learning and checking it.

## Distinguish behavior, retained experience and the decision rule

A rule can respond to events without learning from them. A well-developed rule
that retrieves evidence on uncertainty or refreshes an index after a document
change is a serious comparator. It need not always choose the same action.

Conversely, a system with frozen executor weights can learn through retained
records or modified code. A fixed harness can host a learned memory policy.
State explicitly **what persists, who changes it and when**. An external research
agent revising a harness during development demonstrates something different
from a deployed agent improving its choices through its own experience.

For any proposed decision, distinguish the observation available at the time,
the available interventions, and the later behavior used to judge them. Changing
records, access, procedures, weights or runtime rules can be complementary actions.
Keeping the present arrangement is also an action. “Decision rule” names a role
in this analysis; it does not require a separate controller model or a new layer
of software.

The hybrid hypothesis also requires compatibility. A procedure learned with one
tool interface may no longer fit a revised interface; a new executor may already
perform work previously delegated to a lesson. Independently useful changes need
not remain useful together. Public results now provide direct reasons to test
that interaction rather than assume it away.

## Three predictions and their possible failures

These are root expectations, not new commissions or claims of undiscovered
methods. AD1 is developed here; AD2 and AD3 restate the independent A/B expectations
already recorded in [research selection](RESEARCH_DIRECTION.md). Their treatment
here precedes any review of the underway placement study's results.

**AD1 — Experience can improve intervention choice beyond an event-responsive
rule.** On a workload containing both missing-evidence failures and failures to
use available evidence, we expect prior intervention outcomes to improve choices
between functioning remedies on fresh episodes. Compare with a developed rule
using the same available observations and actions, and with competent explicit
access. The claim concerns the added value of decision experience: an advantage
that disappears when its outcome associations are reset or shuffled would help
locate that value. Better task learning alone does not establish better selection.
The expectation weakens if a simple rule matches the learned choice, if one action
dominates, or if deciding consumes the benefit. Identifying these conditions is
scientific progress even without a controller advantage.

**AD2 — Decision experience transfers imperfectly when the receiving system
changes.** We expect a choice rule calibrated on some learner histories to lose
value on materially different histories, with small current-state observations
recovering some useful value. Histories held out from calibration matter more
than new wording for old cases. Compare the unchanged rule, selective recalibration
and direct validation of candidate actions, including their costs. Stable transfer
would favor reusable regularities; observation without decision improvement would
weaken the adaptation hypothesis. The [maintenance-decision note](MAINTENANCE_DECISIONS.md)
develops this comparison. S2 supplies motivation, not a tested forecast.

**AD3 — The useful lifetime of learned access follows relevance as well as
content.** We expect some accumulated retrieval experience to survive changed
record values when evidence needs remain stable, but to lose value when new goals
change those relationships. A competent explicit reader may then become preferable,
or access experience may need revision. Compare cumulative useful quality and all
acquisition, access and revision costs. Equal decay under both changes, or a cheap
baseline matching the learned method throughout, would weaken the proposed benefit
of separating explicit content from learned access. This is the existing placement
expectation; its investigator owns the implementation and experimental design.

## What would count as learning from the outcome

Successful behavior after a change is insufficient evidence that the change helped.
Only the selected intervention is ordinarily observed; the alternatives are
counterfactuals. A small controlled comparison can estimate available decision
value, while an oracle using held-out outcomes only supplies a diagnostic upper
bound. Trials on copied learners and validation calls remain paid observations.
Later success credited to an earlier memory write can also reflect an easier
question or another component's improvement.

The target must therefore include newly required behavior and still-valid earlier
behavior over a stated future sequence. Correctly replacing a superseded answer
is not forgetting a valid obligation. An accurate forecast is useful only when
an available action improves that sequence. When every action is inadequate,
improving the action set or acquisition method is more informative than refining
the chooser. Useful quality and cost remain separate measurements unless an
explicit utility conversion is justified.

## Status when the expectations were written

The user had reported that [memory-placement-under-revision](https://github.com/alignment-farm/memory-placement-under-revision)
([local brief](../../ancillary-studies/memory-placement-under-revision/README.md))
was underway. The synthesis above was written without reading its unpublished
results or changing its assignment. Maintenance-decision transfer remained independent root development.
Neither question must finish before other scientifically useful work proceeds.

The larger program continues to ask what experience should become and where it
should persist. This note makes one implication of the existing hybrid hypothesis
testable: experience may improve both a capability and the decisions about how to
maintain or replace it. Whether these improvements remain compatible and useful
is an empirical question, not a reason to prescribe one permanent architecture.

## Assessment after the placement publication

The [16 September placement assessment](../studies/2026-09-16-placement-findings.md)
accepts the completed bounded phase. AD3 receives evidence for persistence of
score-prediction value through content edits and its decline under changed evidence
needs. Its stronger useful-quality/cost expectation is weakened here: competent
lexical retrieval matches or exceeds the learned methods' aggregate quality
without their scoring calls. The combined-change sample has no answer-changing
targets, so it cannot settle consequential joint revision. The original AD3
wording above is preserved, including its stated adverse outcome.

AD1 and AD2 remain untested by this study. Most learned-reranker failures are
truncated answers, demonstrating a dependence on context selection and the
receiving answerer's budget without isolating a universal failure mechanism.
The result strengthens the distinction between learnable regularity and useful
intervention value; it does not establish a learned intervention selector or
change the root directive. No follow-up commission accompanies this assessment.

## Assessment after maintenance-decision transfer

The [publication assessment](../studies/2026-09-16-maintenance-transfer-findings.md)
accepts the independent bounded phase. AD2 now has a local test: matching known
history selects 524/768 complete orders, equal to the two-support aggregate bound
across two newly acquired learners. Paid endpoint validation adds no aggregate
gain. This weakens the predicted loss-and-observation-rescue pattern in this
setting. The pre-observation and prefix controls were already constant before
assessment, so their results cannot establish that observations lack information.

All candidate endpoints remain incomplete. A validation-visible tie exchanges
new/earlier waiver failures for still-ineligible-order failures, showing why zero
aggregate regret does not certify maintenance. A 16-key retained-example table
completes 192/192 under supplied addressing, entity invariance and correction
authority. The result narrows selector investment without resolving general
maintenance or choosing a universal substrate. AD1 remains untested locally;
AD3's assessment and the original wording of all three predictions are preserved.
No further experiment is commissioned.
