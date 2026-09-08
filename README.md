Construct-2 is a **research apprenticeship organized around live scientific questions**. Each cycle should produce two things: a clearer understanding of how to do research, and an evidence-based change in what we believe about agents.

The root project maintains a connected account of the research:

| Component | What it teaches | What it produces |
|---|---|---|
| Explanations | How weights, context, retrieval, training, and harnesses work | Understandable accounts with small worked examples |
| Literature investigations | How to read papers critically and locate an unanswered question | Comparisons of claims, methods, evidence, and limitations |
| Theory development | How to turn an intuition into competing explanations | Predictions, assumptions, and observations that would distinguish them |
| Experiment proposals | How to design an informative comparison | A concrete question and design for a derivative |
| Evidence synthesis | How to update beliefs after results arrive | Revised theories, bounded conclusions, and unresolved questions |

Educational material should emerge from the work. When a proposed experiment depends on understanding gradients, explain gradients and inspect a small weight update. When a result depends on retrieval, trace exactly which information reached the model. When a comparison appears convincing, examine what else could explain it. This emphasis on making understanding reusable echoes Olah and Carter’s argument for reducing “research debt” through explanation and synthesis. [Research Debt](https://distill.pub/2017/research-debt/) Ensure the program includes direct contact with all three:

- **Weights:** inspect and change a small model’s parameters, then measure what persists and transfers.
- **Harnesses:** trace and manipulate the context, tools, state, and recovery mechanisms surrounding a model.
- **Research method:** reproduce a result, challenge its explanation, and design a comparison that could change our minds.

**The unit of progress would be a complete research cycle.** For example:

1. Encounter a phenomenon or puzzling result.
2. Read the closest existing work and reproduce something small enough to understand.
3. Develop competing explanations and identify their different predictions.
4. Run a bounded investigation in a derivative.
5. Return the evidence here and explain what changed—including changes to the question itself.

A derivative would own its code, data, configurations, raw outputs, analysis, and experimental report. The root would explain how its findings affect the larger inquiry. That division keeps the evidence close to the machinery that produced it while allowing theories to develop across several experiments.

The current focus here is theory development and synthesis. The user directs empirical agents in derivative projects and brings their reports back. The [theory map](notes/THEORY_MAP.md) connects those returns to the larger questions: when experience remains applicable, where learning should reside, and how its influence can be corrected. A derivative may need substantial further work without becoming the center of this project's agenda. Progress here includes sharpening an explanation, finding a boundary condition, or retiring a claim across the accumulated evidence.

The active inquiry is [Cycle 2: from a correction to a reusable lesson](notes/CYCLE_2_QUESTION.md), beginning with Construct M2 and related work on learning from experience. The [Cycle 1 pilot return](notes/CYCLE_1_PILOT.md) remains part of the evidence base while its derivative continues separately.

Serious empirical work can include exploration. We should be free to discover that a task is unsuitable, a representation is unusable, or an unexpected behavior deserves attention. When we move to testing a claim developed during that exploration, we should specify the comparison and analysis in advance and use fresh evaluation material. Registered Reports offer a useful precedent for separating prospective tests from exploratory analyses while reporting both. [Center for Open Science](https://www.cos.io/initiatives/registered-reports)

**Failures should change the account of the research.** Each report should explain what happened, which explanations remain possible, and what would resolve the uncertainty. A broken scorer is evidence about the instrument. A treatment that reliably harms performance is evidence about the intervention under those conditions. An imprecise null leaves a different uncertainty. The previous Construct synthesis shows why these distinctions matter.

There is also a limit to celebrating failure: an uninterpretable experiment can teach us something about our methods while contributing little evidence about agent memory. We should record both its educational value and its scientific limits.
