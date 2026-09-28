# Evidence-set memory: acquisition, energy search and complete use

28 September 2026. Root accepts phases 1–5 at
[`8ac9b694a32e53e5941912b65e2c8881ce0d7c4b`](https://github.com/alignment-farm/evidence-set-memory/tree/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b)
as bounded contributions, with the qualifications below. This advances the
previous preparation-only boundary, `5a0e8f7`. It does not close the broader
question or add a commission. The user's expanded authorization for continued
EBM exploration remains in force.

**The study establishes functioning acquisition and explains several failures
of energy-based selection. It has not established an advantage in complete LLM
work over competent ordinary access.** Its strongest new distinction is between
learning a useful ordering of discrete evidence sets and learning an energy
surface that a practical inference procedure can use. These are different
achievements even when both are described as energy learning.

## What the five phases establish

| Phase | Supported finding | Limit that changes its interpretation |
|---|---|---|
| [1: quotes and revisions](https://github.com/alignment-farm/evidence-set-memory/blob/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/FINDINGS.md) | Purposeful acquisition diagnosis produces a useful eight-coefficient set scorer. Exact learned selection and ordinary dependency-following complete 30/30 later native quote tasks; one-swap search completes 24/30 before repair. | Six histories of five related episodes, with authored links and authority. The ordinary solution supplies successful acquisition examples. This is not learned representation discovery. |
| [2: natural-text selection and QA](https://github.com/alignment-farm/evidence-set-memory/blob/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/phase2/FINDINGS.md) | A small neural joint scorer acquires benchmark support selection. Exact search covers all annotated supports on 26/64 questions, versus 15/64 for ordinary and learned unary selection. Beam search matches exact search. | Imported annotations, supplied 20-paragraph candidate pools and a frozen encoder. Annotation quality prevents treating the downstream metric as validated source-grounded task success. |
| [3: candidate scaling](https://github.com/alignment-farm/evidence-set-memory/blob/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/phase3/FINDINGS.md) | Relaxation becomes cheaper than exhaustive enumeration as pools grow; discrete beam remains cheaper and reaches the best energy in every tested case. | Four previously seen questions, enlarged with distractors; no fresh QA evaluation. Better energy is not necessarily better support coverage. |
| [4: fractional energy](https://github.com/alignment-farm/evidence-set-memory/blob/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/phase4/FINDINGS.md) | An intervention that preserves every binary set score changes gradient-search outputs. Binary ranking supervision alone does not identify fractional behavior. | Algebra plus a diagnostic on 48 seen development questions, not a new transfer result or novelty claim. |
| [5: native configuration](https://github.com/alignment-farm/evidence-set-memory/blob/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/phase5/FINDINGS.md) | Learned coefficients reduce delivered material relative to their untrained initialization while retaining exact-search completion through revisions and longer chains. Representation errors, objective errors and optimizer failures are separately explained. | An authored configuration workload using unchanged Python semantics and a supplied syntax parser. Ordinary dependency-following remains slightly more compact, with less selection work and no acquisition cost. No LLM reader is tested. |

Phase 1 preserves failed acquisition: simply increasing classification training
did not recover development tasks. Pairwise learning then reached 20/20, although
the objective and effective weighting changed together. Its one-swap failures
have a checked local-optimum explanation. The small reader diagnostic reports
2/5 complete answers with either identical compact policy and 0/5 with all
current records; only one distinct successful calculation plus its repeat is
represented. A public calculator fixes all mapped cases and is invoked on every
reader output. This is a useful diagnostic of context and execution, not evidence
that a learned selector improves on ordinary compact access.

## The strongest complete-task comparison

Phase 5 learns from 2,448 executed subset attempts on twelve development
histories. Its successful examples include ordinary dependency closure, so the
teaching is deliberately constructed. A frozen model then faces twelve fresh
histories, half with two extra dependency-chain sections. All policies share
explicit source scope, latest-revision rules and a source-ID-validated cache.

| Frozen policy | Complete uncached attempts, before repair | Complete episodes, before repair | Repairs | Delivered bytes, including repair |
|---|---:|---:|---:|---:|
| Ordinary syntax closure | 48/48 | 72/72 | 0 | 34,442 |
| Full current records | 48/48 | 72/72 | 0 | 80,240 |
| Untrained energy, exact search | 48/48 | 72/72 | 0 | 73,082 |
| Learned four-coefficient energy, exact search | 48/48 | 72/72 | 0 | 35,111 |
| Same learned energy, frozen gradient search | 34/48 | 58/72 | 14 | 39,476 |
| Learned three-coefficient energy, exact search | 29/48 | 53/72 | 19 | 41,316 |
| Unlearned hard feasibility plus minimum size | 48/48 | 72/72 | 0 | 34,442 |

Every policy reaches 72/72 after public native-error repair. Each has 24 cache
hits; a cached repaired result is not a new learned success. These are twelve
correlated histories using six template families, not 72 independent trials.
The improvement over initialization is **compactness at preserved completion**,
not acquisition of a previously absent complete-task capability. Smaller delivery
also does not establish faster native execution: full context was marginally
faster than closure in the saved tiny timing comparison.

The causal diagnosis is useful. A naive representation mishandled default values
and escaped interpolation syntax. With that fixed, rewarding resolved dependency
edges sometimes attracted unrelated connected records. Removing that reward
improved this behavior but left a finite missing-edge penalty: on longer chains,
omitting necessary sections could have lower energy than including them. Exact
search cannot fix an objective that prefers an incomplete answer.

Conversely, the four-coefficient energy ranked complete answers best, but the
frozen four-start, 60-step gradient recipe missed fourteen of the 24 uncached
longer-chain cases. Additional steps or starts recovered 48/48 on the already
examined material. That is post-hoc diagnostic evidence, not fresh confirmation
of a revised policy. It establishes a limitation of the tested inference budget,
not impossibility for gradient methods.

Weights stay frozen across these later episodes. Source revisions and cache
invalidation supply maintenance; source authority is not learned. The old-valid
checks concern another still-applicable request, not retention of a previously
mastered obligation for the same item. Logical episode resets and a separate
confirmation process also fall short of extended agent sessions on natural work.

## Natural-text results require a narrower claim

Phase 2's 674-parameter neural scorer uses lexical/link features and frozen
MiniLM representations. The encoder's 22.7 million parameters, labels and
encoding work belong in its resource account. Benchmark-supervised selection is
different from acquiring useful experience through prior agent work.

The original 24-question reader slice gives exact selection 2/24 on the published
answer-plus-citation metric, ordinary selection 0/24, full context 6/24, and
annotated supports 9/24. Public format/empty-answer fallback changes exact and
ordinary to 3/24 and 1/24. Root reproduced those scores from 166 saved responses
mapped to 192 outcomes, including request contents and fallback decisions.

Those numbers are **annotation-relative scores**. Root checked three disclosed
examples against the recovered source paragraphs: one joins Mohamed Salah's
award to Ahmed Salah Hosny's biography; another connects Maycon's club to an
unrelated player's different club; a question requesting a year is graded against
a full date. The second problem also occurs in an apparent exact-match success.
Thus both successes and failures can be misleading. These selected checks
confirm material label problems; they are not an estimate of their prevalence
or a substitute corrected leaderboard. The study's broader audit remains
post-hoc and author-reported beyond these checks.

A post-freeze retry of all and only length-stopped outputs uses a larger budget.
The published full-context metric rises from 6/24 to 7/24; exact selection stays
at 2/24 before fallback. Its repaired score falls from 3/24 to 2/24 because a
well-formed answer with incomplete citations no longer triggers full-context
repair. This is not evidence that more budget worsened answer correctness.

One previously inspected question entered the 64-row confirmation partition;
excluding it leaves exact 26/63 versus ordinary 15/63. Component overlap within
the later partition and repeated source paragraphs limit independence despite
component-disjoint training/development/confirmation splits. The first 24 reader
questions exclude that exposed question. These qualifications preserve the
useful selection finding without promoting it to validated general QA benefit.

## Consequences for theory and selection

Phase 4 makes the inference distinction precise: adding
`lambda * sum(z_i * (1-z_i))` leaves every binary energy unchanged but changes
fractional gradients. The same ambiguity exists within the study's zero-diagonal
quadratic family at fixed cardinality. Root checked the algebra and reran the
test over all 4,845 size-four sets and sampled fractional points. A discrete
ranking and an inference path therefore require separate identification.

The closest complementary method added here is
[P118, end-to-end SPEN learning](https://proceedings.mlr.press/v70/belanger17a.html):
it trains through the actual finite inference procedure. That established method
narrows the interpretation of these local ranking-trained models; the study has
not tested jointly learning the deployed gradient procedure's useful behavior.
The [source ledger](../sources/2026-09-28-evidence-set-review/README.md) records the
inspection limits. This is a method lead, not a demonstrated local remedy.

For Construct-2, retained evidence, learned compatibility, inference and native
execution can work together. The unresolved question is where additional learning
improves complete later work after competent ordinary access leaves real work
unresolved. Neither more sweeps of the solved explicit graph nor a relabeled
retrieval score would settle that question. Natural evidence should have valid
grounding, and practical inference should be evaluated as part of the learned
system, with acquisition and repair included.

The study's proposed configuration/code-edit pilot is a reasonable discovery
direction within its existing user authorization. It remains the investigator's
proposal, not a new root commission or a methods prescription. If it moves toward
repository editing, distinguish its EBM contribution from the independently open
experience-guided investigation question. Broader LLM improvements remain open;
these bounded results neither establish nor refute the user's hypothesis.

## Review boundary and reproducibility

Root inspected local instructions, the starting brief, all five findings,
relevant protocols, source/label/exposure/cost records, implementation and Git
history. Local HEAD and remote `main` both identified `8ac9b69`; review used an
isolated archive of that revision. The phase-5 freeze precedes confirmation at
`f8651b8`; later optimizer diagnosis is kept distinct. Earlier manifests belong
to their publication revisions, not subsequent README edits.

Root reran phase-1 confirmation and its local-optimum audit; reproduced 6,185
phase-5 native executions and five bit-identical fits with the study's audit;
reran frozen selection and confirmed all 504 policy/episode outcomes using 369
additional native executions;
independently regraded the original 192 QA outcomes and aggregated selection,
configuration and raw token records; verified all 52 phase-5 manifest files; and
passed all 18 supplied tests after restoring data. Python 3.12.14 was unavailable
through the local `uv` catalog, so the native replay used 3.12.12 with a different
`configparser` hash. No fresh reader calls or phase-2 neural/encoder replay were
performed; phase-3/4 numerical sweeps were inspected rather than rerun. Root
replays are verification costs, not new samples. Detailed limits, setup failures,
reports and provenance are in the [review ledger](../sources/2026-09-28-evidence-set-review/README.md).
