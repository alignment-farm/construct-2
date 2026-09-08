# Cycle 2 entry: what M2 actually changed

2026-09-08 · Read-only examination of the original Construct record.
This is a new interpretation of existing evidence, not an experimental rerun.
The [Cycle 2 question](QUESTION.md) develops its implications.

## The phenomenon

**An externally corrected failure became a retained record that improved a
later decision. What part of that process constitutes learning, and what would
establish a reusable change beyond the corrected case?**

M2 provides a concrete starting point because its intervention is unusually
inspectable. Its [specification](../../../../construct/notes/SPEC_M2_RESIDENT_SUBSTRATE.md)
separates the source of a correction from the model's account of having learned.
The [findings](../../../../construct/notes/M2_FINDINGS.md) report a bounded benefit
across a cold session boundary.

## The retained object is a supplied correction

In [session 1](../../../../construct/episodes/m2/rs-e1.json), the agent receives an
apparently valid fish age-estimation finding and decides whether to cite it.
The external corpus records a retraction. After a scored failure,
[the mint](../../../../construct/harness/resident.py) constructs a record from the
corpus's claim, event, and stated reason. It ends with an explicit instruction:
“Decline to cite it as a current finding.”

This is deterministic correction construction. The mint does not ask the
agent to explain its mistake or infer a general principle. The failure gates
creation of the record; the corpus and the programmed decision rule supply
its content. That distinction follows the original design, rather than
identifying a defect in it.

In [session 2](../../../../construct/episodes/m2/rs-e2.json), both branches receive
the original finding. The resident also receives the correction; the control
does not. The [runner](../../../../construct/harness/run_m2.py) makes the added record
the sole difference in offered record membership and provides enough retrieval
slots to avoid displacement. The later question concerns the same finding in
a review-writing context. No new retraction or procedural problem is tested.

The retained text bundles a case-specific fact with the desired decision.
This is legitimate corrective information for M2's question. It means the
experiment does not separately estimate the contributions of the fact, the
instruction, or an agent-generated interpretation of the earlier failure.

## What the primary record supports

Inspected both session ledgers for all ten `nsample` runs and the later `abl5`
run. These are readings of recorded outcomes and verdicts, not newly generated
scorer verdicts.

| Recorded evidence | gpt-oss-20b, five draws | Claude, five draws |
| --- | --- | --- |
| Session 1 oracle score | 0 in all five | 0 in all five |
| Session 2 resident decision | Decline in all five | Decline in all five |
| Session 2 control decision | Cite in all five | Cite in all five |
| RS-1 verdict, including ablation requirement | 5/5 pass | 4/5 pass |

All ten recorded precondition checks passed. The Claude miss was an ablation
that still declined without the correction, so that draw did not satisfy the
record-influence requirement. In the separate `abl5` run, all five
correction-removal samples changed to cite. This supports influence under the
tested conditions; it does not make every future ablation deterministic.

All eleven inspected runs contain identical lesson text. Repeated draws sample
responses to one corrected case; they are not eleven independently learned
rules or eleven task families. The ledger paths and file hashes are retained
in the [source manifest](SOURCES.json).

## The boundary the next cycle should preserve

**M2 supports the value of making a checked correction available in a later
session. It does not isolate the value of personally making the earlier error.**
There is no branch given the same correction without the failure history,
nor one that constructs a lesson from the same evidence by a different method.

There is also a useful analytic boundary. Under M2's intended cold-instance
assumption, if weights, effective model inputs, available actions, and execution
conditions are identical, changing only the undocumented origin of a record
cannot change the conditional response distribution. An identical copied
record can carry the same useful information. This is a consequence of the
specified information flow, not a newly measured equivalence result.

Experience can still be valuable because it determines what gets discovered,
checked, recorded, selected, or trained. The interesting comparisons concern
those changes and their costs. An identical-record comparison would primarily
check isolation, not distinguish theories of procedural acquisition.

Two stronger interpretations in the historical narrative also need care:

- Failed controls establish failure to use the correction unaided on those
  draws. They cannot prove that related information is absent from pretrained
  weights.
- The disclosed stale-memory cases do not establish that capable models always
  override obsolete guidance on fair tasks. They establish that the proposed
  pathology was not observed in those cases.

These qualifications preserve the observed positive result while keeping its
mechanism and generality open. The existing [research synthesis](../../RESEARCH_BRIEF.md)
already adopts the narrower scope.

## Inspection limits

Reviewed the M2 specification, findings, episode inputs, mint, runner, prompt
construction, scorer, and the named ledgers. The inspected Construct checkout
was at `786374ce9616c2c155d2a5603bed9149a6fc956e`, with unrelated working-tree
changes; file hashes identify the actual materials read. Current code is used
to understand the implementation, not asserted to reconstruct every historical
server detail. The publisher's retraction sources were not rechecked, and the
original model endpoints were not contacted. No Construct files were changed.
