# What experience must preserve: assessment of the concurrent follow-ups

After this assessment, the user approved the [learning-maintenance phase](../notes/LEARNING_MAINTENANCE.md).
The assessment and its original decision boundary below are preserved.

That subsequent phase is now complete and assessed in the
[third-phase maintenance synthesis](2026-09-15-maintenance-findings.md).

15 September 2026. The three repositories were fast-forwarded from `origin/main`
and their resulting heads verified against GitHub before completing this review.
The previous root write-up remains in the working tree; this assessment extends
it without replacing the first publications or their predictions.

**The follow-ups establish functioning learning and make the explanation more
specific.** An experience already answered correctly can become useful rehearsal
during another update. A small set of contrasting examples can establish routing
scope without a broad archive, while extra history has state-dependent effects
on the rest of the action. A learned memory can omit distinctions and also answer
poorly about information it still contains. The three bounded publications are
accepted; none establishes a general memory-placement ranking.

## Publications reviewed

| Study | Follow-up publication | Synced publication commit |
|---|---|---|
| S1: experience selection | [FOLLOWUP_FINDINGS.md](../../ancillary-studies/experience-selection/FOLLOWUP_FINDINGS.md) | `dee1e3159ed0105f6a090c65b72f57cbc386fb10` |
| S2: retention and revision | [FINDINGS-SCOPE.md](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-SCOPE.md) | `6e7049458732c4f3e37e5b8a3d1993129c2bdcfa` |
| S4: memory under goal shift | [followup/FINDINGS.md](../../ancillary-studies/memory-under-goal-shift/followup/FINDINGS.md) | `0d516aaa82d30d07e239b44e88ac43b5fdbfddef` |

These follow-ups were published on 14 September and reviewed at the root on
15 September. The [first-round assessment](2026-09-14-concurrent-findings.md)
and the committed local handoffs supply the preceding questions. They are
qualitative research commitments, not registered numerical forecasts. Methods,
failed attempts, saved states and reproduction instructions remain study-owned.

**Review scope.** We read the publications, protocols, consequential development
and diagnosis decisions, implementations, retained evidence and Git histories.
Independent S1 checks rescored all 3,664 follow-up response records (1,896 fresh),
verified 186 manifest files, paired starts and selection chronology, and confirmed
15 identical development checkpoints, 512 repeated update records and 488 shared
responses across the duration extension. S2 checks rescored all 5,131 records,
verified 96 manifest entries and executed snapshots, common starts, final update
schedules, acquisition/repair counts, fresh-input separation and paired losses.
S4 checks recomputed all 67 code partitions and risk decompositions and 32 saved
networks on all 16 inputs: hard codes matched exactly, with maximum output
difference 2.48 × 10⁻⁷ and risk discrepancy 4.45 × 10⁻¹⁶. Its frozen files and
moment-analysis donor hashes matched. No material inconsistency was found.
These checks did not rerun training, model generation, tokenizer decoding or
diagnostic reader fitting; S4 sampled tensor-state regeneration was also not
repeated. All three study working trees remained clean.

## S1: learning only the current gap can destroy what already works

Two regions have opposite channel-to-destination mappings. Each learner starts
with one region acquired and the other wrong. All candidate observations are
correct. A policy uses labeled probes to choose the region with more errors;
a fixed mixture alternates both regions. Branches restore common starting
weights and use the same loss and optimizer.

At the development-selected 256-update endpoint, the fixed mixture scores
**96/96**, versus **48/96** for gap targeting, either pure source, and no update.
In **all six partial states**, targeting the gap acquires the missing region
and loses the previously learned region. The mixture preserves both. Mixture
and selected updates match in total updates and aggregate training input/target
tokens; more training does not explain their difference. Construction costs
384 updates, and either policy adds 1,536, for 1,920 total. Verification and
synthetic label access are disclosed separately.

This is an informative result against the expectation that remaining gaps would
motivate a useful change in the best source composition across states. The gap
policy identifies what is wrong but not what its update will damage. A fixed
balanced mixture suffices throughout this workload. It is not a test of repeated
online reselection, predicted-interference selection or every adaptive policy.

Development initially failed to acquire the mixture within 64 updates. Extending
the same trajectories and testing joint learning from base established a working
256-update regime before fresh evaluation. The fresh shorter mixture endpoint
scores **82/96 at 128**, so the first phase's simple short-training explanation
does not carry over unchanged. This is successful acquisition with measured
interference, not another unexplained learning failure.

