# When should experience become a retained program?

Root selection, 17 September 2026, originally written while evidence-use-under-revision
ran independently. That phase is now accepted and complete. The subsequent
[artifact assessment](../studies/2026-09-17-executable-feasibility.md) closes the
review selected below; its implications follow at the end. The user authorized this focused review of executable
experience. It broadens the comparison within the enduring directive; it does
not replace the neural-learning emphasis or the evidence-use question.

**Select the marginal value of retaining an implementation, compared with
retaining experience sufficient to regenerate executable behavior.** The next
step selected at that point was a bounded artifact feasibility review. The
sections through EX1–EX3 preserve that selection; the later sections record the
completed reviews and subsequent commission.

## What is already answered

The [reading ledger](../sources/2026-09-17-executable-experience/README.md) adds
P60–P70, with exact versions, inspected sections and limits. Voyager was already
indexed as background; this round deepens its methods reading and follows newer
and complementary results. None was reproduced locally.

Public work substantially answers whether agents can acquire, test, abstract,
reuse, share and revise executable artifacts. Several papers also measure costs
or compare contextual and callable workflows. Generic demonstrations of tool
creation, code reuse, portable interfaces or regression-gated updates therefore
do not justify another study. The literature is neither uniformly positive nor
well summarized by a count of acquired skills.

The remaining selection is about attribution and allocation. Did persisting the
implementation improve later work, or did the system benefit from more attempts,
extra teacher information, an executor, a stronger maker, a better interface or
more environmental observations? Those may all be useful changes, but they answer
different questions about where experience should live.

## Refined theory

Separate four things that the word “skill” often combines:

| Retained object or capability | What it contributes | What must still be established |
|---|---|---|
| Trajectories, examples and procedural descriptions | Evidence and guidance for reconstructing an action | Enough information survives abstraction for fresh use. |
| Executable implementation | Avoids repeatedly reconstructing a procedure | Invocation, current assumptions and complete behavior remain correct. |
| Tests, contracts and usage conditions | Evidence about where the procedure works | Coverage extends beyond the examples that produced it; obsolete requirements are retired. |
| Runtime observation and fallback | Responds to state not fixed at compilation | Its cost and information access are visible and shared in comparisons. |

These objects can coexist. Code may be read as context, invoked directly,
parameterized by current facts or repaired through another retained tool. Text
may be converted into code and executed. Thus “code versus text” is not a clean
contrast unless the execution and observation opportunities are specified.

A useful working inference is that code saves repeated reconstruction of a
procedure whose assumptions persist. It can also preserve stale assumptions
precisely. A textual lesson can become stale too. Neither representation has an
intrinsic exemption from maintenance; repair locality and validity conditions
may matter more than file format.

For example, an agent can retain a tested procedure for reconciling records, or
retain examples and a description from which it regenerates that procedure.
Both can use the same parser, executor and current schema. If one field's meaning
changes, a competent retained implementation may accept a new parameter or need
one local edit. Comparing only against a frozen, hard-coded script would miss
that alternative. Conversely, regenerating everything can lose an earlier fix.
This is an illustration of the contrast, not a prescribed workload.

## Selection and overlap

| Candidate | Decision |
|---|---|
| Can agents create their own reusable tools? | Answered sufficiently by the inspected precedents; do not select another possibility demonstration. |
| Learn abstraction, portability or automated repair | Established methods and positive evidence exist. Use them as alternatives rather than relabeling them as gaps. |
| Add regression tests to evolving libraries | Already a direct public method; tests and update acceptance alone are not a new question. |
| Compare static scripts with flexible contextual agents | Reject as an identifying comparison if only one side can observe intermediate state or repair itself. |
| Attribute persistence benefit under comparable execution, experience and compute | Select for bounded feasibility review. An actionable result can be either an existing answer or a justified comparison. |

The active evidence-use study concerns acquired model behavior using authoritative
changing evidence. This candidate concerns a retained executable artifact versus
reconstruction from explicit experience. Keep model weights fixed initially if
that is sufficient to identify this distinction. Adding neural arms is not
required merely to span the entire directive, and this review does not enlarge
the active commission.

## The consequential comparison

Ask whether storing and maintaining executable implementations improves complete
future outcomes or reduces total work relative to regenerating code from retained
procedural experience, with both sides allowed execution, current information
and purposeful repair. A competent code library includes parameters, modularity
and conditional reads where useful; a competent regeneration alternative includes
successful examples, known failure cases and adequate development.

Evidence budgets need not be byte-identical, but neither side should silently
receive an oracle implementation, privileged tests or extra observations. Distinguish
what was acquired from what the harness supplied. Reusing a solver already present
in a standard library is a legitimate solution, with a different acquisition claim.

