**Much of the original question list is already background knowledge or an active research topic.** This revision separates that background from narrower questions that could justify ancillary work. It builds on the [Construct synthesis](../notes/PREVIOUS_RESEARCH.md) and [research perspective](../notes/RESEARCH_PERSPECTIVES.md), with priority given to neural memory, live weight updates, and learned memory policies. Executable skill libraries remain background; see the [research preference](../sources/README.md#research-preference-to-date).

This map connects the root's questions, ancillary publications and current experimental directions. Four projects have published bounded contributions; procedure-transfer's additional diagnosis establishes functioning acquisition and a controlled repair of failed routing. The [synthesis below](#what-the-completed-investigations-change) connects their implications without assigning them a common failure mechanism. [Current selection](#6-research-selection) commissions three independent projects under S2, S4 and S1 for concurrent investigation. Their directories are prepared; experiments were not started during preparation. Read each study's own directory for its latest work. “Candidate extension” means a comparison is not established by the specific evidence reviewed here; it does not mean nobody has studied it. A useful replication or explanation can proceed without a novelty claim. A proposed new contribution needs its closest methods and evaluation settings checked before we call it new.

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

**Empirical connection — 10 September 2026.** The ancillary [feasibility report](../../ancillary-studies/update-source-selection/output/pdf/update-source-selection.pdf) makes part of this distinction concrete: its final native Qwen3-4B comparison reports lower second-step loss in 72/72 updated branches and changed generation token streams in 288/288 matched action calls, while all sources and no update complete 24/24 retrieval legs. Changed generation streams do not imply changed task actions. Every action still receives the full historical evidence, so this comparison does not establish retention after removing the training information. See [S1](#s1-can-an-agent-choose-which-experience-to-train-on-during-an-episode) for our assessment and the study's [results and reproduction note](../../ancillary-studies/update-source-selection/notes/2026-09-10-interface-results.md) for evidence and limitations.

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

The [13 September methods review](../sources/2026-09-13/README.md) records the added reading and the selection rationale for procedure transfer. P17/P18 are additions to the original paper map; this is not a claim of comprehensive or latest-version coverage.

The [14 September positive-demonstration review](../sources/2026-09-14/README.md) adds P19/P20, revisits P4's adaptation results and extends P8 reading through §5.1/Table 1. It supports the root's [procedural-learning predictions](../notes/PROCEDURAL_LEARNING.md#predictions-before-the-next-findings), without claiming these preparations have been reproduced locally.

Additional existing background: [Reflexion v4](https://arxiv.org/html/2303.11366v4) §§3–4 explains bounded reflection buffers and repeated trials; [TT-SI v1](https://arxiv.org/html/2510.07841v1) Algorithm 1 restores the original parameters after instance-specific adaptation. [DeepSeek-R1 v2](https://arxiv.org/html/2501.12948v2), including Appendix F, provides training/distillation background. [Composer's developer report](https://cursor.com/blog/self-summarization) describes training summaries within rewarded trajectories. These establish useful mechanisms, with different evidence and reset boundaries.

The original SWE-agent, Voyager, compute-allocation, small-model, production, AgentDojo, and methods references remain background in [Perspectives](../notes/RESEARCH_PERSPECTIVES.md). They received abstract/source-summary review in the earlier pass; they are not newly audited in full here. Executable skills are not a proposed study priority.

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

**Status — 14 September 2026:** [Experience selection and abstention](../../ancillary-studies/experience-selection/README.md) is commissioned as an independent experimental project, prepared alongside S2 and S4. It starts with useful acquisition and investigates candidate-source utility and abstention; it need not wait for the other projects' results. The earlier [update-source-selection project](../../ancillary-studies/update-source-selection/README.md) supplies feasibility evidence and the assessment below. P3 explicitly identifies online selection/combination of update sources as unresolved in that paper. P13 and P14 narrow what we could claim as new.

**Root assessment of the 10 September 2026 report.** [Update Source Selection: A Local Feasibility and Behavioral Diagnostic](../../ancillary-studies/update-source-selection/output/pdf/update-source-selection.pdf) establishes a local route for reproducible LoRA interventions, with exact adapter resets, unchanged base weights, and measurable generation changes. Early first-action gains on 0.6B did not establish four-action episode success: all sources completed 0/24 legs in that diagnostic. The later native 4B reasoning comparison reached 24/24 for every source and no update. These are exploratory results from correlated synthetic cases; neither the floor nor the ceiling settles whether source selection can help elsewhere. No dynamic selector was tested.

The theoretical update is that **source reliability and source training value must be distinguished**. A verified correction can supersede an earlier plan without making its text the best material for a parameter update. This study did not demonstrate that the best training source changes across circumstances. Full historical context and explicit reliability rules also let the competent baseline solve every case without adaptation. No update used the fewest action-generation tokens in the final run, but those descriptive counts do not establish a general cost advantage. Source-dependent training utility, useful retention, and an agent's ability to choose remain unresolved.

We accept the report as completing the initial focused feasibility investigation. The question it leaves is: **when does training on experience improve later performance or reduce total cost compared with retaining accessible evidence and reasoning over it?** A workload with meaningful context, retrieval, or repeated-use costs would give that comparison a purpose. Evidence that different sources help under different observable conditions—or that selective abstention saves cost—would motivate selector development. The 14 September commission assigns this exploration to the new study, without requiring a positive effect.

The later procedure-transfer diagnosis adds a useful starting distinction: the same teacher and examples can support acquisition under one objective and fail under another, and the learner's starting state changes the outcome. That motivates checking useful update behavior before interpreting source comparisons. It does not itself demonstrate varying source utility or a working selector. Hold the update method comparable when isolating source effects, or explicitly investigate the interaction.

Assessment scope: we read the [manuscript source](../../ancillary-studies/update-source-selection/paper/update-source-selection.tex), its included results, the [results note](../../ancillary-studies/update-source-selection/notes/2026-09-10-interface-results.md), recorded analysis, and the diagnostic implementation. We did not rerun the experiments or independently rescore all raw traces. Methods, operational state, and the supporting evidence remain with the study.

**Question:** Does choosing between self-generated text, environmental observations, summaries, and no update improve later decisions when the most useful source changes during an episode?

**Competing explanations:** A source-selection policy identifies evidence relevant to the current failure; alternatively, it merely saves updates or picks the single source that is generally best for that model.

**Possible comparison:** Keep the base model, adapter, optimizer, and update budget fixed. Compare a selector with each fixed source, a fixed mixture, and a matched random selector. Choose the strongest static policy using development data, not the evaluation outcomes. Include no-update and same-information-in-context controls. First compare updates on common recorded prefixes, then test live trajectories, where selection changes subsequent experience.

**What it would add:** A prospective comparison of changing source usefulness, beyond selecting spans for an already-known question or suppressing repeated text. Crossing source reliability with novelty can supply candidate conditions, such as repeated verified corrections and novel incorrect assertions, but does not itself establish changing training utility. Any verification labels available to the selector must be equally available to its controls.

**Evidence to collect:** Task success, unnecessary/harmful updates, retention of corrections, selection cost, and update count. A tie with the best fixed source would weaken the case for dynamic selection. A gain that disappears after charging verification or matching update counts would support a simpler explanation.

**Reading/implementation needed:** P3's exact update and reset code; P13's selection baselines; P14's matched validation. The abstract-level [decision-theoretic TTT paper, 2606.15569v1](https://arxiv.org/abs/2606.15569v1) should be read for relevant assumptions about update selection. Build on existing implementations where usable.

### S2. Can a learned procedure survive later learning and accept a scoped correction?

**Status — 14 September 2026:** [Procedure retention and revision](../../ancillary-studies/procedure-retention-and-revision/README.md) is commissioned as an independent experimental project, prepared alongside S4 and S1. The completed acquisition diagnosis below supplies functioning regimes and transferred routing as starting evidence. Later-learning retention and scoped correction remain untested locally. They, multi-hop consequences and locality are not individually new tests.

**Related study and scope:** [Procedure acquisition and reuse](../../ancillary-studies/procedure-acquisition-and-reuse/README.md) investigated acquisition, transfer to new inputs, and repeated-use costs. Its initial experiment and bounded follow-up are complete. S2's additional question concerns interference from later learning and scoped correction; neither was tested in that investigation. S5's broader consolidation comparison also remains open.

**Root assessment — 13 September 2026.** The [initial results](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-acquisition-results.md) report 12/12 training-call recall from a fixed twelve-demonstration LoRA adapter, but 26/64 correct new-input calls versus 41/64 with retained examples. The [fresh follow-up](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-followup-results.md) reports 28/64 for the unchanged adapter versus 51/64 for examples, including 13/32 versus 31/32 on ordinary words. This is scored contact with acquisition and transfer, with a bounded result favoring retained examples. It does not establish a general limitation of parameter learning.

The lesson-construction method also failed: none of three candidates passed acquisition validation, and the selected fallback remained explicitly unvalidated. The supplied correct rule scored 64/64 in each evaluation but contained privileged information; it diagnoses execution ability without establishing acquisition from the same evidence. The intended compositional rule is not uniquely determined by the demonstrations, and inputs share identifier clusters. These limits constrain the transfer claim.

The theoretical implication is that **training recall, usable transfer, and acquisition-cost repayment need separate evidence**. The adapter reduced prompt tokens and measured inference time, but its lower accuracy prevented a repayment claim at comparable useful performance. Repeating its use does not by itself resolve the observed transfer deficit. This investigation already addresses the workload concern empirically; a further study needs a motivated acquisition method or different question, without an obligation to obtain an adapter win.

Assessment scope: we read the study README, initial results, follow-up addendum, and frozen follow-up protocol. We did not rerun experiments or independently rescore raw traces. Methods, evidence, and the completed investigation's operational state remain with that study.

<a id="next-investigation-procedure-transfer"></a>

#### Procedure transfer: completed local recipe test

**Root assessment and publication acceptance — 14 September 2026.** The user accepted the [local publication](../../ancillary-studies/procedure-transfer/FINDINGS.md), at study commit `78965ca7ffd4ac9389a77505a768cf6dfd6be957`, as the completed first comparison. **Distillation acquisition failed under the tested recipe.** The user rejected treating an acceptable negative publication as a quickly executed stop condition, and the root prioritized acquisition diagnosis. The original comparison and its assessment below retain their scope; the [subsequent diagnosis](#procedure-transfer-acquisition-diagnosis) now supplies explanatory progress and a functioning acquisition regime.

The [13 September preparation](../sources/2026-09-13/README.md) selected evidence-conditioned distillation following the earlier adapter's transfer deficit. The completed study covers all four condition combinations with 16 checked calls, uses two coupled initialization/order seeds, and compares direct imitation with full-vocabulary reverse KL on checked answer prefixes and on student-generated prefixes. The secondary comparison holds the loss, teacher, evidence and training inputs fixed. All six final checkpoints preceded fresh evaluation. The development-selected teacher reminder, additional development labels and pretrained teacher capabilities are disclosed in the [protocol](../../ancillary-studies/procedure-transfer/protocol/transfer-v1.md).

The [audited outcomes](../../ancillary-studies/procedure-transfer/evidence/transfer-v1-analysis/README.md) are:

| Method/reference | Training-call recall, seeds 17 / 29 | Fresh-input success, seeds 17 / 29 |
|---|---:|---:|
| Direct imitation | 16/16; 16/16 | 24/96; 32/96 |
| Reverse KL, checked prefixes | 3/16; 4/16 | 3/96; 1/96 |
| Reverse KL, student-generated prefixes | 0/16; 3/16 | 0/96; 2/96 |
| Retained examples + selected reminder (one base-model reference) | 14/16 | 89/96 |
| Supplied complete rule (privileged reference) | Not measured | 65/96 |
| No acquisition (one base-model reference) | Not measured | 0/96 |

The useful teacher establishes that the evidence supports new-input behavior in this model. Both distillation variants fail largely at acquisition, so their result does not isolate a transfer failure after successful learning or student-generated prefixes as the cause. Imitation again fits demonstrations while generalizing poorly. Distillation costs more to acquire and achieves much lower accuracy; no repayment at comparable useful performance was demonstrated. The supplied-rule prompt was not optimized alongside the examples prompt, so their scores do not establish a general ordering of rules and examples.

The overall score also conceals **partial procedural transfer**. The [component audit](../../ancillary-studies/procedure-transfer/evidence/transfer-v1-components/components.json), independently reproduced by the root from saved responses, gives imitation tool-choice accuracy of 72/96 and 96/96 for seeds 17 and 29, with correct identifier transformations on only 26/96 and 32/96. Both preserve call syntax on every fresh case. This distinguishes transfer of a routing decision from reliable argument transformation and complete-call success. It motivates a controlled comparison of the operations separately and together; the existing counts alone do not establish why they differ.

**Scientific weight.** Mechanics checks establish that the specified updates occurred, but do not establish that the shared LoRA configuration and optimizer settings are suitable for reverse KL. The pilot did not develop an effective distillation acquisition recipe. Root inspection also found substantially larger gradient spikes in the distillation logs; differing objective scales and those observations do not identify a cause. Optimization, teacher distributions on incorrect prefixes and parameterization remain unresolved. This is evidence against the tested recipe, with little weight against the broader method. One synthetic procedure, four training identifiers and two coupled seeds further limit generality; the reported bootstrap intervals condition on these runs and resample identifier clusters.

**Reason for the diagnostic continuation.** Repeatedly closing minimally developed neural recipes after acquisition failure could create an apparent general advantage for explicit memory without a comparison against an adequately developed neural alternative. Keeping that caveat in the root's beliefs was insufficient progress. The two-update pilots established mechanics; separate development material supported purposeful calibration and diagnosis in the subsequent phase. The initial failures remain evidence, and a subsequently developed transfer claim needs fresh evaluation. Retention, correction and consolidation were not tested by this comparison.

**Assessment scope.** The root read the publication, protocol, development and reproduction notes, implementation, raw responses, training events and saved audits. It independently rescored all 976 responses, verified 27 evidence-manifest entries, checked paired initialization hashes and training-input orders, and confirmed that executed source snapshots match frozen commit `5f636fb2d2768d1818d53aa51928cbe043c4f2c2`. These checks passed. It did not rerun model training or inference. The native unit-test command could not start because the review environment lacked the recorded Python 3.14.7 interpreter; the study's native audit remains reported evidence. Operational details and any future repairs stay with the ancillary study.

#### Procedure transfer: acquisition diagnosis

**Root assessment — 14 September 2026.** [DIAGNOSIS.md](../../ancillary-studies/procedure-transfer/DIAGNOSIS.md), published at `dcdc0d6f54dde235549f8abfba407598b6635667` with evidence at `c183674`, completes a useful bounded diagnostic contribution. It establishes a functioning soft-target acquisition checkpoint, a controlled effect of loss orientation on failed routing, and conditional separation of routing, identifier production and suffix completion. These are development and intervention results; they do not replace the accepted prospective transfer test or establish a forward-KL transfer advantage.

With common examples, teacher, initialization, input order and canonical answer prefixes, forward KL reaches 16/16 training calls at 128 updates; reverse KL reaches 4/16. From identical failed reverse-KL parameters, 128 further updates under forward KL repair routing from 8/16 to 16/16 and yield 11/16 complete calls, while the matched reverse continuation remains at 4/16. All five remaining rescue errors omit the fast suffix. Reducing the reverse learning rate tenfold does not repair acquisition within the matrix's budget. This excludes that specific rate change as a sufficient remedy, not every reverse-KL configuration.

The saved distributions identify eight teacher-clear wrong routing decisions with negligible reverse correct-logit derivatives and strong forward derivatives. The same pattern occurs in both original reverse-KL variants. These are first-position logit signals, not full parameter gradients or a complete causal account; the orientation intervention establishes recoverability beyond the observed signal contrast. A separate warm start from the acquired imitation checkpoint preserves 16/16 training recall through reverse updates, while development performance declines from 12/16 to 8/16. The usefulness of the objective therefore depends on the starting policy in this setting. Preservation under continued same-task training is not retention under unrelated learning.

The selected imitation and forward checkpoints route all 48 random-identifier development calls correctly, but complete 28/48 and 17/48 respectively. Supplying the correct route leaves identifier production weak; supplying both route and uppercase identifier permits 48/48 suffix/closing completions for each. This localizes a remaining behavioral difficulty without establishing independently learned internal modules. Prefixes supply privileged answers and can alter tokenization. The teacher makes 46/48 complete calls, with all identifiers correct. Forward's 13/16 versus imitation's 12/16 on earlier development words did not predict an advantage on these random identifiers.

Teacher error also matters: forward's training recall declines from 16/16 at 128 steps to 14/16 at 256, with the two later errors matching wrong teacher routing targets. That is consistent with fitting teacher mistakes more closely, without isolating every effect of longer training. The evidence supports functioning acquisition and a specific rescue; it establishes neither neural superiority, a capacity limit, nor universal reverse-KL failure.

**Root implications and review scope.** The diagnosis supports R1 and R3 of the [earlier procedural-learning note](../notes/PROCEDURAL_LEARNING.md#assessment-after-reading-diagnosis), partly addresses R2, and leaves R4 untested. Acquired routing can now motivate retention and revision experiments; reliable whole-call copying is not a prerequisite for studying that specific learned behavior. In the root review, 944 response records and 16 teacher records independently reproduce all 45 audited aggregate groups; 41 manifest entries, matched initialization/input-order controls and scalar derivatives at 224 saved probability records check out. The root inspected the plans and executed source snapshots but did not rerun model training or inference. The study reports native tests and reload checks. One diagnostic training seed, one small task and adaptive development limit generality. Methods, costs and evidence remain with the study.

#### Retention and correction: current experimental question

**Question:** After an agent internalizes a procedure, can a correction to one condition change its later actions while preserving the rest of the procedure and unrelated abilities?

**Competing explanations:** The update retains a reusable conditional procedure; it instead memorizes the training answer, biases a familiar action, follows the latest statement indiscriminately, or loses unrelated knowledge during repair.

**Possible comparison:** Teach a small tool-use rule from checked examples; remove those examples from the later prompt. Present new compositions, then unrelated learning episodes, then a valid exception or a less-authoritative conflicting assertion. Compare reset versus carried adapters, a retention-oriented parametric method, and an explicit lesson using the same evidence. Use an independent environment to score actions and outcomes. A simple example is a routing procedure whose destination depends on two changing conditions; a correction changes only one condition's scope.

**What it adds:** Measure the joint sequence of acquisition, interference, scoped procedural revision, and subsequent action. Reuse P9's distinction between component knowledge and consequences, adapting it to actions. Do not present the resulting task format or a single successful edit as a new learning mechanism.

**Evidence to collect:** Initial acquisition, later compositional success, stale versus corrected actions, inappropriate application of the exception, and unaffected-task performance. If initial acquisition fails, the run informs acquisition rather than correction. Report that outcome; do not select only convenient successful writes without also reporting the full denominator.

**Reading/implementation needed:** P4's sequential-edit setup; P6/P7's retention and locality controls; P9's revised data and scoring. Read [LOKI, 2606.19679v1](https://arxiv.org/abs/2606.19679v1) and the closest procedural-editing literature before claiming a novel intervention. This first pass only reviewed LOKI's abstract. The study can still begin as an explicitly labeled replication-plus-extension.

### S3. When does deeper neural memory repay its harder update problem?

**Status:** The [neural-memory-depth investigation](../../ancillary-studies/neural-memory-depth/README.md) is complete as a bounded contribution, published and assessed on 13 September 2026. Its [FINDINGS.md](../../ancillary-studies/neural-memory-depth/FINDINGS.md), at study commit `4a8dfd1299d11478635e6a13f5fb64564269ba61`, is the accepted local publication. The original cross-paper question remains open. No further experiment or separate manuscript is required to complete this contribution.

**Root assessment — 13 September 2026.** The [written comparison](../../ancillary-studies/neural-memory-depth/notes/INITIAL_COMPARISON.md) and [configuration follow-up](../../ancillary-studies/neural-memory-depth/notes/CONFIGURATION_FOLLOWUP.md) exclude two simple explanations of the reported contrast: Titans v1's depth sweep uses memory without attention, and Modular TTT's negative depth trend survives nonzero initialization and its reported stability variants. Architectures and update schedules still differ. The later Titans paper's general 16-token update chunk is not a verified setting for its depth figure; the exact depth-run recipe and original-checkpoint mapping remain incomplete. The comparison narrows the uncertainty without resolving it.

The [graph audit](../../ancillary-studies/neural-memory-depth/notes/GRAPH_EXECUTION_AUDIT.md) identifies an omitted fast-weight derivative during outer differentiation in the pinned Modular TTT implementation. Source-loaded deep cases disagree with the reference derivative while shallow controls agree; completing the derivative agrees with finite differences and preserves numerical forward outputs. Intent is unknown, and explicit CPU kernel substitutions limit the implementation claim. The subsequent [recall pilot](../../ancillary-studies/neural-memory-depth/notes/RECALL_PILOT_RESULTS.md) and [refresh comparison](../../ancillary-studies/neural-memory-depth/notes/REFRESH_COMPARISON_RESULTS.md) find no consistent final recall benefit from completing the derivative or increasing gradient-refresh frequency. Some trajectories change substantially, but this does not establish an error in either paper's reported results.

The strongest behavioral evidence concerns **interactions among initial representations and the training stream**. A [10×10 crossing](../../ancillary-studies/neural-memory-depth/notes/SEED_SEPARATION_RESULTS.md) separates whole-model initialization from training-example sampling and ordering; neither factor alone explains the outcomes. [Reciprocal group swaps](../../ancillary-studies/neural-memory-depth/notes/GROUP_SWAP_RESULTS.md) then localize strong effects to initial embeddings. In the [query/key/value factorial](../../ancillary-studies/neural-memory-depth/notes/EMBEDDING_SWAP_RESULTS.md), replacing only queries or only values from selected donor 11 into donor 16's background changes low-loss success from 0/10 streams to 10/10. Combining those replacements gives only 1/10; replacing keys as well restores 10/10. Both derivative modes give this pattern. These interventions demonstrate compatibility effects for particular tensors and conditions. They supply neither a universal ranking of embeddings nor a complete account of the training dynamics; initial query–key cosine alignment alone cannot explain the results.

The [post-hoc checkpoint inspection](../../ancillary-studies/neural-memory-depth/notes/RETRIEVAL_MODES.md) finds distinct value-confusion and key-confusion patterns, leaving some failures unclassified. [Six frozen-feature linear-readout fits](../../ancillary-studies/neural-memory-depth/notes/FROZEN_READOUT_RESULTS.md) preserve the selected ambiguities while successful controls retain full recall. Readout initialization can influence joint learning, while the tested later linear refit leaves these selected retrieval failures unresolved. The supported description is partial retrieval at a fixed training horizon. These probes do not establish irreversible information loss, stable attractors, or inability to recover through longer training or a different decoder.

The theoretical update is that **architectural memory capacity and the capacity a training procedure learns to use require separate evidence**. The same deeper architecture supports full recall under other tested initial conditions, so the observed failures are not an unavoidable capacity limit on this task. The tested shallow baseline also reaches full recall: this study locates difficulties in learning to use deeper memory, without demonstrating a benefit from depth. The result refines our starting emphasis on write dynamics to include the learned representations and their joint training with the reader.

**Limits and assessment scope.** The deeper synthetic model has 1,196 parameters and trains for 600 updates. Later interventions use selected donors and previously inspected evaluation mappings; they are adaptive mechanism investigations, not independent donor/task replications. Within-depth interventions hold architecture fixed, while earlier cross-depth comparisons are not parameter-matched and fixed training events do not establish compute matching. CPU results do not establish fused CUDA/BF16 parity. The study's saved verification records support reproducibility within that scope. The root reviewed the publication, linked comparisons, protocols, diagnostics and saved summary/verification records; it did not rerun the experiments, independently rescore checkpoints, or audit the original papers' model runs. Methods and evidence remain in the ancillary directory.

**Remaining question:** Under which inner updates, representations and outer training conditions can additional fast factors deliver useful capacity, and when does that repay their cost? Relating this local result to the published depth curves still requires the missing configurations and a meaningful comparison of tasks, parameters and compute. Generality of the representation interaction is a separate uncertainty. These are open research directions, not a commissioned continuation; the current publication is sufficient for root synthesis.

### S4. What does learned memory lose when the future goal changes?

**Status — 14 September 2026:** [Memory under goal shift](../../ancillary-studies/memory-under-goal-shift/README.md) is commissioned as an independent experimental project, prepared alongside S2 and S1. The investigator selects and develops its own usable memory mechanism and specified change in future use. It does not depend on resolving the procedural learner's remaining identifier errors or receiving either other project's results.

**Question:** Does memory optimized for likely future predictions retain information needed by a later, previously unannounced goal?

**Competing explanations:** The learned objective preserves broadly reusable evidence; alternatively, it allocates capacity toward expected queries and discards rare but later decisive details. More expensive explicit retention may succeed simply because it preserves more information.

**Possible comparison:** Give all branches the same history. After compression, reveal either an expected query or a different goal requiring information present in that history. Compare a trained neural memory, a compact explicit representation, and full-context or retrieval access. Add a query-known-before-compression condition to isolate the value of advance knowledge. Run within a model family where possible; comparisons across differently pretrained architectures remain system comparisons.

**What it adds:** A controlled change in future use, beyond ordinary long-context recall or query-conditioned selection. A capacity-limited memory cannot be expected to preserve every possible future detail; specify the distribution and measure the tradeoff instead of assuming lossless retention is attainable.

**Evidence to collect:** Expected-goal and changed-goal accuracy, exact evidence availability, latency, and retained-state size. For TTCD-like methods, charge the teacher computation and history it needs. Full-context success checks that the task is answerable. If both neural and explicit compression fail similarly at matched constraints, the limiting factor may be capacity or task uncertainty.

**Reading/implementation needed:** P11's teacher windows and causal update timing; P8's held-out query construction; P13's query access. P10's results and [M+, 2502.00592v2](https://arxiv.org/abs/2502.00592v2), currently abstract-reviewed, are relevant alternatives before inventing recovery machinery.

### S5. When should a useful temporary update be retained or consolidated?

**Status:** Later synthesis/measurement study, contingent on an update that already has useful behavior. Not a proposal to train a large general model from scratch.

**Related study and scope:** [Procedure acquisition and reuse](../../ancillary-studies/procedure-acquisition-and-reuse/README.md) measured acquisition and repeated-use costs for examples, a generated lesson, and an adapter; see the [root assessment under S2](#s2-can-a-learned-procedure-survive-later-learning-and-accept-a-scoped-correction). It found no acquisition-cost repayment at comparable useful accuracy. It did not compare reset-and-relearn, consolidation, or changing revision rates. S5 would add those lifecycle comparisons once an appropriate acquisition mechanism is available.

**Question:** Across recurring tasks and changing facts, when is it worth carrying an adapter, consolidating its stable content, or reconstructing it from explicit evidence?

**Competing explanations:** Recurrence amortizes acquisition and consolidation; revision costs and interference erase that advantage. A merged update may only change its packaging, with no improvement in capability.

**Possible comparison:** Use a mechanism that has demonstrated acquisition in S2 or existing work. Compare reset-and-relearn, retain separately, a specified consolidation method, and explicit memory across varied recurrence and revision rates. Distinguish algebraically merging an adapter from training a durable policy: they are different interventions. Keep source evidence accessible under disclosed costs rather than granting one branch a free archive.

**What it adds:** A measured decision boundary for a stated workload and mechanism, not the generic claim that reuse amortizes cost. P10 and model-editing work make “merge memory into weights” insufficient novelty by itself.

**Evidence to collect:** Cost at matched useful performance, acquisition, inference, state storage, reconstruction, correction, and collateral repair. Preserve latency, token counts, and compute separately unless a disclosed conversion combines them. A finite workload may never repay consolidation; that is a useful bounded result.

**Reading/implementation needed:** P10's lifecycle and compression details; P7's routing/merging; P16's separate adaptation/evaluation accounting. The existing compute-allocation paper supplies an alternative investment, not a universal cost conversion.

<a id="what-the-three-completed-investigations-change"></a>

### What the completed investigations change

The investigations examine different mechanisms and tasks. Together they sharpen the claims required to answer where experience should live:

| Investigation | Distinction supported by the bounded evidence | Implication for the root question |
|---|---|---|
| Update-source selection (S1) | Source reliability differs from its value as training material; changing loss or generation need not change task success. | A trustworthy record alone does not tell us whether training on it is useful. |
| Procedure acquisition and reuse (relevant to S2/S5) | Recall of demonstrations differs from transfer to new inputs; cheaper repeated inference need not repay acquisition at comparable useful accuracy. | Retaining a parameter update is valuable only to the extent that its learned behavior serves the later workload. |
| Procedure transfer and acquisition diagnosis (relevant to S1/S2) | Loss orientation and starting policy affect acquisition; a controlled objective switch repairs failed routing. Acquired routing transfers more reliably than identifier production. | Useful learning depends on the update and learner state as well as the evidence. A learned relation supplies a subject for retention and correction even while complete actions remain imperfect. |
| Neural memory depth (S3) | An architecture's capacity differs from the retrieval behavior its joint training reaches; individually helpful initialization changes can interfere when combined. | The writer, representations, reader and training conditions must be considered together when assessing usable memory. |

This is a synthesis of distinct local findings, not evidence that the adapter's transfer deficit and the deeper memory's partial retrieval share a cause. The experiments also concern different persistence boundaries: training a fast-memory system to learn within sequences does not demonstrate accumulation of experience across agent sessions. S3's successful synthetic recalls supply no placement or acquisition-cost comparison against accessible explicit evidence.

The acquisition failures also do not accumulate into a general verdict against neural memory. The diagnostic continuation now demonstrates functioning soft-target acquisition and a specific repair, while retained examples remain the stronger observed complete-call reference. The two procedure studies share a model family and closely related LoRA recipes and routing tasks, so they supply limited methodological diversity. The new S4 project can broaden the mechanisms and workloads under study. Acceptance of a publication, confidence in a broad hypothesis and retirement of a research question are separate judgments; the diagnosis demonstrates the value of turning an unresolved failure into a discriminating intervention.

For S2, these findings keep acquisition and transfer separate from subsequent retention or correction. For S4, they motivate distinguishing information that training never made usefully retrievable from information lost when the future goal changes. For S5, total cost depends on producing useful behavior reliably, including the cost of unsuccessful acquisition attempts. Those are implications for future questions, not new protocols or claims that the existing studies have tested those later stages. The root's working question is therefore conditional: **which training and memory mechanisms produce useful, transferable behavior on a specified workload, and when is maintaining that behavior preferable to retaining and reasoning over explicit evidence?**

<a id="6-suggested-order-for-discussion"></a>

## 6. Research selection

**Current decision — 14 September 2026:** The user approved three concurrent ancillary investigations after reviewing procedure-transfer's completed diagnosis. The root has prepared separate projects with questions, starting evidence, resources and an immediate expectation of bounded empirical work. Experiments were not started during preparation. Each fresh ancillary session can develop and run its comparison without waiting for either other project's findings.

| Commissioned project | Experimental question and starting point | What its result changes in the larger account |
|---|---|---|
| **S2: [Procedure retention and revision](../../ancillary-studies/procedure-retention-and-revision/README.md)** | Start from acquired procedural behavior and test subsequent learning and scoped revision, including new-input consequences and unaffected behavior. The procedure-transfer diagnosis supplies a usable acquisition lead. | Whether learned relations can accumulate and be maintained, rather than merely recalled immediately after training. |
| **S4: [Memory under goal shift](../../ancillary-studies/memory-under-goal-shift/README.md)** | Select a usable memory mechanism and test expected versus changed uses of the same history, with explicit-evidence references. Its mechanism and workload need not use the procedural task family. | Which future-use assumptions make learned compression useful or cause consequential loss. |
| **S1: [Experience selection and abstention](../../ancillary-studies/experience-selection/README.md)** | Establish useful acquisition and compare candidate sources and no update under specified learner conditions. Investigate changing utility before assuming an adaptive selector helps. | When an agent should convert experience into an update, and when retaining evidence or abstaining is preferable. |

The projects share published starting evidence, not an experimental dependency chain. A difficult acquisition recipe in one project does not postpone an unrelated investigation. Each investigator owns workload choice, methods, calibration, numerical resource sizing and publication. Reuse existing working mechanisms where appropriate; broaden mechanisms and tasks where that helps distinguish the explanations. If acquisition fails, pursue bounded diagnosis or establish a concrete limitation rather than treating a failed first recipe as the result.

The root develops predictions and compares the publications against the common question: **what should be learned, what should remain accessible as evidence, and what remains useful through later experience and changing needs?** The [procedural-learning note](../notes/PROCEDURAL_LEARNING.md#assessment-after-reading-diagnosis) now assesses its original predictions against the diagnosis. R1 and R3 receive support in development probes, R2 is partly addressed, and selective editability remains open. Local findings should revise this shared account without being generalized across untested mechanisms.

**S5 remains a cross-study cost question and a possible later consolidation project.** Charge acquisition, evidence access, reuse, reconstruction and revision for the behavior actually supplied. Lower cost at poorer complete-call quality does not establish repayment. Workload and cost analysis can develop alongside the active experiments; a dedicated retain/reset/consolidate comparison needs a specified useful mechanism and recurrence/revision pattern. S3's bounded contribution remains complete, with no new depth campaign commissioned.

Concurrent investigation does not require simultaneous heavy jobs on a shared device. Investigators coordinate use of the Mac Studio and disclose contention when interpreting timings, while reading, development and analysis proceed independently. The [ancillary-study approach](../notes/ANCILLARY_STUDY.md) continues to govern the division of responsibility.

Every empirical candidate needs gradient or state access for its neural treatment. An inference-only model endpoint can supply comparison answers or summaries but cannot substitute for inspecting the update. S1 established a native MLX training route on its 48 GB Apple M3 Max, and the procedure-acquisition study subsequently used native MLX for a fixed Qwen3-4B adapter comparison. Procedure transfer verified native MLX teacher distributions and LoRA gradients on the 64 GB Mac Studio M1 Ultra. S3 used small source-loaded CPU graphs with explicit kernel substitutions; it required no model endpoint or language-model pretraining. These results do not establish feasibility or budgets for other neural mechanisms. Read each study's own documentation and applicable AGENTS.md for current resources; the [root resource notes](../AGENTS.md#model-resources) identify the Mac Studio as the preferred serving resource.

## 7. Search scope and remaining uncertainty

This is a focused map, not an exhaustive novelty review. On 10 September 2026, we followed the original bibliography, inspected the primary full-text sections identified above, and used the arXiv query API for adjacent discovery and version metadata. API requests used one connection at a time, were spaced by more than three seconds, and used the descriptive User-Agent `Construct-2 literature mapping (local research metadata cache)`. Temporary responses were cached outside the notes directory; the durable review is this file and its versioned citations.

The discovery searches were:

- `ti:"Self-Adapting Language Models" OR ti:"Test-Time Training" OR ti:"Lifelong Knowledge Editing"`, first 35 results by descending submission date.
- `ti:MQuAKE OR ti:Locas OR ti:PERK OR ti:MEMORYLLM`, first 15 results by descending submission date; unrelated name matches were excluded.
- A batch `id_list` query verified the selected adjacent versions, including WISE, TTT layers, SEAL, TT-SI, Beyond Perplexity, TTCD, VANE, Modular TTT, Self-Guided TTT, LOKI, the TTT safety paper, and the decision-theoretic paper.

B0 additionally uses the original [LoRA paper, 2106.09685v2, §4.1](https://arxiv.org/html/2106.09685v2) for its factorized update equation. Its scalar calculations and two-slot latent-memory illustration are educational constructions, not additional literature findings or experimental replications.

These bounded searches can miss older work, different terminology, and later follow-ups. In particular, procedural editing, continual meta-learning, and adaptive update-source selection deserve a focused search when we choose a study. “Explicitly open in P3” means open in that paper, not proven open across all subsequent literature. None of S1–S5 is labeled a confirmed novel contribution.

On 13 September, the [focused acquisition-methods reading](../sources/2026-09-13/README.md) added P17/P18 and revisited P4/P8. Its attempted API discovery returned rate-limit errors and supplied no search results; the reading followed versioned primary HTML and references already identified in the local study. Procedure transfer therefore began with specific method leads and substantial known overlap. Its [14 September source note](../../ancillary-studies/procedure-transfer/sources/README.md) adds versioned primary-method and author-code reading for its local adaptation; neither review establishes comprehensive novelty coverage. A newly selected question needs its own focused source assessment.

The root's [14 September reading record](../sources/2026-09-14/README.md) adds the positive demonstrations used in the procedural-learning note. Its single API attempt returned HTTP 429 and stopped without metadata results; targeted web discovery and primary full text supplied the reading. P19 uses the published journal article; P20 uses the identified arXiv version. This selected reading does not establish coverage of later compositionality work or a preferred local implementation.

The earlier abstract review remains historical background. This file now owns the working paper/question/study map; subsequent assessments and discussion should update it here.
