# Feedback for choosing what to change

16 September 2026. Independent root development of
[AD1](ADAPTATION_DECISIONS.md#three-predictions-and-their-possible-failures), while the user reports
maintenance-decision-transfer underway. The original AD1 expectation is preserved.
This note selects a narrower question; it commissions no experiment.

The useful question is whether experience improves the choice of a remedy beyond
a developed rule, and whether obtaining better feedback repays its cost. A generic
comparison of memory credit signals would substantially overlap public work.
The [new primary-method review](../sources/2026-09-16-feedback-comparison/README.md)
finds learned memory attribution, behavioral intervention validation, and
retrieval correction already implemented. Their evidence narrows the inquiry to
**learning which functioning remedy to use when similar failures have different
causes**. This is a conditional research opportunity, not a novelty claim.

## What the feedback can establish

These are root distinctions between quantities, not a ranking of algorithms.

| Feedback available to the agent | What it can teach | What remains unresolved | Relevant cost |
|---|---|---|---|
| Complete-task outcome after a chosen action | Return associated with that action in the observed situation | Untried alternatives; which intermediate record deserved credit | Task execution, failed exploration, delayed feedback |
| Fixed provenance, schema or evidence check | Whether a particular condition holds | Whether fixing it changes the complete answer | Checking and maintaining the rule |
| Targeted environment observation | New evidence about a suspected failure or a retained claim | Whether the observation changes the best remedy | Tool calls, inspection, latency |
| Answer-scoring proxy under changed memory | A local change in the scorer's preference for an answer | Actual continuation, later uses, correctness of the target | Scoring access, target provision, forward passes |
| Executed alternative followed to completion | A task-return contrast under specified interventions and continuation behavior | Other interventions, future distributions, effects below sampling resolution | Replays, restoring state, repeated continuations |

Terminal reward can train a useful decision policy without identifying the causal
contribution of every token. Conversely, a score's agreement with an intervention
does not establish that buying that score improves future decisions. Preserve
both distinctions when comparing mechanisms.

Public evidence rules out several tempting restarts. P49 already includes live
memory reversion and an offline target-noise study. P50 supplies trained memory
attribution; P51 supplies a separate step-credit audit. P52 makes a substantial
event-responsive retrieval rule a necessary comparator. See the ledger for exact
methods, scope and author-reported evidence. None is a local test of AD1.

## A worked decision problem

Consider a fresh failed task with a relevant record in the store. Failure may
arise because the answer context never received the needed evidence, or because
the reader failed to use evidence it received. The action set includes retrieving
additional evidence, rereading the existing evidence with a stronger procedure,
and a competent explicit route that performs both. A presence flag alone does
not reveal whether the evidence is sufficient or usable.

The following values are constructed, not measured. Complete success is worth
one unit; net value subtracts action cost in the same illustrative units.

| Failure regime | Retrieve: success minus cost .10 | Reread: success minus cost .10 | Explicit route: success minus cost .25 |
|---|---:|---:|---:|
| Needed evidence absent from answer context | .90 − .10 = .80 | .20 − .10 = .10 | .95 − .25 = .70 |
| Evidence present but unsuccessfully used | .20 − .10 = .10 | .90 − .10 = .80 | .95 − .25 = .70 |

In an equal mixture, either constant narrow remedy returns .45; the explicit
route returns .70. A perfectly informative diagnostic costing .05 permits .75.
At cost .15 it permits only .65, so the explicit route wins despite perfect
diagnosis. With symmetric diagnostic accuracy q, diagnostic-then-remedy value is
.10 + .70q − c. At c=.05 it beats .70 only when q > 13/14. A diagnostic that
sounds accurate can therefore be too weak to justify replacing competent access.

There is a separate learning issue. Suppose earlier sessions always used the
explicit route, with the same visible observations and .95 success in both
regimes. Those outcomes cannot distinguish which narrow remedy is better: two
worlds can agree on the recorded history and disagree on the untried actions.
Experience becomes informative through varied interventions, additional
observations or justified structural knowledge. This is an ordinary partial
feedback problem, not a new impossibility theorem. If a cheap existing check
already distinguishes the regimes, a developed fixed rule may capture the value.

The example connects AD1 to the existing decision-value argument (P46/P47), but
changes the scientific object. Maintenance-decision-transfer asks whether known
choice regularities survive different acquired learners. Here the issue is what
feedback produces a useful choice regularity at all. Both concern decision value;
their empirical contributions should remain distinguishable.

## Selected comparison and expectations

Develop one candidate around missing evidence versus unsuccessful use, retaining
the original AD1 prediction. Compare accumulated action/outcome experience with
a frozen event-responsive rule on the same visible observations and functioning
remedies. Then ask whether a purchasable diagnostic improves the learned choice
beyond outcome feedback alone. Keep the competent explicit route available.
Charge acquisition and diagnostics as well as subsequent execution; report
complete quality and costs separately before any combined utility judgment.

The initial scientific expectations are:

- Prior outcomes help when observable recurring circumstances predict which
  remedy works, and the experience includes informative action variation.
- Additional diagnosis helps when it resolves action differences missed by those
  circumstances cheaply enough. It need not provide perfect causal attribution.
- Experience adds little when one remedy dominates, the explicit route is already
  inexpensive, or a fixed check captures the relevant distinction. These outcomes
  would narrow AD1 without requiring another controller design.

Hold fresh episodes apart from selector development. An outcome-association
shuffle can distinguish remembered decision value from mere extra task training;
use it if that attribution is a material uncertainty. If weights are trained,
check that comparison arms receive comparable effective learning opportunity.
Failed acquisition requires diagnosis before interpreting a selection null.

## Next root work and boundary

The next useful step is a bounded feasibility review of the existing S4 evidence
and the closest retrieval-correction implementations: identify a task family
where both remedies function, their relative value crosses, and visible feedback
does not already settle the choice cheaply. Follow the ancillary review procedure
and its recorded revision boundary when opening S4. Existing aggregate omissions
and reading gains alone do not establish these conditions on matched episodes.

That review should yield either a concrete independent ancillary brief or an
explanation that competent access, an existing rule, or public evidence resolves
the candidate. Discovery should follow any sharper uncertainty it exposes.
Do not commission a generic credit audit, redo placement, or use the active
maintenance study's unpublished outcomes to choose this question. This bounded
literature-and-theory phase is complete; AD1 and the larger research program remain
open.

## Assessment after bounded feasibility review

The [completed review](../studies/2026-09-16-remedy-feasibility.md) does not select
this candidate for a new experiment. S4's published access rules lack a retrieval
remedy, its fitted reader improves MSE in all evaluated changed-task cells, and
competent full raw storage resolves its current workload. CRAG provides prepared
contexts, while P53 Adaptive-RAG already supplies outcome-derived strategy
learning and released competing-action outputs. None isolates the proposed
same-evidence reading repair versus additional evidence at a failed decision
point. This closes feasibility work on these artifacts without refuting AD1 or
changing its original expectation. No replacement experiment is automatically
selected; future workload discovery must earn priority through the uncertainty
it can resolve.

## Checking a reusable lesson — 19 September

The next root candidate concerns the passage from an observed episode to a
reusable lesson: **when does paying to check a proposed lesson improve later work
enough to justify that checking?** This develops the feedback question without
reopening the completed S4 remedy-feasibility phase or changing AD1–AD3. It is a
selection candidate, not a commissioned study.

Three local findings motivate the distinction. The
[continuing-consolidation review](../studies/2026-09-18-continuing-consolidation-findings.md)
found a correct answer from the wrong ranking computation. The
[lineage comparison](../studies/2026-09-17-migration-lineage-findings.md)
found correct state repair followed by unsuccessful task execution. Successful
acquisition has also depended on authored teaching and source-quality diagnosis.
Thus task outcome, episode explanation, lesson validity and future usefulness
are different objects. A successful retry can validate a repair on one episode
without establishing when to reuse it.

The [public-method reading](../sources/2026-09-19-experience-credit/README.md)
adds P92 CHIME's reflective memory selection and P93 Causal Agent Replay's
executed interventions. Together with P44/P48–P51, these narrow the contribution
to the additional decision value of paid verification. Another generic
reflection or memory-credit loop would overlap existing work.

The clean initial comparison would hold source episodes and proposed lessons
available across acceptance policies: retain raw experience for competent later
reuse; accept lessons through inexpensive grounded checks and reflection; or
selectively purchase an executed check before acceptance. Ordinary executable
checks and retained programs remain available. Any additional examples acquired
through checking are part of its treatment and cost, not free shared teaching.
If checking also rewrites lessons, distinguish that generation benefit from
better acceptance of the same candidates.

Later fresh tasks must test the claimed lesson's scope, consequential changes
and unchanged obligations. Measure complete outcomes alongside checking,
storage/retrieval, training where used, later execution and repair costs in their
native units. Improving attribution accuracy alone is insufficient. Different
learner histories matter because the same lesson can be useful, redundant or
misleading depending on what the recipient can already do.

The prospective expectation is conditional: selective checks should help where
recurring misleading lessons escape cheap checks and an affordable intervention
predicts later usefulness. They should add little where ordinary validation
already settles acceptance, source reuse is cheap, or the lesson rarely recurs.
Even an accurate check can cost more than the failures it avoids. Neural
consolidation could amplify either benefit or error; an adapter advantage is not
required to answer the initial question.

Next, assess workload feasibility: find naturally arising candidate lessons with
different future value, a functioning and affordable check, and a competent raw
experience baseline. Preserve P91's diagnostic that eligible experience delivery
must first have useful potential; unused retrieval is not itself a defect. A
workload already resolved by simple checks or reconstruction can close this
candidate without new model runs. Root owns this selection and literature work;
an eventual ancillary investigator would own methods and execution.

The [runtime memory-worker build](../derivatives/README.md#memory-worker-development--19-september-2026)
can later supply instruments for this comparison. Its completion is neither a
prerequisite for root development nor evidence that lesson checking pays.

## Runtime-review refinement — 19 September

The [memory-worker review](../sources/2026-09-19-runtime-memory-review/README.md)
at `09f6683` adds functioning learned evidence use: a separate trained memory
model improves original final completion from 9/28 to 26/28, with the primary
fixed. Ordinary retrieval completes 28/28 and is cheaper. The worker learns
selection from authored read/deliver demonstrations. Correctness and authority
of the archived rules are supplied, not inferred from the raw episodes.

This sharpens the proposed comparison in three ways:

1. **Hold later access competent while testing lesson acceptance.** The first
   comparison can use ordinary delivery and the same primary across policies.
   Otherwise, a weak or representation-sensitive reader can hide useful checks.
   Independently vary what evidence supports accepting a candidate; distinguish
   accepting a better subset from generating better candidates.
2. **Separate supplied authority from learned empirical claims.** The runtime
   correctly blocks delivery of records marked uncertain or superseded, but the
   controller assigns those marks. A verified external correction differs from
   a hypothesis that a behavior generalizes. Record a proposed lesson's scope,
   supporting observations and paid checks in the investigator's controller;
   do not treat model confidence or a declared `checked` flag as new evidence.
   The existing archive/state interfaces provide a usable execution boundary.
3. **Test the lesson and its use across representation and history changes.**
   Renaming IDs and shuffling the catalog jointly breaks this learned reader
   despite unchanged facts. Separate these changes when diagnosing dependence.
   Fresh histories are needed before claiming a reusable selection relation.
   Once accepted lessons have demonstrated downstream value, a distinct
   comparison can ask what memory-model training adds to their construction or
   use, with comparable acquired experience.

The root feasibility deliverable is now a candidate source stream with naturally
arising plausible lessons, a specific affordable check, and a competent reader
that leaves a consequential acceptance decision unresolved. The runtime's current
authoritative rule catalog is authored as correct and does not supply that uncertainty. Preserve its
successful ordinary solution rather than restricting access to create headroom.
No general-purpose verification subsystem or new adapter capacity is selected.

The derivative's suggested independent-history and varied-address development is
useful within its own remit. This review accepts the completed build and bounded
phase, including failed acquisition and the later primary-contract repair. Root
keeps the lesson-checking candidate independent of that development; original
predictions and completed ancillary boundaries remain unchanged.

## Lesson-acceptance commission — 19 September

The user subsequently authorized preparation of an independent study. The
[selection note](LESSON_ACCEPTANCE.md) records the question, workload lead and
prospective LA1–LA3; [lesson-acceptance](../../ancillary-studies/lesson-acceptance/README.md)
now owns bounded discovery, methods and experiments. P48's deeper cost-accounting
review and P94 narrow the public overlap before preparation. The initial comparison
holds candidate generation and competent delivery stable while varying acceptance
evidence, with raw experience and acquired programs retained. Additional checking
must earn its cost on later complete work. Preparing and publishing the repository
starts no investigator or model run and reopens no completed ancillary phase.
