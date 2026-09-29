# Construct-2: what we have learned about accumulating useful experience

Executive summary · Ancillary findings, root synthesis and selection through 29 September 2026

Construct-2 asks how agents can accumulate useful experience across sessions, and where that experience should live: explicit memory, contextual lessons, executable tools, model weights or runtime rules. Eighteen ancillary investigations have completed reviewed bounded phases, alongside a review of public research. Completed phases do not close the broader investigations. Our starting hypothesis already allowed these mechanisms to work together. The studies have sharpened the conditions under which that combination helps, and exposed several ways apparently successful learning can fail to produce useful capability.

**The clearest finding is that successful learning, durable usefulness and repayment of learning costs are separate achievements.** A system may acquire a pattern without completing the task, retain information without being able to use it, or improve predictions without outperforming a simpler alternative. Useful accumulated experience must improve complete future behavior or avoid work at comparable quality, while remaining accessible and correctable as the task and agent change.

The [evidence-set review](studies/2026-09-28-evidence-set-findings.md) adds another
distinction: **a useful learned ranking need not be usable by the deployed search
procedure**. On native configuration tasks, exact search with learned coefficients
completes 48/48 uncached attempts, while its initial gradient recipe completes
34/48. Ordinary dependency-following completes 48/48 with slightly less evidence
and no acquisition cost. Learning substantially improves compactness over the
untrained initialization, which already completes every task. Separate diagnostics
show that even identical scores for every discrete evidence set can yield different
gradient-search behavior. Natural-text selection also improves, but defective
source chains and grading labels prevent a clean downstream success claim.

The [29 September code-edit review](studies/2026-09-29-action-feedback-findings.md)
adds executed edit feedback and a second source project. A frozen learned selector
saves context on one edit but uses more tokens across the two-task sequence than
ordinary access. Both pass the executable tests yet omit requested documentation
on one task. Empirical reuse delivers both artifacts at higher cost, but fails to
finish one attempt. **Passing tests, delivering every requested artifact and
correctly declaring completion are distinct achievements.** The self-tests also
include wrong expectations and miss a known defect; a later public review repairs
the documentation omission, with its cost and assistance kept separate.

**Access can matter as much as storage.** In controlled memory experiments, changing the reader recovered useful answers from an unchanged stored state. Other failures reflected information that was actually absent. Losing detail also did not necessarily prevent a particular later use. These distinctions matter operationally: better access, retaining more evidence and learning again address different problems. A failed answer alone does not identify which one is needed. [Memory and later use](studies/2026-09-15-maintenance-findings.md).

The [28 September recovery assessment](notes/RECOVERABLE_MEMORY.md) extends this
account to the full retained system. Compact context can coexist with recoverable
sources, but preservation alone does not make evidence affordable to find and
use. New public-method reading narrows generic compression proposals toward
reliable recovery under changing demands, with acquisition, access and maintenance
included in cost. This is theory and literature synthesis, not another local
learning result.

**Learned behavior can become useful, but improvement is conditional.** Purposeful diagnosis turned some failed acquisition attempts into functioning learners, and later studies demonstrated complete procedural behavior and bounded preservation through revision. One study found a learned behavior that remained useful while authoritative values changed, with a modest measured advantage over an uncached contextual lesson. Longer training reversed that benefit. Across the program, lower loss and better intermediate predictions were insufficient evidence of better complete behavior or a worthwhile investment. [Evidence use under revision](studies/2026-09-17-evidence-use-findings.md).

**Present competence does not determine future maintainability.** Two equally accurate learned states responded differently to the same correction; their histories changed which revision support helped. A subsequent study found that a simple history rule could select the best tested aggregate outcome while substantial obligations still failed. Successful maintenance therefore requires checking both new requirements and preserved responsibilities. Choosing the best of inadequate remedies does not establish a maintained capability. [State and support](studies/2026-09-15-state-support-findings.md); [maintenance decisions](studies/2026-09-16-maintenance-transfer-findings.md).

