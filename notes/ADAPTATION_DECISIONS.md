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


## Assessment after evidence-use-under-revision

The [17 September assessment](../studies/2026-09-17-evidence-use-findings.md)
adds limited positive evidence for reusable behavior over changing explicit
values. Varied-history 128 remains above base through two corrections and has
lower measured training-plus-use time than a stronger uncached contextual lesson
at higher aggregate complete accuracy. Further training reverses the benefit;
paired losses, missing cache controls and assessment-based checkpoint selection
qualify deployment value. A supplied interpreter completes the task cheaply.

This distinguishes the useful lifetime of an acquired behavior from both document
revision frequency and further acquisition. Keeping authoritative values explicit
can avoid weight repair for these changes; it does not ensure the inherited
reader remains reliable. The mixed-substrate hypothesis is sharpened, not newly
established. EU1–EU3 have their own bounded assessment. This study does not test
AD1's remedy choice, AD2's observation value or AD3's learned access policy, so
those original predictions and assessments remain unchanged. No continuation is
commissioned; independent executable-experience work continues.

## Assessment after executable-experience retention

The [17 September assessment](../studies/2026-09-17-executable-retention-findings.md)
adds a bounded example of changing persistence policy. Source recovery and ready
source each complete 8/8 requests with no future model calls. A policy beginning
with lessons retains its first reconstruction, then needs no later generation.
Keeping the alternatives in fixed representation categories would miss that
transition and overstate recurring reconstruction costs.

This sharpens the existing combination hypothesis: the relevant comparison is
what information and usable capability remain available at each decision, and
what it costs to change that availability. Library registration itself adds no
observed value over archive recovery here. The transition is supplied by the
harness, not learned from feedback, so AD1 remains untested; AD2/AD3 and EU1–EU3
retain their previous assessments. The full contract and known dispatch also
limit claims about experience acquisition and autonomous applicability.

One paid lesson correction illustrates that moving experience into prose can
create a new maintenance obligation, even when the original implementation works.
It does not demonstrate a general representation disadvantage or the value of
dependency tracking. The independent migration and correction-lineage questions
retain their own predictions. This completed phase supplies an explanation, not
a standing instruction to extend the most recent experiment.

## Assessment after procedural migration and correction lineage

The [17 September assessment](../studies/2026-09-17-migration-lineage-findings.md)
adds two functioning capabilities and two limits on additional investment.
Unchanged acquired guidance improves a new recipient from 1/12 to 12/12 fresh
tasks. Paid family selection matches 12/12 and reduces use tokens, but nearly
triples setup-plus-use tokens relative to inheritance. The receiving model
changes the guidance's marginal value without making adaptation necessary here.

Acquired semantic lineage supports correct selective repair through two
corrections, yet rebuilding the small state is cheaper. Maintenance introduces
a false support link despite perfect initial acquisition. That link causes no
observed repair failure; later arithmetic fails after correct state repair and
identical use prompts across methods. The separate wording diagnostic narrows
this read-time problem without establishing general reliability.

Thus the ability to act and the machinery that chooses or maintains it each need
their own value assessment. Reduced inference work or a smaller repair set may
not repay acquiring and maintaining the decision information. Source archives
enable competent alternatives, but these comparisons do not isolate archive
retention's causal benefit. Their different mechanisms do not establish a common
failure cause or a general preference for one substrate.

PM1–PM3 and CL1–CL3 have separate assessments in their original notes. AD1 remains
untested: the selector chooses among guidance banks, not remedies for missing
evidence versus unsuccessful use. AD2/AD3 retain their previous assessments.
Both bounded commissions are complete. Further selection should target useful
capability across continuing realistic work, with consequential changes and
strong alternatives, rather than assume another adaptation layer is beneficial.

## Assessment after weight consolidation

The [17 September assessment](../studies/2026-09-17-weight-consolidation-findings.md)
adds a direct comparison of weights with source experience still accessible.
Partial acquisition produces a manual retained-code gain, 3/12 to 5/12. A
developed contract compiler brings both models to 12/12; the adapter adds repair
calls. Manual adaptation also worsens a changed exclusion rule despite improving
aggregate completion. An acquired behavior's value depends on the execution
route and obligations, not only whether the source material was learned.

The compiler and workflow guidance remove work previously delegated to the model.
They are investigator-authored capabilities, not agent-acquired experience.
This limits what the experiment says about autonomous improvement while explaining
why further weight training is unnecessary to complete this finite workload.
Equal external access is verified; none of the confirmation models retrieves the
full training rows. The result does not establish optimal retrieval or identical
lifetime exposure.

The adapter predates the compiler and source-interface changes. Its extra
malformed actions warrant checking learned behavior after an interface change,
but do not isolate an internal interference mechanism. The [public review](../sources/2026-09-17-weight-consolidation-review/README.md)
finds existing compatibility methods; generic harness/model co-evolution is not
a new question. Learning a useful residual behavior under competent tools remains
more informative than manufacturing headroom by withholding those tools.

WC1–WC3 have bounded assessments in the original note. AD1 remains untested:
the investigator, not an acquired controller, selects the compiler intervention.

## Assessment after continuing consolidation

The [18 September continuation](../studies/2026-09-18-continuing-consolidation-findings.md)
adds two learning points on one database history. It reduces familiar execution
work without an incremental fresh-completion advantage or quality-matched cost
repayment. Shared external evidence remains accessible, but final-SQL teaching
coexists with zero fresh adapter searches or saved-query executions. This sharpens
the distinction between available experience and a policy that uses it; it does
not identify retrieval avoidance as the causal failure mechanism.

The sole scored stale-to-updated loss was an accidental output match from an
incorrect ranking query. It therefore does not demonstrate loss of a correct
procedure. Shared authored views already handle schema migration. These limits
leave AD1–AD3's existing assessments unchanged and narrow the next learning-target
and evaluation comparison. WC1–WC3 receive their separate updated assessment.
Previous AD2/AD3 assessments stand. One source history and one adapter update do
not establish continuing accumulation, and closing this explained workload limit
does not close the broader allocation question.
