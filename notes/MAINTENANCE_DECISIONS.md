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