**Competent alternatives change the allocation decision.** Cheap explicit access matched or exceeded learned retrieval on a directly addressable collection, even though the learned predictor improved. In the executable-retention study, all four policies completed eight fresh requests. Ready and archived source needed no future model calls; reconstructing each session needed eight; retaining the first reconstruction needed one. Usable source avoided repeated work, and the alternative could itself become a source-retaining policy. These results make availability, recovery and subsequent behavior central to the comparison. [Memory placement](studies/2026-09-16-placement-findings.md); [executable retention](studies/2026-09-17-executable-retention-findings.md).

**Choosing and maintaining memory must justify its own cost.** Unchanged guidance improved a new model from 1/12 to 12/12 complete SQL tasks. Paid selection also reached 12/12 and reduced use tokens, but nearly tripled the total after migration setup was included. In a separate correction study, acquired support links reduced repaired fields from 48 to 18, yet rebuilding the small state cost less. Every method repaired all six states, while shared arithmetic failures left later task episodes at 4/6. Useful inheritance, selective repair, complete future behavior and net savings are distinct results. [Migration and correction lineage](studies/2026-09-17-migration-lineage-findings.md).

**Evidence must be informative and competently interpreted.** In two constructed
reporting histories, paid tests exposed defects that a weak reviewer still
misread. A competent reviewer found those defects from the visible schema alone;
extra tests then added cost without improving the six measured task outcomes.
Ordinary raw-experience repair also recovered all six current answers, yet one
returned program failed on new data. Cheaply corrected SQL handled every case
without further model calls. A successful episode, a valid lesson and a reusable
correct procedure require different evidence. This study compared curation and
code repair together; it did not isolate lesson acceptance or test learned
selection. [Lesson acceptance](studies/2026-09-20-lesson-acceptance-findings.md).

The subsequent [root analysis](notes/OBSERVATION_BOUNDARIES.md) distinguishes
testing an implementation from identifying its intended contract. If conflicting
requirements produce identical available observations, more execution cannot
settle which applies. Existing clarification methods narrow the next independent
candidate to learning which evidence source to consult, beyond competent review
and retained source answers. This is an analytical conclusion; its proposed
comparison has no validated workload or new commission.

The [28 September follow-up](notes/EVIDENCE_ACQUISITION.md) grounds that distinction
in public maintenance and dialogue records. It separates retaining a resolved
answer from learning to construct an observation that helps on new work. Existing
public methods narrow the value of another generic source-choice classifier;
complete investigation transfer remains open. A targeted software replay confirms
an implementation defect and repair, without establishing an agent-learning result.

**What remains for the model to do determines the value of learning.** With source
experience externally accessible, an adapter improved manual configuration of
retained code from 3/12 to 5/12 complete tasks. A developed compiler brought both
models and direct execution to 12/12, while the adapter added twelve repair calls.
Its aggregate gain also hid worse handling of a revised exclusion rule. The
compiler was investigator-written for a finite generated language, and the study
used one history and one training run. This explains a workload limit without
settling the value of continuing weight consolidation. [Weight consolidation](studies/2026-09-17-weight-consolidation-findings.md).

Its database follow-up made familiar source execution shorter, but two periodic
updates completed 6/20 fresh jobs versus 7/20 using the same external experience
without learning. Teaching contained only final SQL submission and finish;
fresh adapter runs never searched the retained history or executed saved queries.
This motivates testing whether weights can improve use of external experience.
It does not establish why transfer failed. [Continuing consolidation](studies/2026-09-18-continuing-consolidation-findings.md).

The investigation pilot adds a caution: teaching tool-use demonstrations changed
action choices without producing the required branch implementation. Both models
passed a smaller repair test while still violating its stated contract, and both
claimed success for probes that had failed. Recognizable investigation steps and
passing limited checks do not establish useful investigation. Its teaching was
authored, not derived from learner attempts, so the intended acquisition question
remains open. [Initial investigation pilot](studies/2026-09-21-experience-investigation-findings.md).

