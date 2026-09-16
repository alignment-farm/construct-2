# Predicting whether learned behavior will survive an update

**Current assessment — 15 September 2026:** S2's
[state/support publication](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/FINDINGS-STATE-SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-STATE-SUPPORT.md))
is complete and accepted in the [root synthesis](../studies/2026-09-15-state-support-findings.md).
Inherited state and current support interact; the developed directional prediction
holds in both fresh acquisitions. Equal-accuracy hidden susceptibility remains a
selected diagnostic result. The [assessment below](#assessment-after-the-state-support-crossing)
updates MR1; MR2 and MR3 remain untested. No further phase is commissioned.
The original theory, prospective expectations and commission below are preserved.

**Original preparation, 15 September 2026.** The user approved maintenance reliability as the immediate
mechanism question, with useful memory placement governing the investment.
This root note follows the [completed third-phase assessment](../studies/2026-09-15-maintenance-findings.md),
committed at `d2f3a08`. The three experimental phases remain complete. This is
theory development and preparation for choosing a comparison, not a new local
commission or an experimental result.

**Question:** What observations available at a decision point predict whether
further learning will acquire useful behavior, preserve earlier behavior or
damage it—and when is acting on that information worth its cost?

The decision point may precede an update or fall between update blocks. Information
observed after damage cannot retrospectively count as a successful warning.
Complete current accuracy describes behavior on assessed cases; it need not
describe susceptibility to the next update. A trustworthy archive supplies
evidence, but its presence does not establish effective protection.

## What the existing evidence separates, and what it does not

S1's fixed and damage-aware policies both finish with complete acquisition,
yet differ along the way. Selection improves acquisition uses, worsens recurrence
and adds computation. Its virtual step reproduces the next actual incoming step,
but ranking is refreshed every sixteen updates and does not simulate the full
intervening replay sequence. A correct local loss forecast can therefore coexist
with a poor forecast of later complete behavior. The completed study does not
identify whether the signal, its horizon or the resulting intervention is limiting.

S2 offers a particularly useful distinction. Within seed 401, Novel and Bridged
both score 192/192 after the first revision. They nevertheless carry different
weights into revision 2. Their 192/192 versus 120/192 final divergence measures
the whole support strategy across two revisions; it does not isolate the effect
of familiar examples supplied only at the second revision. Optimizers reset
at each revision, so retained optimizer moments across revisions do not explain
this particular difference. The weights and subsequent examples can still interact.

**Post hoc inspection of existing evidence, not a new experiment.** In S2's
[final events](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/evidence/maintenance-final-v1/events.jsonl) ([local](../../ancillary-studies/procedure-retention-and-revision/evidence/maintenance-final-v1/events.jsonl)),
each revision-2 trajectory has 64 historical updates, of which ten rehearse the
first waiver. The last two such seed-401 updates, indices 183 and 186, concern
the same familiar entity and stock conditions. Their pre-step teacher-forced
losses are approximately .06813/.00142 in Novel and .50475/.31276 in Bridged.
The schedules and valid labels match, but losses at the evolving states differ.
The published schedule, experiment and runtime files match the executed snapshots.
We recomputed these counts and values from saved records without model calls.

These losses are a descriptive lead, not a validated predictor or causal
explanation. They are late training observations on two examples, not complete
generations from matched frozen states. Historical-label availability and update
counts alone do not show whether the earlier behavior is being maintained.

## Competing explanations and identifying contrasts

| Account | Why it remains plausible | A contrast that would distinguish it |
|---|---|---|
| **Learning history changes susceptibility.** | Equal complete accuracy after revision 1 conceals different weights and training paths. | Cross the two saved revision-1 states with the same candidate revision-2 support. A difference under identical current support establishes an inherited-state effect in those states. |
| **Current evidence allocation drives damage.** | Correction, negative boundaries and old-waiver rehearsal exert different pressures; valid labels do not determine their effective influence. | From an identical state, change one identified part of current support or its allocation while retaining comparable resources. Separate familiar identity in correction from identity in boundary examples if that is the hypothesis. |
| **The loss signal misses consequential behavior or the relevant horizon.** | Average token loss, individual margins and complete success can change differently; a one-step forecast need not predict a sequence. | Relate a fixed signal to subsequent complete losses on material not used to choose it, then test an action based on that signal against a strong fixed policy. State the forecast horizon. |

These accounts can coexist. “Interference” names the observed problem unless
an intervention or predictive account makes it more specific. Similarly,
explaining the two selected states does not establish generality across newly
acquired states, condition structures or tasks.

For S2, the smallest informative crossing suggested by the record is:

| Revision-1 weights | Novel revision-2 support | Bridged revision-2 support |
|---|---|---|
| Novel history | Existing trajectory | Unmeasured crossing |
| Bridged history | Unmeasured crossing | Existing trajectory |

This separates current-support effects, inherited-state effects and their
interaction. The published endpoints cannot fill the missing cells. Reusing
these already inspected states would be diagnostic development; a developed
claim would then need fresh evaluation. This is an identifying example for a
future investigator, not a prescribed protocol or a requirement to resume S2.

The saved records do not contain intermediate complete generations or frozen-state
logit margins. Characterizing those quantities requires new inference; filling
the crossed cells requires new updates. Further CPU analysis of existing logs
cannot substitute for those missing observations.

## What existing methods already supply

Gradient Episodic Memory constrains remembered task losses using a local gradient
approximation. A-GEM substitutes one constraint based on a sampled average memory
gradient. Gradient-based sample selection treats buffer contents as a choice of
constraints and develops a gradient-diversity surrogate. These are established
ways to address interference, with different aggregation and computation costs.
[GEM, 1706.08840v6, §3](https://arxiv.org/html/1706.08840v6#S3),
[A-GEM, 1812.00420v2, §4](https://arxiv.org/html/1812.00420v2#S4),
[GSS, 1903.08671v5, §§3.1–3.5](https://arxiv.org/html/1903.08671v5#S3).

Our inference is that the next question should concern the relationship between
those surrogate quantities and the complete behaviors we need to maintain.
Protecting average loss does not, by definition, protect every instance or
procedural obligation. Applying a method here would require checking its actual
optimizer, step size, evidence access and unit of protection; the local AdamW
sequence cannot inherit a guarantee for another update rule by name.

MIR/P22 is already adapted in S1. Candidate validation and rollback are also
existing background in P14/VANE. A new selector, validator or projection is not
automatically a contribution. The [focused reading record](../sources/2026-09-15-maintenance-reliability/README.md)
adds P23–P25 with exact versions and scope; no new algorithm is proposed here.

## Prospective expectations for a future comparison

These expectations follow inspected third-phase outcomes and the descriptive
loss inspection above. They precede any new experimental test. They do not
replace M1–M3 or count the already known outcomes as fresh confirmations.

| Expectation | Expected pattern | What would change the account |
|---|---|---|
| **MR1: equal assessed competence can conceal different update susceptibility.** | Some differing revision-1 states will respond differently to identical current support even when both initially complete the assessed tasks. | In the crossed comparison, current support explains the divergence with little inherited-state effect. This redirects attention toward the immediate intervention; interaction would support a conditional account. |
| **MR2: observations of specific obligations can improve damage prediction.** | A fixed signal tracking earlier corrections and unchanged behavior will add predictive information beyond current aggregate success or an average training-loss summary. | The extra observations do not predict held-out complete damage, or only predict cases already used to construct the signal. This weakens that proposed observation, without proving that all observable warnings fail. |
| **MR3: competence-sensitive decisions can improve on a fixed stopping schedule.** | Where acquisition varies, a development-selected check can avoid freezing incomplete learning while allowing some unnecessary updates to be skipped. | The check misses failures, cannot distinguish useful actions beyond strong fixed schedules, or its verification/repair cost consumes the benefit at comparable quality. Predictive accuracy without useful decisions is insufficient. |

A mechanistic comparison can establish a bounded effect without implementing an
entire controller. A decision claim additionally needs the consequences of the
chosen actions. Keep those contribution levels distinct, with fresh assessment
of claims developed through diagnosis. Existing training losses may be cheap to
observe, but their labels and scope annotations are supplied information. A
frozen-state trial with new generations, a shadow update or a gradient calculation
adds computation and must be charged if the deployed method requires it.

## Useful placement remains the reason to investigate

A reliability method can reduce damaging updates while making the learned system
too expensive to maintain. For a stated sequence of uses and revisions, compare
complete utility and all recurring costs with the best developed fixed method
and competent explicit evidence. Treat construction and research search
separately from acquisition, monitoring, rehearsal, inference and deployed repair.
Keep seconds, tokens, updates and storage in their native units. Similar average
accuracy can conceal different failures on earlier corrections; report those
consequences alongside the cost comparison.

The existing sandboxes give explicit solutions convenient structure. A further
placement experiment should expose a real burden of retaining or interpreting
experience, such as repeated use of a learned relation across new combinations,
while giving the explicit comparator the same relevant observations and serious
development. Artificially withholding decisive evidence or accepting an
undeveloped prompt baseline would not establish learning's value. Handwritten
rules and learned-from-example methods can both be useful references, with their
different preparation disclosed.

The next root selection should favor one identifying reliability contrast with
a credible path to a decision or placement claim. The state/support crossing
and the signal-to-complete-damage comparison are independent leads, not a
dependency chain or two automatically renewed studies. S4's completed account
remains relevant when retained evidence requires different reading; its next
extension need not precede this work. Ancillary investigators own implementation,
workload refinement and numerical budgets once a question is commissioned.

## Commissioned continuation

Historical commission, now completed and assessed below.

The next bounded investigation remains in
[procedure-retention-and-revision](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/README.md) ([local](../../ancillary-studies/procedure-retention-and-revision/README.md)).
The local [STATE_SUPPORT.md](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/STATE_SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/STATE_SUPPORT.md))
brief contains the question, artifact provenance, identifying contrast, resources
and publication expectation independently of this root checkout.

Its first task is to separate inherited state from current support, with a
bounded diagnostic crossing of the already inspected revision-1 checkpoints
or an equally informative comparison. The investigator owns the protocol,
reproduction checks, budget and fresh assessment appropriate to the claim.
An inherited-state effect, current-support effect or interaction would each
change the explanation; another recipe win is unnecessary.

MR2's warning-signal question and MR3's decision question remain independent
leads. They are not prerequisites or additional required campaigns in this
commission. The root will assess the resulting publication against MR1 and
its implications for reliable, useful maintenance. Routine local development
and execution are authorized; this preparation itself ran no models.

## Assessment after the state-support crossing

15 September 2026. The [root review](../studies/2026-09-15-state-support-findings.md)
accepts S2's fourth publication at `3e71eb5f146e6493c60cef26d15d86dedd2249fb`.
The commissioned identifying comparison and fresh assessment are complete.

MR1 receives direct support in the selected seed401 pair: both starts complete
192/192, but common Novel support produces 192/192 versus 120/192. Changing
support in the Novel-history state reduces success by 70 orders; in the
Bridged-history state it changes the aggregate by zero. Neither an inherited-state-only
nor current-support-only account explains the table. The crossed intervention
identifies a behavioral interaction, without identifying its internal cause.

The positive-interaction prediction holds in the two fresh acquisitions (+7 and
+34 complete orders), following a protocol fixed before acquisition. In seed502,
Novel support helps Novel history by ten orders and harms Bridged history by 24.
No seed502 combination completes all 192 orders. The fresh Novel/Bridged starts
score 182/192 versus 192/192 and 183/192 versus 192/192, respectively. These fresh
results extend the conditional account, not the equal-accuracy demonstration.
Higher initial aggregate accuracy does not consistently rank subsequent safety.

Every newest correction succeeds, yet earlier waivers and other unchanged cases
can fail. Remembering the earlier waiver is itself insufficient: seed502's
Bridged/Bridged endpoint retains 24/24 while losing 47 other unchanged orders.
This motivates observations of multiple obligations; **MR2 and MR3 remain
untested** because no advance warning or adaptive maintenance policy was evaluated.

The next preferred question is whether information available before revision or
after a bounded trial can improve prediction and a useful decision on fresh
acquired states. Current accuracy, known history and developed fixed support
choices are relevant comparators. Charge trial, checking and repair costs;
skipping a damaging update does not by itself satisfy the new obligation. Choosing
between the two tested support sets cannot always supply a fully preserving action.
This recommendation does not renew the commission. S2's publication is sufficient
to stand down the phase, while reliable maintenance and useful placement remain
open research questions.