The context reference scores 44/96 across partial states and 36/48 from base,
but uses one fixed, unoptimized prompt. The 96 outcomes contain only 48 distinct
requests, crossed with two states; three seeds vary initialization, order and
nuisance tickets within four fixed rule cells. The study demonstrates a local
source-composition effect, not broad superiority over accessible evidence.

**Root update:** repeating known material alone was redundant in the first
phase; including known material while learning competing experience is useful
here. Training value therefore depends on the other planned updates and the
later workload, as well as current accuracy and source truthfulness. Rehearsal
and interference-aware selection are established approaches: the study's
[CLEAR/MIR reading](../../ancillary-studies/experience-selection/sources/followup-rehearsal/README.md)
prevents us from presenting this as a new replay principle or treating failure
of current-error targeting as failure of those methods.

## S2: scope examples can suffice for routing; history changes other behavior

The correction changes copper/fast routing while preserving every other
condition and argument rule. Seven investigator-labeled examples cover all
unchanged conditions on one identifier also present in the corrections. This
crossing constrains identifier-specific shortcuts left open by the initial
development set. Four starts include the inherited pair and two new acquisitions;
one new start required a bounded replay repair. They are not four replications
of an identical full acquisition pipeline.

The primary comparison gives both boundary treatments identical correction
examples, boundary cases and condition order. A third update either repeats
the boundary case or rehearses a valid historical example of the same condition
with a different identifier. Both use **384 updates**; training token counts
are close but not identical. The investigator supplies labels and removes
obsolete records. Small-set rehearsal, additional identifier diversity and
evidence of invariance remain part of the comparison; it does not isolate
pure scope information from all rehearsal.

With only the seven boundary cases alongside the corrections, inherited FK and
new seed 101 achieve **96/96 fresh routes** and correct all four familiar scoped
routes. Broad history is therefore unnecessary for routing locality in those
regimes. Correction-only and tripled-correction controls acquire their examples
but preserve only **48/84 unchanged fresh routes** in every start. Extra updates
alone do not supply the missing boundary behavior.

Historical examples have an additional, conditional effect on complete calls:

| Start | Complete fresh calls: boundary repetition / history, out of 96 | Previously correct unchanged calls lost: repetition / history |
|---|---:|---:|
| Inherited CE | 27 / 46 | 19 / 15 |
| Inherited FK | 14 / 57 | 33 / 7 |
| New CE seed 101 | 35 / 74 | 8 / 5 |
| New CE seed 202 | 30 / 23 | 17 / 24 |

History reduces paired call losses in three starts and increases them in the
fourth. Every one of the 16 primary endpoints loses some previously correct
unchanged calls. Net gains include newly correct answers and do not establish
preservation. Routing-only successes can conceal large argument failures:
the FK boundary treatment gets all fresh routes right but completes **0/12**
fresh corrected calls. The revised tool metric is independent of argument
syntax; its counts are not interchangeable with the first phase's strict metric.

A further distinction matters for correction. Inherited CE with history gets
11/12 fresh scoped routes right but leaves **all four familiar scoped routes
stale**. Deleting obsolete examples from replay did not remove their learned
effects. A counterexample rule that retains old behavior on original identifiers
fits all supplied training examples. That establishes remaining ambiguity in
the evidence, not the network's internal rule. Fresh-input transfer and revision
of previously acquired instances must both be checked.

