# Experience-guided investigation: conditional repair and autonomous use

28 September 2026. Root review of
[`523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6`](https://github.com/alignment-farm/experience-guided-investigation/tree/523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6),
following the [pilot assessment](2026-09-21-experience-investigation-findings.md)
at `47e5b28` and user-authorized continuation instructions at `121242c`.
The [publication](https://github.com/alignment-farm/experience-guided-investigation/blob/523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6/evidence/continuation-02/README.md)
and detailed methods remain study-owned. The
[root ledger](../sources/2026-09-28-investigation-continuation-review/README.md)
records inspection, replay, provenance and complementary reading.

**Accept this bounded diagnostic phase, with qualifications.** A correction-trained
adapter produces a correct filter implementation from a supplied recorded context,
but does not reach that repair autonomously or execute the taught investigation.
A further correction changes its tool choices without producing repair. Full
ordinary-history access fixes an earlier comparison defect. These are explanatory
advances; useful autonomous acquisition, fresh transfer and repayment remain open.
The original commission is not complete, and this review launches no experiment.

## What the evidence establishes

All twelve episodes are development on an authored ETL program, with six matched
pairs. Scores below are counts of eighteen external contract checks on each saved
program, **not eighteen independent tasks**. Root replay reproduces every score
and the six-test public suite. The initial shared program and task contract are
supplied, not products acquired by the learner over earlier work.

| Development comparison | Ordinary base | Adapted learner | Meaning |
|---|---:|---:|---|
| Rename field normalization | 16/18 | 16/18, pilot adapter | Both fail the rename requirement and one public test. The adapter changes row values instead. |
| Limit zero | 18/18 | 18/18, pilot adapter | Both repair this behavior and pass public tests; neither verifies a successful targeted probe. |
| Strict boolean filter | 9/18 | 13/18, pilot adapter | The adapter's truthy predicate remains wrong for numbers and strings. |
| Filter after new correction training, autonomous | 9/18 | 9/18, 28 updates | The new adapter repeatedly reads source without editing. |
| Same filter with three recorded prefix turns supplied | 9/18 | 18/18, same 28 updates | Conditional strict repair and passing public tests; no probe or finish. |
| Filter after one additional correction at a learner-visited context | 9/18 | 9/18, 32 updates total | Eleven probes, seven application-successful, eleven failed assertions, no edit. |

The conditional result is a bounded positive learned effect under matched supplied
context. It is not acquisition of the complete procedure. Its first prompt is
byte-identical to the taught probe prompt, yet the learner reads again instead of
probing. It later makes the strict `is True` edit, passes public tests and loops
on reads to the turn limit. No maintenance episode consults history or passes a
probe assertion. Repeated deterministic base runs on the filter are not independent
replications, and their failures do not establish a competent ordinary alternative.

The new training is grounded in an actual failure, with limited authorship claims.
Two successful read actions and a rejected malformed action come from the pilot
adapter's filter attempt. The investigator then executes five authored corrective
actions: discriminate, repair, recheck, test and finish. Seven training targets
contain two learner reads and those five corrections; the malformed output remains
in the prefix but is not a target. Training starts a new adapter from the base
model, not from the policy that produced the prefix. The later four-update bridge
uses the new adapter's own autonomous read context, replacing one read with the
already executed probe. It does not aggregate a growing curriculum of successful
investigation episodes.

These interventions distinguish three achievements: producing a correct local
repair under supplied context, reaching useful actions autonomously, and interpreting
feedback to complete work. The evidence establishes the first in one development
case. It does not isolate a single cause for the remaining failures. In particular,
missing the probe at its exact training prompt prevents a pure context-distribution
explanation. The bridge was not retested at the earlier conditional repair context,
so its autonomous failure does not establish forgetting of that conditional skill.

## What the continuation repairs, and what still limits it

The shared interface now rejects incomplete or composite JSON, paginates reads,
raises the generation ceiling from 384 to 1,024 tokens, and separates application
success from expected-output assertions. It also supplies a boolean-versus-truthy
warning to both arms. None of the 135 generated actions reaches the new ceiling;
short malformed actions and schema mistakes persist. These bundled changes do
not identify which change helped, and no rerun explains the original branch failure.

Both arms now receive identical initial code, task text, public tests and complete
eligible history within each pair. That archive includes full teaching records,
attempts and repaired code. The old summary-only access defect is resolved. Actual
retrieval competence is not established: none of these runs reads the archive.
Training delivery and ordinary pull-based access still differ, as intended parts
of the comparison. Each episode uses a fresh process and loads base/adapter state;
saved load/reset tests now check actual outputs and hashes. Root inspected those
records and code but did not rerun models or verify live base tensors.

Root also verifies a collateral defect beyond the published eighteen checks.
For an ordinary rename from `amount` to `price`, the input value
`"  keep spaces  "` should survive unchanged. The adapted normalization submission
returns `"keep spaces"`; the base submission preserves it. This confirms that equal
16/18 scores conceal an added regression, not just failure to improve. It is a
post-publication diagnostic of existing code, not a new learner trial or an estimate
of regression frequency. Even 18/18 plus six public tests is bounded coverage,
and does not by itself fulfill the requested investigation procedure.

The nine-case subsequent extension is prepared but unevaluated. No fresh-transfer
result exists. Adaptive decisions and a budget are documented, but this continuation
arrived as one publication commit; root has no separate pre-run Git freeze to
independently certify their timing. All executed material is appropriately labeled
development, and original failed attempts remain preserved.

## Costs and scope of acceptance

Raw episode records reproduce 135 model calls, 396,996 prompt tokens and 7,694
completion tokens. Episode time is 551.92 seconds, including 534.53 seconds of
model generation. The two jobs total 32 updates, eight training rows and 129.16
seconds, with reported peak MLX allocation 13,086,098,982 bytes. Two load/reset
checks take a further 15.37 and 15.84 seconds. Investigator/teacher token and money
costs and complete preparation/validation time remain unknown; prior pilot costs
are separate. These native units supply no comparable-quality repayment result.

The phase used its stated episode/update allocation, well below its 90-minute
GPU ceiling. Stopping on the explained conditional/autonomous gap is justified;
hardware exhaustion and a general model limitation are not established. The study
requests Astra provenance but cannot expose actual backend identity or reasoning
effort. Root records those limits without attributing performance to the investigator.

## Consequences for the program

**Root inference:** retained knowledge must be assessed together with the policy
that reaches and uses it. The related [evidence-set findings](2026-09-28-evidence-set-findings.md)
show that useful rankings and successful deployed inference can separate. Here
correct conditional repair and successful autonomous investigation separate. This
is a common evaluation requirement across different mechanisms, not evidence that
their internal failure causes are the same or that one substrate should win.

The complementary **DAgger method (P119)** narrows the acquisition question:
collect expert actions at states visited by the learner and train on the aggregated
experience. Its guarantees require assumptions not verified for this LoRA learner.
One corrected context trained four times is not a test of that method.
[Primary paper](https://proceedings.mlr.press/v15/ross11a/ross11a.pdf).
The [ledger](../sources/2026-09-28-investigation-continuation-review/README.md#complementary-public-method-p119)
distinguishes this inspected method from a proposed remedy; P42 and P101 remain
relevant prior readings, not local replications.

The next useful work within the existing study is bounded acquisition of correct
action arguments, feedback use and completion from actual failed contexts. Establish
that autonomous behavior before spending fresh material on transfer claims. Treat
competent ordinary reuse of the now-complete archive as a scientific requirement,
not as satisfied by equal file access. More copies of a long JSON target, more turns
or a standalone tool-name classifier are not justified by these results alone.
The investigator owns the choice among training, interface and participant-model
changes. This is a research preference within the open remit, not a new commission.

[Original CC1–CC3](../notes/CONTINUING_EXPERIENCE_STUDY.md#prospective-expectations)
remain unchanged. **CC1 is unresolved:** neither fresh benefit nor residual need
for earlier experience is demonstrated. **CC2 and CC3 are untested:** there is no
competent extra-allowance comparison, repayment horizon or contrast of acquired
work products. Independent EBM exploration and root theory/literature continue.
