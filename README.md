The research direction is:

> how agents can accumulate useful experience across sessions, and where that experience should live: explicit memory, contextual lessons, executable tools, model weights, or runtime rules.

The task is to read the [previous research](notes/PREVIOUS_RESEARCH.md), [perspectives](notes/RESEARCH_PERSPECTIVES.md) and then put concepts from those files into contact through comparable tests.

The [source guide](sources/README.md) links the literature review, and the [study map](studies/README.md) connects mechanisms, evidence, and candidate questions. Its [worked examples](studies/README.md#b0-a-worked-explanation-of-neural-writes-reads-and-resets) explain neural writes, reads, and resets. The [ancillary-study approach](notes/ANCILLARY_STUDY.md) describes how independent studies inform the root's theory and synthesis.

Contributors can use the [repository list](studies/repos.txt) and [clone instructions](studies/README.md#cloning-the-studies) to retrieve all ancillary studies or select them by name.

Current work prioritizes neural memory, live weight updates, and learned memory policies. Four ancillary projects have published bounded contributions. Update-source selection established reproducible local adapter updates without a task-success advantage in its final full-context comparison. Procedure acquisition and reuse found that its tested adapter transferred less reliably than retained examples and did not demonstrate acquisition-cost repayment at comparable useful accuracy. [Neural memory depth](../ancillary-studies/neural-memory-depth/FINDINGS.md) found that interactions among initial representations and training streams strongly affect whether a tiny deeper memory learns full or partial recall. Correcting a verified derivative omission and increasing gradient-refresh frequency did not provide a uniform remedy; the differing published depth trends in Titans and Modular TTT remain unexplained.

[Procedure transfer](../ancillary-studies/procedure-transfer/FINDINGS.md) first found poor distillation acquisition and partial transfer through imitation. Its subsequent [diagnosis](../ancillary-studies/procedure-transfer/DIAGNOSIS.md) establishes a working forward-KL acquisition checkpoint and a controlled repair of failed routing from identical weights. Both selected learners route all 48 new development calls correctly, while identifier production remains unreliable. These diagnostic results explain part of the original failure without establishing a forward-KL transfer advantage. The [root assessment](studies/README.md#procedure-transfer-acquisition-diagnosis) records the evidence, checks and limits.

The [root synthesis](studies/README.md#what-the-completed-investigations-change) distinguishes useful evidence, successful acquisition, transfer, and the capacity a training procedure learns to use. Retention through later learning, scoped correction, and acquisition-cost repayment need separate evidence. Repeated failures of limited neural recipes do not establish that explicit memory is generally superior.

Three independent ancillary projects are now [commissioned for concurrent investigation](studies/README.md#6-research-selection). Their directories are prepared for fresh ancillary sessions; experiments were not started during preparation.

| Project | Experimental question |
|---|---|
| [Procedure retention and revision — S2](../ancillary-studies/procedure-retention-and-revision/README.md) | Can acquired behavior survive later learning and accept a scoped revision? |
| [Memory under goal shift — S4](../ancillary-studies/memory-under-goal-shift/README.md) | What does learned memory lose when its later use differs from what training anticipated? |
| [Experience selection and abstention — S1](../ancillary-studies/experience-selection/README.md) | Which experiences yield useful updates, and when should an agent refrain from updating? |

Each investigator owns its methods, workload discovery and bounded experiments, independently of the other projects' future results. The root develops predictions and synthesizes what the publications imply for accumulating experience. S5's acquisition, reuse and revision costs remain relevant across the experiments. A negative first recipe calls for purposeful diagnosis, not immediate retirement of the question.

The [procedural-learning note](notes/PROCEDURAL_LEARNING.md) preserves predictions written before reading the diagnosis and adds their [assessment](notes/PROCEDURAL_LEARNING.md#assessment-after-reading-diagnosis). Transferred routing supplies a concrete learned behavior for S2 while S4 broadens the mechanisms and workloads studied. The remaining identifier problem does not block either independent direction.