**Root update:** the scope part of our expectation receives support, and broader
rehearsal has conditional value beyond the seven explicit boundary cases.
It is neither universally necessary nor reliably protective. The stronger
[R4 preservation claim](../notes/PROCEDURAL_LEARNING.md#assessment-after-scope-and-rehearsal)
remains unsupported. The relevant system includes the learned state, examples
defining the change, and the validity and diversity of retained evidence.

## S4: a nonlinear memory can lose information and misread what remains

Each fixed-key record contains four independent signs. Expected tasks ask two
pairwise parities; changed tasks ask for raw signs. Learned encoder/decoder
networks use two or four binary code slots per record. Fixed addressing and
interference-free gradient writes remain. Actual queries are withheld at writing,
but both task families are investigator-known, and broad reconstruction directly
supervises the changed raw-field targets.

Every four-slot expected-objective fit acquires the parities essentially
perfectly, yet uses only **9–12 of 16 available codes**. Its population changed
error decomposes exactly:

**2.384825 ordinary MSE = 0.350000 conditional uncertainty + 2.034825 reader excess.**

Exhaustive enumeration of all 16 input types establishes exact code collisions;
different inputs become indistinguishable under the stated access boundary.
A fitted reader of the same frozen states approaches the resulting optimum
at **0.350615** fresh-history MSE. Broad reconstruction uses all 16 codes and
recovers both task families, as does four-slot explicit raw storage without
learning. Unlike the first study's full-rank inverse example, loss here is
not forced by nominal capacity: the narrow objective's learned representation
leaves available distinctions unused.

Reader repair is also more than recalibration. The ordinary network estimates
raw fields and multiplies them to answer parity; the alternative reader
estimates each target separately. If two equally likely inputs have
`(a,b) = (1,1)` or `(-1,-1)`, each field mean is zero but parity is certainly
one. Multiplying optimal field estimates is not optimal estimation of their
product. The alternative therefore changes the answering rule and receives
additional labeled fitting data; it is diagnostic, not ordinary performance.

At two slots, joint expected-task training fails acquisition in all five fresh
seeds despite adequate parity capacity. Bounded development shows that supplied
parity codes let the same reader learn, and direct intermediate supervision
lets the encoder learn those codes. This establishes a functioning route within
the architecture without isolating the precise joint-optimization difficulty.
The desired retention tradeoff between equally functioning learners at genuinely
restricted capacity remains unresolved.

**Root update:** objective-dependent information selection and reader failure
extend beyond the linear example and can coexist in one state. The strongest
result concerns underuse of sufficient capacity. The experiment changes tasks,
distribution, precision and architecture together; it does not isolate a causal
effect of nonlinearity. All 16 record types occur in training, so fresh histories
are new draws, not novel record types or unforeseen goal structures. Episodic
payload is matched, total preparation/reader costs are not. There is no learned
storage advantage over the competent explicit reference.

## Assessment of the preceding expectations

The [original wording](2026-09-14-concurrent-findings.md#prospective-expectations-and-independent-continuations)
is preserved. These judgments concern the tested settings.

| Expectation | Assessment after the follow-up |
|---|---|
| S1: different remaining gaps can favor different useful source choices beyond duration/abstention | Weakened as a case for adaptive source choice here. A fixed mixture is best in every state; targeting the right gap loses other behavior. Known experience can have conditional rehearsal value. |
| S2: boundary evidence reduces overgeneralization; broader rehearsal may protect other computation | Supported in its scope component and narrowed in its retention component. Small crossed evidence sometimes suffices for all routes; extra history reduces call losses in three starts and increases them in one. Pure scope information and rehearsal are still not separated completely. |
| S4: broader-use objectives retain more useful changed-goal information beyond the linear construction | Supported at sufficient four-bit capacity, with simultaneous reader excess and genuine collisions. The equally functioning comparison under tighter capacity remains untested because two-bit joint acquisition fails. Competent explicit storage matches the successful learned result. |

## Consequences for the research program

The unit of update value is the **combined learning plan and its later uses**,
not an isolated record's correctness or present prediction error. S1 gives a
direct behavioral example; S2 shows why the supporting evidence must also express
revision scope and preserve more than a routing label. The broader inference is
that what should remain explicit can include material needed to maintain learned
behavior, even when that material adds no immediate answer accuracy.

Information retained and computation available for reading it also belong in
the same account. S4 shows that adequate capacity and expected-task success do
not determine what else is recoverable. This connects to S3's distinction
between nominal capacity and the behavior training reaches, without establishing
a common optimization cause. Success on a familiar task is a limited description
of the state available for subsequent learning, correction or new questions.

These are substantive answers with functioning learners. Their limitations
identify narrower uncertainties rather than excuse an unengaged experiment.
The remaining generality gap is still real: two closely related Qwen routing
studies and one finite, fixed-address memory do not establish agent learning
across varied environments.

The commissioned follow-ups are complete; no further experimental campaign is
launched by this review. The next research choices should build on the distinctions
now established: selection by predicted update damage versus a strong mixture
(with MIR as prior art), correction of both familiar and unfamiliar cases from
evidence identifying the intended scope, and recovery under changing goals that
are not directly covered by reconstruction targets. These are open directions,
not three automatically renewed assignments. S5 still needs a specified recurring
workload and total cost at comparable useful performance, including acquisition,
rehearsal, evidence maintenance, reader repair and correction. S3's earlier
bounded publication remains complete.