Count the actual primitives executed inside a tool, not just one high-level call.
Charge creation, verification, indexing, invocation, regeneration, observation
and repair. Match or report generation opportunities, tokens and execution work;
matching call counts alone is incomplete. Compare costs at comparable complete
quality, rather than merging partial success and cost into an unexplained score.
Where scalar costs are meaningful, retention repays only when avoided reconstruction
exceeds its extra preparation, lookup, validation and repair costs over observed
reuse. This accounting identity is not an empirical prediction of a crossover.

Separate unchanged reuse, changed implementation interfaces and changed task
semantics. Not every change invalidates a procedure; not every previous expected
answer remains valid. Prefer a consequential real change or an explanatory
controlled contrast over arbitrarily breaking an API to manufacture brittleness.

## What to do next, and when to stop

Inspect a small set of public artifacts before choosing runs. AWM's contextual
and action variants and SkillWeaver's generated functions are direct starting
points; the TroVE re-evaluation supplies a compute-control precedent. Check exact
code revisions, retained artifacts, evaluation access, internal observations and
available cost traces. Investigate AWM's table/prose inconsistency only if its
precise comparison is needed. This is not a requirement to reproduce every paper.

The review should decide whether a released workload and functioning alternatives
can identify the marginal value of persistent code. It may conclude that existing
results already answer the scoped question, that artifacts cannot support it, or
that a bounded independent investigation would be informative. Stop this review
on that explanatory conclusion or a concrete access/resource constraint. No
novelty claim, code win or new ancillary repository is required.

Prospective expectations for interpreting the candidate, not commissioned tests:

- **EX1:** With repeated stable operations, retaining functioning code should
  reduce reconstruction work; the complete-quality advantage may be small when
  regeneration is already reliable.
- **EX2:** Local interface changes should often favor local repair over complete
  regeneration when the retained abstraction still matches the task. Broadly
  changed assumptions may reverse that advantage. Mere exposure to a new case
  is not evidence of either kind of change.
- **EX3:** An apparent code-memory advantage will shrink when extra sampling,
  execution and observation access are accounted for. Residual savings or gains
  would be stronger evidence for persistence itself.

These are root conjectures to refine against artifacts, not local findings.
AD1–AD3 and EU1–EU3 retain their original predictions and assessments. Completed
studies stay complete; ancillary investigators retain operational ownership.


## Artifact assessment and next selection

The [bounded review](../studies/2026-09-17-executable-feasibility.md) is complete.
AWM's release lacks the runnable action comparison; SkillWeaver already implements
an executable/reference-only switch. The latter is a useful method donor, not a
new Construct proposal. Its bundled libraries lack verification metadata, and
its default evaluation, reference content and permitted primitives require care
before attributing a gain to persistent implementation. No model or browser task
was run; exact revisions and static checks are preserved in the
[artifact ledger](../sources/2026-09-17-executable-artifacts/README.md).

This refines the theory: invoking code versus regenerating from the same source
isolates some reconstruction work while both sides retain implementation.
Comparing retained implementation with lessons/examples additionally tests which
information survives abstraction. These are different allocation claims, not
interchangeable controls. EX1–EX3 remain prospective.

Recommend a bounded independent investigation that acquires functioning routines
and develops a competent reconstruction alternative from shared experience,
starting from public methods where useful. Acquisition records, actual primitive
execution and recovery costs matter more than a large library or full benchmark.
The investigator should own workload discovery and the smallest identifying
comparison. This review does not commission a repository or experiment.
The evidence-use publication does not reopen its own phase: supplied perfect
execution motivates the acquisition distinction without answering it.

## Additional public comparison — 17 September

The [persistence-control reading](../sources/2026-09-17-persistence-controls/README.md)
adds a closer ephemeral-script precedent and a pinned SkillCraft route, alongside
online maintenance and efficient contextual delivery. The
[comparison note](EXECUTABLE_COMPARISON.md) sharpens the recommendation: distinguish
retained information from execution and avoid forced reconstruction when source
can simply be loaded. Shared acquisition, equal checking and costs on all requests
define the useful remaining comparison. This is a refinement of EX1–EX3's
interpretation, not confirmation or rewritten predictions. No new experiment or
ancillary repository is commissioned.

**Subsequent commissioning decision:** The user's direction to continue led to
the independent [executable-experience-retention study](https://github.com/alignment-farm/executable-experience-retention).
The [comparison note](EXECUTABLE_COMPARISON.md#commissioning-after-preparation)
records its preparation boundary. Bounded investigation is commissioned; workload
and execution belong to its investigator, and preparation has launched no runs.
