# Complete behavior, maintenance reliability and later use

15 September 2026. Assessment of the three completed third phases against the
[prospective M1–M3 expectations](../notes/LEARNING_MAINTENANCE.md#prospective-expectations).
The [preceding follow-up assessment](2026-09-15-followup-findings.md) and original
expectations remain unchanged.

**The broader empirical milestone is met within small, controlled workloads.**
Learned policies now complete state-changing procedures through recurring
learning, one revision trajectory preserves every complete case through two
changes, and learned memory supports cross-event questions absent from writer
training. These are functioning learning results. Their central limitation is
reliability across states and uses, rather than another unexplained acquisition
failure. Competent explicit references remain stronger or simpler here; none of
the studies demonstrates repayment of learning cost at comparable useful quality.

## Publications and review boundary

All three clean study repositories were fast-forwarded from `origin/main`.
Their local and tracking heads were verified against the remote branch.

| Study | Publication | Reviewed commit |
|---|---|---|
| S1: experience selection | [MAINTENANCE_FINDINGS.md](../../ancillary-studies/experience-selection/MAINTENANCE_FINDINGS.md) | `6179d8d0d8bcbaa236e42f53470eddc39199d502` |
| S2: procedure retention and revision | [FINDINGS-MAINTENANCE.md](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-MAINTENANCE.md) | `28aa881833ac2f9cf478b0d2f8a0f233ecc90023` |
| S4: memory under goal shift | [future-use/FINDINGS.md](../../ancillary-studies/memory-under-goal-shift/future-use/FINDINGS.md) | `981719ffcda62fed0913461b50c0e97dbb4c10c8` |

We read the publications, frozen comparisons, consequential development decisions,
implementations, costs and retained evidence. Review checks and their limits are
recorded here. Training and model generation were not rerun. Methods, failed
attempts and operational records remain in the ancillary repositories.

Independent read-only checks found no material discrepancy. S1 checks verified
182 manifest entries, rescored 3,152 saved response states (1,520 fresh), checked
192 fresh selection blocks and twelve stopping-checkpoint equalities, and
confirmed frozen source/protocol snapshots and ticket separation. S2 checks
verified 138 manifest entries, independently rescored all 6,752 work-order
generations, recomputed obligations, paired losses and candidate costs, checked
320 repeat outputs and the matched formal workloads, and passed fourteen CPU
instrument tests. S4 checks verified 58 provenance/hash comparisons, reconstructed
all fourteen encoders' atomic sign codes, independently grouped all 65,536
four-record tuples for each of 28 representations, and reconciled 160 summary
cells and cost totals. Maximum S4 population-risk discrepancy was 1.63 × 10⁻¹³.
S1/S2 checks did not freshly decode token IDs, reload neural checkpoints or repeat
the reported model probes. S4 checks did not regenerate sampled histories or
replay PyTorch fresh-history metrics. Those limits distinguish our checks from
the ancillary studies' retained audits.

## S1: better acquisition does not establish better maintenance

Each dispatch must reserve an eligible resource, perform its required preparation
and ship, leaving the correct inventory and shipment state. Four sites and two
parcel kinds produce eight rule cells. All historical rules remain valid. After
an acquired first site, three other sites arrive and then recur. The study adapts
MIR's predicted loss-increase selection to blockwise LoRA replay, using a virtual
AdamW update with cloned optimizer state. This is an adaptation, not a replication
of the original image-classifier method.

Development first establishes complete acquisition, then remedies a selector
floor by extending training and matching the strongest fixed mixture's 75% replay
fraction. Both methods complete development behavior. The fresh protocol is
fixed at `ba91a06` before evaluation; its two seeds are retained without choosing
a replacement policy from their outcomes.

| Policy | Acquisition uses | Recurring uses | All post-arrival uses | Final cases | Paired successes lost |
|---|---:|---:|---:|---:|---:|
| Fixed 75% replay | 55/72 | 88/96 | 143/168 | 32/32 | 9 |
| Damage-aware 75% replay | 67/72 | 84/96 | 151/168 | 32/32 | 11 |
| Fixed replay, then stop | 55/72 | 63/96 | 118/168 | 21/32 | 6 |
| No maintenance | 24/72 | 24/96 | 48/168 | 8/32 | 0 |
| Explicit archive | 72/72 | 96/96 | 168/168 | 32/32 | — |

The selector gains eight complete uses overall, but gains twelve during initial
acquisition and loses four relative to fixed replay during recurrence. All
differences between the updating and stopping policies come from seed 107;
seed 103 succeeds throughout. Initialization and ticket strings vary together.
The 168 uses repeat 32 distinct requests across these two starts, not 168
independent task draws. Later paired losses concern each policy's own evolving
state; they do not isolate the causal effect of one selected record.

Actual maintenance updates and target tokens match: 3,072 and 15,360 respectively
per full policy across both runs. Damage prediction additionally costs 192
virtual updates and 6,144 labeled scoring forwards. Inclusive selection takes
905.16 measured seconds beyond approximately 611 seconds of actual training;
these shared-hardware observations are not general latency estimates. The result
is an accuracy/work tradeoff, with no demonstrated maintenance-efficiency gain
over the developed mixture. A loss-increase score is not yet a validated predictor
of complete-task damage.

Stopping shares the fixed policy's first three checkpoints exactly, then freezes
them. It preserves a fully acquired state in one seed but freezes 5/16 success
in the other, where continued learning reaches 16/16. Encountering every rule
does not establish acquisition. This diagnoses the fixed stopping schedule; it
does not test a learned or verification-based abstention decision.

The explicit reference retrieves a checked trace by site/kind and executes it
through the same sandbox, with no future-site records before their arrival.
It succeeds on every use without model updates. Its structured lookup key,
ticket irrelevance, supplied labels and checker are designed knowledge; the
comparison includes useful engineering rather than demonstrating autonomous
discovery of a memory strategy. Inventory resets between dispatches, tickets need
not be copied, and fresh testing introduces no new rules or workflow semantics.

**Root update:** M1 receives mixed evidence on complete use and contrary evidence
for the hoped-for preservation and useful-cost advantage in this setting.
Anticipating token-loss damage can change acquisition, but did not reliably
protect complete behavior better than a fixed mixture. The study explains its
early failure and tests the functioning recipe; further tuning to obtain a
selector win is not required to accept this contribution.

## S2: complete preservation is possible, but familiar support is not sufficient

A work order combines eligibility, reservation, shipment, stock and terminal
status. Two successive revisions waive certification in different scopes. The
first waiver must survive the second. Two acquired starts each branch into
**Novel** correction/boundary examples on new entities and **Bridged** support
that substitutes two familiar entities. Conditions, labels, rehearsal and
192 updates per revision match; identity overlap changes in both correction and
boundary evidence. The investigator supplies correction authority, validity
filtering and relabeling of first-waiver records for second-stage rehearsal.

Acquisition is functioning in both final starts: each completes all 192 original
orders. A predeclared development ladder selects 256 updates for seed 401 and
512 for seed 402, preserving the latter's failed 256 checkpoint. Their differing
budgets prevent attributing cross-start variation to initialization alone.
Development separately shows that allocating boundary updates to unchanged
ineligible examples repairs its first-revision losses. The fresh comparison uses
that selected recipe; it does not independently repeat the boundary intervention.

| Start and support | After revision 1 | After revision 2 | First waiver retained after revision 2 | Second-boundary unchanged successes lost / gained |
|---|---:|---:|---:|---:|
| Seed 401, Novel | 192/192 | 192/192 | 24/24 | 0 / 0 |
| Seed 401, Bridged | 192/192 | 120/192 | 0/24 | 72 / 0 |
| Seed 402, Novel | 179/192 | 132/192 | 12/24 | 60 / 13 |
| Seed 402, Bridged | 179/192 | 130/192 | 0/24 | 61 / 12 |

New-policy obligations are 0/24 before their corresponding updates. Seven of
eight endpoints correct all 24 afterwards, and fresh-entity obligations are
8/8 throughout. The exception is an acquired but withheld familiar case in the
first seed-402 Bridged endpoint: directly relabeled familiar examples are correct,
but that additional instance remains stale. Both Bridged final endpoints then
lose the entire first waiver, despite its relabeled rehearsal records.

The successful Novel trajectory is substantive positive evidence: all 672 uses,
including repeats across three policy versions, succeed. The other trajectories
complete 588, 587 and 584 uses. Repeats reproduce earlier tokens rather than
providing independent replication or new query-driven learning. Pairing unchanged
orders separates old successes lost from old errors repaired; net totals alone
would conceal considerable damage.

All 1,536 primary trained-endpoint outputs parse, and complete execution succeeds
whenever eligibility is correct (1,316/1,316). Thus this task removes the earlier
identifier-production bottleneck and gives decisions consequential state changes,
but does not establish acquisition of arbitrary multistep operations. All Boolean
conditions are covered by training or support; fresh entities vary identity.
Plans are emitted at once into independently reset sandboxes.

The competent explicit reference is a maintained JSON policy and interpreter,
which succeeds on the identical 672-use sequence. It receives investigator-written
executable clauses, stronger information than examples. A weak model prompted
with rules remains in the record; its failure cannot represent competent explicit
memory. The perfect learned trajectory requires 256 acquisition plus 384 revision
updates and substantial model inference. Manual policy construction and evidence
authority are unpriced, so this establishes neither an information-matched causal
ranking nor a universal cost ratio. No learning-cost repayment is demonstrated.

**Root update:** M2's proposed benefit from connecting familiar and unfamiliar
applications is weakened for this intervention. Such support does not reliably
remove stale familiar behavior or preserve earlier corrections. A complete
preserving path now exists, an advance over the preceding routing-only successes.
It is not confirmation of R4's original transformation-preservation claim: this
workload removes identifier copying, and three of four trajectories still lose
unaffected behavior. Behavioral success also does not identify independently
editable parameters.

## S4: availability is relative to the question and its read computation

The study reuses all accepted four-slot writers: two development and five
evaluation seed pairs. They were trained on individual four-sign records for
local parities or broad raw reconstruction. New histories contain 32 independent
events; changed questions ask two- and four-event parity or agreement in two
fields across events. These composed targets were absent from writer training.
All atomic record types were previously trained, and every reader receives
supplied query algebra. This tests later composition, not learning new operators.

Each evaluation seed receives 8,192 fresh histories, 40,960 in total. All ten
learned evaluation donors answer expected questions perfectly. Writer results
were known from the previous phase; these are fresh histories and compositions
of existing writers, not five new independent acquisitions.

| Expected writer read method | Two-event parity MSE | Four-event parity MSE | Two-field agreement MSE |
|---|---:|---:|---:|
| Ordinary | 1.820447 | 2.422528 | .329352 |
| Fitted conditional moments | .387176 | .511742 | .136104 |
| Exact population irreducible error | .387500 | .511719 | .137500 |

Fitted readers use the same frozen states, with additional raw labeled calibration
records but no composed training labels. They approach the analytic optimum.
The table compares sampled MSE with population risk; small finite-sample
differences do not contradict the bound.
Two narrow writers have zero irreducible error on these changed questions despite
previously losing some raw-field information. Three lose query-relevant
distinctions. Therefore a representation can be insufficient for reconstructing
everything yet sufficient for a particular later relation.

For distinct independent events, optimal k-event parity error is
`1 - (E[E[a | code]^2])^k`: local ambiguity compounds with the number of events.
The agreement query additionally requires the within-record moment `E[ab | code]`.
Replacing it with `E[a | code] E[b | code]` increases mean population MSE from
.137500 to .234375 without changing memory. This is avoidable read-computation
error, separate from unavailable distinctions. Exhaustive finite-support bounds,
not failure of a fitted probe, establish the residual unavailability. Independence,
distinct queried keys and recordwise writing are essential to the full-history
bound; temporal or correlated histories require another analysis.

Broad writers and explicit full records answer all tested questions correctly.
Both use 512 bytes of episodic state; learned weights add 2,336 bytes and fitted
readers require extra calibration and tables. Explicit full records need neither.
Smaller two-parity explicit storage is a disclosed lower-capacity comparison.
No new writer training was needed; donor acquisition costs are reported separately
for reuse and rebuilding. Single CPU batch timings do not establish a general
throughput advantage, and there is no demonstrated learning payback.

**Root update:** M3 receives bounded support beyond directly querying writer
reconstruction targets. Retained components support later combinations when the
reader supplies the operations. Narrow objectives can preserve enough incidentally
or discard decisive distinctions. A different reader can recover retained
information; it cannot distinguish states whose stored codes are identical.
This is a useful extension of the account, not evidence for a generally superior
neural store, unfamiliar atomic knowledge or learned reasoning.

## Assessment of the prospective expectations

| Expectation | Assessment |
|---|---|
| **M1: anticipated damage improves preservation per replayed example** | Mixed overall and weakened for the intended maintenance advantage. More complete acquisition uses, fewer recurring successes and more paired losses than the strongest fixed mixture, with substantial selection overhead. Loss prediction's alignment with complete-task damage remains unresolved. |
| **M2: familiar/unfamiliar evidence improves transferable revision** | Weakened for the tested identity-bridging intervention. Direct corrections generally work, but one withheld familiar case remains stale and both bridged trajectories lose the first correction. One unbridged trajectory preserves complete behavior through both revisions. |
| **M3: future-use assumptions affect retention and reading** | Supported in a factorized compositional setting. Same-state reader repair coexists with exact query-relevant collisions; broad retention supports targets absent from writer training. Operations are supplied, and competent explicit storage matches successful learned memory. |

S5 now has actual recurring-use and maintenance ledgers rather than only a proposed
measurement. None demonstrates a learned economy at comparable complete quality.
The explicit comparisons differ: S1 indexes the same observed examples using a
supplied key; S2 receives privileged executable rules; S4 directly stores the same
raw records with supplied query operations. These are informative references,
not interchangeable tests or a universal ranking of memory formats.

## Consequences and next research choices

The working unit is a **maintained capability**: learned behavior, supporting
evidence, update decisions and the reader or execution procedure that turns it
into useful outcomes. Acquisition, preservation during another update, correction
of familiar instances and answering a later question remain distinct achievements.
This connects the studies without assigning their failures a common internal cause.

The user’s concern about explaining inconclusive experiments is addressed by
scored contact here. Both procedural studies diagnose poor development recipes
before fresh evaluation; S4 extends an already functioning mechanism. The new
results include successful whole behaviors, controlled interventions and contrary
evidence for our expectations. Their limitations do not erase that progress.

The next high-value procedural question is why apparently competent starts differ
in subsequent maintenance, and whether an observable signal can guide update,
stopping or repair decisions at useful cost. S1 motivates separating acquisition
benefit from protection and checking loss predictions against complete damage.
S2 motivates explaining earlier-correction loss under known valid rehearsal and
isolating the effects of familiar support. These can proceed independently; a
shared benchmark or another study's implementation is not a prerequisite.

For S4, the present compositional question has a sufficient bounded answer.
A further study would need a consequential uncertainty, such as dependent events
that alter what can be recovered or a reader that must acquire its operations.
Simply increasing independent-history length would not supply that distinction.
The next placement comparison should make evidence access or maintenance
consequential while developing competent controls; difficulty or a neural win
is not an admission condition.

We accept all three publications as completing these commissioned phases.
The broader questions remain open. This assessment recommends directions; it
does not commission another round, launch experiments or reopen S3. Preserve
parallel ancillary ownership and choose continuations for the explanations they
can distinguish, rather than automatically renewing every study.
