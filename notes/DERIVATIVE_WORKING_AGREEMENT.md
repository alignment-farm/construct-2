# Derivative working agreement

Version 0.1.1 · 2026-09-08 · Clarifies independent agent assignments; experiment scopes are unchanged.

**A derivative owns a bounded investigation through a reviewable evidence
return.** The root owns the connected theory, interpretation across cycles,
and choice of the next research question. The user assigns derivative agents
and controls resource commitments. Finishing an investigation can mean an
informative loss, an unresolved comparison, or a documented instrument limit.
A favorable result is never a completion requirement.

This is a working agreement based on the first two cycles, not a new research
method or a fixed organization. Use existing documents where they already
cover a field. A short diagnostic needs less documentation than a large study.
The templates provide a common entry point without requiring a new framework,
dashboard, or reporting service.

## Current assignments and agent continuity

- **Cycle 1 — `construct-memory-utility`: Grok continues to own this
  investigation**, including cleanup, review corrections, and further work
  within its assigned scope through its evidence return. Use this agreement
  to organize that work. It does not redirect Grok to Cycle 2.
- **Cycle 2 — `construct-lesson-transfer`: Codex executed the separately
  assigned application attempt and [returned its protocol stop](CYCLE_2_APPLICATION_REVIEW.md).**
  The diagnostic remains incomplete. Further execution is a separate user
  assignment, open to another agent family or session. Its charter is a worked
  example; reading it does not assign its experiment to the reader.

The agreement applies across agent families and sessions. The user may assign
a different agent or a fresh session to any derivative; continuity must come
from the committed project, protocol, evidence, and handoff, without requiring
access to an earlier conversation. Each assignment is to a specified
derivative, with no automatic progression from one cycle to the next.

The agent conducting the research is distinct from the model being tested.
Changing the assigned research agent leaves the experiment's model pins,
treatments, and other protocol conditions in force.

## The small document set

| Document | Purpose | Starting point |
| --- | --- | --- |
| `notes/CHARTER.md` | Question, competing explanations, scope, budget, decision rights, and completion | [Charter template](../templates/derivative/CHARTER.md) |
| `AGENTS.md` | Instructions for the agent taking ownership | [Agent instructions template](../templates/derivative/AGENTS.md) |
| `notes/returns/NNN-progress.md` | A milestone, surprise, or decision that warrants root attention | [Progress template](../templates/derivative/PROGRESS_REPORT.md) |
| `notes/returns/NNN-final.md` | The completed or stopped investigation and its evidence | [Final template](../templates/derivative/FINAL_REPORT.md) |

The charter links to the detailed protocol rather than duplicating it. The
protocol defines treatments, controls, evaluation isolation, sampling,
measurements, analysis, stopping, and recovery. A derivative README points to
the charter, active protocol, latest return, and current next action. Retain an
existing `HANDOFF.md` when it usefully records commands and operational state.
Code, tests, environment locks, configurations, raw artifacts, and analysis
remain in the derivative's existing structure.

Record the adopted agreement version. Later template edits do not silently
amend an active experiment. A populated charter records the scope actually
assigned by the user; copying a template does not authorize additional work.

## Ownership and decisions

| Decision | Derivative agent's responsibility | When it returns to the root/user |
| --- | --- | --- |
| Implementation and housekeeping | Choose code structure, improve documentation, commit work, and maintain a usable handoff | No routine approval; preserve evidence and existing user work |
| Instrument repair | Diagnose, fix, and test defects; document their effect on existing evidence | Return if continuation changes the comparison, needs new resources, or cannot preserve the protocol's conditions |
| Experiment execution | Run the assigned protocol within its budget, stopping and recovery rules | Report milestones and stops; no permission request for already assigned steps |
| Scientific design | Develop concrete alternatives and bounded diagnostics within any declared exploration allowance | Changing the question, primary comparison, evaluation population, primary analysis, or a frozen treatment needs a decision before dependent inference |
| Resources and scope | Track spend and work within the declared envelope | A larger budget, another experiment, or use of resources outside that envelope needs the user's decision |
| Interpretation and follow-up | Make bounded claims, retain alternatives, and recommend the most informative next comparison | Root synthesizes across projects; a follow-up proposal is not automatic authorization to run it |

Do useful independent work while a decision is pending. Bring a concrete
amendment, its scientific consequences, cost, and recommended choice. Do not
send routine implementation choices upward. If an unforeseen change is
necessary to make the run interpretable, stop the affected inference rather
than quietly changing the question mid-run.