The [28 September continuation](studies/2026-09-28-investigation-continuation-findings.md)
supplied complete teaching history to both arms and builds corrections from
actual failed attempts. A new adapter repairs the strict filter from a supplied
recorded context (18/18 external checks), but loops without repair autonomously
(9/18). Further correction induces probes without repair; none of the twelve
runs uses history or passes a probe assertion. Root verifies an additional rename
regression hidden by unchanged aggregate scores. Correct conditional behavior,
autonomous action and useful feedback interpretation are distinct achievements.
The bounded diagnosis is accepted; fresh transfer remains untested.

The [29 September investigation review](studies/2026-09-29-action-feedback-findings.md)
now demonstrates competent ordinary history use. A larger reference completes
and verifies a joint repair; the new 4B adapter reads history without acting,
while ordinary 4B repairs only part of the task and falsely finishes. The new
training estimator detaches prefix gradients, and the learner's stopping point is
adaptive, so the result does not isolate an acquisition cause. This is explanatory
development progress, with autonomous learned acquisition and fresh transfer
still open. Useful history, capable action and valid feedback must work together.

Together, the findings support evaluating memory as a maintained capability: retained evidence, learned behavior, access procedures, and ways to check or replace them. A practical inference is to preserve recoverable evidence and working implementations, and justify additional learning through its contribution to future tasks. Changing facts can remain explicit while reusable behavior is learned or implemented. The value of that arrangement depends on the receiving agent, expected reuse and maintenance work. This is a working design preference, not a validated universal architecture or a general verdict against neural memory.

The evidence is strongest within small, controlled workloads. Many supplied the task contract, identities, correction authority or routine selection. Positive cost comparisons omit some engineering work or leave stronger alternatives untested. Equal scores on small samples do not establish equal reliability, and the executable study does not isolate the value of its acquired lessons beyond the supplied contract and examples. We have not demonstrated an agent that independently recognizes recurring work, chooses what to learn and where to retain it, and reliably improves over an extended realistic job.

The [adaptation-selection synthesis](notes/ADAPTATION_SELECTION.md) adds an
independent research preference: test whether earlier intervention outcomes help
choose useful changes after the receiving agent changes. Improved remedies and
improved decisions need separate evidence. The new public-method comparison
deprioritizes another general co-evolution demonstration; competent current
diagnosis and unchanged reuse are central alternatives. The user subsequently
approved the [bounded feasibility commission](notes/INTERVENTION_CHOICE_STUDY.md);
its first publication is now reviewed at `cb25d5c`.

The [intervention-choice findings](studies/2026-09-29-intervention-choice-findings.md)
explain a limit of that first workload. An acquired category policy completes
16/18 fresh tasks after an API change, while a fixed canonical adapter completes
17/18. Shared repair brings them to a tie. A later source-only parser completes
36/36 fresh API tasks with no model calls because the authored prose has a closed,
invertible grammar. **Different remedy outcomes do not by themselves justify
learning a chooser.** Better ordinary remedies can remove the apparent selection
opportunity. This closes the template phase, not the broader question; varied
language, useful decision information and full costs remain to be established.

The next evidential milestone is continuing practical capability: better complete outcomes or less total work across repeated use and consequential change, including acquisition, checking, failures and repair. The [experience-guided investigation](notes/CONTINUING_EXPERIENCE_STUDY.md) remains responsible for autonomous acquisition and fresh transfer; accepting its diagnostic phase does not complete that commission. Competent ordinary reuse is now demonstrated in its development instrument; learned productive action and feedback use remain the next evidential needs, with costs interpreted after capability. Broader migration, correction, consolidation and acceptance questions remain open. Root continues synthesis, literature and independent questions. The program's direction remains useful accumulated experience across sessions.

On 28 September the user selected [evidence-set memory](notes/EVIDENCE_SET_MEMORY.md)
and subsequently authorized broader EBM exploration. Seven phases are now reviewed
at `5e2d06a`, with functioning acquisition, narrow cross-project use and explained
limits in feedback and complete-task grading. The broader
question remains whether learning improves complete later work beyond competent
access at a useful total cost. Native dependency success does not yet establish
useful LLM infrastructure or broad task improvement. Further exploration belongs
to the existing investigator; this review adds no commission and preserves the
independent experience-guided investigation remit.
