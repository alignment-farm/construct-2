Retrieved 10 September 2026.

`arxiv-query.xml` is the unmodified Atom response from one HTTPS GET to:

```text
https://export.arxiv.org/api/query?id_list=2405.15793,2303.11366,2305.16291,2510.04618,2501.00663,2607.03441,2501.12948,2408.03314,2506.02153,2512.04123,2406.13352&max_results=11
```

User-Agent: `Construct-2 literature review (local research; arXiv metadata cache)`.
The response contains all 11 requested records, with versioned identifiers,
titles, authors, dates, abstracts, and paper links. It preserves the metadata
read without requiring another API request. Paper PDFs and source archives
were not downloaded in this pass.

The review also used browser retrieval of these primary pages:

- https://cursor.com/blog/self-summarization
- https://metr.org/notes/2026-01-22-time-horizon-limitations/
- https://distill.pub/2017/research-debt/
- https://www.cos.io/initiatives/registered-reports
- https://arxiv.org/abs/2607.03441
- https://arxiv.org/abs/2512.04123
- https://arxiv.org/html/2512.04123v4#S5.SS2

These browser responses are not archived here. The dated review preserves
paraphrased reading notes and links, rather than a reproducible snapshot of
the unversioned web essays.

---

## Abstract and source-summary review

This review covers the 11 distinct arXiv papers linked in [Perspectives](../../notes/RESEARCH_PERSPECTIVES.md). The [Construct synthesis](../../notes/PREVIOUS_RESEARCH.md) supplies the local evidence. The [ancillary-study manuscript](../../notes/ANCILLARY_STUDY.md) supplies organizational context. arXiv access and submission documentation are operational references, outside this scientific reading list.

All 11 paper abstracts and their metadata were retrieved together through the arXiv query API. The exact response is [cached here](arxiv-query.xml); versioned links below identify the abstract records reviewed. Paper bodies, code, and experimental artifacts have not been systematically reviewed. The production paper's linked weight-tuning section received an additional targeted check. Web essays were read at their linked URLs on this date; they have no arXiv version identifier.

The summaries below report authors' claims. The limitations and questions are our assessment of what this reading establishes. Abstract-level review can identify overlap and useful questions, but cannot establish that a question is unanswered across the literature.

## Papers

### L1. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