Cleanup must preserve the research record. Improve navigation and mark old
material as superseded; retain failed runs, earlier protocols, raw responses,
and accounting. Do not rewrite history or remove evidence to make a return
look cleaner. Other derivatives and shared model services remain outside the
agent's ownership unless the user assigns them explicitly.

## Before and during model contact

Before an experimental batch, identify the actual protocol, code,
configuration, data, and model/backend used. Prefer committing source before
inference; if that is impractical, capture the base commit plus the complete
relevant changes and file hashes before the first request. A later commit
does not establish which unrecorded working tree produced an earlier run.
Keep the pre-run source identity distinct from the later evidence-return
commit. Record model digest/version, backend/template identity where
observable, exact requests, caps, seeds, and requested settings. Label settings
whose effective backend behavior has not been verified.

Use validation suited to the actual workload, including each role the claim
depends on. A short format probe or an actor-only smoke does not validate a
memory writer, retrieval, or their composition. A writer needs a check for its
own contract. Distinguish fake-endpoint tests, real-model diagnostics,
independent outcome checks, and full experimental evidence.

Maintain append-only attempt accounting. Name the units: episodes, model
requests, histories/worlds, task pairs, tokens, and time are different counts.
Include diagnostic and calibration calls in an explicitly assigned allowance;
report them separately from scored episodes. Failed and excluded attempts
still cost resources. No relabeling, hidden retries, or replacement draws to
evade a cap or improve a result.

Record an amendment before its affected calls: what changed, why, which prior
outcomes were already seen, which runs it affects, and whether a fresh test is
needed. Repairs must not overwrite raw evidence or previous scores. A scoring
correction produces a versioned reanalysis with the affected outcomes and
claims identified. A parser or transport repair may restore an intended
contract; a changed prompt, model, memory representation, or fallback may also
change the treatment. State that consequence explicitly. Resume only under a
documented, tested recovery consistent with the protocol; otherwise return
the partial record.

## When and how to return evidence

Send a progress return when an agreed stage completes, a surprise changes the
interpretation, a stop prevents continuation, or a decision is needed. Routine
coding and unchanged run progress belong in the derivative's own log. A
progress report can be a few paragraphs and a small table. It should state
what changed since the last return and whether a response is needed.

The derivative writes and commits its report beside its evidence. The user
relays **repository, full return commit, report path, status, and any decision
request** here. Put the enclosing commit in that relay after committing; the
report itself records pre-run source pins and run IDs, avoiding a
self-referential commit hash. This agreement does not authorize automated
messages or edits to another repository.

For final review, the reader must be able to follow each material claim to its
denominator, saved output/state, analysis, and protocol. Provide commands to
recompute analysis and verify evidence without new model calls or mutation of
the original artifacts. Identify commands that instead require live services,
spend inference, or write state. If evidence cannot be supplied, state exactly
which claims cannot be independently checked. Exact rerunning may remain
limited by backend behavior even when the observed evidence is verifiable.

Separate observations from interpretations, and instrument findings from
mechanism findings. Report adverse cases and costs alongside gains. Repeated
calls sharing a history are not independent histories. Distinguish an
imprecise null, absence of treatment need, failure to apply supplied knowledge,
and inability to measure the intervention. Explain what each leaves open.

## Root review and closure

The root reviews a pinned return, records what it checked and what it did not,
and writes its assessment here. It should answer:

1. What does the evidence support or weaken under the tested conditions?
2. What alternative explanations or measurement limits remain?
3. Which broader theory changes, and which does not?
4. Is the return ready to synthesize, does a specific claim need correction,
   or is the record incomplete for its intended comparison?

Acceptance of a return means the record supports its bounded account. It does
not imply a positive treatment effect, authorize a larger experiment, or
oblige the root to adopt the derivative's next engineering priority. An
uninterpretable run can close operationally while leaving the hypothesis
untested. Corrections stay in the derivative, followed by a new pinned return;
root reviews retain their historical pins and link subsequent revisions.

## Adoption and revision

The [Cycle 2 charter](CYCLE_2_DERIVATIVE_CHARTER.md) applies this agreement to the
already prepared application diagnostic. It records the current scope; the
derivative's existing protocol and handoff remain the execution specification.
It is for the separately assigned Cycle 2 agent; no new experiment is launched
by this document.

For Grok's continuing Cycle 1 work, use the
[channel review](CYCLE_1_CHANNEL_REVIEW.md) as the specific correction record,
and these templates to organize the next return without retroactively claiming
the earlier runs followed this agreement. After that return, the root will
review this agreement based on missing information, unnecessary reporting
burden, and decisions that still required avoidable course correction. See also the
[Cycle 2 development return](CYCLE_2_PILOT.md) for the application/construction
distinction that motivated its present scope.
