# Is acquired correction lineage worth maintaining?

17 September 2026. Independent root selection within the question of how agents
accumulate useful experience and where it should live. This commissions
**correction-lineage**, following the user's request for at least two further
ancillary studies. It does not restart a completed correction or S2 phase.

> Does acquiring and maintaining dependency information while memory is written
> improve later complete correction enough to repay its cost, compared with
> reconstructing dependencies or rebuilding from the same source archive?

An agent can retain both a conclusion and information about why it should be
revised. The second is another allocation choice: pay while learning, when a
correction arrives, or during a later use. Keeping an accurate source record
does not by itself ensure that derived summaries, plans or lessons stop relying
on superseded evidence. Conversely, retaining every visible input as a reason
can cause unnecessary repair. This is an analytical motivation, not an observed
local failure or a claim that dependency maintenance is new.

## What the public work answers and leaves to compare

The [methods review](../sources/2026-09-17-independent-study-selection/README.md)
finds direct precedents for dependency-guided repair (P81/P82), dependencies
extracted during ingestion (P37), and correction through source-grounded draft
auditing (P83). Randomly deleting supplied edges is also already studied. We
therefore select the **decision value and lifetime cost of acquired lineage**,
rather than graph reachability, generic propagation or a missing-edge curve.

Distinguish three objects. A runtime can record exactly what an operation read.
That exposure trace is not proof that its output semantically depends on every
input. A model can instead propose selective support links; these are acquired
claims that can omit dependencies or invent them. An evaluator may know the
true dependency for scoring; that knowledge must not silently become treatment
input. A conservative all-input trace is a serious comparison, not a nuisance
to remove so semantic selection wins.

Hold the recipient fixed and begin with an authoritatively supplied correction
or invalidation. This separates propagating a known correction from detecting
which source was faulty. A later timestamp does not establish supersession;
the changed obligation needs explicit semantics. Preserve unrelated valid
conclusions and independently supported conclusions. Measure later recurrence
on fresh complete tasks as well as immediately repaired state.

Retain the same source archive for the alternatives. Compare maintained lineage
with dependency reconstruction when needed, competent query-time auditing and
whole-state rebuilding where feasible. The investigator chooses an identifying
subset and may combine methods. Withholding the archive would change this into
an information-retention comparison. Tests, current evidence and checking must
be comparably available; dropping all memory or refusing all tasks is not
successful correction.

Account for normal writes and dependency checking as well as withdrawal, repair,
validation, later reads and failures. Selective lineage needs to save enough
useful work to repay costs paid even when no correction arrives. Quality on
unaffected obligations matters alongside completeness of the correction. The
relative frequency of correction and cost of reconstruction are explanatory
conditions, not knobs to tune until one mechanism wins.

## Prospective expectations — CL1–CL3

These new expectations precede execution and leave earlier predictions intact.

- **CL1:** Acquired selective lineage will save useful repair work only when its dependency judgments are reliable enough to preserve complete correction; precise-looking but incomplete links can make it worse than conservative exposure records.
- **CL2:** Reconstructing dependencies from a shared source archive will be competitive when corrections are rare or reconstruction is cheap. Maintained lineage can repay its write and checking costs when repeated corrections avoid substantial reconstruction.
- **CL3:** Preserving independently supported conclusions will matter for complete future behavior. Aggressive invalidation can improve a stale-memory diagnostic while damaging valid obligations, and a strong rebuild or query-time audit may outperform selective repair.

## Why an independent study

[Procedural migration](EXPERIENCE_PORTABILITY.md) changes the recipient while
holding evidence fixed; this study changes source validity while holding the
recipient fixed. The active retained-implementation study compares acquired code
with reconstruction. None needs another's next result. Root synthesis will ask
whether maintaining the **ability to revise** should receive a different storage
and learning investment from maintaining the **ability to act**.

The private [study repository](https://github.com/alignment-farm/correction-lineage)
([local brief](../../ancillary-studies/correction-lineage/README.md)) owns workload
discovery, operational methods and publication. Small controlled environments
can expose the distinction; no particular graph, benchmark or weight treatment
is mandated. If usable lineage cannot be acquired, bounded diagnosis should
explain the limitation before closing. A strong simple alternative is an
acceptable outcome. The [study map](../studies/README.md#correction-lineage)
records the preparation revision; preparation starts no experiments.

## Assessment after publication — 17 September

The [root assessment](../studies/2026-09-17-migration-lineage-findings.md#correction-lineage-fewer-repaired-fields-need-not-mean-less-work)
accepts publication `f8ad1e1ce8b9842efa90305c1206b8690578a204` and closes the
bounded commission. The original CL1–CL3 and its rationale above remain intact.

**CL1 is partly informed, without a demonstrated failure threshold.** Initial
acquisition recovers all 33 fresh support candidates. Selective lineage repairs
18 fields versus 48 under the other methods, preserving complete state in all
six episodes. One false support link appears during maintenance but causes no
scheduled correction failure. Acquiring links can work; maintaining them remains
fallible. Fewer repaired fields alone do not establish useful savings.

**CL2 receives bounded cost evidence.** Selective lineage is more expensive than
dependency reconstruction after one correction, then narrowly cheaper after two
(13,613 versus 14,037 tokens across three histories). Whole-state rebuilding is
cheaper at both horizons and ends at 9,789 tokens. At this archive size, separate
link acquisition and maintenance calls cost more than they save. Joint writes,
larger archives and longer histories remain untested.

**CL3's preservation requirement succeeds in every arm.** All retain the site
escort requirement after the account requirement is removed and withdraw escort
only after the site correction. There is no selective advantage or direct
aggressive-invalidation contrast. All four methods repair 6/6 states yet complete
only 4/6 later task episodes because of shared arithmetic errors. A separately
frozen two-instance wording diagnostic improves 1/2 to 2/2 without changing
evidence or state; it narrows the explanation but does not replace primary scores.

The [review ledger](../sources/2026-09-17-migration-lineage-review/README.md)
records independent state/order scoring, cost reconstruction and public follow-up.
Correct state, reliable acquired support, correct later use and total-cost value
are separate claims. Functioning repair, the small-archive cost limitation and
fresh read-time diagnosis justify phase closure. The broader value of lineage
remains open; no continuation is commissioned.