[2405.15793v3](https://arxiv.org/abs/2405.15793v3) · Empirical system paper

**Abstract:** An interface designed for language-model agents supports repository navigation, editing, and execution. The authors report improvements on software-repair benchmarks and examine how interface design affects behavior.

**Assessment:** This makes the model–interface combination a relevant unit of comparison. It does not, by itself, demonstrate persistent learning or isolate a memory mechanism. Later methods reading should examine which interface changes receive controlled comparisons.

**Question:** How much apparent memory improvement comes from making already available information easier to access and act on? Connects to T1 and T7.

### L2. Reflexion: Language Agents with Verbal Reinforcement Learning

[2303.11366v4](https://arxiv.org/abs/2303.11366v4) · Empirical memory framework

**Abstract:** Agents turn feedback into textual reflections retained in an episodic buffer, improving later trials without updating model weights. The paper reports results across decision-making, coding, and reasoning, with feedback and agent ablations.

**Assessment:** Retaining feedback in text is established prior art for our agenda. Improvement on subsequent trials does not automatically show transfer to a different task; the task and retry boundaries need inspection before interpreting reported benchmark scores.

**Question:** What distinguishes a reusable lesson from advice that helps repeat the same problem? Connects to T2 and T5.

### L3. Voyager: An Open-Ended Embodied Agent with Large Language Models

[2305.16291v2](https://arxiv.org/abs/2305.16291v2) · Empirical embodied-agent system

**Abstract:** Voyager combines an automatic curriculum, an executable skill library, and iterative feedback. The authors report improved Minecraft exploration and reuse of learned skills in a new world through black-box GPT-4 calls.

**Assessment:** Persistent competence can include executable artifacts. The system combines several mechanisms, so its overall gains cannot simply be assigned to the storage medium. Transfer within Minecraft also has a narrower scope than transfer across environments with different semantics.

**Question:** When does code preserve a procedure more reliably than a textual lesson, and what happens when the environment changes? Connects to T2, T3, and T7.

### L4. Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

[2510.04618v3](https://arxiv.org/abs/2510.04618v3) · Empirical context-adaptation framework

**Abstract:** ACE maintains contextual playbooks through generation, reflection, and curation. Structured incremental updates aim to avoid information loss from repeated rewriting. The authors report agent and domain-specific benchmark gains and lower adaptation costs.

**Assessment:** Evolving contextual lessons and preserving details are already studied. The abstract does not settle long-run growth, correction of obsolete entries, or which component causes each gain. Those require methods and ablation review.

**Question:** How should useful detail survive while obsolete, redundant, and misleading material loses influence? Connects to T1, T4, and T5.

### L5. Titans: Learning to Memorize at Test Time

[2501.00663v1](https://arxiv.org/abs/2501.00663v1) · Neural architecture paper

**Abstract:** A learned neural memory module complements attention with retained historical information. The authors compare architectural variants on several sequence tasks and report strong long-context retrieval results.

**Assessment:** This expands the available memory mechanisms, but a neural memory module is not equivalent to an explicit agent record store or a deployed base-model adapter. Sequence retention does not establish correction of individual facts, source attribution, or cross-session agent learning.

**Question:** Which properties of explicit memory survive a move into neural state, and which become difficult to inspect or revise? Connects to T3 and T5.

### L6. No Time Like the Present: Agentic Test-Time Training for LLM Agents

[2607.03441v1](https://arxiv.org/abs/2607.03441v1) · Empirical online-adaptation method

**Abstract:** Continuous updates during agent episodes can help with new trajectory information and amplify drift when training text repeats. aTTT downweights repeated token sequences. The authors report gains on ALFWorld and SWE-bench Lite, with benefits concentrated where models already possess task competence.

**Assessment:** The authors themselves distinguish preserving existing competence from acquiring new abilities. Persistence after the episode, transfer, and response to contradictory evidence remain questions for this review. Repetition control is not inherently an external correctness check.

**Question:** Does an update improve later independent work, or mainly keep the current episode on course? Connects to T2 and T5.

### L7. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

[2501.12948v2](https://arxiv.org/abs/2501.12948v2) · Empirical training paper

**Abstract:** Reinforcement learning develops reasoning behavior on verifiable tasks; the authors also describe using larger models' reasoning to improve smaller models.

**Assessment:** Training and transfer into smaller models belong in the comparison space. This does not establish that ordinary agent transcripts, without equivalent outcome signals and selection, make useful training data. Training provenance and evaluation scope matter.

**Question:** Which recurring lessons justify consolidation into weights, and what evidence should qualify their training examples? Connects to T3 and T5.

### L8. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

[2408.03314v1](https://arxiv.org/abs/2408.03314v1) · Empirical compute-allocation paper

**Abstract:** The usefulness of additional inference computation varies with problem difficulty. Adaptive allocation improves efficiency over a best-of-N baseline; under some FLOPs-matched conditions a smaller model outperforms a much larger one.

**Assessment:** Additional computation is a necessary competing explanation and alternative investment when assessing memory. The result is conditional on the evaluated tasks and methods, and does not establish agent-level operating costs.

**Question:** Does memory offer better outcomes than spending an equivalent budget on reasoning, search, or verification? Connects to T6.

### L9. Small Language Models are the Future of Agentic AI

[2506.02153v2](https://arxiv.org/abs/2506.02153v2) · Position paper

**Abstract:** The authors argue that small models suit many repetitive agent operations, propose heterogeneous systems where broader abilities are needed, and outline conversion from larger models to specialists.

**Assessment:** This supplies a specialization hypothesis and design motivation. It is not a controlled demonstration that specialists minimize total cost on our workloads.

**Question:** At what recurrence and error rate does specialization repay acquisition, routing, verification, and maintenance costs? Connects to T3 and T6.

### L10. Measuring Agents in Production

[2512.04123v4](https://arxiv.org/abs/2512.04123v4) · Observational interviews and survey; [weight-tuning section](https://arxiv.org/html/2512.04123v4#S5.SS2)

**Abstract:** The study combines 20 case studies with a survey of 86 deployed-system practitioners across 26 domains. It reports widespread use of simple, controllable designs and identifies reliability as a central challenge.

**Assessment:** Deployment choices help identify practical constraints. They do not establish which architecture would win a controlled comparison. Preserve the distinction between interview and survey denominators when repeating specific percentages; the existing perspective's weight-tuning claim concerns the interview sample.

**Question:** Which laboratory memory gains survive human intervention, model upgrades, and maintenance in ongoing work? Connects to T6 and T7.

### L11. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

[2406.13352v3](https://arxiv.org/abs/2406.13352v3) · Empirical evaluation framework

**Abstract:** AgentDojo evaluates tool-using agents exposed to untrusted data, with both ordinary tasks and adversarial cases. The authors report task failures without attacks as well as security failures under attacks.

**Assessment:** Authorized-task performance and resistance to redirection require separate measurements. The abstract does not establish protection of persistent memory admission, withholding, or later reuse; memory-specific overlap requires closer reading.

**Question:** Can an agent learn from an untrusted source without allowing that source to determine its own authority? Connects to T8.

## Research and methods essays

### L12. Training Composer for longer horizons

[Cursor, 17 March 2026](https://cursor.com/blog/self-summarization) · Developer report

Summaries participate in training trajectories and receive the eventual task reward. Cursor reports shorter summaries and better internal benchmark results than its prompted-compaction baseline. This is concrete evidence of training a policy that operates through an external memory mechanism, with the limits of a developer's own evaluation.

**Question:** Does a trained summary preserve information valuable for later changes of direction, beyond what predicts the current task reward? Connects to T4 and T7.

### L13. Clarifying limitations of time horizon

[METR, 22 January 2026](https://metr.org/notes/2026-01-22-time-horizon-limitations/) · Author's methodological clarification

The note distinguishes human task duration at a specified success rate from autonomous operating time, and discusses uncertainty, domain dependence, and task-distribution limitations.

**Question:** Which direct measures would show continuity across interruptions and changes of state? A time-horizon headline cannot substitute for those observations. Connects to T7 and T9.

### L14. Research Debt

[Olah and Carter, 2017](https://distill.pub/2017/research-debt/) · Research-method essay

The authors argue that explanation, synthesis, and improved abstractions reduce the effort required to understand and build on research. This motivates the root project's educational work; it does not validate a particular memory architecture or research organization.

**Question:** Can we explain each proposed mechanism with a small example that reveals its causal assumption? Connects to T9.

### L15. Registered Reports

[Center for Open Science](https://www.cos.io/initiatives/registered-reports) · Publishing-method guidance, accessed 10 September 2026

The format reviews questions, methods, and proposed analyses before data collection and allows exploratory findings to be reported. It offers a precedent for separating discovery from prospective claim testing. Reading this guidance does not independently establish the size of its benefits or make journal procedures local requirements.

**Question:** How do we preserve freedom to discover while keeping later tests independent of the observations that shaped a claim? Connects to T9.
