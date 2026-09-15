# Learning, revision and changed use: assessment of the concurrent studies

The [15 September follow-up assessment](2026-09-15-followup-findings.md) now
evaluates the expectations below. This first-round assessment is preserved.

14 September 2026. Root assessment after reading the three first publications.
All three are accepted as bounded empirical contributions. Their functioning
learners establish useful updates, harmful interference, scoped revision and
objective-dependent retention. This is progress beyond explaining an
unsuccessful acquisition recipe. It also weakens some of our expectations.

The user approved the independent continuations below after discussing this
assessment. The root prepares questions and predictions; ancillary investigators
own their methods, resource sizing, experiments and publications. Preparing
the follow-up briefs does not itself launch experimental runs.

## Publications and evidence boundary

| Study | Accepted publication | Git revision reviewed |
|---|---|---|
| Experience selection, S1 | [FINDINGS.md](../../ancillary-studies/experience-selection/FINDINGS.md) | `dca27dd46b634616e8895e0a137f23225c5dc7cc` |
| Memory under goal shift, S4 | [FINDINGS.md](../../ancillary-studies/memory-under-goal-shift/FINDINGS.md) | `968c4d89960ef54849dc3625b2a9991cde128cae` |
| Procedure retention and revision, S2 | [FINDINGS.md](../../ancillary-studies/procedure-retention-and-revision/FINDINGS.md) | `9696af5ef32a86571b66bcedec3b3cd241aef9a0` |

The review covered findings, protocols, development decisions, implementations,
supporting evidence and Git chronology. Independent checks rescored 2,432 S1
response records across development and fresh runs, excluding 128 duplicated
baseline records; checked its separate source/probe records and 181 inventory
hashes; and rescored all 3,036 S2 responses, checking common stage starts, update
orders, 26 final manifest entries and inherited checkpoint provenance. For S4,
independent matrix calculations on 15 retained representations/readers agreed
with the reported mechanism results; 108 result-file hashes and recorded
runner/protocol/lock hashes matched. No material inconsistency was found in
these checks. Training and model inference were not rerun; the S4 check did not
regenerate its PyTorch states or refit its readers. Detailed operational evidence
remains with each study.

## S1: update value depends on what is already acquired

Checked training improves the base learner from **30/48 to 48/48** fresh routing
answers. The already-acquired learner scores **48/48** without further updates;
repeating checked training adds nothing. Base self-training yields **24/48**,
and deliberately opposite labels yield **0/48**, despite fitting their training
targets. Source accuracy and useful behavioral change are distinct quantities.

The fixed supervised gate matches always-checked training at **96/96**, against
**78/96** without updating and **87/96 expected** under matched-count random
placement. The random result is calculated from measured branches, and the gate
is evaluated by replaying independently reset branch outcomes, not by deploying
a live sequential policy. It uses checked training-probe labels; these are a
supplied resource, not inferred source reliability.

The gate saves updates against the prescribed 128-step comparator: 384 versus
768 subsequent updates. Including the common construction of acquired states
gives 768 versus 1,152. But **fixed 32-step checked training also reaches 96/96**,
using only 192 subsequent updates, or 576 including construction. Development
supported the prospective 128-step choice, but the fresh shorter endpoint
prevents a general efficiency claim for gating. Whether to update, for how long,
and on which experience must be considered together.

This primarily tests abstention from repeating the exact material used to
construct acquisition. In the acquired state, self-generated and checked labels
are identical, as are their resulting checkpoints. It does not establish a
changing ranking among competing useful sources. The three seeds cover one
binary routing family with nuisance identifiers. Retained examples solve all
48 base cases but only 39/48 acquired-state cases; eight of those nine errors
come from one seed. This is evidence of a state/context interaction, not a
general penalty for retaining evidence. The context prompt also supplies an
invariance instruction alongside its examples.

## S2: successful revision does not establish independent editability

The forward-KL-acquired starting state, followed by new learning and correction
with filtered replay, achieves **12/12 revised routes and 84/84 unaffected
routes**. The correction transfers across fresh identifiers. Complete calls
remain **19/96**, including only **3/12** in the revised scope. On the identical
36 unchanged old queries, five formerly correct complete calls become wrong
and one becomes correct: full correctness changes **11 to 7**.

