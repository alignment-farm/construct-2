# Cycle 1: first empirical return

2026-09-08. The [proposal](PROPOSAL.md) is now implemented in the
[construct-memory-utility derivative](../../../../construct-memory-utility/README.md).
The derivative owns the [full pilot report](../../../../construct-memory-utility/notes/PILOT_REPORT.md),
pinned upstream source, environment, protocol, raw traces, amendments and analysis.
The completed pilot evidence is committed in the derivative as `80f6d18`.
The later [channel diagnostic review](CHANNEL_REVIEW.md) covers Grok
4.6's return at `6eaaed6`: a declared interface change produced 13/13 nonempty
actor responses and 5/6 successes on a no-memory smoke. It preserves the pilot
and does not add utility-reset evidence.

The first 84-episode development comparison is complete. It required 90 attempts:
an earlier four-episode partial run, two instrument failures, and the included
comparison. One failure was a shared connection-pool defect; the other was my
mistake in running database tests against an active experiment's scratch database.
Both are preserved. The final branch was recovered from an unchanged, verified
checkpoint after database isolation was fixed. These interruptions limit the
evidence; they are not memory-policy losses.

## What changed in our understanding

**The intervention is real.** Resetting utility changes the selected memory set
in all twelve fixed-checkpoint original/migrated retrieval replays. The
deterministic integration checks also verify numeric Q updates and isolation
between cloned branches. A null result would therefore require more explanation
than “the reset did nothing.”

**The proposed stale-identifier failure did not appear.** No obsolete SQL
identifier was executed. Nine of twelve affected migrated attempts produced SQL;
three produced none. Transparent suffix renaming with the current schema visible
appears easy enough here that obsolete memories need not cause obsolete actions.
Retain/reset succeeded on 6/6 versus 4/6 migrated tasks, while both original
branches scored 5/6. That single-history interaction of −33.3 percentage points
does not establish a population effect or a causal account of those differences.

**Utility feedback mixes several kinds of behavior.** Twenty-seven of 148 actor
calls returned empty final content. Some failures occurred after a useful SQL
query, while three DML episodes scored correctly despite final-output validation
failure because their database state was correct. The reward is defined by the
benchmark, but it cannot be read as a clean measure of the quality of retrieved
SQL procedures. We need to distinguish response-production behavior from the
specific mechanism proposed in the theory.

**The pilot horizon measures immediate transfer more than adaptation.** Each
affected task appears only once after migration. There is no later encounter
with that task after its first migrated memory has been acquired. A main study
of inherited-score inertia needs repeated post-change encounters.

The adapted reproduction's last-pass counts were 3/6 without memory, 4/6 with
similarity, and 5/6 with MemRL; both adaptive policies ever solved 5/6 tasks.
These dependent development counts do not confirm the paper's quantitative
claim. All 84 included scorer outcomes agree with independent checks.

## Empirical follow-up in the derivative

The following work remains with the derivative, under the user's direction.
It is not the root project's current task; the broader implications belong in
the [theory map](../../THEORY_MAP.md).

The empty-response issue is now characterized and an actor-only workload smoke
has completed. The revised writer and full memory-conditioned path still need
declared workload checks before scaling. Then freeze a fresh-data design with repeated post-migration encounters,
several independently acquired histories, and a compute budget chosen with
prospective precision in mind. Preserve the migration family and competing
hypotheses; do not tune the task change simply to produce obsolete SQL.

The derivative's [next-run design](../../../../construct-memory-utility/notes/NEXT_RUN_DESIGN.md)
includes explicit precision scenarios and costs. No main experiment has started
and no confirmatory protocol is frozen. The [learning appendix](../../LEARNING_APPENDIX.md)
now points into actual code, tests, protocol decisions and failure records.
