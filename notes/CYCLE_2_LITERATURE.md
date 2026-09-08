# Cycle 2: correction, reflection, and transfer

2026-09-08 · Targeted primary-source review, not a systematic review or a
reproduction of published results. Exact versions and inspection coverage are
recorded in the [source manifest](CYCLE_2_SOURCES.json).

The search began with M2 and Reflexion, then followed work on experiential
learning, cross-task memory, principle extraction, and contextual guidelines.
Additional searches covered agent memory and transfer in 2026, learning from
one's own experience, and in-context learning versus eliciting prior knowledge.
Paper selection favors comparisons that help distinguish explanations, rather
than benchmark rank. The review did not audit the author implementations.

## Closest mechanisms and their evidence boundaries

| Work and inspected sections | What changes and what is evaluated | Implication for this cycle |
| --- | --- | --- |
| [Reflexion, 2303.11366v4](https://arxiv.org/pdf/2303.11366v4), §§3–4 | A model generates reflections from trajectories and feedback for subsequent attempts. Feedback sources differ across tasks, including external grading and model evaluation. | Closest foundational comparison to M2's supplied correction. Success on retries does not by itself establish transfer to a different problem. |
| [ExpeL, 2308.10144v3](https://arxiv.org/pdf/2308.10144v3), §§4–5 and algorithms | Training-task experiences produce insights and retrievable successful examples; evaluation uses unseen tasks. The study separates insights from example retrieval and includes handcrafted-insight controls. | Generic advice is already a studied baseline. Its HotpotQA-to-FEVER transfer adapts insights using target-task demonstrations and retains the shared search interface; account for that assistance. More elaborate reflection is not uniformly helpful in its ablations. |
| [CLIN, 2310.10134v1](https://arxiv.org/pdf/2310.10134v1), §§3.2–4.3 | Textual action-condition abstractions and meta-memory support retries, new environments, and related new tasks in ScienceWorld. The paper compares structured memory with free-form advice. | New-task success can partly reuse a location fact. Its controller also improves the memory-free baseline, so the whole-system comparison cannot assign all gains to memory. An inspected failure selects an unsuitable heating rule despite an alternative being stored. |
| [LEAP, 2402.05403v2](https://arxiv.org/pdf/2402.05403v2), §3 and principle-generation prompt | Incorrect solutions to supplied examples are compared with their provided correct outputs; extracted principles accompany the original examples on unseen questions. | Direct precedent for turning a correction into a reusable instruction. It uses supplied correct examples and extra generation, although it requires no additional examples beyond its few-shot baseline. “No additional examples” does not mean no supervision or no additional compute. |
| [AutoGuide, 2403.08978v2](https://arxiv.org/pdf/2403.08978v2), §§3–4 | Contrasting offline trajectories yield guidelines associated with contexts; the agent identifies its current context and selects guidance while acting. The study includes applicability and generalization analyses. | Context-conditional lessons are established prior work. Its cross-environment transfer adds a grounding module, so assistance in applying the lesson also matters. A contribution here must go beyond attaching conditions to instructions. |
| [Agent Workflow Memory, 2409.07429v1](https://arxiv.org/pdf/2409.07429v1), §2.3 and generalization setup in §3 | Offline induction uses training experiences; online induction adds workflows from trajectories judged successful. The settings differ in when memory is acquired and which experience is available. | Workflow reuse belongs in the comparison alongside reflections. Separate fixed-memory transfer from adaptation during an evaluation stream. |
| [ReasoningBank, 2509.25140v2](https://arxiv.org/pdf/2509.25140v2), §§3 and 5 | An LLM judge labels trajectories, from which reasoning memories are extracted for later tasks. A failure-inclusion ablation compares success-only memory with memory drawn from both outcomes. | Prior work already addresses learning from failure and abstract strategies. Self-judged labels are a different information source from M2's checked external correction; compare those regimes explicitly. |
| [ERL, 2603.24639v2](https://arxiv.org/pdf/2603.24639v2), §§2–3, Figure 3, appendices C and E | Single-attempt trajectories plus binary outcomes generate heuristics. Evaluation holds out data universes while keeping applications and tools. Comparisons cover raw trajectories, retrieval, outcome feedback, and repeated performance. | Figure 3 shows larger gains in succeeding on all three runs than in succeeding at least once. Appendix E also reports better source-task performance but worse held-out performance after iterative acquisition. These are clues about reliability and acquisition bias, not proof of their causes. |

CLIN and ERL are especially useful next readings because they expose different
ways an apparent learning gain can arise or fail. ExpeL and LEAP help specify
the construction comparison; AutoGuide establishes substantial overlap with
the theory map's applicability conjecture.

## Broader work that constrains our interpretation

**In-context performance can draw on both prior knowledge and supplied
relationships.** [Min et al., 2202.12837v2](https://arxiv.org/pdf/2202.12837v2)
find that demonstration format and label/input distributions explain much of
the gain on their classification and multiple-choice setups, even with
randomized labels. [Wei et al., 2303.03846v2](https://arxiv.org/pdf/2303.03846v2)
show that sufficiently large tested models can instead follow flipped or
semantically unrelated label mappings. These papers' introductions and setups
were inspected. Neither supports a universal claim that context only elicits
existing answers, nor directly settles procedural learning by agents.

**Feedback is an intervention.**
[Huang et al., 2310.01798v2](https://arxiv.org/pdf/2310.01798v2), introduction
and problem definition, distinguish intrinsic self-correction from correction
supported by external information. Their negative results concern the tested
models and reasoning setups without external feedback. They motivate recording
who supplies the correction and what it reveals, not a timeless prohibition
on self-correction.

**A memory history is a source of variation.**
[On the Fragility of Self-Improving Agents, 2608.18066v1](https://arxiv.org/pdf/2608.18066v1),
introduction and evaluation setup, re-evaluates AWM and ReasoningBank across
runs and task orders. Unlike the original methods' model judges, its main
memory construction receives ground-truth rewards. It reports sensitivity to
order and incomplete task or environment specifications. This strengthens the case for examining acquired
histories and failure conditions rather than interpreting one evolving bank
as a general learning curve.

**Comparing persistence mechanisms is already an active empirical program.**
[S3Gym, 2608.31100v1](https://arxiv.org/pdf/2608.31100v1), introduction and
§4, separates exploration from stricter held-out evaluation across seven text
games and compares history, summaries, and parameter training. Its main setup
keeps verifier scores outside the agent's exploration inputs. This is a close,
recent neighbor of our placement question. The follow-up inspected §§4.4–4.5:
exploration and evaluation use disjoint seeds, and evaluation trajectories do
not enter subsequent history, summaries, or training. The training implementation
and all result tables remain unaudited. The [derivative proposal](CYCLE_2_PROPOSAL.md)
explains why this cycle isolates supervised text construction first.

ACE v3 was located and cached during discovery but was not substantively
reviewed in this pass. Cycle 1's review of v2 remains a separate source record.

## What this changes in the theory

The broad proposals to learn from failure, extract reusable principles, attach
conditions to lessons, or compare text memory with weights are occupied.
This review establishes relevant overlap; it does not establish that any
particular controlled comparison is absent from the literature.

The useful synthesis is to separate three questions:

1. **Construction:** Does processing experience produce better usable guidance
   than retaining its evidence or using an independently prepared strategy?
2. **Application:** Does the guidance supply a specific answer, convey a
   reusable relation, or help the agent execute a familiar operation reliably?
3. **Scope:** Does the benefit survive a relevant change and disappear or
   reverse appropriately when the guidance no longer applies?

These mechanisms can coexist. A model can use a pretrained ability to interpret
a newly acquired rule, and a rule can both enable a solution and reduce errors.
The [Cycle 2 question](CYCLE_2_QUESTION.md) makes those distinctions operational
without claiming access to the model's complete latent repertoire.
