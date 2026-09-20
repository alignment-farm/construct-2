# Research selection within Construct-2's fixed direction

16 September 2026. The user asked the root to resume independent scientific work
while ancillary investigations retain ownership of their experiments. This note
reassesses the next questions using a fresh
[public-research review](../sources/2026-09-16-research-direction/README.md).
It originally prepared research choices without commissioning a study. The
[subsequent preparation](#preparation-after-the-users-agreement) below records
the user's agreement and the resulting handoff; preparation launched no model run.
The prior local publications and prospective R, M and MR expectations remain
historical evidence with their original wording.

The [root directive](../README.md) remains unchanged. The useful lifetime of a
learned component is a selected study question within it, not the program's new
direction. Our existing working hypothesis allows models, records and harnesses
to develop together as experience warrants. The subsequent
[adaptation synthesis](ADAPTATION_DECISIONS.md) develops that hypothesis using
additional public research and distinguishes it from any one study's focus.

**Several broad next steps already have public answers.** Forgetting prediction,
prediction-guided replay, amortized context storage, learned memory admission and
learning how to retrieve experience all have concrete methods and evaluations.
Our local results remain useful, but a generic demonstration of one of those
ideas would need to be justified as replication or adaptation. The root should
select consequential unresolved comparisons using both public and local evidence.

## What the reading changes

**Maintenance decisions have closer precedents than our earlier map captured.**
P26 learns example-level forgetting forecasts and uses them in replay, including
sequential error correction. P27 extends empirical association modeling to larger
models and held-out tasks. Its online variant observes damage after an initial
training prefix; its offline variant pays for an extra training run. Thus sparse
probes, forecast utility and their costs are already studied. Our candidate
contribution must concern a specified generalization or decision boundary.
[P26, §§2–5](https://arxiv.org/html/2402.01865v3),
[P27, §4 and Appendix A](https://arxiv.org/html/2406.14026v8).

Adaptive reset also has an implemented precedent in P28, using collapse signals
and selective recovery in visual test-time adaptation. P35 investigates factual
connectivity as a damage signal and selects preservation anchors. Neither a
monitor nor a selected protection set is new by itself. These are method leads,
with different tasks and information access from the local procedural studies.
[P28, §3](https://arxiv.org/html/2603.03796v1),
[P35, §§4–5](https://arxiv.org/html/2609.08067v1).

**Useful placement has positive public demonstrations as well as our local
negative cost results.** P29 trains reusable KV state for repeated queries over
a corpus, reports serving advantages, and discloses substantial preparation cost.
P30 meta-learns context-to-adapter generation, moving work into an earlier training
stage; its unrelated-query probe also finds interference. Neither is equivalent
to our fixed local LoRA recipe. Our absence of demonstrated repayment cannot be
generalized to the absence of useful learned storage.
[P29, §§3–6](https://arxiv.org/html/2506.06266v3),
[P30, §3 and Appendix C.4](https://arxiv.org/html/2602.15902v1).

**Conditional allocation is already an empirical research program.** P31 compares
eleven memory implementations across multiple workloads and finds regime-dependent
tradeoffs. Its exclusions and implementation substitutions matter when importing
a comparison. P32 combines write admission and parametric consolidation, measures
knowledge transitions, and explicitly leaves temporal conflicts and interference
as limitations. These sources narrow what S5 should add; a general substrate
ranking or a two-layer architecture would overlap substantially.
[P31, §§2–5, Appendices B and G](https://arxiv.org/html/2608.15008v1),
[P32, §§3–5](https://arxiv.org/html/2608.22215v2).

**Learning can improve access while the evidence remains explicit.** P33 retains
relevance scores and estimates unscored query–memory relationships. Its evaluated
budget declines on a fixed schedule, and its discussion identifies changing
memory meanings as a threat to reuse. That supplies a concrete alternative to
putting the evidence itself into an adapter.
[P33, §§V–VIII](https://arxiv.org/html/2608.22767v1).

Finally, P34 finds sensitivity to task order and feedback specification in
text-memory agents. Our learned-state dependence therefore belongs beside a
broader history-dependence problem, without establishing a shared cause.
[P34, §§3–4](https://arxiv.org/html/2608.18066v2).

## Connection to the root account

The useful object of study is an agent's maintained capability: retained evidence,
learned behavior, access procedures and the decisions that change them. The
division between explicit and learned memory can occur inside that system.
Evidence can remain explicit while a learned policy improves its use. Conversely,
learned content may still require explicit correction and fallback evidence.

The local findings supply controlled examples of three dependencies: training
value depends on the receiving state; retention is relative to a later query and
reader; maintenance can change the costs and quality that initially justified
learning. Public work supplies broader demonstrations and mechanisms addressing
each. Their combination motivates a more specific placement question:

> Which part of using experience is worth learning, for how long does that learned
> component remain useful, and what must remain available to revise or replace it?

This is a framing for the selected comparisons, not a replacement for the root
directive, a new theorem or an asserted gap across all literature. It preserves
the priority on neural memory and learned policies while allowing the evidence
to favor explicit or combined arrangements.

## Two independent comparisons worth developing

### A. Does a maintenance decision remain useful after the learner changes?

Local S2 shows that a support preference can reverse between learned states.
Public forecasting methods give concrete comparators rather than a reason to
invent a generic damage score. The question is whether a predictor or action
rule calibrated on some histories remains useful on separately acquired and
subsequently revised states, including valid new obligations.

Our prospective expectation is that a fixed mapping from update examples to
damage will sometimes lose usefulness across changed learner histories, and
that a small observation of the current state can recover decision value. A
strong static comparator performing as well, or observation costs consuming
the benefit, would weaken that expectation. This is untested locally and not
claimed to be unexplored publicly.

Any later study should distinguish forecasting before an update from extrapolating
after a paid trial. Its target should include complete new and preserved behavior,
and its decision comparison should include developed fixed support and direct
validation. Skipping an update has a cost when the new obligation remains unmet.
Changing cases while reusing the same acquired history does not test transfer
across histories. The investigator would own the actual protocol and resource
choice. No automatic fifth S2 phase follows from this question.

### B. When does a learned memory component repay its cost before it needs revision?

The immediate root task is workload discovery for repeated use under meaningful
change. A candidate is a versioned operational reference used across many requests:
the same observations support retrieval, a reusable learned representation, or
learned access to retained records. Changes must affect answers or actions; an
append-only history does not by itself impose correction of a previous rule.

Vary reuse between changes, the scope of a change, and the cost of evidence access.
Develop competent explicit retrieval and cached-context controls alongside a
published learned method. A method's original workloads and implementation costs
should guide feasibility; the laboratory need not rebuild its full training regime
merely to demonstrate the architecture again.

Our prospective expectation is a conditional crossover: longer useful reuse can
favor paying an acquisition cost, while frequent consequential revisions can
remove that advantage or favor learning only the access procedure. A published
method's gain on stable corpora is a reason to test this, not a prediction of a
local win. No observed crossover, after functioning acquisition and serious
controls, would also answer the bounded question.

A useful contrast separates **changes in evidence** from **changes in how it is
used**. Our inference is that a learned access policy may remain useful when
record values change but relevance relationships remain stable. When new goals
change those relationships, its accumulated retrieval experience may also need
revision. Crossing those changes would distinguish an advantage of learning
access from the easier explanation that nothing important to the learned
component changed. The public reading motivates this comparison; it does not
establish either outcome or its novelty.

For a fixed sequence of uses, account for preparation, use, revision, checking
and repair. All methods incur their actual costs. Compare complete quality and
cost jointly; reducing them to cost per success can conceal unacceptable failures.
Use native units until a justified conversion is needed. Prior training cost may
be shared across deployments, but its allocation must be stated. Neither setup
nor the potential source of a crossover should rely on withholding accessible
evidence from the explicit comparator.

The root's preferred next preparation is this placement comparison, alongside
development of A as an independent question. Useful placement has received less
direct attention than the recent S2 chain. B does not require A to produce a
successful controller first; fixed maintenance and explicit fallback already
define meaningful alternatives. Learned retrieval under changed memories is a
candidate within B, not an automatically commissioned third project.

## How this changes root work

The root continues theory, public discovery and research selection during local
execution. It reads an ancillary publication to assess the claim and its effect
on the program, extending the evidence review when a material uncertainty calls
for it. A local follow-up competes with other questions on scientific value; its
proximity to the latest result does not give it priority.

Public evidence can settle a root question, supply a method or baseline, suggest
a complementary comparison, or justify a deliberate replication. We should
record which of those happened. A new bibliography alone is insufficient if the
same local assignment would have been issued regardless of what was read.

Here the concrete change is to replace broad invention of forecasting and memory
allocation with comparisons of existing methods under changing histories and
useful lifetimes. The next preparation should choose a workload and closest
published comparator, check remaining overlap and local feasibility, and identify
the result that would change the account. Ancillary methods and execution remain
local. No new review gate, reporting layer or continuous monitoring service is
introduced by this note.

## Preparation after the user's agreement

The user approved these revised preferences. The root then inspected released
methods and a workload, with the record in the
[preparation review](../sources/2026-09-16-study-preparation/README.md).
Further reading found direct precedents for update robustness and operation-cost
comparisons (P36), structured state revision (P37), and learning supersession
(P38). Those broad demonstrations do not need to be recreated as our contribution.

**B was prepared as an independent study:**
[memory-placement-under-revision](https://github.com/alignment-farm/memory-placement-under-revision)
([local brief](../../ancillary-studies/memory-placement-under-revision/README.md)).
Its first implementation lead is EARM's learned access, with a versioned subset
of the released τ-bench document workload. Content storage remains a possible
comparison, subject to bounded feasibility work. This choice makes contact with
learning using a released lightweight method while preserving the distinction
between learned retrieval and neural content. Preparation has not started the
ancillary agent or any experiments.

**A has an independent [comparison note](MAINTENANCE_DECISIONS.md):** hold out
learner histories, distinguish frozen forecasts from paid current-state
observations, and evaluate the action's value against fixed support and direct
validation. It is root scientific development, not a fifth S2 commission.

The common theoretical quantity is the *useful lifetime of the learned component*,
which need not equal the interval between document changes. For a scalar cost
measure and comparable useful quality, a simplified stable-period comparison is:

```text
learned cost  = setup_L + N * use_L + revision_L
explicit cost = setup_E + N * use_E + revision_E
```

If `use_E > use_L`, the corresponding cost crossover is
`N > ((setup_L - setup_E) + (revision_L - revision_E)) / (use_E - use_L)`.
This is accounting, not an empirical prediction. With no per-use saving, reuse
alone cannot rescue a larger initial cost in this simplified model. Real query
mixes, cache warmup, changing quality and repeated revisions require cumulative
measured costs rather than extrapolating a single timing. Count terminal revision
only if it is actually incurred within the compared sequence, and do not count
the same refresh again as the next period's setup.

For learned retrieval, changed values may preserve useful relevance structure;
changed evidence needs may invalidate it. The proposed comparison tests that
conditional distinction. It also allows the cheap explicit method to win. A
maintenance predictor would be valuable only when its information changes an
available action enough to justify its own costs, so B can proceed without A.

## Status after handoff

The user subsequently reported that memory-placement-under-revision was underway.
The root did not inspect its unpublished results for that update. The
[adaptation synthesis](ADAPTATION_DECISIONS.md) now develops independent theory
and predictions while that study owns its execution. Its broader account of
learning what to change does not alter the existing A/B expectations or assign
another experimental phase.

## Assessment after publication

The [16 September placement assessment](../studies/2026-09-16-placement-findings.md)
accepts B's bounded phase: learned score prediction functions, but cheap explicit
access matches or exceeds complete answers without scoring calls. Prediction
quality persists through content edits better than changed evidence needs; that
does not establish useful repayment. Reuse lengths are confounded with seeds,
and the combined branches contain no answer-changing targets. The prospective
expectations above remain unchanged. The broader placement question remains open,
A remains independent, and this assessment commissions no further experiment.

## Independent development after placement

The [decision-value reading](../sources/2026-09-16-decision-value/README.md)
adds established decision-focused and metareasoning theory (P46/P47). The
[maintenance extension](MAINTENANCE_DECISIONS.md#when-observation-can-change-the-decision)
uses it to narrow A: a history change may alter absolute damage forecasts while
leaving the best action unchanged. Useful observation must resolve consequential
action differences relative to competent fixed choices, explicit fallback and
direct validation. Its constructed examples separate information about a learner
from information worth acquiring for a decision.

This selects further root development of action-value transfer, not generic
forecasting or a renewed placement run. AD1–AD3 and their empirical status remain
unchanged. No new ancillary phase or model experiment is commissioned.

**Concrete preparation:** The [maintenance comparison](MAINTENANCE_COMPARISON.md)
now specifies the workload, functioning support choices, observation alternatives
and illustrative resource scope. The [targeted review](../sources/2026-09-16-maintenance-preparation/README.md)
finds that a simple known-history rule matches the aggregate state oracle on
published S2 endpoints. This is retrospective, but redirects the first investment
toward testing history-rule transfer before a larger learned-selector campaign.
An independent bounded comparison is recommended; no new phase is commissioned.

**Subsequent commissioning decision:** Following the user's direction to continue,
the root prepared and published the independent
[maintenance-decision-transfer study](https://github.com/alignment-farm/maintenance-decision-transfer)
([local brief](../../ancillary-studies/maintenance-decision-transfer/README.md)).
The bounded comparison is authorized for ancillary execution. Preparation has not
started the investigator or model runs. This is a new independent question, not
an S2 renewal or a change to the program's directive.

## Root work while maintenance-decision transfer runs

The user reports the ancillary study underway. The root has not inspected its
unpublished results or altered its assignment. The next independent root question
is how useful decision experience is obtained in the first place:

> When does ordinary outcome feedback teach which experience to retain or which
> remedy to use, and when does that require additional evidence?

This develops AD1 alongside the active AD2 comparison. The active study examines
decisions across learned histories with checked task specifications. This root
question concerns the feedback from which an agent could learn those decisions.
The broader directive still permits records, contextual lessons, tools, weights
and runtime rules to develop together.

Local S4 distinguishes missing information from unsuccessful reading; S5 shows
that learned score predictions can fail to improve complete answers. These
motivate distinguishing a supported proposition, useful access to it, and benefit
attributable to retaining or applying it. They do not demonstrate an agent that
can diagnose these distinctions from its own feedback.

The [focused primary-method reading](../sources/2026-09-16-memory-feedback/README.md)
supplies two concrete precedents: environment-probing memory curation (P48) and
delayed response-quality credit for learned memory policies (P44). Thus the root
should not propose generic memory verification or delayed reward as a new method.

The next deliverable is a comparison of feedback sources: terminal task outcomes,
fixed verification rules, targeted environmental observations and paid memory
removal/replacement comparisons. Determine what each can teach, what it costs,
and whether it improves fresh choices beyond a developed fixed policy. Keep
functioning remedies and competent explicit access. A useful policy need not
estimate causal credit exactly; conversely, a passing task does not validate
every retained inference. Outcome shuffling or memory removal are possible
diagnostics, not mandatory new infrastructure.

Before proposing an experiment, inspect the closest learned retrieval/repair
and credit-assignment methods, identify a consequential comparison, and record
whether public results answer, narrow or redirect it. This is independent theory
and literature development, not another commissioned study or a requirement to
wait for the active investigation. AD1 remains untested.

**Subsequent assessment:** The
[feedback comparison](FEEDBACK_DECISIONS.md) and
[new primary-method review](../sources/2026-09-16-feedback-comparison/README.md)
complete this deliverable. P49–P52 supply direct memory-credit, replay-audit and
retrieval-correction precedents. A generic credit comparison would overlap this
work. The selected next step is a bounded feasibility review of remedy choice:
can existing evidence support functioning retrieval and reading remedies whose
relative value differs, with useful decision experience beyond a developed rule
and competent explicit access? Additional feedback must repay its cost. The
review may resolve the candidate without new runs. No additional ancillary study
is commissioned, and the original AD1 expectation remains untested locally.

**Bounded review completed:** The
[remedy feasibility assessment](../studies/2026-09-16-remedy-feasibility.md)
inspects S4 at its unchanged accepted revision and two pinned author releases.
It does not select a new experiment. S4 does not supply the proposed retrieval
action; P53 Adaptive-RAG already learns strategy choice from outcome-derived
labels. Recalculated released outputs confirm competing useful actions, but
their evidence and computation vary together. The specific AD1 distinction
remains unresolved, without warrant for relabeling these existing comparisons or
extending S4. Close this feasibility phase and retain the candidate as an open
question, not the default next experiment. The active maintenance assignment and
original AD1–AD3 predictions are unchanged.

## Assessment after the independent maintenance publication

The [maintenance-transfer assessment](../studies/2026-09-16-maintenance-transfer-findings.md)
accepts the completed phase. All nine ancillary projects now have bounded
publications. Matching known history reaches the fresh two-support aggregate bound
(524/768), while every candidate fails substantial obligations. Paid validation
does not improve that total; the fitted observation controls were constant before
assessment, so they do not establish the absence of useful information.

This narrows AD2: its aggregate observation-rescue prediction is unsupported in
this comparison, with weak calibration coverage. The demonstrated limit is not
just inaccurate forecasting. Available actions are inadequate, and equal totals
can conceal different new-obligation and preservation failures. The retained-example
table completes the finite task under explicit addressing and authority assumptions.

No new experiment is selected through acceptance of this publication. Another
selector round or an obligation-prioritizing tie-break alone would not resolve
maintenance. If further work is selected, first specify the consequential
uncertainty about adequate actions, task structure or obligation tradeoffs and
check its closest public evidence. AD1's bounded feasibility review remains closed
without a selected experiment; the broader AD1 question stays open. The fixed
directive, hybrid working hypothesis and original predictions remain intact.


## Selection after the maintenance-transfer assessment

The [evidence-use synthesis](EVIDENCE_USE.md) completes another root selection
round. The local explicit controls differ in supplied addressing, operations and
authority; their success does not establish that every useful operation should
remain fixed or that learning cannot help. Public reading adds positive learned
reading and counterfactual reasoning results, a contextual alternative and a
training-dynamics explanation. Generic learned evidence use is already answered
well enough that another possibility demonstration has little selection value.

Select the useful lifetime of evidence-use behavior across successive
authoritative corrections, compared with developed contextual lessons from
matched available experience. This is an allocation and maintenance comparison
within the enduring directive. It asks whether learning reusable use, while
keeping current evidence explicit, actually earns its acquisition and repair cost.
The new EU1–EU3 expectations remain prospective and do not replace AD1–AD3.

A bounded independent investigation is recommended, with workload development,
methods and acquisition diagnosis owned by its investigator. The selection note
states the consequential contrasts and closure criteria without prescribing an
experimental grid. Another observation selector, a reopened AD1 feasibility phase
and deliberately weakened explicit access are not selected. No repository or
experiment is commissioned in this root selection round.


**Subsequent commissioning decision — 16 September:** The user asked to create
this ancillary study. The independent
[evidence-use-under-revision repository](https://github.com/alignment-farm/evidence-use-under-revision)
([local brief](../../ancillary-studies/evidence-use-under-revision/README.md))
contains the question, EU1–EU3 expectations, versioned primary-source starting
points, resources and local research instructions. Its bounded exploration and
execution are commissioned. Preparation launches no investigator or model run;
workload development and operational decisions belong to the ancillary session.
Nine earlier projects retain their completed contributions; this is the tenth
ancillary project and has no findings yet. The root continues independent theory,
public discovery and synthesis while it runs.


**Execution update — 16 September:** The user reports the study underway with an
ancillary agent. This records user-reported execution status, not an inspection
of unpublished evidence. Methods and operational ownership remain with the study.


## Executable experience selection — 17 September

While the evidence-use study runs, the user authorized another allocation review.
The [executable-experience synthesis](EXECUTABLE_EXPERIENCE.md) and
[primary reading ledger](../sources/2026-09-17-executable-experience/README.md)
complete this selection round. Public work substantially answers generic tool
acquisition, abstraction, portability and repair; its evidence also identifies
compute confounds and a distinction between contextual guidance and invocation.

Select a bounded artifact review of whether retained implementation adds useful
value over regeneration from retained procedural experience under comparable
execution, observations and compute. This is a question about where experience
lives, not a proposal to rediscover automated programming or require a library
win. Modular repair and competent contextual reconstruction remain alternatives.
EX1–EX3 are prospective conjectures; AD1–AD3 and EU1–EU3 are unchanged.

The next deliverable should assess exact public artifacts for an identifying
comparison and may resolve the candidate without new runs. No experiment or
additional ancillary repository is commissioned. The active study retains methods
and execution ownership, and its unpublished evidence was not consulted.


## Assessment after evidence-use publication — 17 September

The [root assessment](../studies/2026-09-17-evidence-use-findings.md) accepts the
tenth bounded ancillary contribution. One prespecified checkpoint transfers
modestly and retains an advantage through two corrections. Its measured
training-plus-use time repays against an uncached contextual lesson over the
observed sequence, while a later checkpoint regresses. This is a narrower claim
than reliable full-cost repayment: a winning-checkpoint selection rule, cached
and compact contextual controls, construction and repair remain untested. The
supplied executable solves the finite task completely.

This qualifies the earlier program-wide absence-of-repayment summary and closes
the phase on explanatory progress. It does not select another training round.
Continue the already-selected executable artifact review: whether an acquired
implementation saves reconstruction beyond what retained procedural experience
can supply, with both alternatives able to execute, observe and repair. The
perfect supplied interpreter makes the acquisition distinction salient but does
not itself establish an acquired-code advantage. Preserve EU1–EU3 and AD1–AD3.


## Executable artifact review completed — 17 September

The [feasibility assessment](../studies/2026-09-17-executable-feasibility.md)
closes the selected review. AWM's release does not implement its relevant action
branch. SkillWeaver supplies a closer code-generating and reference-only method,
but bundled verification metadata, reference serialization, primitive permissions
and full acquisition/cost traces limit an off-the-shelf comparison.

This redirects the next investment toward a bounded independent investigation
using public methods as donors, with workload discovery owned by its investigator.
Separate avoiding reconstruction with source retained from choosing between code
and lessons as the retained object. Establish functioning acquisition and a
competent reconstruction alternative, then assess complete outcomes and actual
work. The new evidence-use result strengthens the supplied-versus-acquired
operation distinction without selecting another adapter round. EX1–EX3 remain
prospective. No repository or model experiment is commissioned in this selection.

## Persistence comparison sharpened — 17 September

The [additional primary reading and pinned SkillCraft inspection](../sources/2026-09-17-persistence-controls/README.md)
find closer overlap: ephemeral code execution is already a public comparator,
online routine maintenance is implemented, and contextual lesson delivery has
serious efficiency alternatives. These findings narrow the selected contribution;
they do not supply a matched acquired-experience lifetime result.

The [comparison note](EXECUTABLE_COMPARISON.md) separates execution, preservation
of procedural information and avoided reconstruction. When source is available,
ordinary loading or copying is an eligible alternative; forced model rewriting
would manufacture cost. Equal checking and full-sequence accounting matter to
the remaining allocation claim. Keep bounded independent development recommended,
with SkillCraft and SkillWeaver as donors and workload choice owned by its
investigator. This completes the preparatory comparison, commissions no study,
and preserves all existing predictions and completed phases.

## Executable-experience commission — 17 September

The user's direction to continue advances the completed preparation into an
independent commission. The private
[executable-experience-retention repository](https://github.com/alignment-farm/executable-experience-retention)
([local brief](../../ancillary-studies/executable-experience-retention/README.md))
is prepared at `34a902fedf99a22fff3c9429d49146809af8a86a`. The investigator owns
the bounded workload development, functioning acquisition, competent alternatives
and evidence needed to resolve the comparison. EX1–EX3 are copied unchanged.
This is the eleventh ancillary study; the preceding ten contributions remain
complete. Preparation starts no investigator or model runs. Root theory, public
discovery and synthesis continue independently of its execution.

## Root work while executable-experience retention runs

The user reports the ancillary agent underway. This is an execution-status update,
not a review of unpublished findings; the preparation revision remains the root's
review boundary. Its workload and methods remain with the investigator.

The next root focus is [experience portability](EXPERIENCE_PORTABILITY.md): what
should carry over unchanged, be adapted or be retired when the model or harness
changes? It develops the existing compatibility hypothesis beyond the active
implementation-versus-reconstruction comparison. Assess inherited experience
relative to the new recipient's own competence, while distinguishing changes in
the recipient from changes in required behavior.

The [initial targeted reading](../sources/2026-09-17-experience-portability/README.md)
finds direct transfer and revision precedents, so the next deliverable is a
focused theory and methods comparison of useful inheritance and adaptation costs.
At this initial stage it could resolve the candidate without new runs, and no
additional study was commissioned;
AD1–AD3, EU1–EU3, EX1–EX3 and the completed phases retain their existing status.

## Two independent commissions after further discovery — 17 September

The user then directed the root to continue until it found and created at least
two further studies. The [new reading](../sources/2026-09-17-independent-study-selection/README.md)
adds P77–P84, deepens P37 and inspects pinned Agent-KB code. It changes the
selection rather than merely furnishing citations. Public work already covers
unchanged transfer to unseen recipients, model-aware sharing, model-upgrade
forecasting, dependency-guided repair and acquired dependency propagation.
Generic demonstrations of those mechanisms are therefore weak investments.

**Procedural-memory-migration** asks whether paid experience with a previously
unseen recipient improves retaining, adapting or retiring procedural guidance
enough to justify its cost against unchanged inheritance and reconstruction.
The [selection note](EXPERIENCE_PORTABILITY.md#selection-after-the-methods-review)
preserves the earlier theory and adds PM1–PM3. The private
[repository](https://github.com/alignment-farm/procedural-memory-migration)
([local](../../ancillary-studies/procedural-memory-migration/README.md)) is prepared
at `f7ca4fc9c07f2d531802caf2ae46ea58d7a375b1`.

**Correction-lineage** asks whether acquiring dependency information during
memory construction repays its write/checking costs when correcting derived
memory and future behavior, against reconstruction from the same source archive.
The [selection note](CORRECTION_LINEAGE.md) records CL1–CL3 and distinguishes
runtime exposure from acquired semantic support. The private
[repository](https://github.com/alignment-farm/correction-lineage)
([local](../../ancillary-studies/correction-lineage/README.md)) is prepared at
`b5853b747cfa1cca44fbce3a4aad287f5b3888fb`.

These comparisons change different parts of the system: the recipient with
evidence held fixed, and evidence validity with the recipient held fixed. They
also distinguish investment in useful behavior from investment in the ability
to revise it. Neither requires the active implementation comparison's result.
The studies own methods, workloads, development, resource use and publication;
small controlled comparisons and strong simple alternatives are acceptable.

Both initial commits are pushed to private repositories, with clean local main
branches tracking matching origin/main revisions. The registry now contains
thirteen studies: ten accepted bounded contributions, one investigation underway
by user report, and these two newly prepared commissions. Preparation launched
no investigator or model run. No ancillary review boundary advances beyond its
recorded preparation or accepted publication, and no completed phase reopens.
Earlier AD, EU and EX predictions are unchanged.

## Executable-retention publication assessment — 17 September

The [root assessment](../studies/2026-09-17-executable-retention-findings.md)
accepts publication `baf4d764cb4e571551a2b69d45751bb7f3281eaf` and closes the
stable-use phase. Ready source, archived source, lessons-only reconstruction
and reconstruction with caching all complete 8/8 fresh requests. Their future
model-call counts are 0, 0, 8 and 1. Source availability explains avoided work;
the ability to retain the first reconstruction limits the ongoing advantage.
The [review ledger](../sources/2026-09-17-executable-retention-review/README.md)
records independent output/cost checks and targeted public follow-up on sampling
controls and resource KV caching.

EX1 has bounded support, EX2 is untested, and EX3's attribution concern is partly
addressed without a direct test of predicted shrinkage. A supplied full contract,
known dispatch and no lesson-free reconstruction control limit acquisition claims.
There is explanatory progress sufficient for phase closure; neither new model
calls nor a repair phase follows automatically from the untested broader cases.

Eleven of thirteen registered studies now have accepted bounded contributions.
Procedural-memory-migration and correction-lineage retain their independent
commissions and recorded preparation boundaries. Their methods and execution
remain ancillary responsibilities; no review of their unpublished work occurred.
The root continues theory, public discovery and synthesis within the fixed
directive. Original AD, EU, EX, PM and CL predictions remain identifiable.

## Migration and lineage publication assessment — 17 September

The [joint root assessment](../studies/2026-09-17-migration-lineage-findings.md)
accepts procedural-memory-migration at `5a670d355491a853e32779260bfe73ea09f02f45`
and correction-lineage at `f8ad1e1ce8b9842efa90305c1206b8690578a204`, advancing
both preparation boundaries. Thirteen of thirteen registered studies now have
accepted bounded contributions; no current commission remains in execution.
The chronological preparation/execution statements above are historical.

The first study establishes useful unchanged guidance for a changed model and
finds that paid selection does not repay its costs at the tested horizon. The
second acquires usable support information and repairs every tested state, but
cheap rebuilding matches quality at lower cost. Correct state still fails some
later orders; fresh diagnostic work narrows that failure to the use procedure.
These explanations justify closing the bounded phases. The
[PM](EXPERIENCE_PORTABILITY.md#assessment-after-publication--17-september) and
[CL](CORRECTION_LINEAGE.md#assessment-after-publication--17-september) assessments
preserve original expectations, failed acquisition and untested predictions.

The [public follow-up](../sources/2026-09-17-migration-lineage-review/README.md)
revisits migration forecasting and source-grounded auditing, and adds MemLineage
as P86. It narrows further work toward complete behavior and the full cost of
acquiring decision information; generic migration, propagation or enforcement
remain weak contributions. No public implementation was replicated.

The next evidential milestone is a capability that remains useful across repeated
realistic work and consequential change. This requires selecting a setting where
reuse, acquisition or correction changes the best feasible action beyond known
family labels, a fully visible tiny archive and supplied routines. Root theory
and public research should develop that selection before commissioning more
runs. Longer reuse, larger archives or more difficult recipients are possible
conditions to explain, not instructions to extend an experiment until it wins.
AD1 remains untested; prior AD2/AD3 assessments stand. This synthesis commissions
no new study and does not close the enduring question.

## Applied derivative preparation — 17 September

Following discussion of practical prototypes and Hermes, the user chose an owned
execution environment for direct control of experimental instruments. Its public
surface serves other agents and machine clients; an end-user harness is outside
the initial scope. The user also challenged a skills-first direction: model-side
adapters belong in the prototype's actual learning lifecycle.

The [derivative registry](../derivatives/README.md) records **Construct Runtime**
at `alignment-farm/construct-runtime`, outside this root under the sibling
`derivatives/` directory. One initial repository keeps execution, instrumentation
and learning development together. The first milestone includes an actual
train/save/reload/evaluate adapter path, continuing tasks, consequential change
and complete outcomes against competent alternatives. Workload and implementation
choices belong to its development agent. No service or model run starts merely
by preparing the repository.

Selected Hermes code at `5b80838ea2520339f91c532b0e33d3a198c17ffc` supplied
ideas about recoverable artifacts and mutation records; the user prefers control
over the execution environment to adopting that harness. Public model/harness
co-evolution already includes LoRA, so this derivative does not claim to invent
neural adaptation. A2A 1.0.0 supplies a transport reference, with conformance left
for implementation and testing. The derivative keeps its own starting design,
reading provenance and first assignment.

This is applied development, not another ancillary commission or the root's new
research direction. The thirteen accepted contributions and their predictions
retain their boundaries. Root theory, public discovery and independent scientific
selection continue while the derivative develops and publishes useful milestones.

## Weight-consolidation commission — 17 September

After the [targeted methods and runtime review](../sources/2026-09-17-runtime-study-selection/README.md),
the user approved an independent study of what learned weights add when competent
external reuse remains available. The [selection note](WEIGHT_CONSOLIDATION.md)
preserves WC1–WC3 and the identifying comparison through fresh compositions and
changed requirements. The private
[weight-consolidation repository](https://github.com/alignment-farm/weight-consolidation)
is prepared at `a9e609a892fb8e34507e20b5fdf9b504c7c93170`, with `main` pushed
and verified. The user will task its ancillary agent; preparation launched no runs.

The investigator owns workload development, acquisition diagnosis, methods,
resource estimates and publication. Construct Runtime `9ffb10a` is a pinned
starting instrument, with no dependency on its next development milestone.
There are now fourteen registered studies, thirteen with accepted bounded
contributions. Completed phases stay closed; root theory, literature and
independent question selection continue.

## Weight-consolidation assessment — 17 September

The [root review](../studies/2026-09-17-weight-consolidation-findings.md) accepts
`491c0f8a745f48327f6d095d2c3fa7f07d768b44` and closes bounded feasibility and
confirmation. All fourteen registered studies now have accepted bounded
contributions and completed commissioned phases. No continuation is commissioned.
The original WC1–WC3 remain intact with separate assessments.

The study demonstrates partial source acquisition and a small gain configuring
retained code, then explains why a competent compiler eliminates that marginal
quality gain. It corrects a source-access flaw before fresh confirmation, preserves
failed runs, and charges one actual training run. The adapter's added repair work
and worse revised exclusion handling matter alongside aggregate completion.
This is explanatory progress, not a reason to tune indefinitely until weights win.

The experiment also leaves the intended continuing-work milestone unmet: one
authored history, one update and a finite contract language supply neither repeated
consolidation nor independent realistic histories. The code and reference teaching
are investigator-authored. The runtime proved usable as an unchanged independent
instrument; its availability does not turn that workload into a realistic agent
learning problem.

The [public refresh](../sources/2026-09-17-weight-consolidation-review/README.md)
adds P89 and revisits P42. Compatibility between changing harnesses and policies
already has concrete methods. Those narrow a potential diagnosis; they do not
establish why this adapter emits malformed calls or make another co-evolution
loop the next contribution.

Root selection should now describe a consequential decision that remains after
competent explicit execution, and how recurring experience could improve it.
Examples include interpreting ambiguous source contracts or recognizing when
an established procedure applies, but neither is commissioned by this synthesis.
Existing tools remain available wherever valid; natural ambiguity and changing
work should supply the uncertainty, rather than artificial evidence restrictions.
The provenance and cost of newly acquired capability must be distinguished from
investigator engineering. This preserves neural learning as a serious option
inside the hybrid hypothesis while making its useful contribution identifiable.

## Continuing-work authorization — 18 September

Following discussion of investigator autonomy and workload selection, the user
authorized [a follow-up in weight-consolidation](../../ancillary-studies/weight-consolidation/CONTINUING_WORK.md).
The same unresolved question makes continuation in that repository appropriate.
Its prior publication remains accepted; the new instruction delegates bounded
workload discovery, implementation, diagnostic development and fresh experiments.
The investigator selects among existing artifacts and motivated constructed
episodes, with public benchmark overviews as leads rather than adopted methods.
The [selection note](WEIGHT_CONSOLIDATION.md#continuing-work-follow-up--18-september)
records the discovery boundary and comparison.

An agent that acquires a useful executable implementation has made progress even
if later work becomes deterministic. Attribution must distinguish that acquisition
from investigator engineering, with retained artifacts available to both weight
conditions. There is no requirement to preserve neural headroom or demonstrate an
adapter advantage. Publication does not require a routine return to root; the
investigator should explain and act on the value of further bounded work. The
instruction is prepared; root has launched no experiments or ancillary session.

## Continuing-consolidation assessment — 18 September

The [second publication](../studies/2026-09-18-continuing-consolidation-findings.md)
at `80c17db` completes that follow-up. The investigator selected existing database
artifacts, diagnosed several acquisition failures and pursued better source
teaching before fresh evaluation. This is the intended bounded autonomy. Familiar
source execution becomes shorter, but the periodic strategy completes 6/20 fresh
jobs versus external reuse's 7/20. Both retain the same source material. Shared
views handle schema changes; one constructed history limits generality.

The teaching records contain final SQL and finish actions. Fresh adapters never
search the history or execute its saved programs. Learning to use evidence is
therefore the next promising comparison, subject to demonstrating useful
development behavior and charging teacher acquisition. P42/P89 already identify
nearby trajectory methods. P90's database methods clarify that supplied schema
normalization changes the upstream learning target. This is not a new generic
loop or a new commission, and the observed tool choices do not isolate the cause
of poor transfer.

Root also reproduced an accidental answer match: the stale adapter ranks by
product count in a price-ranking task. Its loss after updating is not demonstrated
forgetting of correct price reasoning. Further evaluation should test intended
computations and unambiguous obligations, with fresh data/history variants where
appropriate. Closing the present recipe after explanatory development is
reasonable; neither phase closure nor this review revokes useful continuation
within the investigator's remit. The broader allocation question remains open.

## Lesson-acceptance assessment — 20 September

The [root assessment](../studies/2026-09-20-lesson-acceptance-findings.md) accepts
`cbe62b9` and closes the bounded SQL phase. All fifteen registered studies now
have accepted bounded contributions and completed reviewed phases. Paid evidence
adds no value beyond competent schema review here; corrected acquired code
supports direct reuse. A current correct answer can still come from a defective
program. Original LA1–LA3 are preserved with assessments; AD1–AD3 are unchanged.

Further acceptance work should identify consequential uncertainty remaining after
competent ordinary review, with affordable observations that could change later
complete behavior. The [P95 reading](../sources/2026-09-20-lesson-acceptance-review/README.md#public-method-refresh)
narrows the evaluation novelty without establishing such a workload. No successor
is commissioned; this preference competes with independent questions through its
scientific value. The fixed directive remains useful accumulated experience across
sessions, with explicit memory, lessons, code, weights and runtime rules all eligible.
