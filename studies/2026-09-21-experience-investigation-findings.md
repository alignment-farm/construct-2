# Experience-guided investigation: changed tool use without acquired capability

21 September 2026. Root reviews the [pilot publication](https://github.com/alignment-farm/experience-guided-investigation/blob/47e5b284cf520bc89b0411ae2f0bf40e8cef046a/README.md)
at **`47e5b284cf520bc89b0411ae2f0bf40e8cef046a`**, advancing from preparation
`7717645b318d3f3e94673c814fd4acb001869dd3`. The development record is accepted
with the qualifications below. The investigator reports the pilot complete;
the commissioned acquisition-and-transfer work remains open. This review does
not establish a functioning learned investigator or justify closing that work.

**Review disposition clarified 22 September:** revision required for completion
of the commissioned work. Retain the reproducible pilot observations; reject the
interpretation that the smaller repair is complete and the implication that this
pilot establishes a developed acquisition limit. The concrete revision needs are
identified below. This judgment follows the evidence, independently of which
model conducted the investigation.

The [review ledger](../sources/2026-09-21-experience-investigation-review/README.md)
records source inspection, frozen-action replay, additional checks of submitted
code and a focused public-method refresh. No inference, training or new ancillary
run was launched. The study's checkout was left unchanged.

## What was actually tested

The investigator wrote a compact ETL program inspired by the prepared public
sequence, two small repair demonstrations and their tests. The demonstrations
repair trimmed rename fields and zero-row limits. They are two scripted
seven-action trajectories, giving fourteen supervised rows, rather than the
four trajectories described in the protocol. They are not attempts generated
by the learner. The transfer workspace is a fresh copy of the researcher's
checkpoint-2 implementation, not code acquired by a participant through that
sequence. This is a local feasibility adaptation, not a SlopCodeBench result.

A quantized Qwen3-4B-Instruct-2507 model receives rank-8 LoRA on query/value
projections in its final eight layers. Twenty-eight updates over the fourteen
rows change the saved adapter; logged first/last losses are 1.984375/0.033203125.
Those losses concern different presented rows and do not measure task acquisition.
The first training attempt fails on a dtype API error; the corrected retry is
preserved alongside it. Training, adapter persistence and fresh-session execution
are implemented, but no learner evaluation on the two acquisition repairs is
published.

Both transfer arms receive the same authored code, six visible tests, current
requirement and two history summaries. The summaries retain action names,
success flags and a generic researcher-written lesson. The adapter's teaching
contains the full executed demonstrations, including source/tool outputs and
exact repairs; the ordinary arm cannot retrieve those full records through its
workspace. Thus matched workspaces do not establish parity of full source
experience. Nor does this pilot test learning from the agent's own earlier work.

## Outcomes and what the replay adds

| Frozen participant output | Existing tests | Original new-behavior checks | Root's additional contract checks |
|---|---:|---:|---:|
| Ordinary branch change | 6/6 | 0/3 | — |
| Learned branch change | 6/6 | 0/3 | — |
| Base filter repair, added after branch failure | 6/6 | 1/1 | 0/2 |
| Adapter filter repair, added after branch failure | 6/6 | 1/1 | 0/2 |

These are two branch episodes and two diagnostic episodes on one authored
program, not counts of independent histories. Root reconstructed each final
program from recorded actions and matched its recorded hash before execution.
Original evaluations reproduce. A researcher-written branch implementation also
passes the three branch checks and, in root's replay, the six existing tests.
That establishes executable reference behavior, not learner feasibility.

**Neither branch arm made an edit.** Their final source hashes equal the initial
hash. Existing tests pass because the original working program is unchanged.
The learned arm begins with history search and testing, but the search returns
no matches. Eleven attempted edits reach the 384-token generation ceiling and
fail parsing; the run ends at sixteen turns. This locates an observed failure
in action production, without proving a larger output allowance or revised editor
would produce a correct program.

The ordinary arm makes three malformed probe attempts. Its final response
contains an edit object followed by a done object. The parser extracts the last
action, executes only done and labels the episode complete without applying the
edit. Even that ignored edit refers to text absent from the source, so merely
choosing the first object would not solve the task. External evaluation correctly
records failure. The harness completion flag is not a task-success observation.

**The smaller repair demonstrates partial behavior, not the full stated repair.**
Both models replace the faulty predicate with Python truthiness. Their identical
final code correctly rejects a false boolean on the study's diagnostic, but
also accepts a nonzero number and a nonempty string. The task explicitly requires
boolean true; root's two additional frozen-code checks reject both outputs,
while the unmodified reference meets that requirement. These extra checks do not
change the original 1/1 scores; they narrow the interpretation of those scores.

Both diagnostic agents also claim their targeted probe worked after it returned
a schema error. Neither performs a successful targeted probe. The adapter's
history search again returns no matches. More recognizable investigation actions
therefore coexist with failed evidence use and an incomplete repair. The saved
record supports changed action choices, not acquisition of a useful general
investigation procedure or causal value from retrieved experience.

## Costs and reproducibility limits

| Episode | Model calls | Prompt tokens | Reported completion tokens | Reported episode seconds |
|---|---:|---:|---:|---:|
| Ordinary branch | 6 | 16,242 | 596 | 24.88 |
| Learned branch | 16 | 108,981 | 4,286 | 193.85 |
| Base filter diagnostic | 5 | 12,797 | 301 | 17.87 |
| Adapter filter diagnostic | 7 | 16,869 | 167 | 21.22 |

These sums are recomputed from saved events: 34 calls, 154,889 prompt tokens,
5,350 reported completion tokens and 257.83 episode seconds. The implementation
counts stream chunks as completion tokens; root did not retokenize generations.
The successful training report adds 108.49 seconds and about 16.34 GB peak MLX
allocation; the failed attempt adds 3.51 seconds. These are recorded instrument
times, not controlled latency comparisons or total deployment costs. Researcher
construction, service probes, energy, money and some startup work are unaccounted.
No extra-resource arm, longer reuse sequence or artifact-evolution comparison ran.

The model and implementation have explicit pins, and the adapter is tracked.
Root hashed the artifacts and inspected the loading path without running the
model. The reported isolation check verifies unchanged base parameters and a
saved-adapter digest, then expects a restored model to answer `READY`. It does
not compare all restored adapter tensors or an independently measured pre-load
behavioral reference. Root therefore records these as inspected mechanics and
reported reset checks, not independent proof of exact behavioral restoration.
The environment's study revision is the pre-experiment `7717645`; the complete
reviewed implementation and evidence are identified by publication `47e5b28`.

**Investigator provenance supplied 22 September:** the user reports that this
study's investigator was `gpt-5.6-luna` at `max`, whereas previous ancillary
investigators used `gpt-6-astra` at `medium`. The publication records the Qwen
participant but does not independently establish these investigator configurations.
Treat the user's report as provenance, not a measured explanation of quality:
study difficulty, starting context, harness, interventions and resources were
not controlled across those assignments. No investigator-model comparison has run.

## Predictions and research implications

Original [CC1–CC3](../notes/CONTINUING_EXPERIENCE_STUDY.md#prospective-expectations)
remain unchanged, with assessments appended to that brief.

- **CC1 is unresolved.** Neither branch succeeds; the study does not establish
  a task-relevant contribution from earlier experience. A new requirement alone
  does not show that residual experience is needed, and the analysis's claim
  that branching required it is not supported by these comparisons.
- **CC2 is untested.** The adapter incurs more measured work without better
  outcomes here, but no competent extra-allowance comparison or reuse horizon
  tests the opportunity-cost prediction. This is not evidence that learning
  generally fails to repay its cost.
- **CC3 is untested.** Matched supplied code controls one artifact difference;
  it does not compare policies that acquire different code/tests. Unchanged
  failed branch outputs cannot identify mediation through better artifacts.

This pilot adds a concrete distinction to the root synthesis: a model can adopt
the visible order of investigation without obtaining informative evidence,
interpreting it correctly or completing the required change. The previous SQL
study lacked investigation actions in teaching. Adding authored action traces
does not by itself resolve that limitation. That is not evidence that the two
studies share an internal cause, or that adapters cannot learn investigation.

The [public-method refresh](../sources/2026-09-21-experience-investigation-review/README.md#public-method-refresh)
adds selected methods from SWE-agent (P101, `2405.15793v3`) and revisits P42
(`2609.09134v1`). Compact editing, informative feedback and correction of the
learner's own failing turns are established methods to consider. They narrow
the next scientific comparison toward a functioning model/interface/teaching
combination; they do not demonstrate that any particular change will repair
this pilot or that harness improvement is a weight-learning result.

## Status and next selection

Accepting this publication does not complete the original commission. The pilot
explains where observed executions stopped, but does not establish the targeted
acquisition, a developed limit on it or a study-level resource constraint.
The publication itself identifies interface and teaching development as its next
useful step. A turn limit on one episode is not a resource limit on that work.

The highest-value continuation within the existing study is bounded diagnosis:
establish usable editing and truthful completion feedback on development material;
test complete acquisition including the observed predicate-type failure; and
obtain actual learner attempts with compatible corrections and recoverable raw
experience for the ordinary comparator. Change one consequential factor when
that separates explanations. Preserve these failed runs and use fresh material
for a resulting transfer claim. A shared harness improvement belongs in both
arms and must be separated from the additional value of learning.

The ancillary investigator owns those choices under its existing commission;
this review launches no follow-up and creates no duplicate project. Root continues
theory, public research and independent acceptance/intervention questions. The
enduring directive, AD1–AD3 and other completed-study assessments are unchanged.
