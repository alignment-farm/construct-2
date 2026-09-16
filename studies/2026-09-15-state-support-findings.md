# Revision support has different value in different learned states

15 September 2026. Root assessment of S2's completed
[state/support investigation](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/FINDINGS-STATE-SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-STATE-SUPPORT.md)),
following the [third-phase synthesis](2026-09-15-maintenance-findings.md) and
[MR1–MR3 expectations](../notes/MAINTENANCE_RELIABILITY.md#prospective-expectations-for-a-future-comparison).

**Accept the fourth publication and close this commissioned phase.** The crossing
separates inherited-state effects from current-support effects and demonstrates
their interaction. The developed directional prediction holds in both fresh
acquisitions. In one, changing support helps one inherited state and harms the
other. This is explanatory progress about learning, rather than another failed
recipe whose interpretation remains entirely open. Predicting the interaction
in advance and making maintenance reliably useful remain separate questions.

## Publication and review boundary

Reviewed study head: `3e71eb5f146e6493c60cef26d15d86dedd2249fb`, matching both
`origin/main` and the live remote branch, with a clean working tree. The publication
identifies `c6eb90c` as its evidence/audit commit. The original three publications
remain accepted and unchanged. Experimental ownership and retained evidence stay
in the ancillary repository.

The root read the publication, diagnostic decision, fresh protocol, acquisition
diagnosis, executed source snapshots, response records and audit ledger. Checks
verified 88 manifest entries and independently recomputed complete correctness
for all 4,736 saved responses from the work-order rules. Paired unchanged losses
and gains, both waiver scopes, all starting and endpoint scores, restored-state
hashes, matched schedules and 4,096 update records reconcile. Executed source
snapshots match their recorded Git revisions. The frozen fresh protocol matches
`795b649`, the acquisition execution revision.

CPU regeneration reproduces all published analysis fields and the entire phase
ledger. The current analyzer additionally reports pre-update newest-waiver scores
absent from the earlier diagnostic analysis; its shared results are unchanged.
All sixteen instrument, schedule and probe-selection tests pass. No material
discrepancy was found. The root did not rerun training, tokenize saved outputs,
reload adapters or repeat model probes. The study's four separate-process audits
report retokenization and 221 exact checkpoint probes; those are retained study
evidence, not additional root model runs or independent accuracy samples.

## What the crossing identifies

The inherited state comes from the Novel or Bridged first-revision history. At
the second revision, each saved state receives either current support set from
an independent restore. Novel uses four identities outside original acquisition;
Bridged uses two acquired and two target identities. These labels concern original
acquisition overlap, not whether every identity is new at the second revision.

AdamW resets in every cell. All receive 192 updates: 64 corrections, 64 negative
boundaries and 64 history examples, including ten rehearsals of the earlier
waiver. Within a support condition the histories receive identical examples;
within a history the support intervention changes correction/boundary identities.
Condition/label order and history stay fixed. Input-token totals match at 17,148
per cell, and supervised tokens at 1,536. Individual input lengths can differ;
this does not isolate an abstract familiarity effect from identity or tokenization.

| Acquisition | Initial Novel / Bridged | NN | NB | BN | BB | Interaction |
|---|---:|---:|---:|---:|---:|---:|
| 401, selected diagnostic | 192 / 192 | 192 | 122 | 120 | 120 | +70 |
| 501, fresh | 182 / 192 | 192 | 185 | 120 | 120 | +7 |
| 502, fresh | 183 / 192 | 143 | 133 | 121 | 145 | +34 |

Counts are complete orders out of 192. The first letter denotes inherited
history; the second denotes current support. Interaction is
`(NN − NB) − (BN − BB)`, measured in complete orders. The 192 correlated cases
are a finite assessment set, not 192 independent learned-state replications.

In the selected diagnostic, changing current support costs Novel history 70
complete orders but leaves Bridged history's aggregate unchanged. Holding Novel
support fixed separates the two initially perfect states by 72 orders. Neither
starting state alone nor current support alone explains this table. All starting
outputs, published diagonal outputs and diagonal adapter files reproduce exactly.
Optimizer carryover cannot explain the contrast because each cell resets it.
This identifies a behavioral interaction under the controlled intervention; it
does not identify a particular internal representation or gradient mechanism.

The fresh test fixed the positive-interaction expectation before either new
acquisition. Both signs agree, with substantially different magnitudes. Seed 502
is especially informative: Novel support adds ten complete orders to Novel
history but removes 24 from Bridged history. A support preference learned in
one state can therefore be wrong in another. Seed 501 also shows why higher
current accuracy is an inadequate safety ranking here: the initially imperfect
Novel history finishes better than the perfect Bridged history under either
common support condition.

## Successful new learning can coexist with substantial damage

Every one of the twelve revision-2 endpoints completes all 24 newest-waiver
obligations. Poor acquisition of the new correction is therefore not the cause
of their maintenance failures. Damage concerns earlier revised and unchanged
behavior, including explicit negative-boundary examples.

The diagnostic's failing cells lose the entire earlier waiver and wrongly grant
46 or 48 of the 48 still-forbidden waivers. Seed 501's Novel/Novel cell repairs
ten initial errors without losing an unchanged success; Novel/Bridged repairs
the same ten but loses seven. Its Bridged-history cells each lose 72 unchanged
orders. Complete success separates preservation and repair that a net score
alone would combine.

Seed 502 has no fully preserving choice. Its earlier-waiver scores are 23, 13,
0 and 24 out of 24 for NN/NB/BN/BB, while unchanged losses/gains are 49/9, 59/9,
71/0 and 47/0. NN wrongly grants all 48 still-forbidden waivers; BB remembers the
earlier waiver perfectly but loses 47 other unchanged cases. Monitoring only
the newest correction or only earlier-waiver recall would miss consequential
damage. This motivates broader observations; it does not establish that a cheap
predictive monitor exists.

## Freshness and the limits of MR1

Both fresh acquisitions fail readiness at 256 updates and pass at the prespecified
512 checkpoint. The failed scores are 48/64 training and 24/32 development for
501, and 40/64 and 20/32 for 502; both then reach 64/64 and 32/32. Seed 501's early
failure includes claiming shipment without reserving or shipping. Continuing
the fixed acquisition ladder establishes functioning complete behavior. Neither
failure was silently excluded, called forgetting or used to replace a seed.

After revision 1, the fresh Novel histories reject some certified violet/slow
orders and score 182/192 and 183/192, while both Bridged histories score 192/192.
All four are crossed without repair or a success filter. **Freshness therefore
supports the interaction, but does not independently replicate equal-accuracy
hidden susceptibility.** MR1 has direct support in the selected diagnostic pair;
its broader conditional account gains fresh support. Two fresh initialization/order
seeds on the same task are limited evidence of generality. New evaluation identities
are absent from training and readiness, while policy structure and templates are
shared.

MR2's advance damage prediction and MR3's useful decision advantage remain
untested. The findings do not rehabilitate familiar bridging as a universal
remedy, demonstrate an autonomous validity filter, or establish independently
editable parameter modules. The investigator supplies correction authority,
valid historical labels and rehearsal. The task remains one five-field proposal
executed atomically with reset stock; earlier identifier-copying problems remain
outside this assessment.

## Costs and the next research decision

The investigation uses 4,096 updates and 4,736 generations, including failed
readiness checks, acquisition, both histories and every crossing. It records
366,020 training input tokens, 32,768 supervised tokens, 389,728 inference prompt
tokens, 37,823 completion tokens, 2,212.07 active seconds and 52,497,860 bytes of
new adapters. Independent study audits add 127.07 seconds and 221 generations.
These are full investigation costs, not the price of deploying one trajectory.
The reused diagnostic states had earlier acquisition costs; reuse is disclosed.
Hardware timings are observational. No learning-cost repayment is demonstrated,
and the prior executable-policy reference retains its privileged supplied rules.

The root account now becomes more specific: **maintainability depends on the
relationship between the learned state and the proposed learning intervention.**
Current task success and the presence of correct replay evidence do not determine
it. This strengthens the case for studying decisions conditional on the state,
without establishing that such decisions can be made cheaply or reliably.

The preferred next question is whether an observation available before a full
revision, or after a bounded trial, can predict complete damage on new acquired
states and improve an actual maintenance decision. Compare its information with
current accuracy, known learning history and strong fixed support choices. Charge
trial updates, verification and any repair; abstaining also leaves the new
obligation unmet unless another route supplies it. Seed 502 shows that choosing
between these two support sets alone cannot always provide complete maintenance.
This is a recommendation, not a newly commissioned experiment or controller.

S2 can stand down with its four publications sufficient for synthesis. S1's
signal question remains an independent lead; S4's completed findings remain
relevant to the value of retained evidence. Their questions need not wait for
a single serial campaign. The larger placement question still asks when the
benefits of learned behavior repay acquisition, reliable maintenance and use
relative to competent explicit evidence. The present result clarifies one reason
that comparison is conditional; it does not change the project into a search
for a guaranteed neural win.
