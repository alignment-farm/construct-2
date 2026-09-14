# What is acquired when an agent learns a procedure?

The original predictive note below is preserved. A [subsequent assessment](#assessment-after-reading-diagnosis) records what changed after reading the diagnostic publication.

14 September 2026. Root theory note, written while procedure-transfer's acquisition diagnosis is underway. The local evidence boundary is its accepted first publication at commit `78965ca7ffd4ac9389a77505a768cf6dfd6be957` and the earlier studies assessed in the [study map](../studies/README.md#what-the-completed-investigations-change). We have not read the diagnostic phase's new results for this note. The predictions below precede that reading; they are theory commitments, not a registered experimental protocol or claims of independence from the study's existing brief.

**Working hypothesis:** a small parameter update can acquire a reusable decision about what to do before it reliably handles the arguments or composes the full action. Transfer should follow the relations that training makes stable across examples and the computations the model can execute. This predicts selective successes and failures under changes to inputs and rules. It also makes a stronger demand than recalling demonstrations: the learned relation must survive changes that should be irrelevant to it.

## Three accounts of apparent procedural learning

Consider the local routing task as a behavioral decomposition:

```text
call = render(route(condition), transform(identifier), modifier(condition))
```

This describes the task, not three proven modules inside the model. Its components can fail together, so their marginal accuracies cannot simply be multiplied to explain whole-call accuracy.

| Account | What the update makes available | Characteristic transfer pattern |
|---|---|---|
| Familiar-response learning | Associations between observed inputs, output fragments and templates | Good demonstration recall; errors track unfamiliar strings, formats or combinations. |
| Reusable decision learning | A condition-to-action relation that can operate on new arguments, potentially using existing capabilities | Correct choices survive irrelevant argument changes; argument processing may remain unreliable. |
| Compositional procedure learning | Operations and their coordination support new combinations or longer computations | Components remain usable when recombined; success extends beyond the specific strings and combinations practiced. |

These accounts can coexist in one adapter. Behavioral generalization supports a reusable procedure over the tested range; it does not by itself identify an internal algorithm or show that pretraining lacked the computation. A learned decision that invokes an existing capability still counts as useful acquisition. To claim acquisition of an operation, we also need a comparison with the base model's ability to perform that operation under a clear instruction.

The first procedure-transfer result already gives us something positive to explain. One imitation run chose the correct tool on **96/96** fresh inputs while correctly transforming **32/96** identifiers. The other run chose **72/96** tools correctly. That supports partial transfer and motivates the decision-learning account; it does not yet show routing invariant to wider input changes. The distillation runs mostly failed even their training calls, leaving their potential form of transfer unresolved. These are different scientific situations. [Accepted root assessment](../studies/README.md#procedure-transfer-completed-local-recipe-test).

## Successful demonstrations and what enabled them

The following are author-reported results, not local replications. They provide concrete mechanisms to investigate, with different preparation and persistence boundaries.

**Practice transferring relationships.** Lake and Baroni's meta-learning for compositionality trains transformers across many tasks with changing symbol meanings and queries that require composition. It reports under 1% error on systematic lexical generalization benchmarks, while failing the SCAN/COGS productivity splits. The test-time model has frozen weights and receives study examples in context: its learned skill is interpreting and recombining new bindings, rather than storing each test episode in weights. The relevant lesson is that training explicitly exercises the desired generalization; success on new bindings does not imply arbitrary new structures. [P19, published article, results and meta-training methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/).

**Expose the structure needed by a computation.** Abacus embeddings represent digit position within a number. Combined with recurrence and input injection, transformers trained from scratch on operands up to 20 digits reach up to 99% accuracy on 100-digit addition in the reported configuration. Training uses 20 million samples and digit-reversed inputs. This is substantial preparation for a specific operation, and an existence demonstration of length generalization. It motivates investigating representation, rather than inferring an inability to learn a computation from failure on a small dataset. It does not establish that changing Qwen's identifier format will repair our task. [P20, 2405.17399v1, §3](https://arxiv.org/html/2405.17399v1#S3).

**Learn how to prepare an effective update.** SEAL rewards self-edits using performance after adaptation. On eight evaluation ARC tasks selected to be solvable with an effective training configuration, 72.5% of sampled learned self-edits lead to success, versus 20% without the prior reinforcement learning. These percentages score five edit attempts per task, not independent tasks. The policy selects augmentations and training settings; its success demonstrates useful acquisition after purposeful preparation in a restricted task set. It supplies a positive comparison with an undeveloped update policy, without establishing general ARC competence. [P4, 2506.10943v2, §§3.2–4.1](https://arxiv.org/html/2506.10943v2).

**Train the write process for later use.** PERK meta-learns a LoRA initialization through context updates and subsequent question answering. On BabiLong two-hop reasoning at 64K tokens, its Qwen2.5-0.5B result is 62.5%, versus 26.3% for the fine-tuned in-context baseline with Yarn and DCA; both learned from 8K contexts. This is usable parametric context storage with task-directed preparation. It does not isolate acquisition of a new reasoning operation or settle our total-cost comparison. [P8, 2507.06415v3, §§3, 5.1 and Table 1](https://arxiv.org/html/2507.06415v3).

Our inference from these demonstrations is that **a learner's preparation is part of the mechanism under test**: which variations it practices, which structure its inputs expose, and whether its updates are trained to support later behavior. None supplies a reason to expect sixteen demonstrations and a shared optimizer recipe to inherit its results. Equally, none licenses dismissing that small-data setting before developing or diagnosing it. The [reading record](../sources/2026-09-14/README.md) identifies the inspected material and discovery limits.

## Predictions before the next findings

Our leading local expectation is reusable routing with weaker argument handling, rather than uniform failure to learn. The following contrasts would change that belief. The ancillary investigator owns their implementation and may find better ways to distinguish the accounts.

| Prediction | Expected pattern | What would weaken the explanation |
|---|---|---|
| **R1. Routing has learned an argument-independent relation.** Change identifiers while preserving routing conditions and an intelligible input format. | Routing survives new strings and length changes better than exact identifier transformation. | Routing errors track argument novelty as strongly as transformation errors, including where the base model can parse the inputs. That favors entangled response learning over the proposed separation. |
| **R2. Argument transformation is currently the larger bottleneck.** Compare operation performance separately and in fresh combinations within complete calls, with comparable acquisition opportunity. | Transformation remains harder than routing even in isolation; composition alone does not account for most of the deficit. | Both operations transfer well separately but fail mainly together. That redirects the explanation toward coordination or interference. If a clear base-model instruction already makes transformation reliable, difficulty acquiring access to that operation becomes more plausible than inability to execute it. |
| **R3. Repairing distillation's training-call acquisition will leave a transfer problem to explain.** Compare an acquisition-successful recipe on fresh inputs with the accepted failure. | Training recall improves much more than novel-argument performance; routing and transformation remain uneven. | A narrowly targeted acquisition repair also restores broad component transfer. That gives the acquisition failure greater explanatory weight and weakens our expectation of a separate transfer bottleneck. This prediction becomes assessable after a functioning recipe is found; continued acquisition failure instead calls for a causal diagnosis of that failure. |
| **R4. Stronger conjecture: reusable routing is selectively editable.** Later, revise one routing relation after establishing it, while keeping argument operations fixed. | The correction applies across new identifiers in its scope and preserves other routing relations and transformations. | Changes remain tied to corrected examples, or spread into unaffected operations. That weakens selective editability; it does not undo evidence for the initial transfer. |

These are qualitative forecasts, not numerical effect estimates. R1–R3 address the active question; R4 is a future question under S2, not a new assignment. Reusable behavior alone does not establish independently editable parameters. Withheld combinations also need evidence that identifies the intended composition within the stated task family; otherwise failure can reflect an ambiguous rule. A changed training set, teacher, budget or interface may improve the combined method without isolating a cause. For example, making both isolated operations work and then selectively disrupting their composition would teach us more than another undiagnosed low full-call score.

## What this changes at the root

The unit of accumulated experience can be a **learned relation within a procedure**, rather than an entire successful task. If routing is acquired robustly, its retention and scoped revision become meaningful questions even while string transformation remains imperfect. That would support a bounded claim about retained decisions; an economic claim about complete calls would still require complete-call quality and the costs of the remaining computation. We need not wait for a flawless general learner to study what it has actually learned.

The same distinction sharpens S4: information never acquired usefully cannot later be classified as forgotten under a changed goal. For S5, measure acquisition, reuse and correction costs for the behavior the system actually supplies, against accessible evidence at comparable useful quality. Retained examples remain an essential reference; they do not substitute for understanding a trainable mechanism.

The next root synthesis should revisit R1–R3 explicitly, preserving their original wording when contradicted and revising the explanation. The desired progress is an account of how a useful relation or operation was acquired, or an intervention that identifies why acquisition failed. A publication's acceptability alone does not answer that question.

## Assessment after reading diagnosis

14 September 2026, after the original note. [DIAGNOSIS.md](../../ancillary-studies/procedure-transfer/DIAGNOSIS.md), publication `dcdc0d6f54dde235549f8abfba407598b6635667`, provides new development and intervention evidence. The [root assessment](../studies/README.md#procedure-transfer-acquisition-diagnosis) records its scope and independent checks. The predictions above remain unchanged.

| Original prediction | Assessment against the diagnosis |
|---|---|
| **R1: routing survives argument changes better than transformation** | Supported within these probes. Both selected students route 48/48 calls correctly across twelve new random identifiers of lengths 4, 6, 8 and 10; complete-call/identifier scores are 28/48 for imitation and 17/48 for forward KL. These are clustered development cases, not a general invariance claim. |
| **R2: transformation remains the larger bottleneck in isolation** | Partly addressed. Supplying correct routing leaves identifier errors; supplying routing and the correct uppercase identifier enables every suffix/closing completion. This excludes wrong routing as a sufficient explanation. It does not test separately trained transformation or fully distinguish copying, casing, tokenization and coordination. We should not count R2 as fully tested. |
| **R3: acquisition repair leaves a transfer deficit** | Supported in the diagnostic setting. Forward KL reaches 16/16 training recall while the selected checkpoint completes 17/48 random-identifier calls. A separate controlled switch from failed reverse weights repairs routing but leaves five training-call suffix failures. The developed acquisition result does not establish a forward-KL transfer advantage. |
| **R4: reusable routing is selectively editable** | Untested. Preserving training recall through further same-task reverse-KL updates is neither scoped correction nor retention under unrelated learning. |

The strongest new explanation concerns the interaction between the objective and the learner's starting policy. From identical failed parameters, a loss-orientation intervention repairs routing; reverse KL also preserves training recall when started from an acquired imitation policy. The saved first-position distributions identify weak reverse correction signals for strongly suppressed correct tokens, including in the original failed adapters. This explains part of a local learning failure without making the same claim about every reverse-KL learner or identifying a shared cause with S3.

Our behavioral account becomes more specific. The learners acquired routing that works on unfamiliar arguments, and suffix use is available conditional on a correct preceding answer. Most identifier mistakes observed in the root's additional descriptive inspection already used uppercase letters: 18 of imitation's 20 wrong identifiers and all 31 of forward's wrong identifiers contained no lowercase letters. For example, both produced `NOD` for `noud` in some calls. This inspection of the saved [component responses](../../ancillary-studies/procedure-transfer/evidence/diagnosis-v2-components/responses.jsonl) is post hoc; it motivates separating faithful string production from case conversion rather than asserting a newly learned uppercase algorithm.

The next empirical directions are concurrent. S2 studies maintenance and revision of acquired behavior; S4 tests how anticipated future use shapes memory; S1 investigates useful source selection and abstention. Their [independent briefs](../studies/README.md#6-research-selection) carry the questions forward without making the remaining identifier problem a prerequisite for all research on accumulated experience.
