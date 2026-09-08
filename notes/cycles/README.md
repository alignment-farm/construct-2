# Research cycles

Start with a cycle's README for its question, current status, and latest root
conclusion. The [theory map](../THEORY_MAP.md) connects findings across cycles;
derivative repositories own executable experiments and raw evidence.

| Cycle | Question | Current status | Latest root assessment |
| --- | --- | --- | --- |
| [001 — Memory utility](001/README.md) | When do learned retrieval utilities stop helping after circumstances change? | Original budget exhausted; proposed continuation awaits user assignment | [Workload review](001/WORKLOAD_REVIEW.md): revised writing/retrieval path exercised; utility-reset question remains open |
| [002 — Lesson construction and application](002/README.md) | Which conditions must a lesson preserve, and can its consumer apply them? | Assigned attempt returned with a protocol stop; larger study parked | [Application review](002/APPLICATION_REVIEW.md): the diagnostic comparison is incomplete; development findings stand |

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
