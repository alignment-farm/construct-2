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

Browse the [cycle index](notes/cycles/README.md) for the research trajectory.
Each cycle has a short README with its question, status, derivative, and latest
conclusion, followed by its proposals, reviews, and source inventories.

The [derivative working agreement](notes/DERIVATIVE_WORKING_AGREEMENT.md)
defines that ownership, when decisions return here, and how an agent reports
progress and completion. It includes four reusable templates and a
[Cycle 2 charter](notes/cycles/002/DERIVATIVE_CHARTER.md) applying them to the
existing handoff. Grok owns Cycle 1 under the user-approved
[C1-02 continuation envelope](notes/cycles/001/CONTINUATION_ENVELOPE.md),
following the [latest review](notes/cycles/001/WORKLOAD_REVIEW.md).
Preparation, protocol freezing, and execution within that envelope are assigned.
Cycle 2's assigned diagnostic attempt
has [returned with an instrument stop](notes/cycles/002/APPLICATION_REVIEW.md).
Further derivative assignments may use a different agent family or session.
The agreement's adoption notes record what the Cycle 1 return taught us about
assigning concrete scope and resources.

The current focus here is theory development and synthesis. The user directs empirical agents in derivative projects and brings their reports back. The [theory map](notes/THEORY_MAP.md) connects those returns to the larger questions: when experience remains applicable, where learning should reside, and how its influence can be corrected. A derivative may need substantial further work without becoming the center of this project's agenda. Progress here includes sharpening an explanation, finding a boundary condition, or retiring a claim across the accumulated evidence.

The current synthesis follows [Cycle 2: from a correction to a reusable lesson](notes/cycles/002/QUESTION.md), beginning with Construct M2 and related work on learning from experience. The [Cycle 1 pilot return](notes/cycles/001/PILOT.md) remains part of the evidence base while its derivative continues separately.

Cycle 2's [proposal](notes/cycles/002/PROPOSAL.md) narrows the comparison to
conditional lesson construction from fixed experience. Its code, protocols,
and evidence live in [construct-lesson-transfer](../construct-lesson-transfer/README.md).
The [Cycle 2 development return](notes/cycles/002/PILOT.md) explains why rule
application needed diagnosis before scaling the construction comparison.
The [application return](notes/cycles/002/APPLICATION_REVIEW.md) records seven
correct scored answers followed by HTTP 500 on the eighth attempt. The fixed
480-call comparison is incomplete; its evidence is preserved, and the larger
study remains parked while the root returns to synthesis.
Grok's [Cycle 1 workload return](notes/cycles/001/WORKLOAD_REVIEW.md) exercises
the revised writer and memory-conditioned actor on development tasks. Its
utility-reset question remains open. The user approved two further development
histories under C1-02; a larger confirmatory study remains unassigned.

Serious empirical work can include exploration. We should be free to discover that a task is unsuitable, a representation is unusable, or an unexpected behavior deserves attention. When we move to testing a claim developed during that exploration, we should specify the comparison and analysis in advance and use fresh evaluation material. Registered Reports offer a useful precedent for separating prospective tests from exploratory analyses while reporting both. [Center for Open Science](https://www.cos.io/initiatives/registered-reports)

**Failures should change the account of the research.** Each report should explain what happened, which explanations remain possible, and what would resolve the uncertainty. A broken scorer is evidence about the instrument. A treatment that reliably harms performance is evidence about the intervention under those conditions. An imprecise null leaves a different uncertainty. The previous Construct synthesis shows why these distinctions matter.

There is also a limit to celebrating failure: an uninterpretable experiment can teach us something about our methods while contributing little evidence about agent memory. We should record both its educational value and its scientific limits.
