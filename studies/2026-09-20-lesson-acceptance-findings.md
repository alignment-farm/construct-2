# Lesson acceptance: competent review can make extra probes redundant

20 September 2026. Root accepts the [lesson-acceptance publication](https://github.com/alignment-farm/lesson-acceptance/blob/cbe62b976e5a9d179a88edbd1a5f573eb0f29254/README.md)
at **`cbe62b976e5a9d179a88edbd1a5f573eb0f29254`**, advancing from preparation
`60552288930555806cef042294ea27145753d1d8`. The bounded SQL phase is complete.
The broader question of when paid acceptance evidence is useful remains open.
The [review ledger](../sources/2026-09-20-lesson-acceptance-review/README.md)
records independent replay, raw cost accounting, preserved failures and a focused
public-method refresh. No new inference, training or follow-up is commissioned.

## What was compared

The investigator constructed two reporting histories: customer invoices/payments
and event registrations/tags. An 8B model produced actual source SQL and two
proposed lessons per history. Both queries worked on their small source slices,
then multiplied rows when independent child tables contained multiple records.
The defects were model-produced, but the fixtures deliberately target a known
relational risk. These are two source calls sharing one failure mechanism, not
an estimate of naturally occurring bad lessons across independent workloads.

All policies retained source requirements, schema, rows, SQL and execution.
Cheap curation additionally retained the common proposed lessons and a review;
paid curation also received an investigator-authored multiplicity probe and its
actual output. The final reviewer and every later reader used the same 27B model
and request controls. Six fresh cases per arm covered three structures per
history. Every task received an initial call and a revision/audit call, including
initially correct tasks. Raw reuse could inspect and repair its retained code.

Curation supplied both scope judgments and corrected SQL. This comparison
therefore measures a bundle of reviewing, rewriting and evidence exposure. It
does not isolate an acceptance bit, the value of abstract lessons alone, or a
learned acceptance policy. Narrow zero-fill and ID-grouping lessons can be valid
inside a faulty whole program; treating every accepted component as an error
would manufacture a lesson-accuracy metric.

## Accepted outcomes

| Policy | Initial outputs correct | Final outputs correct | Final programs passing both extra checks | Fixed program replay |
|---|---:|---:|---:|---:|
| Raw experience with ordinary repair | 2/6 | 6/6 | 5/6 | 2/6 |
| Cheap grounded curation | 6/6 | 6/6 | 6/6 | 6/6 |
| Paid probe curation | 6/6 | 6/6 | 6/6 | 6/6 |

All six raw initial queries matched the source SQL after whitespace/case
normalization. Five changed during revision. The remaining billing program
returned the right answer on its no-fanout case but failed both extra data checks.
Thus ordinary repair recovered every measured current output without establishing
every returned program's broader correctness. The two checks per program are
numerical variants of one multiplicity pattern, not new independent histories
or a proof of SQL equivalence.

Both competent cheap reviews identified the flaw directly from the visible
schema and supplied correct pre-aggregated SQL. Paid reviews supplied equivalent
repairs. Neither curation arm needed to revise its initial task query. Paid
evidence added no observed benefit beyond competent cheap review.

The investigator also evaluated direct deployment of each acquired query,
registered before final evaluation. Cheap and paid corrected programs completed
all six cases without later model calls. The raw source program completed two.
That raw fixed-replay diagnostic is not the competent raw-plus-repair comparator;
it identifies the risk of deploying unchecked source code unchanged. The stronger
result is that once correct general SQL had been acquired, this unchanged-schema
workload no longer required model regeneration.

## Acquisition diagnosis and costs

The initial 8B billing reviewer described correct-looking probe totals that the
execution had not returned. A shared cardinality/reconciliation checklist still
left that reviewer accepting the wrong totals. Attendance review did improve.
Competence escalation then established useful cheap and paid reviews with 27B.
An empty 27B response at the reasoning limit and an interrupted request were
preserved; an explicit serving option produced usable answers before final
evaluation. Empty output alone was not treated as evidence of model incompetence.
This is purposeful diagnostic development, rather than closure on a first failure.

The preserved failures distinguish obtaining informative evidence from using it
correctly. They do not identify model size as the isolated cause of improvement:
the final comparison also follows checklist development and a serving repair.
The cheap-versus-paid comparison itself uses the same developed reviewer.

Standalone deployment accounts cover three reuses per history, counting shared
source collection once per alternative. They must not be summed as experiment
totals. All reader policies used the same two-call task allowance.

| Deployment | Calls | Prompt tokens | Completion tokens | Model seconds |
|---|---:|---:|---:|---:|
| Raw reader and repair | 14 | 11,833 | 5,473 | 346.91 |
| Cheap curation and reader | 18 | 39,269 | 8,154 | 613.55 |
| Paid curation and reader | 18 | 45,745 | 9,026 | 696.55 |
| Cheap curation, direct program | 6 | 3,104 | 4,243 | 212.00 |
| Paid curation, direct program | 6 | 3,731 | 4,563 | 233.00 |

Paid curation added 7,348 model tokens and 83.00 model seconds over cheap curation
with readers; direct replay added 947 tokens and 21.00 seconds. Neither improved
measured quality. The two SQLite probes themselves took about 0.00147 seconds,
but constructing and interpreting them was not free. Raw repair used less model
work than either curation-plus-reader policy, with the residual program defect
qualifying that comparison. Cheap corrected-code deployment was the strongest
measured same-schema alternative, with no claim of universal dominance.

The actual experiment used 54 requests: 53 response artifacts including one empty
answer, plus one interrupted request with unknown consumption. Known totals are
103,511 prompt tokens, 32,207 completion tokens and 1,978.49 model seconds.
These include unsuccessful development separately from hypothetical deployment.
Investigator/teacher effort and money remain unknown. Fixed serial order, caching,
warmup and remote load also preclude treating wall time as a controlled latency
benchmark or these accounts as full economic repayment.

## Prediction assessments and what changes at root

The original [LA1–LA3](../notes/LESSON_ACCEPTANCE.md#comparison-and-prospective-expectations)
remain unchanged; the assessments are appended there.

- **LA1 is narrowed:** competent cheap review already resolved acceptance in this
  workload. Paid probes did not improve later outcomes. Weak interpretation of
  informative evidence is a separate limitation.
- **LA2 has bounded support for the scope distinction:** source replay accepted
  both unsafe programs and multiplicity challenges exposed both. This does not
  establish incremental transfer value over competent schema reasoning.
- **LA3 receives a bounded non-repayment result:** paid checking added measured
  work without benefit at three reuses per history. Selective checking, longer
  horizons and uncertainties unresolved by cheap review were not tested.

This study strengthens the program's distinction between successful episodes
and durable useful procedures. It also shows an acquired executable becoming a
competent low-cost alternative within the experiment: the correct SQL was
model-produced during curation, with investigator-authored tasks, checklist and
evaluation. The useful memory object is therefore not necessarily the proposed
prose lesson. Neither weights nor neural memory were changed; AD1 remains
untested and existing AD2/AD3 assessments stand.

The [P95 methods reading](../sources/2026-09-20-lesson-acceptance-review/README.md#public-method-refresh)
supplies an established precedent for evaluating SQL on multiple databases. It
narrows the measurement contribution and does not resolve affordable acceptance
when the correct environment contract is itself uncertain.

Closing this phase is justified by explanatory progress: reviewer competence was
developed, cheap review settled the visible problem, and the strongest bounded
next step—direct program reuse—was executed. More numeric variants of the same
schema would not establish the missing decision value. A worthwhile successor
would need consequential uncertainty about an actual contract, source provenance
or changed requirement that remains after competent ordinary review, plus an
affordable observation that could change useful behavior. Such a workload is a
selection criterion, not an established resource or a new commission.

The investigator used a stdlib SQLite/HTTP instrument after reporting the prepared
ignored runtime dependency absent in its execution environment. This publication
does not validate Construct Runtime integration. Two closely related constructed
histories, fixed schemas, non-null integer data and supplied requirements also
limit broader memory, transfer and maintenance claims. All fifteen registered
studies now have accepted bounded contributions and completed reviewed phases;
the root's theory, literature and independent question selection continue.
