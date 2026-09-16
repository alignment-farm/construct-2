# Maintenance decisions across learner histories

16 September 2026. Independent root development of question A in
[RESEARCH_DIRECTION.md](RESEARCH_DIRECTION.md). This is a scientific comparison
to develop, not another phase assigned to procedure-retention-and-revision.

## The uncertainty

The [state/support result](../studies/2026-09-15-state-support-findings.md)
establishes that the value of a support choice depends on the inherited learner.
It does not establish that a cheap observation predicts which choice to make.
A useful next question is:

> Does observing a small part of the current learner improve a maintenance
> decision on histories excluded from calibration, enough to repay the observation?

This separates two possible sources of regularity. An update may tend to harm
the same old behaviors across learners, so an association learned once transfers.
Alternatively, the same update may have materially different consequences after
different learning histories, requiring a current-state observation. Both may
hold in different regimes. A history interaction alone does not select between
them or establish that adaptation is worth its cost.

## Use the existing forecasting work

[P26, 2402.01865v3](https://arxiv.org/html/2402.01865v3) already connects forgetting
forecasts with replay, including sequential correction. [P27, 2406.14026v8](https://arxiv.org/html/2406.14026v8)
provides association-based prediction and sparse observed damage; its main
task-matrix analysis does not cover a continuing sequence of task learning.
The [implementation inspection](../sources/2026-09-16-study-preparation/README.md)
finds a released matrix-completion route. Adapting that route to a small local
problem is more informative than inventing an unspecified damage score.

The proposed extension changes the unit held out. Partition **learner histories**,
not merely question text or update examples. Separately acquire learners, then
revise them along different prior sequences. Keep every descendant of a shared
acquisition in the same partition when making an independent-history claim.
S2's published crossings can motivate the question and help development; fitting
a predictor to their outcomes and testing on paraphrases would not answer it.

Represent the target schematically as `D(history, update, support, behavior)`.
Measure it relative to the learner immediately before the proposed update and
the currently valid task specification. Previously incorrect behavior is not
newly forgotten; a superseded obligation should not be counted as damage when
corrected. Absolute complete performance is still needed because a small damage
score can coexist with poor acquisition or an unmet new obligation.

## A comparison that could change the account

| Decision basis | What it tests | Cost that belongs to it |
|---|---|---|
| Developed fixed support; history-agnostic damage-frequency prior | Whether stable regularities already suffice | Development/calibration and ordinary updates |
| Frozen association or representation predictor | Transfer of a learned forecast across histories | Training labels, model fitting, features and prediction |
| Same predictor plus a small current-state sample | Value added by observing this learner | Probes and any trial update required to generate them |
| Direct validation of candidate updates | Whether prediction saves useful work over measuring candidates | Candidate branches, evaluations, selection and final application |

A trial on a copied learner is still an update with a cost. A measurement after
a training prefix is an early observation, not a pre-update prediction. Compare
methods with their actual information access and paid work; do not conceal those
differences behind equal nominal probe counts. An oracle that sees full held-out
outcomes may diagnose available decision headroom but cannot be the deployable
controller.

The action must matter: select support, continue learning, replace a component,
or use an explicit fallback. Evaluate acquired new behavior and preserved valid
behavior together. Abstention is not a successful revision if a required new
behavior remains absent. Forecast ranking, calibration and complete task quality
answer different questions. If no candidate action preserves useful quality,
even perfect prediction cannot make selection successful; that result directs
attention to the action set rather than another predictor.

## Prospective expectation and independence

The root expects some frozen forecasts to lose decision value across materially
changed histories, and a small current-state observation to recover some of it.
This is untested. Strong fixed decisions performing as well would favor stable
regularity; direct validation costing less would undermine forecast investment;
an accurate forecast with no beneficial action would expose a different limit.
Report unsuccessful acquisitions and calibration costs rather than selecting
only states that make prediction convenient.

The investigator would choose the concrete workload, predictor and action set.
A native MLX learner is an established local route; the released forecasting
pipeline itself has not been run here. A small task-matrix adaptation is feasible
to investigate without reproducing the authors' large corpus of fine-tuning runs.
Hardware feasibility and adequate independent histories still need local testing.

This question does not depend on the new placement study. Conversely, placement
can compare fixed revision and fallback strategies without waiting for a learned
controller. Root work can continue by checking how existing forecasting results
separate stable update associations from changing learner state, and deriving
when improved prediction can change an available action. No model run or new
ancillary commission follows automatically from this note.

## When observation can change the decision

16 September 2026, after the placement assessment. This extends the comparison
above without changing AD2 or the original expectation. The
[focused reading](../sources/2026-09-16-decision-value/README.md) connects it to
decision-focused learning (P46) and costly computation selection (P47). Prediction
quality and decision value are already distinct in public theory. The following
deductions specify that distinction for our question; they are not experimental
findings or a new algorithm.

### A forecast can change while the best action stays the same

Let `Q(h,a)` be expected complete uses over a stated future sequence, for learner
history `h` and maintenance action `a`. Include both new obligations and still-valid
earlier ones. For this first argument, actions have equal cost and no additional
quality constraints. A possible decomposition is:

```text
Q(h,a) = b(h) + r(a) + i(h,a)
```

Here `b(h)` is a history effect shared by all actions, `r(a)` an action effect,
and `i(h,a)` their remaining interaction. This is a descriptive decomposition,
not an identified neural mechanism. With no interaction, arbitrarily large
changes in `b(h)` alter absolute outcome predictions but cancel in every action
comparison. Observing that change cannot improve selection among these actions.
An interaction can alter their gaps without reversing their order; it too need
not create selection value.

This qualifies AD2's motivating inference: changed learner histories are a
reason to investigate decision transfer, not proof that a frozen decision loses
value. The accepted S2 assessment contains an actual support preference reversal,
but does not show an affordable observation that recognizes it in advance.
S5 supplies a different boundary: learning the scorer's regularity did not improve
the work already handled by competent direct access. Neither result demonstrates
that a general state predictor is the missing component.

For two actions, define the complete-outcome contrast
`Delta(h) = Q(h,A) - Q(h,B)`. Its sign selects the better action under the stated
assumptions. If each action-value estimate has absolute error at most `epsilon`,
the contrast error is at most `2*epsilon`; a true gap larger than that cannot
have its sign reversed. This elementary sufficient bound is not a calibrated
guarantee for our learners. It explains why errors near consequential choice
boundaries matter differently from equal-sized errors elsewhere. Average forecast
MSE supplies neither the bound nor evidence that a choice improves.

### Price information about actions, including the alternatives

For a fixed observation procedure producing `z`, let `I` contain the information
already available without it. In a calibrated probability model, its gross
one-decision value is given below. Assume the signal informs the learner history,
with future outcome noise independent of the signal conditional on that history:

```text
V(z | I) = E_z[ max_a E[Q(h,a) | I,z] ] - max_a E[Q(h,a) | I]
0 <= V(z | I) <= E_h[max_a Q(h,a) | I] - max_a E[Q(h,a) | I]
```

The right side is perfect knowledge of this history's expected action values,
not foreknowledge of future random outcomes. The lower bound holds because the
decision maker can ignore the observation. An estimated policy can do worse:
calibration error, history shift or a wrong action model can produce negative
realized value. Paid observations need enough gain to justify their work;
seconds and tokens cannot simply be subtracted from complete-use counts. Report
quality and cost together, or explicitly justify a scalar utility conversion.

These expressions assume observation leaves the candidate learner and future
task unchanged. A disposable copied-state trial can approximate that separation
while still consuming compute. A prefix update retained in the deployed learner
changes the state as well as informing the choice; its direct learning effect
belongs in the comparison. A one-observation null also does not exclude a useful
sequence of observations. P47 explicitly identifies this limitation of myopic
selection.

A constructed example makes the scale visible. Suppose two equally likely
histories lead to these complete-use totals over 100 future requests, with equal
action costs:

| History | Support A | Support B |
|---|---:|---:|
| H1 | 100 | 90 |
| H2 | 60 | 90 |

Always choosing B gives 90 expected completions. Knowing the history gives 95,
so at most five expected completions are available from information alone.
A signal identifying each history correctly with probability 0.9 supports
choosing A on an H1 signal and B otherwise, giving
`0.5*(0.9*100 + 0.1*90) + 0.5*(0.9*90 + 0.1*60) = 93`.
The gross gain is three. A symmetric 0.6-accurate signal is informative but
insufficient to choose A: after its favorable signal, A's expected score is 84
against B's 90. The optimal choice remains B and the signal's decision value is
zero. These are checked arithmetic examples, not measured predictor accuracies.

Now add an equally costly explicit fallback that completes all 100 requests
in either history. It removes the information value for this choice. If fallback
instead has higher use cost, or fails on some obligations, a quality/cost tradeoff
returns. Likewise, an observation of the shared history effect `b(h)` can become
useful when fallback does not share that effect. Information value is therefore
relative to the full action set, its costs and the quality requirement. Zero
regret among inadequate actions must not be called successful maintenance.

### Consequence for the independent comparison

The next scientific target is the transfer of **action differences**, including
new learning and preservation, rather than absolute damage prediction alone.
Current-state observations should be judged by whether they resolve those
differences beyond known history and developed fixed choices. Full damage
forecasts remain useful diagnostics; they are not the decision endpoint.

P26/P27 supply practical forecasting comparators. P46 supplies a reason to
evaluate consequences of forecast errors, but assumes richer training outcomes
than a deployment log containing only the chosen action. A later investigator
must distinguish paid counterfactual branches from observed deployment outcomes;
neither missing action values nor transfer across independent histories is solved
by adopting a decision loss.

This sharpens research selection without restarting S2: determine whether
history-dependent action differences are observable at useful cost, with explicit
fallback and direct validation retained as serious alternatives. A fixed decision
that survives substantial forecast drift would narrow AD2 in an informative way.
No new empirical expectation is counted as confirmed by the constructed example,
and no model run or ancillary commission accompanies this extension.

## Concrete preparation and a stronger history control

The subsequent [comparison brief](MAINTENANCE_COMPARISON.md) selects the established
work-order task with newly acquired learners for a bounded history-rule transfer
test. A read-only calculation finds that matching current support to known
revision-1 history ties the state oracle on all six published starts. This is
retrospective development evidence, not confirmation of transfer, and makes a
no-probe history rule an essential comparator. Public code inspection separates
full-update sparse validation from actual early-training prediction. The
[preparation review](../sources/2026-09-16-maintenance-preparation/README.md)
records evidence, code provenance and limits. The brief recommends a bounded
independent investigation; it does not commission or run it.

**Subsequent status:** The user approved proceeding. The independent
[maintenance-decision-transfer study](https://github.com/alignment-farm/maintenance-decision-transfer)
([local](../../ancillary-studies/maintenance-decision-transfer/README.md)) now
owns the commissioned bounded comparison. Its preparation has not launched model
runs. The expectations and earlier preparation history above remain preserved.

## Assessment of the completed independent comparison

The [first publication](../studies/2026-09-16-maintenance-transfer-findings.md)
is accepted at `be7a508bfea002baceec72f32f7f9d6f73f7861a`. Match-history reaches
the two-support aggregate bound on two fresh acquisitions (524/768); sparse and
full validation add no aggregate gain. Every available endpoint remains
incomplete. The calibrated history/pre-observation/prefix controls all reduce to
constant Bridged, a diagnosed limit of their one-acquisition development set.
The broad value of current-state information remains unresolved by those controls.

The study adds an objective distinction to this note's action-value distinction:
equal totals can conceal different violations of new and still-valid obligations.
Paid validation sees such a difference even when its aggregate tie-break ignores
it. Information value therefore depends on the obligations used to judge the
decision as well as the available actions and their costs. This observation does
not retroactively change the frozen primary comparison or confirm AD2's rescue
prediction. The example-table alternative completes the finite task under
disclosed privileges. Close the bounded phase; do not automatically expand the
selector or reopen S2.
