# Research cycles

Start with a cycle's README for its question, current status, and latest root
conclusion. The [theory map](../THEORY_MAP.md) connects findings across cycles;
derivative repositories own executable experiments and raw evidence.

| Cycle | Question | Current record |
| --- | --- | --- |
| 001 — Memory utility | When do learned retrieval utilities stop helping after circumstances change? | [Assignment, evidence, and conclusion](001/README.md) |
| 002 — Lesson construction and application | Which conditions must a lesson preserve, and can its consumer apply them? | [Assignment, evidence, and conclusion](002/README.md) |

## One current record per cycle

Each cycle's **README is its single current metadata record**. Keep the
question, derivative, assigned investigator, latest root decision and its date,
assignment/proposal path and exact adopted revision, latest reviewed derivative
return and full commit, root assessment, and current conclusion there. Link to
the derivative handoff for operations. A pending, unreviewed return may be
listed separately; receiving it does not replace the latest reviewed evidence.
The project README, this index, and the working agreement link to that record
instead of copying changing assignments, approvals, or latest-return status.

Different records own different facts:

| Fact | Authoritative record |
| --- | --- |
| Current root assignment, investigator, and reviewed conclusion | Cycle README |
| Exact approved scope, caps, and delegated decisions | Assignment/envelope revision pinned by that README and adopted in the derivative charter |
| Executable treatment, configuration, and stopping/recovery rules | Derivative protocol and its recorded amendments |
| Actual spend, active processes, and operational next action | Derivative's durable ledgers and maintained handoff |
| What an earlier run or review established | Its preserved report, source pins, and evidence inventory |

For an approval of an existing proposal, update the **cycle README** with the
user's decision, investigator, date, and exact proposal revision, then commit.
The derivative records that root decision commit in its charter and maintains
its own handoff. Scope changes need a new explicit assignment revision; an
approval alone needs no edits to the global overviews or historical reviews.
An index edit cannot create user authority, amend adopted terms, or reset spend.
Preserve earlier decisions in Git and dated assignment records; a current link
does not silently amend a derivative's pinned adoption. If an explicit later
user decision suspends or supersedes an assignment, honor it and reconcile the
records before dependent work; do not infer new authority from a mismatch.

## Cycles and successive reviews

A cycle follows a research question through its competing explanations and
evidence. Diagnostics, repairs, repetitions, and bounded continuations of that
question stay in the cycle. Start a new cycle when the root deliberately takes
up a materially different primary question; link its motivation to the earlier
evidence. A new agent, protocol, budget, or return does not itself start a cycle
or authorize another experiment.

For new root assessments, use `reviews/NNN-<topic>.md` within the cycle, with
`reviews/NNN-<topic>-sources.json` when an inventory is needed. Number these
reviews in order of creation, starting at `001` in each cycle's `reviews/`
directory and taking the next unused number. Existing descriptive review
filenames stay in place; do not retroactively renumber them. Derivative return
IDs have their own sequence and need not match root review IDs. Record the
return path and full commit in each review, including any earlier assessment
it corrects or supersedes.

After review, update the cycle README's evidence pointers and conclusion.
Update theory or shared synthesis only where the interpretation changes.
Preserve older findings and pins; add a historical-status or correction link
when a note could otherwise be mistaken for current instructions. Prospective
plans in an old review describe its recommendation at that time, not a live
assignment. Its cycle README provides the current route forward.

## Organization

Each cycle lives in a numbered directory (`001/`, `002/`, …), with short
filenames such as `PROPOSAL.md`, `PILOT.md`, and `SOURCES.json`. Its README
provides the current account and a reading route through historical proposals
and returns. Add only the documents the investigation needs.

Shared synthesis, perspective, working agreements, and learning material stay
in `notes/`. Reusable derivative templates stay in `templates/derivative/`.
Root cycle directories contain reviews and source inventories, not copies of
the derivative's raw experimental archive.

Workspace links follow the current layout. Recorded commit IDs and source
hashes retain their historical meaning; use the recorded revision when
reconstructing an earlier source tree. Manifest fields ending in
`_relative_to_manifest` resolve from that JSON file's directory; fields ending
in `_relative_to_root` resolve from this repository's root. Paths within a
derivative file inventory remain relative to the named derivative repository.
