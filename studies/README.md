**Much of the original question list is already background knowledge or an active research topic.** This revision separates that background from narrower questions that could justify ancillary work. It builds on the [Construct synthesis](../notes/PREVIOUS_RESEARCH.md) and [research perspective](../notes/RESEARCH_PERSPECTIVES.md), with priority given to neural memory, live weight updates, and learned memory policies. The [17 September executable-experience selection](../notes/EXECUTABLE_EXPERIENCE.md) opens a focused allocation comparison alongside the neural-learning emphasis; the [historical preference](../sources/README.md#research-preference-to-date) remains recorded.

**Independent commission — 17 September:**
[Executable experience retention](https://github.com/alignment-farm/executable-experience-retention)
([local brief](../../ancillary-studies/executable-experience-retention/README.md))
is prepared and commissioned for bounded investigation. It follows the
[persistence comparison](../notes/EXECUTABLE_COMPARISON.md) and completed
[artifact review](2026-09-17-executable-feasibility.md). The investigator owns
workload development and execution; preparation starts neither a session nor
model runs. [EX1–EX3](../notes/EXECUTABLE_EXPERIENCE.md) remain prospective.

**Current work — 17 September 2026:** Ten ancillary projects have published
accepted bounded contributions; the eleventh is prepared without findings.
The [latest assessment](2026-09-17-evidence-use-findings.md)
accepts evidence-use-under-revision at `da1233fdfb26fe6c5daa337a3dbf9f784f34f9f7`:
one checkpoint's modest transfer survives two corrections and has a favorable
measured cost against an uncached lesson. Further acquisition regresses; the
supplied executable is complete. EU1–EU3 are assessed in the
[selection note](../notes/EVIDENCE_USE.md#assessment-after-publication--17-september).
No continuation is commissioned. The independent executable-experience review
is complete; the fixed directive and AD1–AD3 remain intact.


This map connects the root's questions, ancillary publications and current research directions. Ten projects have published bounded contributions. The [third-phase maintenance assessment](2026-09-15-maintenance-findings.md) accepts the latest S1/S2/S4 publications and evaluates the preserved [M1–M3 expectations](../notes/LEARNING_MAINTENANCE.md#prospective-expectations). Complete procedural behavior and later compositional use are now demonstrated in controlled settings; reliable maintenance and economical placement remain open. The [synthesis below](#what-the-completed-investigations-change) connects these findings, and [research selection](#6-research-selection) distinguishes recommended directions from commissioned work. Read each study's directory for its latest evidence. A useful replication or explanation need not claim novelty; any proposed new contribution needs its closest methods and evaluation settings checked.

## Cloning the studies

[repos.txt](repos.txt) is the maintained list of Construct-2 ancillary repositories,
one `organization/repository` per line, including completed studies. It contains
all eleven studies currently in this program, including the newly prepared
executable-experience-retention study and the ten completed projects. The root
and other lab projects are outside its scope. Contributors need Git, an
authenticated GitHub CLI (`gh auth login`), and access to these private repositories.

From a `construct-2` checkout:

```bash
# Show the repository list without contacting GitHub.
./scripts/clone-studies.sh --list

# Clone all studies.
./scripts/clone-studies.sh

# Clone only named studies.
./scripts/clone-studies.sh procedure-retention-and-revision memory-under-goal-shift
```

The [helper](../scripts/clone-studies.sh) clones into `../ancillary-studies/`
relative to the root checkout, preserving this documentation's sibling links.
It also accepts qualified names such as `alignment-farm/experience-selection`.
It validates all requested names before cloning and skips existing paths without
pulling or changing local work. A failed clone stops the command with a nonzero
exit status; rerunning skips already-created paths. The plain-text list is also
usable by contributors' own Git tooling. Committed study artifacts are included;
base-model downloads and environment setup follow each study's reproduction notes.

Add each new repository to the list as part of the
[new-study process](../notes/ANCILLARY_STUDY.md#starting-an-ancillary-study).
Scientific questions and assessments remain in the map below.

## 1. What changed after reading beyond the abstracts

Three important corrections to our starting position:

- Testing behavior after context removal is already an explicit research agenda, with diagnostic experiments, in **Beyond Perplexity** (P5). We should use and critique that work rather than invent another general memory-evaluation framework.
- Neural knowledge acquisition, retention through later updates, and propagation of edits are already studied in **SEAL, MEMORYLLM, WISE, and MQuAKE** (P4, P6, P7, P9). “Can neural memory retain or correct information?” is too broad to serve as our contribution.
- Training a memory mechanism for useful future computation is already central to **TTT layers, PERK, and TTCD** (P1, P8, P11), as well as trained textual summarization. The interesting questions concern conditions and failures of those objectives.

The different depth results in **Titans and Modular TTT** (P2, P12) motivated S3. Its completed investigation narrows the configuration comparison and establishes conditional training failures in a synthetic memory task. It leaves the cause of the published contrast unresolved; see the [root assessment](#s3-when-does-deeper-neural-memory-repay-its-harder-update-problem).

## 2. Mechanisms to understand first

“Neural memory” and “weight updates” overlap. A better vocabulary identifies the mutable object, the write operation, and the boundary across which it persists.

| Mechanism | What changes during use? | What we must distinguish |
|---|---|---|
| Explicit lessons or summaries | Text supplied to later model calls | Better context versus a change in model parameters; examples: Reflexion, ACE, Composer |
| Learned latent memory | Hidden vectors in a memory pool | A neural write can use a forward pass rather than a deployment-time gradient step; example: MEMORYLLM |
| Fast-weight sequence memory | Parameters of an inner learner | These parameters can function as recurrent state; learning the write rule is a separate, outer training process; examples: TTT layers, Titans |
| Online adapters | A restricted parameter update attached to a model | Episode-local adaptation versus carrying the update into later tasks; example: aTTT |
| Learned adaptation or parametric context storage | Generated training material, adapter initialization, or added memory parameters | Learning how to write versus the particular information written; examples: SEAL, PERK, Locas |

### B0. A worked explanation of neural writes, reads, and resets

**Status: Background explanation completed.** The worked numbers below are deliberately constructed teaching examples, with arithmetic checked locally. They illustrate mechanisms from the cited papers, not reproduced model results. B0.4 also connects these distinctions to the first S1 ancillary report.

All these mechanisms have the form `state_next = update(state, observation)`. The important questions are what changes, what drives that change, how a future query uses it, and when it is discarded. Calling the state a parameter does not establish that it supports a different capability.

**The minimum vocabulary.** A forward pass computes outputs using the current weights and input; its intermediate values are activations. A loss measures a specified discrepancy, such as prediction error. A gradient tells us how a small change to each adjustable number would change that loss locally. Gradient descent moves against that gradient, with a learning rate controlling the step size. It does not establish that an observation is true, or that reducing this particular loss improves an agent's decisions.

#### B0.1. Writing an association into fast weights

Consider a tiny memory with two adjustable numbers, `w = (w1, w2)`. A query supplies a key `k`; reading the memory returns the dot product `w · k`. To write a desired value `v`, minimize squared prediction error:

```text
read(w, k) = w · k
loss       = ½ (w · k − v)²
gradient   = (w · k − v) k
w_next     = w − learning_rate × gradient
```

Start with `w = (0, 0)`, write key `k = (1, 0)` with value `v = 2`, and use learning rate `0.5`. The prediction is zero, the loss is `2`, and the gradient is `(-2, 0)`. After the update, `w = (1, 0)`.

Remove the original observation and query `(1, 0)` again: the memory now returns `1`. Something survived in the weights, but the desired value was `2`. The loss fell from `2` to `0.5`; successful optimization and exact recall are already distinct in this tiny example.

Now write another association, `k = (1, 1)`, `v = 0`, using the same learning rate. Starting from `(1, 0)`, the prediction is `1`, the gradient is `(1, 1)`, and the weights become `(0.5, -0.5)`. The new key returns exactly `0`, but the original key now returns `0.5`. Shared adjustable numbers let one write interfere with another. This example demonstrates a possible mechanism of interference, not its frequency in a language model.

Resetting the weights to `(0, 0)` removes both writes. Merely removing the observation from the input does not. Whether these weights survive the next episode or a process restart is a separate implementation choice.

This is a simplified relative of the inner learning in [TTT layers, §§2.1–2.3](https://arxiv.org/html/2407.04620v4), and the associative updates in [Titans, §3](https://arxiv.org/html/2501.00663v1). Their learned representations and update rules are richer than this example. **Fast weights** change as a sequence is processed; **slow weights** are trained across sequences to make those writes and reads useful. Outer training can therefore teach a system how to learn from its next input. “Fast” describes the update timescale, not a promise of low latency. Titans also has a separately named persistent-memory component that is fixed during inference; that name should not be confused with indefinite retention of online writes.

#### B0.2. Updating an adapter to predict observed tokens

A LoRA update modifies a layer through two smaller matrices:

```text
effective_weight = frozen_base_weight + scale × B × A
```

The matrix product restricts the update's rank, reducing the number of trainable parameters. The base weights stay fixed while the adapter factors change. This changes the layer's computation for later inputs; it is not a separate lookup entry for each observation. See [LoRA v2, §4.1](https://arxiv.org/html/2106.09685v2).

For transparent arithmetic, use a scalar version with scale `1`, base weight `0`, `A = 1`, `B = 0`, and input `x = 1`. There is no compression advantage at this size. Suppose the resulting score `z = (base + B × A) × x` predicts one of two possible tokens using `p = 1 / (1 + exp(-z))`.

The observed target is token 1. Initially `z = 0`, its probability is `0.5`, and its negative-log-probability loss is about `0.693`. The loss gradient with respect to `z` is `p − 1 = -0.5`; the gradients for `B` and `A` are respectively `-0.5` and `0`. One simultaneous gradient-descent step with learning rate `1` produces `B = 0.5`, `A = 1`. The target probability becomes about `0.622`, and the loss falls to `0.474`.

The adapter now makes that observed token more likely for this input. Nothing in the calculation says the token describes a true fact or a successful action. A real language model predicts over a larger vocabulary and distributes the update through many layers, but the distinction between fitting observed text and succeeding at a later task remains. [Beyond Perplexity, §§2–7](https://arxiv.org/html/2607.00368v1) explicitly investigates that distinction; we should build on its diagnostics.

Removing the training text leaves this adapter effect intact. Disabling the adapter removes its contribution to the layer; restoring its starting factors resets this adaptation. A complete restart of a learning episode must also handle optimizer state and any other retained state. It does not undo actions already taken in an external environment.

#### B0.3. Writing latent memory without an online gradient step

A learned writer can instead produce new hidden vectors in a forward pass, leaving its own parameters fixed during use. [MEMORYLLM v2, §3](https://arxiv.org/html/2402.04624v2) uses incoming text and existing memory to generate hidden states for its memory pool. It retains new memory tokens and randomly evicts existing entries. Training the writer and reader uses gradients; a deployed memory write need not run an optimizer.

For a two-slot cartoon, begin with `M = [(0, 0), (0, 0)]`. Suppose a trained writer processes an observation and emits `u = (0.2, 0.8)`, replacing the second slot. A later query that assigns attention weights `(0.1, 0.9)` reads:

```text
M_after_write = [(0, 0), (0.2, 0.8)]
read          = 0.1 × (0, 0) + 0.9 × (0.2, 0.8)
              = (0.18, 0.72)
```

These are invented vectors and attention weights, not MEMORYLLM measurements or a complete description of its architecture. A downstream network must still turn the read vector into useful output; the coordinates do not have hand-assigned factual meanings. Removing the source text leaves the new vector available. Clearing the pool removes it while preserving the trained ability to write future memories. Finite slots also mean later writes can displace earlier information.

This is why a frozen base model can still participate in a changing neural system. Persistent activations, inner weights, and adapters offer different write and read operations. Each needs its retention boundary stated explicitly.

#### B0.4. What this implies for S1

Imagine an agent tries a red drawer and receives feedback:

| Available update source | Example text | What fitting this text could encourage |
|---|---|---|
| Self-generated action | “Open the red drawer.” | Reproducing the attempted action, including a failed attempt |
| Environment observation | “The red drawer is locked; the blue drawer is open.” | Predicting the observation, without necessarily learning the appropriate action |
| Generated summary | “Use the blue drawer because the red one is locked.” | Predicting a proposed lesson, whose usefulness depends on the summary's accuracy |
| No update | No training text selected | Preserving the current parameters at this step |

These are possible effects, not guaranteed outcomes. In particular, fitting a failed action does not always cause its repetition, and fitting a correct observation does not guarantee that the agent can act on it. The surrounding training context matters.

[aTTT v1, §§3–5](https://arxiv.org/html/2607.03441v1) already compares Self, Env, and Summary sources for next-token adapter updates and resets adaptation between episodes. S1 would ask whether an agent can select the useful source as circumstances change. Selecting a source changes the training target; it does not by itself change the next-token objective into a reward for successful behavior. SEAL provides a different precedent: it learns adaptation data generation using post-update task performance as reward ([v2, §§3–4](https://arxiv.org/html/2506.10943v2)).

For S1, we should distinguish three outcomes: **the chosen text becomes easier to predict; information remains usable after that text is removed; later decisions improve.** They require different evidence. The proposed study should hold the update mechanism fixed initially and judge selection by later behavior and its total cost. That keeps the question narrow enough to discuss while building on the existing methods.

**Empirical connection — 10 September 2026.** The ancillary [feasibility report](https://github.com/alignment-farm/update-source-selection/blob/main/output/pdf/update-source-selection.pdf) ([local](../../ancillary-studies/update-source-selection/output/pdf/update-source-selection.pdf)) makes part of this distinction concrete: its final native Qwen3-4B comparison reports lower second-step loss in 72/72 updated branches and changed generation token streams in 288/288 matched action calls, while all sources and no update complete 24/24 retrieval legs. Changed generation streams do not imply changed task actions. Every action still receives the full historical evidence, so this comparison does not establish retention after removing the training information. See [S1](#s1-can-an-agent-choose-which-experience-to-train-on-during-an-episode) for our assessment and the study's [results and reproduction note](https://github.com/alignment-farm/update-source-selection/blob/main/notes/2026-09-10-interface-results.md) ([local](../../ancillary-studies/update-source-selection/notes/2026-09-10-interface-results.md)) for evidence and limitations.

## 3. Paper map: what we can build on

**Reading scope:** The entries below identify the exact versions and sections inspected in the original full-text review, rather than claiming a line-by-line review of every appendix. The paper results are authors' reported evidence, not independently reproduced findings; that review did not audit code, checkpoints, or raw outputs. The subsequent S3 publication adds a source-loaded CPU derivative audit and local synthetic experiments, assessed separately below. Its findings do not reproduce the papers' language-model results. The assessment column is our interpretation of the boundary relevant to this program.

| Source and inspected material | Established prior work in the reviewed setting | Implication for our questions |
|---|---|---|
| **P1. [TTT layers, 2407.04620v4](https://arxiv.org/html/2407.04620v4)** — §§2.1–2.3, 2.6–2.7; experimental overview | Uses a learned model as recurrent state; learns reconstruction views in an outer loop. A specified linear/batch-gradient case is equivalent to linear attention. | The distinction between a neural state and parameter learning needs mechanism-level explanation. Rediscovering this equivalence would be educational reproduction. |
| **P2. [Titans, 2501.00663v1](https://arxiv.org/html/2501.00663v1)** — §§3–4, 5.1–5.5 | Writes key–value associations into neural memory with momentum and forgetting. Its separate “persistent memory” is fixed during inference. Its depth experiment reports better perplexity but slower training with deeper memory. | Does not establish indefinitely persistent agent learning. S3's comparison clarifies that the depth sweep excludes attention and gains are not monotonic at every added layer. Its exact depth-run configuration remains incompletely specified. |
| **P3. [aTTT, 2607.03441v1](https://arxiv.org/html/2607.03441v1)** — §§3–5 | Updates an episode-specific LoRA using Self, Env, or Summary text; resets between episodes. Includes random-drop, cadence, same-summary-in-context, and decoding controls. The strongest update source varies by model. | Basic within-episode benefit and several obvious ablations are already covered. Online source selection is explicitly left open in §5; carrying learned procedures across tasks is a different setting. |
| **P4. [SEAL, 2506.10943v2](https://arxiv.org/html/2506.10943v2)** — §§3–5, Table 2, Fig. 6 | Learns to generate adaptation data using post-update task performance as reward. Tests knowledge incorporation without the passage in context and few-shot adaptation. Sequential edits already reveal forgetting. | Acquisition without context and interference are not new phenomena. Its training reward and task packaging differ from ordinary unsupervised agent experience. |
| **P5. [Beyond Perplexity, 2607.00368v1](https://arxiv.org/html/2607.00368v1)** — §§2–7 and audit overview | Distinguishes prediction improvement from deployment-memory behavior. Its sparse-fact diagnostic finds lower loss with zero generated recall under the tested one-step LoRA protocol. Proposes retention, conflict, locality, and explicit-memory comparisons. | Reuse this distinction and protocol ideas. The diagnostic does not show that stronger update mechanisms cannot acquire usable information. Our study must add a specific mechanism or behavioral comparison. |
| **P6. [MEMORYLLM, 2402.04624v2](https://arxiv.org/html/2402.04624v2)** — §§2–3, 4.3–4.7 | Updates a latent memory pool from hidden states; tests editing and retention after intervening writes. Its 650,000-update integrity experiment checks answering about the most recently injected context. | Neural retention is already demonstrated in bounded settings. Long-run ability to absorb a fresh item is different from retaining an early item for that entire duration. |
| **P7. [WISE, 2405.14768v3](https://arxiv.org/html/2405.14768v3)** — §§2.3, 3.1–3.3 | Separates pretrained and edited knowledge into routed main/side memories; evaluates sequential edits, generalization, locality, and scaling. | Selective parametric editing is established prior art. Its edited factual targets do not by themselves settle correction of a procedure learned through interaction. |
| **P8. [PERK, 2507.06415v3](https://arxiv.org/html/2507.06415v3)** — §§2–4 | Meta-learns an adapter initialization so context encoding supports later reasoning without that context explicitly supplied in the outer-loop query. Tests several long-context reasoning settings. | Queryable parametric context storage is already studied. A bare “remove context and ask a question” comparison is insufficient novelty. |
| **P9. [MQuAKE, 2305.14795v3](https://arxiv.org/html/2305.14795v3)** — §§3.3–4; abstract | Separates recall of edited facts from answering their multi-hop consequences, finds failures, and proposes an external-memory approach. The revised diagnostic subset addresses conflicting instances. | “Does an edit propagate to dependent answers?” is already a benchmark question. Procedural action consequences or temporal revision would need an explicit additional comparison. |
| **P10. [Locas, 2602.05085v1](https://arxiv.org/html/2602.05085v1)** — abstract, introduction, §§2.1–2.2 | Develops locally supported parametric memory with initialization informed by the backbone. Describes expansion/compression and reports book-modeling and dialogue-QA evaluations. | Relevant to consolidation and initialization. Results and deployment lifecycle still need closer inspection before selecting it as a study implementation. |
| **P11. [TTCD, 2608.01672v1](https://arxiv.org/html/2608.01672v1)** — §§2–4, Tables 1 and Fig. 3 | Uses a longer-context teacher to supervise a shorter-context student's fast weights. Tests predictive retention, including recall and long-context reasoning. | Learning what to retain for later prediction is already the contribution. An unannounced change in the downstream goal is a possible narrower extension. |
| **P12. [Modular TTT, 2608.07110v1](https://arxiv.org/html/2608.07110v1)** — depth analysis, Appendices 8.4, 9.4–9.5, limitations | In its tested one-step setting, deeper learners remain behind shallow ones despite stabilization and initialization sweeps. External hybrid-model comparisons bundle several mechanisms. | S3 identifies a derivative omission in a pinned implementation and representation interactions in synthetic recall. Neither establishes the cause of this paper's depth trend; the mapping from source configurations to original checkpoints remains unresolved. |
| **P13. [Self-Guided TTT, 2607.09415v1](https://arxiv.org/html/2607.09415v1)** — method and Algorithm 1; abstract | Selects training spans using the current question, retains full context at answer time, and resets after each instance. Reports gains over long-context baselines. | Selection of update text is already studied. Distinguish question-known selection from selection before a future need is known. |
| **P14. [VANE, 2608.09448v2](https://arxiv.org/html/2608.09448v2)** — §§3, 4.2; validation appendix | Adapts latent prompts on a shadow copy and validates candidates using subsequent observations before commitment. Reports task-dependent robotic results. | Validation and rollback of live updates are prior art. This is a related mechanism in a different modality, not an established solution for textual memory authority. |
| **P15. [Test-Time Training Undermines Safety Guardrails, 2605.22984v1](https://arxiv.org/html/2605.22984v1)** — abstract, §4.4 | Studies adversarial TTT and distinguishes substantive failures from degenerate outputs that fool safety judges. | “Weight updates introduce an attack surface” is already studied. Useful-learning preservation and evidence-specific authority would need their own comparison. |
| **P16. [ACE, 2510.04618v3](https://arxiv.org/html/2510.04618v3)** — §§3–4, Appendices A.1, A.3–A.4 | Supports incremental playbook updates, sequential prediction-before-update evaluation, multiple models, cost analysis, and harmful-reflection tests. Evaluation input cost can increase even when adaptation is cheaper. | Revision, robustness, model variation, and cost have existing evidence. Use it as an explicit-memory comparator rather than a new mechanism proposal. |
| **P17. [On-Policy Context Distillation, 2602.12275v1](https://arxiv.org/html/2602.12275v1)** — §3, §§4.2–4.6, Appendices A.3/B.2; read 13 September | Uses student rollouts and a context-conditioned teacher; context-free deployment is prior art. | A method lead for procedure transfer. Preserve evidence and cost distinctions; the reported checkpoint selection uses test results. |
| **P18. [Procedural Memory Distillation, 2607.01480v1](https://arxiv.org/html/2607.01480v1)** — §§3.1–3.2, 4.1; read 13 September | Builds memory from ongoing attempts to guide policy training, with online memory/policy co-evolution. | A fixed-evidence local comparison omits its central co-evolution mechanism; do not present that comparison as a PMD reproduction. |
| **P19. [Meta-learning for compositionality, published article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/)** — results, meta-training methods and discussion; read 14 September | Learns systematic lexical generalization through compositional episodes; productivity remains limited. | Episode examples stay in context. This is preparation for reusable composition, not episode-local weight storage. |
| **P20. [Abacus embeddings, 2405.17399v1](https://arxiv.org/html/2405.17399v1)** — §3, introduction and limitations; read 14 September | Demonstrates arithmetic length generalization with structured positions and extensive training. | Input representation is a concrete acquisition hypothesis; local adapter transfer needs its own evidence. |
| **P21. [CLEAR / Experience Replay for Continual Learning, NeurIPS 2019 proceedings](https://papers.nips.cc/paper_files/paper/2019/file/fa7cdfad1a5aaf8370ebeda47a1ff1c3-Paper.pdf)** — §3 methods prose in cached primary text; root reading 15 September | Combines new/replayed experience in actor-critic training with off-policy correction and additional behavioral cloning on replay. | The S1 fixed mixture is ordinary supervised rehearsal, not CLEAR or a new replay principle. |
| **P22. [Online Continual Learning with Maximally Interfered Retrieval, NeurIPS 2019 proceedings](https://papers.nips.cc/paper_files/paper/2019/file/15825aee15eb335cc13f9b559f166ee8-Paper.pdf)** — §3.1 and Algorithm 1 in cached primary text; root reading 15 September | Estimates an incoming update and retrieves stored examples by predicted loss increase before training on new and replayed material. | S1's third phase now adapts this idea: acquisition gains did not establish better recurrence or useful cost. The earlier current-error policy was a different mechanism. |
| **P23. [Gradient Episodic Memory, 1706.08840v6](https://arxiv.org/html/1706.08840v6)** — §3, equations 5–8 and Algorithm 1 | Uses local gradient constraints to protect remembered task losses. | Remembered examples and the update approximation delimit the protection; complete procedural outcomes require separate evidence. |
| **P24. [Efficient Lifelong Learning with A-GEM, 1812.00420v2](https://arxiv.org/html/1812.00420v2)** — §§2–4, Appendix D.2 | Uses one sampled average-memory gradient constraint; distinguishes average from task-specific forgetting. | Aggregation and observation cost matter when deciding which behavior must survive an update. |
| **P25. [Gradient based sample selection, 1903.08671v5](https://arxiv.org/html/1903.08671v5)** — §§3.1–3.5 | Populates a bounded replay buffer using a gradient-diversity surrogate for constraint selection. | Buffer selection, update constraints and rehearsal are related but distinct interventions. |
| **P26. [What Will My Model Forget?, 2402.01865v3](https://arxiv.org/html/2402.01865v3)** — §§2–5 | Learns forgetting forecasts and uses them for replay, including sequential error correction. | A generic forecast-and-protect study would overlap directly; specify the new generalization or decision question. |
| **P27. [Low-rank Example Associations, 2406.14026v8](https://arxiv.org/html/2406.14026v8)** — §§2–4, Appendices A/D | Predicts forgetting from empirical associations and sparse measured seed damage; evaluates targeted replay. | Distinguish post-trial extrapolation from advance warning. Sequentially changing learner histories are outside its main setup. |
| **P28. [Adaptive and Selective Reset, 2603.03796v1](https://arxiv.org/html/2603.03796v1)** — §3.3–3.5 | Uses collapse signals, selective resets and knowledge recovery in visual adaptation. | Adaptive reset is prior art; restoring a source model need not satisfy a newly revised rule. |
| **P29. [Cartridges, 2506.06266v3](https://arxiv.org/html/2506.06266v3)** — §§2–6, targeted reading | Trains reusable KV state with context-distilled self-study for repeated corpus queries. | Supplies a demonstrated serving tradeoff and substantial preparation cost, not a local maintenance-cost result. |
| **P30. [Doc-to-LoRA, 2602.15902v1](https://arxiv.org/html/2602.15902v1)** — §§2–3, 6, Appendix C.4 | Meta-learns context-to-adapter generation; tests unrelated-query interference. | Fast deployment writes shift costs into prior training and do not guarantee preservation. |
| **P31. [Harness the Memory, 2608.15008v1](https://arxiv.org/html/2608.15008v1)** — §§2–5 overview, Appendices B/G | Compares eleven memory implementations across workloads and costs. | A broad substrate comparison already exists; exclusions and implementation substitutions constrain imported rankings. |
| **P32. [Dual-Layer Agentic Memory, 2608.22215v2](https://arxiv.org/html/2608.22215v2)** — §§3–5 | Combines selective external admission and parametric consolidation. | Direct overlap with S5; temporal conflicts and consolidation interference remain explicit limits. |
| **P33. [Experience-Amortized Reranking, 2608.22767v1](https://arxiv.org/html/2608.22767v1)** — method, §§V–VIII | Retains relevance scores and learns to estimate unscored query–memory relations. | Learned access can coexist with explicit evidence. Fixed budgets and changing relevance are consequential boundaries. |
| **P34. [Fragility of Self-Improving Agents, 2608.18066v2](https://arxiv.org/html/2608.18066v2)** — §§3–4, targeted reading | Finds text-memory sensitivity to task order and feedback specification. | Extends the history-dependence concern beyond weights without identifying a common cause. |
| **P35. [Popular Knowledge Propagates More Errors, 2609.08067v1](https://arxiv.org/html/2609.08067v1)** — §§4–5.5, limitations | Studies factual connectivity, collateral damage and preservation anchors. | Structural risk signals are prior art; entity popularity is a proxy under controlled substitutions. |
| **P36. [Agent-Native Memory System?, 2606.24775v1](https://arxiv.org/html/2606.24775v1)** — §§3–4, especially 4.3/4.5 | Compares dynamic updates and construction/query costs across memory systems. | Dynamic-memory cost evaluation already exists; specify the learned component and its useful lifetime. |
| **P37. [Evolving State, 2608.19652v1](https://arxiv.org/html/2608.19652v1)** — §§4–5 | Defines typed state changes, dependent consequences and anti-update controls; supplies an explicit-state method. | Reuse these distinctions; stale-state diagnosis is not a new contribution by itself. |
| **P38. [Supersede, 2606.27472v1](https://arxiv.org/html/2606.27472v1)** — §§2–4, reported training result | Trains supersession behavior in bounded textual memory without refeeding the source history. | A precedent for learned revision, with different evidence access from our placement comparison. |
| **P39. [AgeMem, 2601.01885v3](https://arxiv.org/html/2601.01885v3)** — method and memory-use ablations | Learns coordinated long- and short-term memory operations. | Learned memory management is established prior work; tool costs still matter. |
| **P40. [Memory-R1, 2508.19828v5](https://arxiv.org/html/2508.19828v5)** — method, ablation overview, limitations | Trains memory editing and answer-time selection separately. | A useful precedent within supplied operations and downstream supervision. |
| **P41. [Life-Harness, 2605.22166v2](https://arxiv.org/html/2605.22166v2)** — §§3–5 | Optimizes a frozen executor's interface from training trajectories. | External development-time adaptation differs from a deployed learner changing its own decision policy. |
| **P42. [Co-Evolving Harnesses and Models, 2609.09134v1](https://arxiv.org/html/2609.09134v1)** — §§3.1–3.3, appendices | Reports interference from imitation and gains from on-policy correction within evolved harnesses. | Component compatibility is already an empirical subject; the mechanism explanation remains provisional. |
| **P43. [HarnessBandit, 2609.13739v1](https://arxiv.org/html/2609.13739v1)** — §§3–5 | Learns training-time selection among fixed harnesses. | Signals follow paid updates; scheduling and batch-composition effects need separation. |
| **P44. [Interactive Memory Learning, 2609.17088v1](https://arxiv.org/html/2609.17088v1)** — method, evaluation and ablations | Co-adapts retention and retrieval policies across sessions. | Online memory-policy learning has a direct precedent; judged response quality has attribution limits. |
| **P45. [Next-Generation Agentic RL, 2607.01120v2](https://arxiv.org/html/2607.01120v2)** — §§5–7 | Proposes selection across memory, harness and weights; prototypes the weight-update branch. | Conceptual overlap does not establish the full proposed selector's effectiveness. |
| **P46. [Smart “Predict, then Optimize”, 1710.08005v5](https://arxiv.org/html/1710.08005v5)** — §2, §3 through §3.1 | Defines prediction-induced decision loss; distinguishes prediction fit from useful action ordering. | Prior theory for action-value comparison; its supplied training cost vectors do not solve missing counterfactual outcomes. |
| **P47. [Selecting Computations, 1207.5879v1](https://arxiv.org/html/1207.5879v1)** — §§1–2 through Definition 6 and discussion | Formalizes costly observation before action and explains a limitation of one-step observation selection. | Prior theory for pricing learner probes; an informative signal need not change a maintenance decision. |
| **P48. [Grounding Agent Memory, 2609.11060v1](https://arxiv.org/html/2609.11060v1)** — §3 and Appendix D | Environment-probing curation of explicit records. | Concrete feedback precedent; see the memory-feedback ledger for limits. |
| **P49. [HiMPO, 2606.16285v2](https://arxiv.org/html/2606.16285v2)** — targeted methods and Appendices E–F | Memory credit with live behavioral validation. | Generic memory-credit validation already has direct precedent. |
| **P50. [AttriMem, 2607.21106v3](https://arxiv.org/html/2607.21106v3)** — methods, selected results, Appendices A–B | Attribution trains memory construction. | Distinguish fixed-answer influence from complete-task effect. |
| **P51. [Credit Without Ground Truth, 2608.19760v2](https://arxiv.org/html/2608.19760v2)** — targeted methods and limitations | Executed-replay audit of step credit. | Limited fidelity and training evidence do not establish general uselessness. |
| **P52. [CRAG, 2401.15884v3](https://arxiv.org/html/2401.15884v3)** — selected methods, ablations and costs | Relevance-based corrective action routing. | A concrete developed rule for AD1 comparisons. |
| **P53. [Adaptive-RAG, 2403.14403v2](https://arxiv.org/html/2403.14403v2)** — §3, selected results and pinned author code | Outcome-derived strategy classification. | Direct precedent for learning which retrieval strategy to use; not isolated reading repair. |
| **P54. [RAFT, 2403.10131v2](https://arxiv.org/html/2403.10131v2)** — §§3–5 | Learned in-domain reading mixed with memorization. | Positive precedent; correction durability is a separate claim. |
| **P55. [RA-DIT, 2310.01352v4](https://arxiv.org/html/2310.01352v4)** — §§2–3, 5.1–5.2 | Separate reader and retriever adaptation. | Isolate reader benefit and retain developed few-shot controls. |
| **P56. [Controlled ICL/finetuning study, 2505.00661v3](https://arxiv.org/html/2505.00661v3)** — methods and selected experiments | Different generalization; inference-augmented training. | Distinguish acquired information, computation and complete-task transfer. |
| **P57. [Context-Parametric Inversion, 2410.10796v3](https://arxiv.org/html/2410.10796v3)** — §§3–5 | Context reliance can decline during successful training. | Training inputs containing evidence need not require using it. |
| **P58. [Context-faithful Prompting, 2303.11315v2](https://arxiv.org/html/2303.11315v2)** — §§3–4 | Instructions and counterfactual demonstrations. | Serious contextual alternative; authority is assumed. |
| **P59. [CARE, 2509.13683v1](https://arxiv.org/html/2509.13683v1)** — §§3–5 | Learned evidence-integrated reasoning, including counterfactual QA. | Generic learning possibility substantially answered; lifetime comparison remains selected. |
| **P60. [Voyager, 2305.16291v2](https://arxiv.org/html/2305.16291v2)** — selected methods/results | Executable experience and new-world reuse. | Possibility answered; persistence and contextual code access coexist. |
| **P61. [LATM, 2305.17126v2](https://arxiv.org/html/2305.17126v2)** — selected methods/results | Tool synthesis, verification and amortization. | Compare against competent regeneration with execution. |
| **P62. [LILO, 2310.19791v4](https://arxiv.org/html/2310.19791v4)** — selected methods/results | Acquired abstractions and documentation. | Code and contextual descriptions can be complementary. |
| **P63. [TroVE, 2401.12869v1](https://arxiv.org/html/2401.12869v1)** — selected methods/results | Online toolbox induction and pruning. | Read performance claims alongside P64. |
| **P64. [TroVE re-evaluation, 2507.22069v2](https://arxiv.org/html/2507.22069v2)** — selected methods/results | Compute-matched reproduction. | Much of the MATH gain is explained by generation budget. |
| **P65. [SkillWeaver, 2504.07079v1](https://arxiv.org/html/2504.07079v1)** — selected methods/results | Interaction-derived APIs and honing. | Outcome checking remains necessary for executable memory. |
| **P66. [PolySkill, 2510.15863v2](https://arxiv.org/html/2510.15863v2)** — selected methods/results | Abstract interfaces and site implementations. | Portable modular code is an established alternative. |
| **P67. [LLM Agents Making Agent Tools, 2502.11705v2](https://arxiv.org/html/2502.11705v2)** — selected methods/results | Repository integration and self-correction. | Acquisition cost and imported capability must be disclosed. |
| **P68. [Harness Continual Learning, 2608.19013v1](https://arxiv.org/html/2608.19013v1)** — selected methods/results | Anchor-tested harness revision. | Regression-gated updates already have direct precedent. |
| **P69. [Agent Workflow Memory, 2409.07429v1](https://arxiv.org/html/2409.07429v1)** — selected methods/results | Contextual versus callable workflows. | Observation access matters; Table 9 and prose conflict. |
| **P70. [SPELL, 2602.01107v1](https://arxiv.org/html/2602.01107v1)** — selected methods/results | Reusable programmatic migration. | Repair itself can be acquired and amortized. |
| **P71. [SkillCraft, 2603.00718v2](https://arxiv.org/html/2603.00718v2)** — targeted §§2–4, 5.1, Appendices B/D.2; pinned code | Acquired compositions and a direct-script comparison. | Existing reconstruction precedent; descriptions, feedback and conditional cost denominators require care. |
| **P72. [CodeMem, 2512.15813v1](https://arxiv.org/html/2512.15813v1)** — §§4–7 | Retained-function architecture with reported executions and model comparisons. | Reconstruction avoidance is an explicit prior proposal; matched retention effects are not isolated. |
| **P73. [PANDO, 2605.24785v2](https://arxiv.org/html/2605.24785v2)** — §§3–6, limitations and skill dynamics | Online rules/routines, checking, demotion and cost accounting. | Whole-system evidence does not isolate implementation retention; seed capability matters. |
| **P74. [Skill Blocks, 2608.14943v1](https://arxiv.org/html/2608.14943v1)** — §§1, 3–7, Appendix C | Conditional delivery of retained procedural text. | Contextual alternatives can reduce delivery work; cache sensitivities are not measured billing. |

The subsequent [pinned artifact review](../sources/2026-09-17-executable-artifacts/README.md)
adds static implementation inspection for P65/P69, distinguishing code availability
and comparison defaults from reproduced experimental evidence.

The [persistence-control ledger](../sources/2026-09-17-persistence-controls/README.md)
records P71–P74 and a separate SkillCraft code boundary. It changes the recommended
comparison without changing any local publication's accepted revision.

The [13 September methods review](../sources/2026-09-13/README.md) records the added reading and the selection rationale for procedure transfer. P17/P18 are additions to the original paper map; this is not a claim of comprehensive or latest-version coverage.

The [14 September positive-demonstration review](../sources/2026-09-14/README.md) adds P19/P20, revisits P4's adaptation results and extends P8 reading through §5.1/Table 1. It supports the root's [procedural-learning predictions](../notes/PROCEDURAL_LEARNING.md#predictions-before-the-next-findings), without claiming these preparations have been reproduced locally.

The S1 follow-up's [rehearsal source ledger](https://github.com/alignment-farm/experience-selection/blob/main/sources/followup-rehearsal/README.md) ([local](../../ancillary-studies/experience-selection/sources/followup-rehearsal/README.md)) records the exact proceedings artifacts and hashes for P21/P22. The root inspected the cached methods text on 15 September, not author code or experimental results in full. CLEAR's extracted equations are imperfect; the cited PDF remains authoritative. This focused reading establishes relevant overlap, not a new reproduction or comprehensive novelty search.

The later [maintenance-reliability reading](../sources/2026-09-15-maintenance-reliability/README.md) adds P23–P25 and a successful cached title query. These methods constrain novelty and motivate examining how loss-based signals relate to complete-task damage. They have not been implemented locally in this root work.

The [16 September reading ledger](../sources/2026-09-16-research-direction/README.md) records exact scopes for P26–P35, discovery queries and source limitations. These are author-reported results, not local replications. It also records a paired-configuration inconsistency in P32's prose; the table entries should be kept paired.

The subsequent [preparation review](../sources/2026-09-16-study-preparation/README.md) records P36–P38 and implementation leads. The [adaptation-decision review](../sources/2026-09-16-adaptation-decisions/README.md) records P39–P45, reading scopes and search limits. It narrows the root's contribution beyond generic memory-policy learning or joint model–harness development.

Additional existing background: [Reflexion v4](https://arxiv.org/html/2303.11366v4) §§3–4 explains bounded reflection buffers and repeated trials; [TT-SI v1](https://arxiv.org/html/2510.07841v1) Algorithm 1 restores the original parameters after instance-specific adaptation. [DeepSeek-R1 v2](https://arxiv.org/html/2501.12948v2), including Appendix F, provides training/distillation background. [Composer's developer report](https://cursor.com/blog/self-summarization) describes training summaries within rewarded trajectories. These establish useful mechanisms, with different evidence and reset boundaries.

The original SWE-agent, compute-allocation, small-model, production, AgentDojo and methods references remain background in [Perspectives](../notes/RESEARCH_PERSPECTIVES.md), with earlier abstract/source-summary review. Voyager now has selected method reading as P60. The [17 September review](../sources/2026-09-17-executable-experience/README.md) motivates a bounded executable-experience artifact review, not a newly commissioned study.

## 4. What Construct and Formation already answered

The original-question table below uses the Construct synthesis. On 10 September 2026 we also read the local [Construct overview](../../construct/README.md), its M2 and GM findings, the [Formation overview](../../formation/README.md), and the two Formation evidence accounts linked below. This is a targeted reading of reported findings, not a new audit of raw requests, experimental ledgers, or scorers. Their external-memory results motivate comparisons but do not transfer automatically to neural mechanisms.

| Original area | What is already answered or substantially covered | What remains useful here |
|---|---|---|
| **T1: Access to stored information** | M1 demonstrates an eligibility effect with the same retained record. P8/P13 already study use of parametric context and selection of update text. | Background explanation of storage/write/read failures. Dynamic choice of update source becomes S1. Autonomous external retrieval is deferred. |
| **T2: Repair versus transferable learning** | M2 demonstrates a bounded cross-session lesson effect; GM joins old continuity with current state. P3/P4/P5/P6/P8 already distinguish or measure relevant forms of adaptation and retention. | Explain the distinct outcomes. Investigate a learned procedure's retention and revision under later updates in S2. |
| **T3: Knowledge placement/consolidation** | P1/P2 explain fast-weight memory; P7/P8/P10 provide parametric storage designs. R1 establishes a training/distillation background. | S3 now distinguishes architectural capacity from usable recall under a training recipe. The workload-dependent value of carrying or consolidating an update remains S5. No universal placement rule is established. |
| **T4: Compression and recovery** | X2 shows a hot-store proxy benefit from recoverable eviction. P11 and Composer already learn retention policies. | A changed future goal becomes S4. Full archive/recovery engineering is deferred; its costs remain relevant to comparisons. |
| **T5: Correction** | Construct's retraction work covers a bounded correction. P7/P9 cover editing, locality, and dependent answers; P4/P6 address interference/retention. | Procedural exceptions after intervening learning become S2. General edit propagation is background, not a new proposal. |
| **T6: Total cost** | X2's metric is limited; warming-budget results depend on charging assumptions. P16 separates adaptation and evaluation costs. | Attach full accounting to every candidate; S5 studies the recurrence/revision tradeoff if a useful neural mechanism is available. |
| **T7: Capability and composition** | Engine-dependent engagement and Body-0's unengaged integration run limit Construct's claims. P3/P12/P16 examine model or component variation. | S3's reciprocal tensor swaps establish interactions among initial parameter groups in a bounded recall task. Their generality remains open; a general architecture-composition project is deferred. |
| **T8: Authority/security** | M3 already shows memory withholding/admission attacks. P14/P15 supply neural-update validation and attack evidence. | Authority is a factor in S1/S2. We are not proposing to rediscover that memory can be poisoned. |
| **T9: Measurement** | Construct scorer/admission audits and P5 already support separating instrument outcomes from behavioral evidence. | Background research method used throughout; no new generic framework is proposed. |

### Direct local evidence relevant to S1 and S2

- **Construct: using an earned record is already demonstrated.** [M2 findings](../../construct/notes/M2_FINDINGS.md) report a cross-session retraction lesson changing later answers, with removal comparisons and repeated draws. The bound is one hop and one retraction, not general procedural learning. [GM findings](../../construct/notes/GM_MEMORY_FINDING.md) report joining an earlier promise with current state: 24/24 relevant cases versus 6/24 state-only. This is explicitly an exploratory finding from a corrected replacement, not a formal validation claim.
- **Formation: selective revision is already demonstrated in a restricted setting.** The [composed revision successor](../../formation/evidence/composed-clerical-revision-engagement-successor-20260820T185545Z/README.md) reports 45/48 matching actions after admitting revised records, equal to supplied correct revisions; removal left the old versions active and scored 0/48. The account explicitly limits this to structured retrieval over model-written fields. It does not establish long-run interference resistance or general acquired competence.
- **Formation: producing a record and using it can fail separately.** In the [opaque-sink coding contact](../../formation/evidence/opaque-sink-coding-contact-20260822T031500Z/README.md), the clerk reversed the observed API fact and every learned record was quarantined. Supplying the correct fact still yielded 0/6 matching functions; most programs failed on field names before the remembered API behavior could matter. That comparison could not establish the intended memory benefit. It also does not show that neural adaptation would repair the failure.

**Implication for our studies:** S1 needs evidence that source selection affects useful downstream behavior, rather than merely changing training text or a reported rationale. S2 must distinguish successful acquisition from successful use and test scoped revision beyond an already-established lookup effect. Supplied-correct-information controls help locate failures, but are not a universal ceiling on what parameter learning can achieve: an update might change computation that a context-only control cannot. These are design implications we draw from the local results, not additional findings. Formation's [current state](../../formation/README.md#present-state) owns its broader thesis assessment and paused empirical route.

## 5. Narrower questions and candidate ancillary studies

The open hypotheses below are proposals for discussion. Root assessments distinguish completed contributions from the questions they leave open. Prospective studies name an intended addition, closest overlap, and evidence that could change the theory; their sample sizes, budgets, implementation versions, and exact protocols belong to the investigating project.

**Workload choice.** For placement and repayment questions, a useful comparison needs a motivated workload, explicit information access, and measured costs that can distinguish the competing explanations. Context or retrieval is a comparator whose cost must be measured. An acquisition failure, an explicit-memory advantage, or a tie at lower total cost can each be informative. Bounded exploration may establish the workload; a subsequent test of a developed claim needs fresh evaluation material. The root motivates the question and assesses its implications; the study owns task and protocol design under the [ancillary-study approach](../notes/ANCILLARY_STUDY.md). S3's mechanism comparison can answer its narrower question without establishing an advantage over explicit context.

### S1. Can an agent choose which experience to train on during an episode?

**Status — 15 September 2026:** All three experience-selection publications are accepted bounded contributions. The latest [complete-workflow study](https://github.com/alignment-farm/experience-selection/blob/main/MAINTENANCE_FINDINGS.md) ([local](../../ancillary-studies/experience-selection/MAINTENANCE_FINDINGS.md)) implements MIR-inspired replay and compares acquisition, recurrence and fixed stopping against a developed mixture and competent explicit archive. Its [commission](https://github.com/alignment-farm/experience-selection/blob/main/MAINTENANCE.md) ([local](../../ancillary-studies/experience-selection/MAINTENANCE.md)) is complete; no further phase is assigned here. The earlier [update-source-selection project](https://github.com/alignment-farm/update-source-selection/blob/main/README.md) ([local](../../ancillary-studies/update-source-selection/README.md)) supplies feasibility evidence and the historical assessment below. P3, P13/P14 and P21/P22 constrain novelty claims.

**Root assessment of the 10 September 2026 report.** [Update Source Selection: A Local Feasibility and Behavioral Diagnostic](https://github.com/alignment-farm/update-source-selection/blob/main/output/pdf/update-source-selection.pdf) ([local](../../ancillary-studies/update-source-selection/output/pdf/update-source-selection.pdf)) establishes a local route for reproducible LoRA interventions, with exact adapter resets, unchanged base weights, and measurable generation changes. Early first-action gains on 0.6B did not establish four-action episode success: all sources completed 0/24 legs in that diagnostic. The later native 4B reasoning comparison reached 24/24 for every source and no update. These are exploratory results from correlated synthetic cases; neither the floor nor the ceiling settles whether source selection can help elsewhere. No dynamic selector was tested.

The theoretical update is that **source reliability and source training value must be distinguished**. A verified correction can supersede an earlier plan without making its text the best material for a parameter update. This study did not demonstrate that the best training source changes across circumstances. Full historical context and explicit reliability rules also let the competent baseline solve every case without adaptation. No update used the fewest action-generation tokens in the final run, but those descriptive counts do not establish a general cost advantage. Source-dependent training utility, useful retention, and an agent's ability to choose remain unresolved.

We accept the report as completing the initial focused feasibility investigation. The question it leaves is: **when does training on experience improve later performance or reduce total cost compared with retaining accessible evidence and reasoning over it?** A workload with meaningful context, retrieval, or repeated-use costs would give that comparison a purpose. Evidence that different sources help under different observable conditions—or that selective abstention saves cost—would motivate selector development. The 14 September commission assigns this exploration to the new study, without requiring a positive effect.

The later procedure-transfer diagnosis adds a useful starting distinction: the same teacher and examples can support acquisition under one objective and fail under another, and the learner's starting state changes the outcome. That motivates checking useful update behavior before interpreting source comparisons. It does not itself demonstrate varying source utility or a working selector. Hold the update method comparable when isolating source effects, or explicitly investigate the interaction.

Assessment scope: we read the [manuscript source](https://github.com/alignment-farm/update-source-selection/blob/main/paper/update-source-selection.tex) ([local](../../ancillary-studies/update-source-selection/paper/update-source-selection.tex)), its included results, the [results note](https://github.com/alignment-farm/update-source-selection/blob/main/notes/2026-09-10-interface-results.md) ([local](../../ancillary-studies/update-source-selection/notes/2026-09-10-interface-results.md)), recorded analysis, and the diagnostic implementation. We did not rerun the experiments or independently rescore all raw traces. Methods, operational state, and the supporting evidence remain with the study.

**Root assessment of experience selection — 14 September 2026.** Publication `dca27dd46b634616e8895e0a137f23225c5dc7cc` establishes useful, redundant and harmful updates under a functioning acquisition method. Checked training improves base routing from 30/48 to 48/48; repeating it after acquisition adds nothing. A supervised abstention gate matches always-checked training at 96/96 with fewer updates than the prescribed 128-step comparator. But the saved fixed 32-step treatment also reaches 96/96 using fewer updates than the gate. The acquired state was constructed from the same checked material, and its self-generated labels equal checked labels. This is a narrow abstention result, not changing choice among useful sources or an established efficiency advantage. The [detailed assessment](2026-09-14-concurrent-findings.md#s1-update-value-depends-on-what-is-already-acquired) records costs, context interactions, chronology and independent checks.

**Root assessment of the follow-up — 15 September 2026.** Publication `dee1e3159ed0105f6a090c65b72f57cbc386fb10` gives fixed-mixture accuracy 96/96 versus 48/96 for the current-error policy, either pure source and no update. In every one of six partial states, gap targeting learns the missing region and loses the acquired region. Mixture and selection match subsequent updates and aggregate training tokens. Development extends unsuccessful short trajectories and establishes joint acquisition before the fresh test; mixture128 scores 82/96 versus 96/96 at the fixed 256 endpoint. The result weakens the preceding expectation that state-dependent gaps would yield a useful changing source choice beyond a strong fixed composition. Known experience can have rehearsal value during another update even when repeating it alone adds nothing. This is a single decision on four synthetic rule cells, not a test of online reselection or MIR. The [follow-up synthesis](2026-09-15-followup-findings.md#s1-learning-only-the-current-gap-can-destroy-what-already-works) records controls, costs and verification.

**Root assessment of complete maintenance — 15 September 2026.** Publication `6179d8d0d8bcbaa236e42f53470eddc39199d502` reports 151/168 complete uses for damage-aware replay versus 143/168 for the strongest developed fixed mixture, at matched actual updates and replay fraction. Its advantage is in acquisition (67/72 versus 55/72); recurrence is worse (84/96 versus 88/96), paired losses are higher (11 versus 9), and prediction adds 192 virtual updates plus 6,144 scoring forwards. All differences come from one of two fresh runs. Both methods finish 32/32; fixed stopping freezes incomplete acquisition in one run. The same observed archive with a supplied lookup key gives 168/168. This meets the broader complete-task milestone without establishing M1's preservation/cost advantage. Eight rule cells, four traces, no ticket copying and per-job resets limit generality. The [detailed assessment](2026-09-15-maintenance-findings.md#s1-better-acquisition-does-not-establish-better-maintenance) records checks and costs.

**Remaining question:** Which observable signals predict complete-task damage or establish enough acquisition to guide useful update and abstention decisions?

**Public-research update — 16 September:** P26/P27 already predict forgetting and use it for replay. A new S1 comparison should concern signal or decision transfer as the learner changes, with a stated horizon and cost, rather than demonstrating prediction-guided replay in general. See [direction A](../notes/RESEARCH_DIRECTION.md#a-does-a-maintenance-decision-remain-useful-after-the-learner-changes).

**Competing explanations:** Predicted loss increases identify replay that protects useful behavior; alternatively, selection primarily accelerates acquisition while later updates still damage acquired behavior. A developed fixed mixture may provide better useful maintenance once selection costs are charged.

**Candidate continuation, not commissioned:** Distinguish acquisition gains from preservation and examine the relationship between predicted loss change and complete-task damage. Compare informative update or stopping decisions against strong fixed schedules, disclosing their verification costs. The existing [third-phase brief](https://github.com/alignment-farm/experience-selection/blob/main/MAINTENANCE.md) ([local](../../ancillary-studies/experience-selection/MAINTENANCE.md)) records the completed scope; S1 remains independent of S2's actual rule revisions.

**What a continuation would add:** An explanation or useful decision boundary beyond the observed two-run accuracy/work tradeoff. Neither a selector win nor another broader workload by itself supplies that explanation.

**Evidence needed for that question:** Complete behavior over the sequence, acquired and lost successes, identifiable starting states, prediction/verification costs and matched learning resources. Later policies' divergent states must not be mistaken for a controlled test of one selected record.

**Reading/implementation context:** P22's virtual-update selection is now adapted locally; [the source record](https://github.com/alignment-farm/experience-selection/blob/main/sources/maintenance-mir/README.md) ([local](../../ancillary-studies/experience-selection/sources/maintenance-mir/README.md)) distinguishes blockwise AdamW replay from the author algorithm. CLEAR/P21 remains related rehearsal work, not a locally implemented method. P3's reset/update boundaries and P13/P14's selection and validation remain relevant. The abstract-level [decision-theoretic TTT paper, 2606.15569v1](https://arxiv.org/abs/2606.15569v1) remains a lead on update decisions.

### S2. Can a learned procedure survive later learning and accept a scoped correction?

**Status — 15 September 2026:** All four retention/revision publications are accepted. The latest [state/support investigation](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/FINDINGS-STATE-SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-STATE-SUPPORT.md)) identifies an interaction between inherited state and current evidence, with the predicted direction in two fresh acquisitions. One support preference reverses between histories; neither support choice fully preserves the second fresh acquisition. The [root assessment](2026-09-15-state-support-findings.md) closes this commissioned phase. Reliable maintenance remains open; no further experiment is commissioned.

**Related study and scope:** [Procedure acquisition and reuse](https://github.com/alignment-farm/procedure-acquisition-and-reuse/blob/main/README.md) ([local](../../ancillary-studies/procedure-acquisition-and-reuse/README.md)) investigated acquisition, transfer to new inputs, and repeated-use costs. Its initial experiment and bounded follow-up are complete. S2's additional question concerns interference from later learning and scoped correction; neither was tested in that investigation. S5's broader consolidation comparison also remains open.

**Root assessment — 13 September 2026.** The [initial results](https://github.com/alignment-farm/procedure-acquisition-and-reuse/blob/main/notes/2026-09-11-acquisition-results.md) ([local](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-acquisition-results.md)) report 12/12 training-call recall from a fixed twelve-demonstration LoRA adapter, but 26/64 correct new-input calls versus 41/64 with retained examples. The [fresh follow-up](https://github.com/alignment-farm/procedure-acquisition-and-reuse/blob/main/notes/2026-09-11-followup-results.md) ([local](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-followup-results.md)) reports 28/64 for the unchanged adapter versus 51/64 for examples, including 13/32 versus 31/32 on ordinary words. This is scored contact with acquisition and transfer, with a bounded result favoring retained examples. It does not establish a general limitation of parameter learning.

The lesson-construction method also failed: none of three candidates passed acquisition validation, and the selected fallback remained explicitly unvalidated. The supplied correct rule scored 64/64 in each evaluation but contained privileged information; it diagnoses execution ability without establishing acquisition from the same evidence. The intended compositional rule is not uniquely determined by the demonstrations, and inputs share identifier clusters. These limits constrain the transfer claim.

The theoretical implication is that **training recall, usable transfer, and acquisition-cost repayment need separate evidence**. The adapter reduced prompt tokens and measured inference time, but its lower accuracy prevented a repayment claim at comparable useful performance. Repeating its use does not by itself resolve the observed transfer deficit. This investigation already addresses the workload concern empirically; a further study needs a motivated acquisition method or different question, without an obligation to obtain an adapter win.

Assessment scope: we read the study README, initial results, follow-up addendum, and frozen follow-up protocol. We did not rerun experiments or independently rescore raw traces. Methods, evidence, and the completed investigation's operational state remain with that study.

<a id="next-investigation-procedure-transfer"></a>

#### Procedure transfer: completed local recipe test

**Root assessment and publication acceptance — 14 September 2026.** The user accepted the [local publication](https://github.com/alignment-farm/procedure-transfer/blob/main/FINDINGS.md) ([local](../../ancillary-studies/procedure-transfer/FINDINGS.md)), at study commit `78965ca7ffd4ac9389a77505a768cf6dfd6be957`, as the completed first comparison. **Distillation acquisition failed under the tested recipe.** The user rejected treating an acceptable negative publication as a quickly executed stop condition, and the root prioritized acquisition diagnosis. The original comparison and its assessment below retain their scope; the [subsequent diagnosis](#procedure-transfer-acquisition-diagnosis) now supplies explanatory progress and a functioning acquisition regime.

The [13 September preparation](../sources/2026-09-13/README.md) selected evidence-conditioned distillation following the earlier adapter's transfer deficit. The completed study covers all four condition combinations with 16 checked calls, uses two coupled initialization/order seeds, and compares direct imitation with full-vocabulary reverse KL on checked answer prefixes and on student-generated prefixes. The secondary comparison holds the loss, teacher, evidence and training inputs fixed. All six final checkpoints preceded fresh evaluation. The development-selected teacher reminder, additional development labels and pretrained teacher capabilities are disclosed in the [protocol](https://github.com/alignment-farm/procedure-transfer/blob/main/protocol/transfer-v1.md) ([local](../../ancillary-studies/procedure-transfer/protocol/transfer-v1.md)).

The [audited outcomes](https://github.com/alignment-farm/procedure-transfer/blob/main/evidence/transfer-v1-analysis/README.md) ([local](../../ancillary-studies/procedure-transfer/evidence/transfer-v1-analysis/README.md)) are:

| Method/reference | Training-call recall, seeds 17 / 29 | Fresh-input success, seeds 17 / 29 |
|---|---:|---:|
| Direct imitation | 16/16; 16/16 | 24/96; 32/96 |
| Reverse KL, checked prefixes | 3/16; 4/16 | 3/96; 1/96 |
| Reverse KL, student-generated prefixes | 0/16; 3/16 | 0/96; 2/96 |
| Retained examples + selected reminder (one base-model reference) | 14/16 | 89/96 |
| Supplied complete rule (privileged reference) | Not measured | 65/96 |
| No acquisition (one base-model reference) | Not measured | 0/96 |

The useful teacher establishes that the evidence supports new-input behavior in this model. Both distillation variants fail largely at acquisition, so their result does not isolate a transfer failure after successful learning or student-generated prefixes as the cause. Imitation again fits demonstrations while generalizing poorly. Distillation costs more to acquire and achieves much lower accuracy; no repayment at comparable useful performance was demonstrated. The supplied-rule prompt was not optimized alongside the examples prompt, so their scores do not establish a general ordering of rules and examples.

The overall score also conceals **partial procedural transfer**. The [component audit](https://github.com/alignment-farm/procedure-transfer/blob/main/evidence/transfer-v1-components/components.json) ([local](../../ancillary-studies/procedure-transfer/evidence/transfer-v1-components/components.json)), independently reproduced by the root from saved responses, gives imitation tool-choice accuracy of 72/96 and 96/96 for seeds 17 and 29, with correct identifier transformations on only 26/96 and 32/96. Both preserve call syntax on every fresh case. This distinguishes transfer of a routing decision from reliable argument transformation and complete-call success. It motivates a controlled comparison of the operations separately and together; the existing counts alone do not establish why they differ.

**Scientific weight.** Mechanics checks establish that the specified updates occurred, but do not establish that the shared LoRA configuration and optimizer settings are suitable for reverse KL. The pilot did not develop an effective distillation acquisition recipe. Root inspection also found substantially larger gradient spikes in the distillation logs; differing objective scales and those observations do not identify a cause. Optimization, teacher distributions on incorrect prefixes and parameterization remain unresolved. This is evidence against the tested recipe, with little weight against the broader method. One synthetic procedure, four training identifiers and two coupled seeds further limit generality; the reported bootstrap intervals condition on these runs and resample identifier clusters.

**Reason for the diagnostic continuation.** Repeatedly closing minimally developed neural recipes after acquisition failure could create an apparent general advantage for explicit memory without a comparison against an adequately developed neural alternative. Keeping that caveat in the root's beliefs was insufficient progress. The two-update pilots established mechanics; separate development material supported purposeful calibration and diagnosis in the subsequent phase. The initial failures remain evidence, and a subsequently developed transfer claim needs fresh evaluation. Retention, correction and consolidation were not tested by this comparison.

**Assessment scope.** The root read the publication, protocol, development and reproduction notes, implementation, raw responses, training events and saved audits. It independently rescored all 976 responses, verified 27 evidence-manifest entries, checked paired initialization hashes and training-input orders, and confirmed that executed source snapshots match frozen commit `5f636fb2d2768d1818d53aa51928cbe043c4f2c2`. These checks passed. It did not rerun model training or inference. The native unit-test command could not start because the review environment lacked the recorded Python 3.14.7 interpreter; the study's native audit remains reported evidence. Operational details and any future repairs stay with the ancillary study.

#### Procedure transfer: acquisition diagnosis

**Root assessment — 14 September 2026.** [DIAGNOSIS.md](https://github.com/alignment-farm/procedure-transfer/blob/main/DIAGNOSIS.md) ([local](../../ancillary-studies/procedure-transfer/DIAGNOSIS.md)), published at `dcdc0d6f54dde235549f8abfba407598b6635667` with evidence at `c183674`, completes a useful bounded diagnostic contribution. It establishes a functioning soft-target acquisition checkpoint, a controlled effect of loss orientation on failed routing, and conditional separation of routing, identifier production and suffix completion. These are development and intervention results; they do not replace the accepted prospective transfer test or establish a forward-KL transfer advantage.

With common examples, teacher, initialization, input order and canonical answer prefixes, forward KL reaches 16/16 training calls at 128 updates; reverse KL reaches 4/16. From identical failed reverse-KL parameters, 128 further updates under forward KL repair routing from 8/16 to 16/16 and yield 11/16 complete calls, while the matched reverse continuation remains at 4/16. All five remaining rescue errors omit the fast suffix. Reducing the reverse learning rate tenfold does not repair acquisition within the matrix's budget. This excludes that specific rate change as a sufficient remedy, not every reverse-KL configuration.

The saved distributions identify eight teacher-clear wrong routing decisions with negligible reverse correct-logit derivatives and strong forward derivatives. The same pattern occurs in both original reverse-KL variants. These are first-position logit signals, not full parameter gradients or a complete causal account; the orientation intervention establishes recoverability beyond the observed signal contrast. A separate warm start from the acquired imitation checkpoint preserves 16/16 training recall through reverse updates, while development performance declines from 12/16 to 8/16. The usefulness of the objective therefore depends on the starting policy in this setting. Preservation under continued same-task training is not retention under unrelated learning.

The selected imitation and forward checkpoints route all 48 random-identifier development calls correctly, but complete 28/48 and 17/48 respectively. Supplying the correct route leaves identifier production weak; supplying both route and uppercase identifier permits 48/48 suffix/closing completions for each. This localizes a remaining behavioral difficulty without establishing independently learned internal modules. Prefixes supply privileged answers and can alter tokenization. The teacher makes 46/48 complete calls, with all identifiers correct. Forward's 13/16 versus imitation's 12/16 on earlier development words did not predict an advantage on these random identifiers.

Teacher error also matters: forward's training recall declines from 16/16 at 128 steps to 14/16 at 256, with the two later errors matching wrong teacher routing targets. That is consistent with fitting teacher mistakes more closely, without isolating every effect of longer training. The evidence supports functioning acquisition and a specific rescue; it establishes neither neural superiority, a capacity limit, nor universal reverse-KL failure.

**Root implications and review scope.** The diagnosis supports R1 and R3 of the [earlier procedural-learning note](../notes/PROCEDURAL_LEARNING.md#assessment-after-reading-diagnosis), partly addresses R2, and leaves R4 untested. Acquired routing can now motivate retention and revision experiments; reliable whole-call copying is not a prerequisite for studying that specific learned behavior. In the root review, 944 response records and 16 teacher records independently reproduce all 45 audited aggregate groups; 41 manifest entries, matched initialization/input-order controls and scalar derivatives at 224 saved probability records check out. The root inspected the plans and executed source snapshots but did not rerun model training or inference. The study reports native tests and reload checks. One diagnostic training seed, one small task and adaptive development limit generality. Methods, costs and evidence remain with the study.

#### Retention and correction: findings and continuation

**Root assessment — 14 September 2026.** Publication `9696af5ef32a86571b66bcedec3b3cd241aef9a0` establishes all 12 revised and 84 unaffected fresh routes after later learning and correction with filtered replay from one acquired start. Complete calls remain 19/96; five previously correct calls on unchanged old inputs become wrong. The stronger preservation claim in [R4](../notes/PROCEDURAL_LEARNING.md#assessment-after-retention-and-revision) is weakened. Correction-only learning acquires its demonstrations but overgeneralizes; replay improves locality, while also supplying boundary evidence and an investigator-provided validity filter. Both starting adapters inherit the same acquisition seed, and all subsequent training uses hard-label cross entropy. The [detailed assessment](2026-09-14-concurrent-findings.md#s2-successful-revision-does-not-establish-independent-editability) records common starts, budget effects, explicit references and independent checks.

**Root assessment of scope and rehearsal — 15 September 2026.** Publication `6e7049458732c4f3e37e5b8a3d1993129c2bdcfa` finds that four corrections plus seven crossed boundary cases produce 96/96 fresh routes in two starting states without broad history. Substituting historical examples for boundary repetitions, at the same condition exposure and update count, reduces paired complete-call losses in three starts and increases them in one. All 16 primary endpoints lose some previously correct unchanged calls. The strongest history result completes 74/96 fresh calls but still loses five formerly correct unchanged calls. Inherited CE with history leaves all four familiar scoped routes stale despite 11/12 correct fresh scoped routes. Removing obsolete records from replay is not equivalent to removing their learned effects. Two new acquisitions, including a preserved failure and bounded repair, broaden the starting states without making all four pipelines identical replications. The [detailed synthesis](2026-09-15-followup-findings.md#s2-scope-examples-can-suffice-for-routing-history-changes-other-behavior) and [R4 update](../notes/PROCEDURAL_LEARNING.md#assessment-after-scope-and-rehearsal) record the distinctions and checks.

**Root assessment of complete maintenance — 15 September 2026.** Publication `28aa881833ac2f9cf478b0d2f8a0f233ecc90023` starts from two states with 192/192 complete original-policy orders. Novel support in one state preserves 192/192 through both corrections; the other three trajectories finish 120/192, 132/192 and 130/192. Both familiar-bridged endpoints lose the entire first waiver despite relabeled rehearsal. Seven of eight newest-correction endpoints are 24/24, while one withheld acquired instance remains stale despite successful direct labels. This weakens M2 for this bridge intervention and separates new learning from accumulated-policy preservation. Complete preservation now has a functioning example, but the task removes identifier copying and does not confirm R4's original transformation-preservation claim. All correct eligibility decisions yield complete actions. The privileged maintained formal policy solves the matched sequence; no learning-cost repayment is demonstrated. See the [detailed assessment](2026-09-15-maintenance-findings.md#s2-complete-preservation-is-possible-but-familiar-support-is-not-sufficient).

**Root assessment of state and support — 15 September 2026.** Publication `3e71eb5f146e6493c60cef26d15d86dedd2249fb` crosses inherited first-revision states with current support. Diagnostic NN/NB/BN/BB complete scores are 192/122/120/120 from two 192/192 starts; the interaction is +70 orders. Fresh scores are 192/185/120/120 and 143/133/121/145, with the prespecified positive interactions +7 and +34. In the latter acquisition, Novel support helps Novel history and harms Bridged history. Fresh starting accuracies differ, so the equal-accuracy MR1 demonstration remains confined to the selected diagnostic. All twelve endpoints acquire the newest correction; earlier and unchanged obligations still fail. Both failed readiness checkpoints and all imperfect revision-1 states are retained. The [detailed review](2026-09-15-state-support-findings.md) verifies saved outcomes, controls, provenance and costs. MR2/MR3 remain untested; this phase resolves the state-versus-support ambiguity sufficiently for closure.

**Remaining question:** Can observations available before revision or after a bounded trial predict complete damage and improve a useful maintenance decision on fresh acquired states?

**Public-research update — 16 September:** P26–P28 supply closer prediction/action precedents; P35 supplies a complementary structural signal. MR2/MR3 remain local expectations, with their broad premises already studied publicly. [Direction A](../notes/RESEARCH_DIRECTION.md#a-does-a-maintenance-decision-remain-useful-after-the-learner-changes) narrows a possible contribution to usefulness across changed learner histories. It does not renew S2.

**Competing accounts:** Observable obligations may reveal differing susceptibility; alternatively, a proposed signal may miss later complete damage or cost too much to improve decisions. The interaction rules out state-only and support-only explanations for the diagnostic table, but does not identify its internal cause or a generally protective support set.

**Completed commission and possible continuation:** The [state/support brief](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/STATE_SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/STATE_SUPPORT.md)) is fulfilled. A later comparison could test a fixed observation and its decision consequences against current accuracy, known history and developed fixed support. Charge trial, verification and repair; abstaining leaves new obligations unmet unless another route supplies them. This is a research recommendation, not another assignment.

**What a continuation would add:** Prospective damage prediction or a useful action advantage beyond the now-demonstrated interaction. Supplied validity filtering and labels remain part of the treatment; successful behavior does not imply independent parameter modules.

**Evidence needed for that question:** Fresh acquired states, observations available at the decision point, consequences for new and earlier obligations, paired unchanged losses/gains, strong fixed choices and full recurring costs. The [fourth-phase publication](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/FINDINGS-STATE-SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/FINDINGS-STATE-SUPPORT.md)) is the current evidence boundary.

**Reading/implementation context:** P4's sequential editing, P6/P7's locality and retention, P9's consequence evaluation, and LOKI's preservation objective are relevant prior art. The study's [maintenance methods](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/notes/maintenance-methods.md) ([local](../../ancillary-studies/procedure-retention-and-revision/notes/maintenance-methods.md)) and [source record](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/sources/README.md) ([local](../../ancillary-studies/procedure-retention-and-revision/sources/README.md)) document its later versioned methods and author-code inspection; the root's original LOKI reading was abstract-only. No author editing algorithm is reproduced locally.

### S3. When does deeper neural memory repay its harder update problem?

**Status:** The [neural-memory-depth investigation](https://github.com/alignment-farm/neural-memory-depth/blob/main/README.md) ([local](../../ancillary-studies/neural-memory-depth/README.md)) is complete as a bounded contribution, published and assessed on 13 September 2026. Its [FINDINGS.md](https://github.com/alignment-farm/neural-memory-depth/blob/main/FINDINGS.md) ([local](../../ancillary-studies/neural-memory-depth/FINDINGS.md)), at study commit `4a8dfd1299d11478635e6a13f5fb64564269ba61`, is the accepted local publication. The original cross-paper question remains open. No further experiment or separate manuscript is required to complete this contribution.

**Root assessment — 13 September 2026.** The [written comparison](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/INITIAL_COMPARISON.md) ([local](../../ancillary-studies/neural-memory-depth/notes/INITIAL_COMPARISON.md)) and [configuration follow-up](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/CONFIGURATION_FOLLOWUP.md) ([local](../../ancillary-studies/neural-memory-depth/notes/CONFIGURATION_FOLLOWUP.md)) exclude two simple explanations of the reported contrast: Titans v1's depth sweep uses memory without attention, and Modular TTT's negative depth trend survives nonzero initialization and its reported stability variants. Architectures and update schedules still differ. The later Titans paper's general 16-token update chunk is not a verified setting for its depth figure; the exact depth-run recipe and original-checkpoint mapping remain incomplete. The comparison narrows the uncertainty without resolving it.

The [graph audit](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/GRAPH_EXECUTION_AUDIT.md) ([local](../../ancillary-studies/neural-memory-depth/notes/GRAPH_EXECUTION_AUDIT.md)) identifies an omitted fast-weight derivative during outer differentiation in the pinned Modular TTT implementation. Source-loaded deep cases disagree with the reference derivative while shallow controls agree; completing the derivative agrees with finite differences and preserves numerical forward outputs. Intent is unknown, and explicit CPU kernel substitutions limit the implementation claim. The subsequent [recall pilot](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/RECALL_PILOT_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/RECALL_PILOT_RESULTS.md)) and [refresh comparison](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/REFRESH_COMPARISON_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/REFRESH_COMPARISON_RESULTS.md)) find no consistent final recall benefit from completing the derivative or increasing gradient-refresh frequency. Some trajectories change substantially, but this does not establish an error in either paper's reported results.

The strongest behavioral evidence concerns **interactions among initial representations and the training stream**. A [10×10 crossing](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/SEED_SEPARATION_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/SEED_SEPARATION_RESULTS.md)) separates whole-model initialization from training-example sampling and ordering; neither factor alone explains the outcomes. [Reciprocal group swaps](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/GROUP_SWAP_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/GROUP_SWAP_RESULTS.md)) then localize strong effects to initial embeddings. In the [query/key/value factorial](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/EMBEDDING_SWAP_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/EMBEDDING_SWAP_RESULTS.md)), replacing only queries or only values from selected donor 11 into donor 16's background changes low-loss success from 0/10 streams to 10/10. Combining those replacements gives only 1/10; replacing keys as well restores 10/10. Both derivative modes give this pattern. These interventions demonstrate compatibility effects for particular tensors and conditions. They supply neither a universal ranking of embeddings nor a complete account of the training dynamics; initial query–key cosine alignment alone cannot explain the results.

The [post-hoc checkpoint inspection](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/RETRIEVAL_MODES.md) ([local](../../ancillary-studies/neural-memory-depth/notes/RETRIEVAL_MODES.md)) finds distinct value-confusion and key-confusion patterns, leaving some failures unclassified. [Six frozen-feature linear-readout fits](https://github.com/alignment-farm/neural-memory-depth/blob/main/notes/FROZEN_READOUT_RESULTS.md) ([local](../../ancillary-studies/neural-memory-depth/notes/FROZEN_READOUT_RESULTS.md)) preserve the selected ambiguities while successful controls retain full recall. Readout initialization can influence joint learning, while the tested later linear refit leaves these selected retrieval failures unresolved. The supported description is partial retrieval at a fixed training horizon. These probes do not establish irreversible information loss, stable attractors, or inability to recover through longer training or a different decoder.

The theoretical update is that **architectural memory capacity and the capacity a training procedure learns to use require separate evidence**. The same deeper architecture supports full recall under other tested initial conditions, so the observed failures are not an unavoidable capacity limit on this task. The tested shallow baseline also reaches full recall: this study locates difficulties in learning to use deeper memory, without demonstrating a benefit from depth. The result refines our starting emphasis on write dynamics to include the learned representations and their joint training with the reader.

**Limits and assessment scope.** The deeper synthetic model has 1,196 parameters and trains for 600 updates. Later interventions use selected donors and previously inspected evaluation mappings; they are adaptive mechanism investigations, not independent donor/task replications. Within-depth interventions hold architecture fixed, while earlier cross-depth comparisons are not parameter-matched and fixed training events do not establish compute matching. CPU results do not establish fused CUDA/BF16 parity. The study's saved verification records support reproducibility within that scope. The root reviewed the publication, linked comparisons, protocols, diagnostics and saved summary/verification records; it did not rerun the experiments, independently rescore checkpoints, or audit the original papers' model runs. Methods and evidence remain in the ancillary directory.

**Remaining question:** Under which inner updates, representations and outer training conditions can additional fast factors deliver useful capacity, and when does that repay their cost? Relating this local result to the published depth curves still requires the missing configurations and a meaningful comparison of tasks, parameters and compute. Generality of the representation interaction is a separate uncertainty. These are open research directions, not a commissioned continuation; the current publication is sufficient for root synthesis.

### S4. What does learned memory lose when the future goal changes?

**Status — 15 September 2026:** All three goal-shift publications are accepted. The latest [cross-event study](https://github.com/alignment-farm/memory-under-goal-shift/blob/main/future-use/FINDINGS.md) ([local](../../ancillary-studies/memory-under-goal-shift/future-use/FINDINGS.md)) extends information/reader distinctions to composed targets absent from writer training. Its [third-phase commission](https://github.com/alignment-farm/memory-under-goal-shift/blob/main/FUTURE_USE.md) ([local](../../ancillary-studies/memory-under-goal-shift/FUTURE_USE.md)) is complete. A further extension needs a consequential new uncertainty rather than automatic renewal.

**Root assessment — 14 September 2026.** Publication `968c4d89960ef54849dc3625b2a9991cde128cae` learns representations with successful expected-goal acquisition. At eight slots, a replacement reader reduces changed-query MSE from 0.909 to approximately 4.65 × 10⁻¹² on the same frozen states. At four slots with independent fields, changed-query error remains approximately 1, as the conditional-covariance calculation predicts. Thus unsuccessful reading and unavailable information are distinct. The linear Gaussian setting, fixed addressing and full-rank inverse make this a controlled illustration rather than a difficult new recovery principle. A stronger explicit pair-sum control matches broad learned compression on correlated fields; payload equality is not total-cost equality. The [detailed assessment](2026-09-14-concurrent-findings.md#s4-unavailable-information-differs-from-an-unsuccessful-reader) records knowledge timing, qualifications and matrix checks.

**Root assessment of the nonlinear follow-up — 15 September 2026.** Publication `0d516aaa82d30d07e239b44e88ac43b5fdbfddef` acquires parity tasks at four bits per record but uses only 9–12 of 16 possible codes. Exact enumeration gives changed-field MSE 2.384825 = 0.350000 collision uncertainty + 2.034825 reader excess. A fitted reader approaches the irreducible term from the same frozen states. Broad raw reconstruction and explicit full records recover both families. The alternative reader estimates each target directly rather than multiplying raw-field estimates, so recovery changes the answering rule as well as fitting its parameters. Two-bit joint acquisition fails despite a successful privileged factorization diagnosis; the tightly constrained comparison between equally functioning learners remains unresolved. All 16 record types occur in training; new histories are not new goal structures. The [detailed synthesis](2026-09-15-followup-findings.md#s4-a-nonlinear-memory-can-lose-information-and-misread-what-remains) records these limits and independent enumeration/network checks.

**Root assessment of later compositions — 15 September 2026.** Publication `981719ffcda62fed0913461b50c0e97dbb4c10c8` reuses accepted four-slot writers on 32-event independent histories. Two- and four-event parity and cross-event two-field agreement were absent from writer training; supplied operations let readers answer them from retained components. Fitted same-state readers reduce parity MSE from 1.820447/2.422528 to .387176/.511742. Exact query-relevant collisions remain in three of five narrow writers, while two retain everything needed by these questions despite losing other raw fields. Broad and full explicit storage solve all tasks. Correct within-record joint moments matter for relational reading; marginal estimates alone add avoidable error. M3 receives bounded support, not evidence of learned operators, unfamiliar atomic records or storage economy. The [detailed assessment](2026-09-15-maintenance-findings.md#s4-availability-is-relative-to-the-question-and-its-read-computation) records exact bounds, access and independent checks.

**Remaining question:** How does useful recovery change when histories have dependencies or the reader must acquire operations, rather than receiving independent records and supplied query algebra?

**Public-research update — 16 September:** P33 supplies an existing example of learning access to retained records. Its memory-stability assumptions connect to the independent placement question; a generic learned retriever is not a new S4 contribution. The completed information/reader distinction remains useful without an automatic extension.

**Competing explanations:** The learned objective preserves broadly reusable evidence; alternatively, it allocates capacity toward expected queries and discards rare but later decisive details. More expensive explicit retention may succeed simply because it preserves more information.

**Candidate continuation, not commissioned:** Introduce one consequential dependency or read-learning contrast, if it would separate new explanations. Preserve full-evidence competence and same-state reader comparisons; disclose what the writer, reader and investigator know. The present independent-history result already answers its bounded compositional question.

**What a continuation would add:** Evidence beyond the factorization that makes current full-history uncertainty exactly calculable. Increasing independent-history length alone does not address that gap. Finite failed probes still cannot establish information absence.

**Evidence to collect:** Expected-goal and changed-goal accuracy, exact evidence availability, latency, and retained-state size. For TTCD-like methods, charge the teacher computation and history it needs. Full-context success checks that the task is answerable. If both neural and explicit compression fail similarly at matched constraints, the limiting factor may be capacity or task uncertainty.

**Reading/implementation needed:** P11's teacher windows and causal update timing; P8's held-out query construction; P13's query access. P10's results and [M+, 2502.00592v2](https://arxiv.org/abs/2502.00592v2), currently abstract-reviewed, are relevant alternatives before inventing recovery machinery.

### S5. When should a useful temporary update be retained or consolidated?

**Status — 15 September 2026:** S1/S2/S4 now report acquisition, use and maintenance costs for completed third phases. None demonstrates learning-cost repayment at comparable complete quality. S5 remains an active research question; no separate retain/reset/consolidate project is commissioned.

**Direction update — 16 September:** P29/P30 supply learned-storage methods, P31 a substrate comparison, P32 a consolidation architecture and P33 learned access to explicit evidence. The next root preparation prioritizes [useful lifetime before revision](../notes/RESEARCH_DIRECTION.md#b-when-does-a-learned-memory-component-repay-its-cost-before-it-needs-revision), using published comparators and a workload with consequential reuse and change. Local absence of repayment is not a general negative result about learned memory.

**Prepared study — 16 September:** [Memory placement under revision](https://github.com/alignment-farm/memory-placement-under-revision) ([local](../../ancillary-studies/memory-placement-under-revision/README.md)) takes up that comparison. EARM is the first implementation lead, with a versioned τ-bench document subset and competent explicit controls. The question separates content changes from changed evidence needs; learned-content methods remain conditional on feasibility. P36–P38 narrow overlap further. No ancillary session or model run was started during preparation. The broader retain/reset/consolidate alternatives below remain possible research directions, not a requirement to implement them all in this first study.

**Status after handoff:** The user reported the placement study was underway. The root wrote the original [adaptation expectations](../notes/ADAPTATION_DECISIONS.md#three-predictions-and-their-possible-failures) without reviewing its unpublished results.

**Publication accepted — 16 September:** The [root assessment](2026-09-16-placement-findings.md) accepts the [completed findings](https://github.com/alignment-farm/memory-placement-under-revision/blob/main/FINDINGS.md) ([local](../../ancillary-studies/memory-placement-under-revision/FINDINGS.md)). Account-aware lexical retrieval matches full reranking at 127/128 complete answers; retained/invalidated EARM score 120/121 with additional work. Learned score predictions persist through content edits better than changed evidence needs, but do not establish useful repayment. Most answer failures are truncations; the combined-change branches have no answer-changing targets. The bounded phase is complete, while broader crossover and learned-content questions remain open.

**Related study and scope:** [Procedure acquisition and reuse](https://github.com/alignment-farm/procedure-acquisition-and-reuse/blob/main/README.md) ([local](../../ancillary-studies/procedure-acquisition-and-reuse/README.md)) found no acquisition-cost repayment at comparable useful accuracy. The [third-phase assessment](2026-09-15-maintenance-findings.md#assessment-of-the-prospective-expectations) adds actual recurrence, revision and recovery costs. S1's same-record indexed archive, S2's privileged formal policy and S4's direct raw store have distinct information access; their results are not one common memory-format trial. Reset-and-relearn, consolidation and a useful cost crossover remain unestablished.

**Question:** Across recurring tasks and changing facts, when is it worth carrying an adapter, consolidating its stable content, or reconstructing it from explicit evidence?

**Competing explanations:** Recurrence amortizes acquisition and consolidation; revision costs and interference erase that advantage. A merged update may only change its packaging, with no improvement in capability.

**Possible comparison:** Use a mechanism that has demonstrated acquisition in S2 or existing work. Compare reset-and-relearn, retain separately, a specified consolidation method, and explicit memory across varied recurrence and revision rates. Distinguish algebraically merging an adapter from training a durable policy: they are different interventions. Keep source evidence accessible under disclosed costs rather than granting one branch a free archive.

**What it adds:** A measured decision boundary for a stated workload and mechanism, not the generic claim that reuse amortizes cost. P10 and model-editing work make “merge memory into weights” insufficient novelty by itself.

**Evidence to collect:** Cost at matched useful performance, acquisition, inference, state storage, reconstruction, correction, and collateral repair. Preserve latency, token counts, and compute separately unless a disclosed conversion combines them. A finite workload may never repay consolidation; that is a useful bounded result.

**Reading/implementation needed:** P10's lifecycle and compression details; P7's routing/merging; P16's separate adaptation/evaluation accounting. The existing compute-allocation paper supplies an alternative investment, not a universal cost conversion.

### Executable experience retention

**Status — 17 September 2026:** Prepared and commissioned as an independent
bounded investigation in
[executable-experience-retention](https://github.com/alignment-farm/executable-experience-retention)
([local brief](../../ancillary-studies/executable-experience-retention/README.md)).
Preparation commit `34a902fedf99a22fff3c9429d49146809af8a86a` is the root's current
boundary; it contains no findings. No investigator session or model run was
launched during preparation. Ten earlier projects retain their completed phases.

**Question:** What does retaining acquired implementation add to competent
reconstruction from shared procedural experience, in complete future behavior
and actual work? The [comparison](../notes/EXECUTABLE_COMPARISON.md) distinguishes
execution, preserved information and avoided reconstruction. Existing source
may be loaded directly; code hidden in logs remains available implementation.

SkillCraft and SkillWeaver are possible method donors, with pinned limits in
the [reading ledger](../sources/2026-09-17-persistence-controls/README.md).
The investigator owns workload discovery, development and diagnosis. Equal
checking, competent contextual alternatives and full-sequence costs support
the allocation claim. Stable reuse comes first; consequential revision is a
conditional extension. EX1–EX3 are preserved verbatim in the brief and remain
untested locally. An explanatory tie or explicit alternative is useful progress.

<a id="what-the-three-completed-investigations-change"></a>

### What the completed investigations change

The investigations examine different mechanisms and tasks. Together they sharpen the claims required to answer where experience should live:

| Investigation | Distinction supported by the bounded evidence | Implication for the root question |
|---|---|---|
| Update-source selection (S1) | Source reliability differs from its value as training material; changing loss or generation need not change task success. | A trustworthy record alone does not tell us whether training on it is useful. |
| Procedure acquisition and reuse (relevant to S2/S5) | Recall of demonstrations differs from transfer to new inputs; cheaper repeated inference need not repay acquisition at comparable useful accuracy. | Retaining a parameter update is valuable only to the extent that its learned behavior serves the later workload. |
| Procedure transfer and acquisition diagnosis (relevant to S1/S2) | Loss orientation and starting policy affect acquisition; a controlled objective switch repairs failed routing. Acquired routing transfers more reliably than identifier production. | Useful learning depends on the update and learner state as well as the evidence. A learned relation supplies a subject for retention and correction even while complete actions remain imperfect. |
| Neural memory depth (S3) | An architecture's capacity differs from the retrieval behavior its joint training reaches; individually helpful initialization changes can interfere when combined. | The writer, representations, reader and training conditions must be considered together when assessing usable memory. |
| Experience selection (S1) | Damage-aware replay improves acquisition uses but not recurrence or preservation over a developed mixture; fixed stopping can freeze incomplete acquisition. | Evaluate the sequence of useful behavior and selection costs, not just final accuracy or exposure to all rules. |
| Procedure retention and revision (S2) | Controlled crossings identify an interaction between inherited state and current support; the predicted direction holds in fresh acquisitions, and one support preference reverses between histories. | Current evidence has training value relative to the state receiving it. Present competence and correct rehearsal do not determine maintainability. |
| Memory under goal shift (S4) | Later compositions expose query-relative omissions and avoidable reader error; broad retention and explicit records support all tested queries. | A representation can lose raw details yet remain sufficient for a particular later use; supplied read operations are part of the capability. |
| Maintenance-decision transfer | Match-history reaches the two-support aggregate bound on fresh acquisitions, while all endpoints remain incomplete and explicit examples solve the task. | A transferable chooser cannot compensate for inadequate actions; aggregate ties can hide consequential obligation failures. |
| Evidence use under revision | One checkpoint improves complete evidence use through corrections; longer acquisition reverses the benefit. Its measured training/use time beats an uncached lesson, with substantial limits. | Learned behavior can outlive changed values; acquisition duration, contextual efficiency and checkpoint selection remain part of allocation cost. Supplied execution is a different acquisition claim. |
| Memory placement under revision (S5) | Learned relevance-score prediction survives some content edits without improving complete quality over direct account-aware access; context selection also affects answer completion within budget. | Persistent structure can be learnable without being worth learning for the task and its available alternatives. |

This is a synthesis of distinct local findings, not evidence that the adapter's transfer deficit and the deeper memory's partial retrieval share a cause. The experiments also concern different persistence boundaries: training a fast-memory system to learn within sequences does not demonstrate accumulation of experience across agent sessions. S3's successful synthetic recalls supply no placement or acquisition-cost comparison against accessible explicit evidence.

The [first concurrent round](2026-09-14-concurrent-findings.md), [follow-ups](2026-09-15-followup-findings.md) and [third phases](2026-09-15-maintenance-findings.md) provide functioning acquisition, complete procedural maintenance and later compositional use. The [fourth S2 phase](2026-09-15-state-support-findings.md) identifies an interaction underlying some maintenance divergence. The [placement study](2026-09-16-placement-findings.md) adds a bounded case of useful statistical prediction without competitive deployment value. These are substantive results after purposeful diagnosis. No generally superior memory format or common internal failure cause follows. The procedural tasks still share a model family and remove identifier copying, while S4 uses familiar independent records and supplied operations.

Where experience lives is part of a larger decision about what to change and preserve. The relevant system includes learned behavior, supporting evidence, update decisions and the read or execution procedure. S5 has no demonstrated useful-cost crossover; the later [evidence-use comparison](2026-09-17-evidence-use-findings.md) adds a favorable measured candidate result against an uncached lesson, without full-cost repayment over supplied execution. The root's working question remains conditional: **which mechanisms produce useful, transferable and maintainable behavior on a specified workload, and when is maintaining that behavior preferable to retaining and reasoning over explicit evidence?**

<a id="6-suggested-order-for-discussion"></a>

## 6. Research selection

**Commissioning decision — 17 September:** Following the user's direction to
continue, the root prepared and published the private
[executable-experience-retention repository](https://github.com/alignment-farm/executable-experience-retention).
Its bounded investigation is commissioned; preparation has not launched an
investigator or experiments. Workload discovery and operational decisions belong
to that study. This advances the recommendation below without reopening any
completed phase or changing the enduring directive.

**Latest independent selection — 17 September:** The
[persistence comparison](../notes/EXECUTABLE_COMPARISON.md) retains bounded independent
development of implementation versus reconstruction from shared experience. New
primary reading and pinned SkillCraft inspection establish closer overlap than
the [earlier artifact review](2026-09-17-executable-feasibility.md) captured.
Separate execution benefits, retained information and avoided reconstruction;
permit direct loading when source is available. Efficient contextual delivery,
equal acquired feedback and costs on the full request sequence strengthen the
comparison. Generic donor search is complete. That preparation itself commissioned
no experiment; the subsequent decision above hands workload development to the
independent investigator. No completed phase is reopened.

**Latest publication assessment — 17 September:**
[Evidence use under revision](2026-09-17-evidence-use-findings.md) is accepted at
`da1233fdfb26fe6c5daa337a3dbf9f784f34f9f7`. Varied 128 scores 65/96 through
corrections versus the stronger lesson's 61/96; measured training plus use is
108.58 seconds versus 121.16 seconds. Later acquisition regresses to 45/96.
Limited transfer and durability support EU1 and part of EU2; EU2's history
mechanism remains unresolved. EU3 has a narrow measured candidate example, with
cache, output-length, checkpoint-selection and construction/repair limits.
Supplied execution completes 96/96. The phase is complete; no follow-up is
commissioned.

**Historical selection after nine publications — 16 September:**
[Reusable evidence use under revision](../notes/EVIDENCE_USE.md) compares the
useful lifetime of learned behavior with retained contextual lessons while
current evidence receives successive authoritative corrections. The note audits
what local explicit alternatives receive, assesses six public precedents,
compares candidates and records new EU1–EU3 expectations. The user subsequently commissioned a bounded independent investigation in
[evidence-use-under-revision](https://github.com/alignment-farm/evidence-use-under-revision).
Its [17 September publication assessment](2026-09-17-evidence-use-findings.md)
now accepts the bounded phase. S2/S4/S5 remain complete.
The [reading ledger](../sources/2026-09-16-evidence-use/README.md) distinguishes
inspected methods, author results and uninspected leads. AD1–AD3 are preserved.

**Preceding publication assessment — 16 September:**
[Maintenance-decision transfer](2026-09-16-maintenance-transfer-findings.md) is
accepted and its bounded phase complete at `be7a508bfea002baceec72f32f7f9d6f73f7861a`.
Known history selects the best aggregate support on two fresh acquisitions, but
neither support maintains the complete task. Observation controls were constant;
paid validation reveals obligation differences even when aggregate scores tie.
The explicit example table supplies a working alternative. AD2's predicted
aggregate observation rescue is not supported here, with important calibration
limits. No follow-up experiment or automatic selector expansion is commissioned.

**Root work developed during execution:** While maintenance-decision-transfer
ran, the root developed an independent [research question](../notes/RESEARCH_DIRECTION.md#root-work-while-maintenance-decision-transfer-runs)
concerns feedback for learning useful retention and intervention choices (AD1).
The [feedback comparison](../notes/FEEDBACK_DECISIONS.md) and subsequent
[bounded feasibility assessment](2026-09-16-remedy-feasibility.md) do not select
a new experiment from S4 or the inspected public artifacts. S4 lacks the proposed
retrieval remedy; P53 already learns retrieval strategy from outcomes. The
specific AD1 comparison remains open, while this feasibility phase is complete.
No unpublished study results were read and no additional experiment is commissioned.

**Historical commissioning decision — 16 September:** The user approved proceeding
with the recommended bounded comparison. The independent
[maintenance-decision-transfer repository](https://github.com/alignment-farm/maintenance-decision-transfer)
([local brief](../../ancillary-studies/maintenance-decision-transfer/README.md))
was prepared and its first phase commissioned. It tested known-history rule transfer
and the added value of paid observations on separately acquired learners, with
direct-validation and explicit-evidence controls. The investigator owns methods,
resource sizing and execution. Preparation launched no model run or ancillary
session; the eight published projects remain completed bounded contributions.

**Concrete preparation — 16 September:** The
[maintenance comparison brief](../notes/MAINTENANCE_COMPARISON.md) recommends a
bounded independent test of history-rule transfer using newly acquired learners
on the established work-order task. A simple rule matching current support to
recorded revision history retrospectively matches the state oracle across all
six published starts. It is a strong no-probe comparator, not a fresh transfer
result. The [preparation ledger](../sources/2026-09-16-maintenance-preparation/README.md)
records the unchanged S2 review boundary, recalculation and public method checks.
The next empirical choice is more specific; no new study or phase is commissioned.

**Independent theory extension — 16 September:** The
[maintenance-decision extension](../notes/MAINTENANCE_DECISIONS.md#when-observation-can-change-the-decision)
and [source review](../sources/2026-09-16-decision-value/README.md) add P46/P47:
decision-focused learning and costly observation selection. They narrow the
next comparison to whether affordable observations recover consequential action
differences across learner histories. Absolute forecast drift can leave the
best action unchanged; competent fallback changes the value of observing it.
These are analytical deductions and constructed examples, with no new empirical
result, ancillary review or experimental commission.

**Third-phase assessment — 15 September 2026:** The three broader phases are complete and accepted in the [maintenance synthesis](2026-09-15-maintenance-findings.md). The [program note](../notes/LEARNING_MAINTENANCE.md) preserves their original commissions and M1–M3 expectations and appends their assessment. That review did not commission another round.

**Subsequent decision — 15 September 2026:** The user agreed to stand down the three experimental phases and approved maintenance reliability as the next root focus, with useful placement governing the investment. The [reliability note](../notes/MAINTENANCE_RELIABILITY.md) proposed a state/support crossing, distinguished damage prediction from useful decisions, and recorded prospective MR1–MR3 expectations. At that point the evidence did not isolate inherited-state effects from current support. The note itself did not renew a local commission.

**Commissioning decision — 15 September 2026:** Following the reliability note, the user approved the next step. S2's [STATE_SUPPORT.md](https://github.com/alignment-farm/procedure-retention-and-revision/blob/main/STATE_SUPPORT.md) ([local](../../ancillary-studies/procedure-retention-and-revision/STATE_SUPPORT.md)) commissioned the identifying comparison and a bounded fresh assessment, primarily addressing MR1. That handoff authorized local execution and did not itself run experiments.

**State/support assessment — 15 September 2026:** The [state/support phase](2026-09-15-state-support-findings.md) is complete and accepted. Its diagnostic supports MR1, while fresh acquisitions extend the interaction without replicating equal starting accuracy. MR2/MR3 remain untested locally. That assessment recommended prediction and decision work without commissioning another phase.

**Earlier research selection — 16 September 2026:** The [placement publication](2026-09-16-placement-findings.md) is accepted and its bounded phase complete. The [maintenance-decision note](../notes/MAINTENANCE_DECISIONS.md) develops the independent comparison across learner histories. The [research-selection note](../notes/RESEARCH_DIRECTION.md#assessment-after-publication) records the placement outcome, and the [adaptation synthesis](../notes/ADAPTATION_DECISIONS.md#assessment-after-the-placement-publication) assesses it against preserved expectations. Its limitations alone do not confer priority on another round; no completed study receives a new phase through this work.

| Question | What the completed phase changes | Recommended research direction |
|---|---|---|
| **S1: selection and recurring learning** | Damage-aware replay helps acquisition but performs worse during recurrence, with more losses and extra work. Fixed stopping can preserve an incompletely acquired state. | Determine whether observable signals track complete-task damage or justify learning/abstention at useful cost. Distinguish protection from acquisition gains. |
| **S2: complete procedural revision** | State and support interact, with the predicted direction in two fresh acquisitions. A support preference reverses between histories, and one acquisition has no fully preserving choice. | **Phase complete.** Test whether affordable observations predict complete damage and improve a useful maintenance action on fresh states, if commissioned. |
| **S4: later combinations and relations** | Query-relative information loss and reader failure coexist for targets absent from writer training; competent explicit records match broad retention. | The present question has a bounded answer. Continue only with a consequential uncertainty, such as dependent histories or acquired read operations. |
| **S5: useful placement** | Learned score prediction works but direct explicit access matches or exceeds complete quality without scoring calls. Broader public positive results remain relevant. | **Bounded phase complete.** A future placement comparison must address a consequential unresolved need; learned content, longer reuse and joint revision remain open without an automatic continuation. |

The complete-task milestone has been met within small controlled workloads. Both procedural studies score state consequences; S4 answers composed queries. The next contribution should distinguish an explanation or establish a useful decision boundary. Simply making a task larger, repeating a mechanism demonstration or tuning until a learned method wins would not do that. Broader generality still requires evidence beyond these finite rules, model family and supplied operations.

The root develops theory and predictions while each ancillary investigator owns methods, workload development, diagnosis, resources and publication. Independent questions can proceed concurrently; an acquisition or implementation problem in one does not block another. Prospective expectations remain identifiable even when contradicted. The [M1–M3 assessment](2026-09-15-maintenance-findings.md#assessment-of-the-prospective-expectations) records mixed or adverse evidence for the procedural hypotheses and bounded support for the future-use account. The [procedural update](../notes/PROCEDURAL_LEARNING.md#assessment-after-complete-procedural-maintenance) distinguishes a new complete-preservation example from confirmation of R4's stronger original claim.

**S5 remains an open research question; its placement phase is complete.** Its completed comparisons do not demonstrate repayment against competent explicit alternatives at comparable complete quality. The later evidence-use phase has a narrow favorable measured cost against an uncached contextual lesson; full-cost advantage over supplied execution remains absent. Further placement claims need consequential evidence-access or maintenance costs, competent explicit controls, and disclosed privileges. Retain acquisition, prediction, rehearsal, verification, reading, repair and inference in their native units; separate executing a selected method from the full experimental search. Neither a separate consolidation repository nor a neural advantage is required. S3's bounded contribution remains complete.

Shared-machine coordination remains local: independent reading and analysis can proceed while investigators avoid conflicting heavyweight jobs. The [resource notes](../AGENTS.md#model-resources) identify the preferred serving machine; serving alone is not gradient access. S1/S2 used the demonstrated native MLX route, while S4 reused trained donors for CPU analysis. Those routes do not establish feasibility or budgets for every future mechanism.

## 7. Search scope and remaining uncertainty

This is a focused map, not an exhaustive novelty review. On 10 September 2026, we followed the original bibliography, inspected the primary full-text sections identified above, and used the arXiv query API for adjacent discovery and version metadata. API requests used one connection at a time, were spaced by more than three seconds, and used the descriptive User-Agent `Construct-2 literature mapping (local research metadata cache)`. Temporary responses were cached outside the notes directory; the durable review is this file and its versioned citations.

The discovery searches were:

- `ti:"Self-Adapting Language Models" OR ti:"Test-Time Training" OR ti:"Lifelong Knowledge Editing"`, first 35 results by descending submission date.
- `ti:MQuAKE OR ti:Locas OR ti:PERK OR ti:MEMORYLLM`, first 15 results by descending submission date; unrelated name matches were excluded.
- A batch `id_list` query verified the selected adjacent versions, including WISE, TTT layers, SEAL, TT-SI, Beyond Perplexity, TTCD, VANE, Modular TTT, Self-Guided TTT, LOKI, the TTT safety paper, and the decision-theoretic paper.

B0 additionally uses the original [LoRA paper, 2106.09685v2, §4.1](https://arxiv.org/html/2106.09685v2) for its factorized update equation. Its scalar calculations and two-slot latent-memory illustration are educational constructions, not additional literature findings or experimental replications.

These bounded searches can miss older work, different terminology, and later follow-ups. In particular, procedural editing, continual meta-learning, and adaptive update-source selection deserve a focused search when we choose a study. “Explicitly open in P3” means open in that paper, not proven open across all subsequent literature. None of S1–S5 is labeled a confirmed novel contribution.

On 13 September, the [focused acquisition-methods reading](../sources/2026-09-13/README.md) added P17/P18 and revisited P4/P8. Its attempted API discovery returned rate-limit errors and supplied no search results; the reading followed versioned primary HTML and references already identified in the local study. Procedure transfer therefore began with specific method leads and substantial known overlap. Its [14 September source note](https://github.com/alignment-farm/procedure-transfer/blob/main/sources/README.md) ([local](../../ancillary-studies/procedure-transfer/sources/README.md)) adds versioned primary-method and author-code reading for its local adaptation; neither review establishes comprehensive novelty coverage. A newly selected question needs its own focused source assessment.

The root's [14 September reading record](../sources/2026-09-14/README.md) adds the positive demonstrations used in the procedural-learning note. Its single API attempt returned HTTP 429 and stopped without metadata results; targeted web discovery and primary full text supplied the reading. P19 uses the published journal article; P20 uses the identified arXiv version. This selected reading does not establish coverage of later compositionality work or a preferred local implementation.

On 15 September, follow-up synthesis added P21/P22 through the S1 study's cached NeurIPS 2019 methods text and [artifact ledger](https://github.com/alignment-farm/experience-selection/blob/main/sources/followup-rehearsal/README.md) ([local](../../ancillary-studies/experience-selection/sources/followup-rehearsal/README.md)). No new arXiv discovery was conducted for this synthesis. This focused inspection identifies established rehearsal/interference ideas; it does not evaluate their author implementations or establish current literature coverage.

The later 15 September maintenance review inspected the studies' new local methods and provenance records. S1 now adapts MIR after inspecting pinned author code; S2 records versioned editing-method inspection; S4 reuses accepted writers and cached TTT reading. This root synthesis added no new public-literature search and makes no new novelty claim.

Subsequent root preparation on 15 September added P23–P25 through one successful arXiv title query and targeted primary-method reading. The [retrieval record](../sources/2026-09-15-maintenance-reliability/README.md) preserves the eight returned entries, exact versions and scope. This is selected overlap checking, not a systematic search of later interference-control or decision-policy methods.

The [16 September discovery record](../sources/2026-09-16-research-direction/README.md) adds three broad API searches, one selected-metadata request, supplementary web discovery and targeted primary-method reading for P26–P35. It changes research selection, rather than only adding citations to the prior plan. Bounded result counts and selective follow-up still preclude a comprehensive novelty claim.

The subsequent [adaptation-decision record](../sources/2026-09-16-adaptation-decisions/README.md) adds two selected-metadata requests, one bounded discovery request, supplementary searches and targeted reading for P39–P45. It separates inspected methods from abstract leads and title screening. Direct precedents narrow claims about learned memory operations, online policy adaptation and model–harness development; the broader intervention-selection question remains a comparison to specify, not a certified literature gap.

The earlier abstract review remains historical background. This file now owns the working paper/question/study map; subsequent assessments and discussion should update it here.