This partly supports routing-level revision but weakens the stronger
[R4 prediction](../notes/PROCEDURAL_LEARNING.md#assessment-after-retention-and-revision)
that other relations and transformations would be preserved. Behavioral
separation does not establish independently editable internal components.
Both starting adapters inherit the same acquisition seed and examples; their
different outcomes are not independent replications or evidence that forward KL
is generally preferable. All subsequent learning uses hard-label cross entropy.

Correction-only treatments learn their demonstrated corrections but generalize
them too broadly. Filtered replay improves locality relative to correction-only
and update-count-matched repetition. However, the investigator removes precisely
the obsolete records and supplies unaffected examples. Replay therefore combines
rehearsal with evidence identifying the correction's boundary and an externally
provided validity filter. The present comparison does not isolate those effects.

Budget also matters before correction: 32 new-learning updates preserve all old
routes and acquire all new routes from both starts, while longer training can
introduce interference. Yet one route-perfect endpoint reduces old complete
calls from **15/48 to 2/48**. Moreover, all correction arms start from the
corresponding replay-trained state; the short new-learning path has not been
tested through correction. Some other reported route failures are malformed
calls with the right tool, because routing is scored only for valid syntax.

Explicit references resist a simple ordering. Revised examples produce **50/96**
complete calls but stale routing on all 12 corrected fresh cases. A supplied
complete rule reaches **81/96**, including all 12 exact corrected calls, with
additional rule information. Whole-call accuracy and correction success answer
different questions; neither permits a general ranking of memory formats here.

## S4: unavailable information differs from an unsuccessful reader

The learned slow projection determines which features enter a fast memory.
The elementary write rule with fixed orthogonal keys is algebraically projected
record storage. Expected-goal acquisition succeeds at adequate capacity, so this
is a functioning learned representation, not merely a verified gradient update.

At eight slots per record, expected-only learning gives changed-query mean squared error
**0.909** through the ordinary tied reader. A fitted reader recovers the same
frozen states at approximately **4.65 × 10⁻¹²**. At four slots per record with independent
fields, changed-query error remains approximately **1**, with the conditional
covariance calculation explaining unavailable information. When fields correlate,
better prediction can exploit retained correlates without retaining the missing
independent variation. These are distinct mechanisms behind apparent forgetting.

The construction is linear and Gaussian. Full-rank inversion explains the
eight-slot rescue, and the four-slot tradeoff is analytically predictable. Actual
queries are withheld at writing, but the investigator knows the possible query
families and training knows the expected distribution. This is a strong worked
mechanism example, not a general theorem about nonlinear or language-model memory.

A fresh stronger explicit control also changes the interpretation. Pair-sum
records achieve approximately **0.100/0.100** expected/changed error, matching
the broad learned representation's **0.100/0.101**. The initial advantage over
simple retained subsets reflects a weak explicit representation. Conversely,
the explicit transform receives investigator-supplied structure that the learned
projection acquires from data. Payload is matched, total preparation and compute
are not; neither economic superiority nor the irrelevance of learning follows.

## What changes in the root account

Where experience lives is part of a larger decision about what to change and
what to preserve. Its usefulness depends on the learner's current behavior,
the update objective and duration, future questions, reader access, and evidence
supporting later correction. These studies identify different dependencies;
they do not establish a common cause across their mechanisms.

Successful weight revision here uses an explicitly maintained evidence archive.
That motivates studying learned behavior supported by retained records, including
the cost and correctness of filtering those records. It does not establish that
such an archive is necessary for every revision method. Similarly, explicit
access can supply correct evidence without ensuring correct use of it.

The remaining weakness is generality. Two studies use small routing families
with related Qwen/LoRA methods; S4 broadens the mechanism but remains linear.
S5's comparison of acquisition, reuse and revision at comparable useful quality
is still open. No new consolidation project or depth campaign is commissioned
by this assessment. The next experiments should challenge the explanations
above rather than merely repeat their existing examples.

## Prospective expectations and independent continuations

These qualitative expectations are written after the first findings and before
the root has received follow-up results. They are theory commitments to revisit,
not frozen protocols, required outcomes or claims of novel methods. Each
investigator chooses a bounded comparison, checks relevant existing methods,
and tests developed claims on fresh material.

| Direction | Root expectation | Outcome that would revise it |
|---|---|---|
| **S1: partial acquisition and competing useful experience** | With distinct gaps in acquired behavior, relative update value will depend on the gap; useful source choice may remain after comparing short and longer training. | One development-chosen source or mixture remains as useful across states once duration and information access are comparable. This would reduce the case for dynamic source choice in that workload. |
| **S2: correction scope versus rehearsal** | Minimal evidence identifying what did and did not change will reduce overgeneralized correction; broader rehearsal may additionally preserve unaffected computation. | Boundary evidence alone preserves the relevant behavior as well as broader replay, or replay's advantage disappears once scope information is equal. Either would narrow the retention explanation of the first result. |
| **S4: beyond the linear construction** | Under constrained capacity and adequate expected-goal acquisition, a broader-use objective will preserve more useful changed-goal information than a narrow one when one consequential linear-study simplification is relaxed. | No objective-dependent tradeoff appears under adequate acquisition, or the difference disappears with a suitable reader. These weaken the information-selection explanation. Separately, a matching competent explicit representation narrows any learned-format advantage. |

The study-owned handoffs are [experience selection](../../ancillary-studies/experience-selection/FOLLOWUP.md),
[procedure retention and revision](../../ancillary-studies/procedure-retention-and-revision/FOLLOWUP.md),
and [memory under goal shift](../../ancillary-studies/memory-under-goal-shift/FOLLOWUP.md).
They authorize independent bounded experimental continuation, with shared-device
coordination where needed. S2 need not solve identifier production before testing
revision, and S4 need not adopt the routing workload. Failure to acquire calls for
purposeful diagnosis; a finding that a simpler method explains or matches the
effect is useful progress, not a requirement to search indefinitely for a win.
