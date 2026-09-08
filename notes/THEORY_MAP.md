# Agent memory: a working theory map

2026-09-08. A synthesis of the [research brief](RESEARCH_BRIEF.md),
[research perspective](TRENDS.md), and [Cycle 1 return](CYCLE_1_PILOT.md).
These are working conjectures, not established general results or claims of
novelty. This map organizes the questions; derivative projects own empirical
designs and execution.

**Central question: what should experience change in an agent, and how should
that change remain useful as its circumstances change?**

The account must distinguish acquiring information, making it available,
applying it, and improving an independently judged outcome. A persistent record
or a parameter update establishes that something changed. Its later value
requires separate evidence.

## 1. Applicability: when should past experience influence the present?

**Conjecture.** Retaining the conditions under which a lesson worked can make
its future use more selective than assigning it a single historical utility
score. This should matter especially when similar-looking tasks require
different behavior after a change in circumstances.

The competing explanation is that current observations and the model's own
interpretation already supply enough discrimination. Additional scope records
could then add cost or suppress useful transfer. Another possibility is that
poorly constructed lessons dominate the outcome, making selection secondary.

Cycle 1 makes this distinction concrete: resetting utility changed selected
memory sets, but obsolete SQL identifiers were never executed. That supports
separating selection from application; it does not establish that the model
correctly recognized and rejected stale advice. The affected records may not
have influenced the relevant action at all. [Pilot evidence](CYCLE_1_PILOT.md)

**Distinguishing evidence.** At matched access to current information, scope
information should reduce inappropriate transfer while preserving benefits on
tasks where the lesson remains valid. If ordinary retrieval and interpretation
repeatedly achieve the same result at lower total cost, the case for explicit
scope machinery weakens. Any extra supervision used to create scope records
must be counted.

## 2. Placement: which parts of learning belong where?

**Conjecture.** The useful allocation depends on recurrence, precision, and
revision needs: changing facts favor explicit records; exact procedures favor
executable tools; recurring judgments may justify training. Training could also
improve the use of external records without absorbing their contents.

This is a proposed allocation, not a fixed boundary. A sufficiently capable
model with ordinary retrieval may make much specialized machinery unnecessary.
Alternatively, weight updates may support precise revision well enough to move
that boundary. The [research perspective](TRENDS.md) leaves both possibilities
open; Construct has not established where external memory reaches a ceiling.

**Distinguishing evidence.** Compare allocations using the same underlying
experience, tracking additional supervision and total acquisition, inference,
verification, and maintenance costs. The proposed allocation should predict
differences in transfer and correction across workloads, beyond an isolated
benchmark win. Consistent success by one simpler allocation across those
conditions would weaken the need for the proposed division.

## 3. Revision: how can useful history survive without retaining obsolete influence?

**Conjecture.** Separating recoverable history from currently active guidance
can preserve useful recurrence while allowing selective correction. The
important boundary is whether recovered material remains eligible to guide
action after subsequent evidence has revised it.

X2 supplies bounded evidence for eviction with recovery at lower hot-store
token cost. M0 and M3 show that correction notices and the channels governing
their availability can affect behavior. Together they motivate this conjecture;
they do not demonstrate a system that combines economical recovery with
reliable revision. [Research brief, sections 1, 3, and 4](RESEARCH_BRIEF.md)

The rival is simpler retention or deletion: recovery and revision machinery
may cost more than it saves, particularly when recurrence is rare. Preserving
history can also reintroduce invalid guidance if recovery loses its correction
context.

**Distinguishing evidence.** Useful old knowledge should remain recoverable,
while superseded guidance should lose influence even after recovery or
consolidation. Quality, correction delay, and total cost all matter. Savings in
hot-store tokens alone cannot establish this broader advantage.

## Connections and evidence returns

These questions constrain each other. Placement determines how easily a
particular lesson can be revised. Applicability determines which experiences
merit consolidation. Recovery must preserve the distinction between historical
evidence and current authority. A local improvement can therefore create costs
elsewhere in the account.

For each derivative return, identify the claim it bears on, the link it actually
tested, the competing explanations still compatible with the result, and the
conditions under which the conclusion holds. Instrument failures qualify what
can be inferred; they remain visible without automatically setting the next
root task.

## Active cycle

[Cycle 2: from a correction to a reusable lesson](CYCLE_2_QUESTION.md) begins
with Construct M2. Its [evidence review](CYCLE_2_M2_REVIEW.md) distinguishes
the value of a supplied correction from the value of constructing a lesson
through experience. The [literature comparison](CYCLE_2_LITERATURE.md) separates
construction, application, and scope; these inform all three conjectures above.
The [derivative proposal](CYCLE_2_PROPOSAL.md) tests conditional rule compression
from fixed experience, with the primary link to applicability and a narrower
cost comparison relevant to placement.
Its [development return](CYCLE_2_PILOT.md) finds both inaccurate constructed
rules and composed-task failures with correct supplied rules. The compression
interaction did not support the predicted direction in four worlds. The next
derivative diagnostic separates compact-rule application from explicit lookup
and supplied-plan execution; the larger comparison remains parked.

Cycle 1's empirical follow-up remains with the user-directed derivative.
This map is a starting set of conjectures to revise, combine, or retire as
evidence arrives.
