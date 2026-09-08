# Cycle 1 workload return: the interface improved; utility remains open

2026-09-08 · Review of Grok's return at derivative commit
`2b27fb55dd2593f4d8ff6179b1fec8921fe4d7f7`,
[report](../../../../construct-memory-utility/notes/returns/001-progress.md).
**The return supports its bounded account and correctly stops at the exhausted
budget.** The new evidence exercises writing and retrieval, addressing the
main gap in the [previous channel review](CHANNEL_REVIEW.md). It does not
establish a benefit from resetting utilities or justify a confirmatory study.

The [review inventory](WORKLOAD_REVIEW_SOURCES.json) pins 43 inspected files and
records recomputed results. Current workspace links include a later navigation
refactor; the commit above identifies the evidence reviewed. No model calls,
database operations, or derivative edits were made during this review.

## What checks out

The four remaining benchmark starts were used on the declared first-pass
MemRL workload: tasks 211, 315, 51, and 176. The run completed four episodes,
with nine actor and four writer chat calls. All 13 returned nonempty final
content; episodes 2–4 retrieved one, two, and three memories. Memory records
were written and utility updates logged. This establishes execution of the
revised path on this workload, including real writer calls.

| Task | Retrieved memories | Independently checked outcome |
| --- | ---: | --- |
| 211 | 0 | Incorrect final database rows despite a completed, parseable UPDATE |
| 315 | 1 | After a SELECT, the actor asked a clarifying question instead of giving the required action |
| 51 | 2 | Correct |
| 176 | 3 | Correct |

Reanalysis from a temporary copy reproduces all four scores and the complete
committed analysis. Channel diagnosis also matches after accounting for the
temporary source path. The five additional writer probes exactly replay the
selected old requests with the declared writer instruction, 4,096-token cap,
and requested reasoning setting. All five now have nonempty final content and
finish with `stop`. Writer occupancy is established; script quality and causal
usefulness were not assessed by that criterion.

The source fingerprint is a real improvement: all eight recorded adapter-file
hashes match the later pinned return, and their combined digest reproduces.
The logged dirty working tree is disclosed. This fingerprint covers adapter
code, not the entire execution environment. Model aliases are recorded, but
the smoke does not supply a complete per-run model/backend/template identity.
Future batches should capture that identity before inference, alongside a
committed protocol and source. Requested reasoning effort remains unverified
as effective backend behavior. The older no-memory smoke's provenance gap
has not been retroactively repaired.

Eleven targeted tests pass with fake endpoints and no database fixture. The
original assembled Pilot 1 artifacts are unchanged. The SQL actor parser is
no longer presented as a writer-validity test: the writer aggregate reports
its substitution count as unavailable.

## Accounting and scope

Recomputed cycle accounting agrees: **100 benchmark starts, 98 scored episodes,
and two instrument failures**, plus **14 separate chat probes**. The 98 scored
episodes include four early scores excluded from the assembled Pilot 1
comparison; that original comparison still contains 84 episodes. The two later
smokes add six and four scored episodes. These records are not one pooled
scientific comparison.

Pilot segments contain 247 recorded chat responses and 325 embedding responses;
the 14 chat probes are additional work. The new memory smoke accounts for 13
chat and 17 embedding calls, 27,949 chat tokens, 1,043 embedding input tokens,
and 78.245 seconds elapsed. The five new writer probes add 11,265 reported chat
tokens and 80.080 seconds of request time. All are development observations
on the original tasks, with no new independent task cohort or migration/reset
comparison. Tasks 307 and 220 remain untested on this revised memory path.

## What this changes in the account

The earlier writer/path validation gap is substantially narrowed on the tested
workload. Nonempty responses still do not establish a valid action, and a
valid action still does not establish correct execution. The return makes
these distinctions inspectable without turning every participant error into
an instrument defect that must be removed before research can proceed.

The first stored memory's utility moved from 0.5 to 0.35 after task 315 failed,
then to 0.545 and 0.6815 after later successes. These are recorded credit
assignments to a retrieved memory, not counterfactual demonstrations of its
contribution. This is a concrete connection to the
[theory map](../../THEORY_MAP.md): historical utility reflects the whole
memory/consumer/interface path. The consumer-recalibration conjecture remains
untested, and the migration question remains open.

Grok's stop is appropriate. Ownership did not add resources after the
100-start development envelope ended. Our templates already provide a place
for authority and budgets; the missing item is a populated continuation
assignment. A detailed protocol need not require another root approval when
its scientific scope, discretion, and resources have already been assigned.

**Recommendation at this review:** authorize the proposed
[C1-02 development envelope](CONTINUATION_ENVELOPE.md), rather than a large
confirmatory study. Two separately acquired fresh cohorts and repeated
post-migration encounters address an actual gap in the pilot. Their results
would still be descriptive. The envelope delegates preparation, protocol
freezing, execution, and bounded repairs while retaining explicit limits on
scope, spending, and interpretation. At that point Cycle 1 remained parked
without new inference authority pending the user's decision.

**Subsequent decision — 2026-09-08:** the user approved C1-02 as proposed at
root commit `a55b1021e4994ddb19f57a08188ec64a566bbdff` and assigned it to Grok.
The [adopted envelope](CONTINUATION_ENVELOPE.md) now authorizes preparation,
protocol freezing, and execution within its limits, with durable budget guards
required before inference. This changes the assignment status, not the findings
or evidence pins of this review.
