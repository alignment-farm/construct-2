# Learning appendix

This is a companion for individual study. The research question determines the
experiment's scope and standards. Use these notes when a concept in the work
would benefit from a slower explanation; completing the reading is not a
prerequisite for project progress.

## Cycle 1: A suggested route

| When you encounter this in the project | Read or inspect | A useful question to answer yourself |
| --- | --- | --- |
| [The reproduction conditions](cycles/001/PROPOSAL.md#reproduction) | [MemRL v2, sections 3–4](https://arxiv.org/html/2601.03192v2#S3) | Which stored numbers change, and how can that change a later answer? |
| [The migration extension](cycles/001/PROPOSAL.md#one-extension-schema-migration) | Sutton and Barto, *Reinforcement Learning*, second edition, chapter 2, especially incremental estimation and nonstationary problems; [publisher page](https://mitpress.ublish.com/book/reinforcement-learning-an-introduction-2), [CMU-hosted text](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf) | Why does a constant learning rate discount old evidence, and why might that still be too slow in elapsed tasks? |
| [The primary contrast](cycles/001/PROPOSAL.md#predictions-and-measurements) | Work through the four cells using invented success rates | Can the interaction be positive even when resetting harms performance in both worlds? |
| [Sampling and evidence](cycles/001/PROPOSAL.md#sampling-and-evidence) | [Agarwal et al., v4](https://arxiv.org/abs/2108.13264v4), introduction and interval-estimate discussion | Why are many episodes from one acquired memory history different from many independent histories? |
| [Prospective protocol decisions](cycles/001/PROPOSAL.md#execution-sequence) | [Registered Reports: workflow and FAQ](https://www.cos.io/initiatives/registered-reports) | Which decisions are legitimate exploration, and which conclusions need fresh evaluation? |
| The distinction between a utility update and model training | [PyTorch's autograd tutorial](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) | What would we have to change for learning to alter neural-network parameters? |

## Two small exercises worth doing

**Trace one scalar update.** Starting with `Q = 0.8`, apply
`Q <- Q + 0.3 * (reward - Q)` to rewards `0, 0, 1`. Then consider a memory
that is never retrieved after the environment changes: how many updates does
it receive? This separates adaptation per observation from adaptation per
elapsed episode. The arithmetic alone cannot predict the model's behavior.

**Read a complete evidence chain.** Once the derivative has a runnable episode,
follow its task input, candidate memories, selected memories, model request,
executed SQL, outcome, and utility update. Write down which facts the scorer
knows that the model does not. Then inspect a failure with the same care.

## Concrete places to inspect

- [The actual Q-update and checkpoint test](../../construct-memory-utility/tests/test_memory.py)
  checks numerical updates, retrieval order and isolation of sibling branches.
  Run it and follow the call into the vendored updater. The learned object here
  is a scalar in memory metadata; no neural-network weight is being trained.
- [The scorer and migration audit](../../construct-memory-utility/src/construct_memory_utility/audit.py)
  executes both the correct reference and deliberately wrong controls. Compare
  that with merely testing that a migration script produces different names.
- [The pilot protocol](../../construct-memory-utility/notes/PILOT_PROTOCOL.md)
  distinguishes a development history from independent histories for inference.
  Six dependent task attempts cannot substitute for six independent experiments.
- [The first stopped run and its amendment](../../construct-memory-utility/notes/PILOT_AMENDMENT_1.md)
  show how to preserve evidence while correcting an adapter. Inspect why the
  database failure does not count as a loss for the memory policy, while an
  empty actor answer remains visible as a benchmark output failure.
- [The recorded inference adapter](../../construct-memory-utility/src/construct_memory_utility/runtime.py)
  exposes exactly what enters the actor and writer endpoints. Trace a request,
  SQL action, outcome and Q update in a run's `events.jsonl`. Keep the oracle
  audit file separate when identifying what the participant could know.

## Cycle 2: tracing what was learned

| When you encounter this in the project | Read or inspect | A useful question to answer yourself |
| --- | --- | --- |
| [The M2 retained correction](cycles/002/M2_REVIEW.md#the-retained-object-is-a-supplied-correction) | [The mint](../../construct/harness/resident.py), especially `corrected_claim` and `mint_earned_record` | Which parts come from the agent's failure, the external source, and the programmer's decision rule? |
| [Construction versus application](cycles/002/QUESTION.md#separate-construction-from-application) | [ExpeL v3](https://arxiv.org/pdf/2308.10144v3), algorithms 1–3 | Which information is available while building memory, and which crosses into evaluation? |
| [The competing explanations](cycles/002/QUESTION.md#explanations-to-distinguish) | [LEAP v2](https://arxiv.org/pdf/2402.05403v2), §3 | Could a principle be useful even if every reasoning operation needed to apply it was available before the experience? |
| [Repeated performance](cycles/002/QUESTION.md#evidence-that-would-move-the-account) | [ERL v2](https://arxiv.org/pdf/2603.24639v2), Figure 3 | Why does solving a task in all three attempts differ from solving it at least once? What can neither tell us about unobserved attempts? |

For the last question, consider an idealized fixed success probability `p` with
independent attempts: success at least once in three attempts has probability
`1 - (1 - p)^3`, while success in all three has probability `p^3`. Work through
`p = 0.5` and `p = 0.8`. This is an illustration, not a model fitted to ERL;
real tasks have different probabilities and runs may share sources of variation.

## Cycle 2: inspecting the derivative

- Follow [one source experience through the simulator](../../construct-lesson-transfer/src/lesson_transfer/environment.py):
  compare `execute`, `reference_plan`, and `independent_valid`. The second
  validator uses an enumerated table instead of the execution function. Why
  would testing a function against itself provide weaker assurance?
- Read the [writer and actor prompts](../../construct-lesson-transfer/src/lesson_transfer/prompts.py)
  beside the [protocol](../../construct-lesson-transfer/notes/PROTOCOL.md).
  Identify which information is fixed across construction treatments and which
  information the raw-evidence and oracle controls receive. Equal output word
  limits do not imply equal tokenizer counts or total compute.
- Work through paired success: a policy that always uses one order might solve
  half of a two-member pair but never both. Then examine why four tasks and
  repeated calls using the same constructed memory still do not constitute
  independent samples of memory construction.
- Compare [CLIN's heating failure](https://arxiv.org/pdf/2310.10134v1), §4.3,
  with the derivative's fixed presentation of the entire memory. Which failure
  mechanisms did this experimental simplification remove, and which remain?
- The derivative's [prospective sample size](../../construct-lesson-transfer/notes/PROSPECTIVE_PROTOCOL.md#fresh-sample-and-precision)
  follows from a conservative bound on independent world differences. Substitute
  48, 192, and 768 for the sample size: quadrupling the number of independent
  worlds halves the interval radius. Why would quadrupling actor repeats within
  the same four worlds not justify that calculation? The original reference is
  [Hoeffding (1963)](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830).
