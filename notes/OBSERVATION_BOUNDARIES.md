# Which observation can justify reusing a lesson?

23 September 2026. Bounded root theory and literature work following the
[lesson-acceptance assessment](LESSON_ACCEPTANCE.md#assessment-after-publication--20-september).
The [reading ledger](../sources/2026-09-23-observation-boundaries/README.md)
records exact sources, inspection limits and investigator provenance.

**Conclusion:** an additional check helps only insofar as its possible results
distinguish decisions that matter. Execution can expose an implementation's
behavior without identifying the intended contract. This gives a bounded answer
to one part of the remaining acceptance question and redirects the next candidate
toward learning which evidence source to consult. It supplies neither a validated
workload nor a new commission.

## What the local evidence leaves open

The accepted SQL phase at `cbe62b9` found an explained cheap solution: competent
schema review identified the defect, and corrected code served all six later
cases without further model calls. Its extra probes supplied no measured gain.
The investigation pilot at `47e5b28` has a different limitation: a stated
boolean-only contract was available, but the limited tests accepted incomplete
repairs. These are existing root assessments, not newly replayed results.

The second failure is not evidence of missing intent; a stronger check against
the already known requirement could expose it. Conversely, calling every
unresolved lesson a testing problem assumes that some available test can settle
the relevant question. The earlier suggestion to investigate contract or
provenance uncertainty needs this distinction before another experiment is chosen.

| Uncertainty remaining after competent ordinary review | Potentially informative evidence | What success alone cannot supply |
|---|---|---|
| Whether code implements an available requirement | Execution on distinguishing inputs, with an independently justified expected result | Correctness beyond the tested conditions |
| Which requirement applies | Existing scoped specification, decision record, or clarification from its responsible source | Intended semantics from the behavior of an implementation that may be wrong |
| Whether an old lesson applies to a changed situation | Evidence about the changed condition and the lesson's scope | Transfer from source replay alone |
| Whether an action is authorized | The applicable permission source and runtime enforcement | Permission inferred from useful or successful execution |

These are root distinctions, not a claim that every case belongs to exactly one
category. A test can reveal an undocumented external service contract when that
service is the relevant source of behavior. A test backed by an authoritative
reference has more information than running the candidate alone. Existing
documents may already settle the issue; consultation need not mean asking a user.

## A limit that does not require a model experiment

Consider two possible worlds with the same learner, prior information, source
history, program and available execution tools. The intended requirement differs,
but no allowed execution returns a contract-dependent judgment. For every query
and reachable transcript, the observation distribution is identical between the
worlds. Any adaptive execution policy therefore has the same transcript
distribution in both worlds: equal histories produce the same next-query
distribution, and equal observation laws preserve equality after that query.

If the final task requires mutually incompatible outputs in the two worlds, a
policy using only those transcripts cannot always complete it correctly. With
equal prior probability and two exhaustive, disjoint correct-output sets, its
mean success is at most one half. More replays, different memory storage, or
training on the same uninformative records do not remove this information limit.
This is an elementary indistinguishability argument under stated assumptions,
not a new theorem or an empirical failure rate. Outside knowledge, informative
feedback or a shared acceptable fallback changes the premises.

For a constructed illustration, a reporting program counts all input rows.
Earlier inputs had unique event IDs. One possible requirement counts deliveries;
another counts distinct events. Replaying duplicates establishes that the old
program counts both copies. It does not determine which requirement the owner
intended. Generating a second implementation exposes the choice without settling
it. A relevant specification or source answer can settle it; a hidden evaluator
with that knowledge must not be represented as an ordinary deployment tool.
This illustration explains the limit and is not a proposed manufactured workload.

The practical question is thus the observation's connection to the uncertainty.
An observation can also distinguish worlds while leaving the best action
unchanged. The existing [decision-value analysis](MAINTENANCE_DECISIONS.md#price-information-about-actions-including-the-alternatives)
already accounts for this and for competent fallback. Its value-of-information
expression should be applied to the full available action set and actual
observation channel, rather than to an assumed perfect answer. No additional
utility scale or empirical probability is introduced here.

## What the closest public work changes

The new reading adds three complementary precedents. P102 SAGE-Agent supplies
structured clarification selection and a trained clarification policy. P103
ClarEval supplies controlled coding ambiguity and scripted answers. P104
DiscoBench connects retrieval, clarification and subsequent answer quality.
See the [versioned method assessments](../sources/2026-09-23-observation-boundaries/README.md#inspected-methods)
for their distinct evaluation and inference limits.

Together they answer generic feasibility proposals about asking for missing
information and narrow the contribution available to Construct. P48/P94 already
cover probing around memory construction; P95 supplies tests relative to a gold
query. None of these inspected methods establishes the full-cost value of learning
which evidence source to use across Construct's continuing work. That is a limit
of this reading, not a certified gap in the literature.

## Consequences for where experience lives

Retain a resolved contract together with its source, applicability and revision
conditions. Encode precise, established behavior in reusable tests or tools when
that avoids work. Contextual lessons or weights can retain strategies for finding
and interpreting such evidence. Runtime rules can enforce authority boundaries.
This is an allocation hypothesis: it does not prove that a fact cannot be stored
in weights, or that every investigation strategy should be trained.

Two experience benefits need separate contrasts. Reusing an earlier sourced
answer can avoid buying it again. Learning how to investigate can improve a new
decision for which that answer is unavailable or inapplicable. A competent ordinary
continuation must be allowed to retain source answers, tests and repaired code;
comparing against repeated needless clarification would inflate the second claim.
Changing an account, contract or permission can invalidate the answer while
leaving the investigation strategy useful. Whether that separation works at
useful cost remains empirical.

## Research selection and stopping boundary

**Retain as an independent candidate:** does accumulated experience improve the
choice among available document review, execution and source consultation on
later unfamiliar acceptance decisions, beyond a developed ordinary policy using
the same history? This sharpens AD1 and LA3 without rewriting their predictions.
It is subordinate to demonstrating functioning evidence access and complete work;
a neural selector is a possible treatment, not the definition of the question.

The next useful root work on this candidate is a bounded artifact-feasibility
inspection of naturally occurring decisions where ordinary review leaves a
material choice. Public clarification benchmarks are method leads, not adopted
workloads. Keep their source information accessible; do not delete a known
requirement to manufacture a need for inquiry. An informative selection would
distinguish source-answer reuse from transferable evidence choice, include a
competent fixed review policy, and evaluate fresh complete tasks after development.
Charge failed inquiries, source preparation, human or simulator responses,
selection, learning, reading and maintenance in their native units.

This root phase closes on the information limit and the narrowed comparison.
No new ancillary study, model run or continuation is commissioned. The original
[experience-guided acquisition commission](CONTINUING_EXPERIENCE_STUDY.md)
remains open under its existing remit; no new result or operational status is
inferred for that study. Lesson acceptance remains a completed bounded phase with
an open broader question. The next program milestone remains useful capability
across repeated realistic work and consequential change.
