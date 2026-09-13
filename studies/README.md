**Much of the original question list is already background knowledge or an active research topic.** This revision separates that background from narrower questions that could justify ancillary work. It builds on the [Construct synthesis](../notes/PREVIOUS_RESEARCH.md) and [research perspective](../notes/RESEARCH_PERSPECTIVES.md), with priority given to neural memory, live weight updates, and learned memory policies. Executable skill libraries remain background; see the [research preference](../sources/README.md#research-preference-to-date).

The comparisons below are proposals; S1 includes our assessment of an ancillary feasibility report, and S2 includes a 13 September 2026 assessment of the completed procedure-acquisition investigation relevant to S2 and S5. Read each study's own directory for its latest work. “Candidate extension” means a comparison is not established by the specific evidence reviewed here; it does not mean nobody has studied it. A useful replication or explanation can proceed without a novelty claim. A proposed new contribution needs its closest methods and evaluation settings checked before we call it new.

## 1. What changed after reading beyond the abstracts

Three important corrections to our starting position:

- Testing behavior after context removal is already an explicit research agenda, with diagnostic experiments, in **Beyond Perplexity** (P5). We should use and critique that work rather than invent another general memory-evaluation framework.
- Neural knowledge acquisition, retention through later updates, and propagation of edits are already studied in **SEAL, MEMORYLLM, WISE, and MQuAKE** (P4, P6, P7, P9). “Can neural memory retain or correct information?” is too broad to serve as our contribution.
- Training a memory mechanism for useful future computation is already central to **TTT layers, PERK, and TTCD** (P1, P8, P11), as well as trained textual summarization. The interesting questions concern conditions and failures of those objectives.

One particularly useful new connection is the different depth results in **Titans and Modular TTT** (P2, P12). This is an opportunity to understand a conditional result, not evidence that either paper is wrong.

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

**Reading scope:** The entries below identify the exact versions and sections inspected in the full-text HTML, rather than claiming a line-by-line review of every appendix. Results are authors' reported evidence, not independently reproduced findings. Source code, checkpoints, and raw outputs have not been audited. The assessment column is our interpretation of the boundary relevant to this program.

| Source and inspected material | Established prior work in the reviewed setting | Implication for our questions |
|---|---|---|
| **P1. [TTT layers, 2407.04620v4](https://arxiv.org/html/2407.04620v4)** — §§2.1–2.3, 2.6–2.7; experimental overview | Uses a learned model as recurrent state; learns reconstruction views in an outer loop. A specified linear/batch-gradient case is equivalent to linear attention. | The distinction between a neural state and parameter learning needs mechanism-level explanation. Rediscovering this equivalence would be educational reproduction. |
| **P2. [Titans, 2501.00663v1](https://arxiv.org/html/2501.00663v1)** — §§3–4, 5.1–5.5 | Writes key–value associations into neural memory with momentum and forgetting. Its separate “persistent memory” is fixed during inference. Its depth experiment reports better perplexity but slower training with deeper memory. | Does not establish indefinitely persistent agent learning. Depth's value is conditional; compare P12 before proposing a depth claim. |
| **P3. [aTTT, 2607.03441v1](https://arxiv.org/html/2607.03441v1)** — §§3–5 | Updates an episode-specific LoRA using Self, Env, or Summary text; resets between episodes. Includes random-drop, cadence, same-summary-in-context, and decoding controls. The strongest update source varies by model. | Basic within-episode benefit and several obvious ablations are already covered. Online source selection is explicitly left open in §5; carrying learned procedures across tasks is a different setting. |
| **P4. [SEAL, 2506.10943v2](https://arxiv.org/html/2506.10943v2)** — §§3–5, Table 2, Fig. 6 | Learns to generate adaptation data using post-update task performance as reward. Tests knowledge incorporation without the passage in context and few-shot adaptation. Sequential edits already reveal forgetting. | Acquisition without context and interference are not new phenomena. Its training reward and task packaging differ from ordinary unsupervised agent experience. |
| **P5. [Beyond Perplexity, 2607.00368v1](https://arxiv.org/html/2607.00368v1)** — §§2–7 and audit overview | Distinguishes prediction improvement from deployment-memory behavior. Its sparse-fact diagnostic finds lower loss with zero generated recall under the tested one-step LoRA protocol. Proposes retention, conflict, locality, and explicit-memory comparisons. | Reuse this distinction and protocol ideas. The diagnostic does not show that stronger update mechanisms cannot acquire usable information. Our study must add a specific mechanism or behavioral comparison. |
| **P6. [MEMORYLLM, 2402.04624v2](https://arxiv.org/html/2402.04624v2)** — §§2–3, 4.3–4.7 | Updates a latent memory pool from hidden states; tests editing and retention after intervening writes. Its 650,000-update integrity experiment checks answering about the most recently injected context. | Neural retention is already demonstrated in bounded settings. Long-run ability to absorb a fresh item is different from retaining an early item for that entire duration. |
| **P7. [WISE, 2405.14768v3](https://arxiv.org/html/2405.14768v3)** — §§2.3, 3.1–3.3 | Separates pretrained and edited knowledge into routed main/side memories; evaluates sequential edits, generalization, locality, and scaling. | Selective parametric editing is established prior art. Its edited factual targets do not by themselves settle correction of a procedure learned through interaction. |
| **P8. [PERK, 2507.06415v3](https://arxiv.org/html/2507.06415v3)** — §§2–4 | Meta-learns an adapter initialization so context encoding supports later reasoning without that context explicitly supplied in the outer-loop query. Tests several long-context reasoning settings. | Queryable parametric context storage is already studied. A bare “remove context and ask a question” comparison is insufficient novelty. |
| **P9. [MQuAKE, 2305.14795v3](https://arxiv.org/html/2305.14795v3)** — §§3.3–4; abstract | Separates recall of edited facts from answering their multi-hop consequences, finds failures, and proposes an external-memory approach. The revised diagnostic subset addresses conflicting instances. | “Does an edit propagate to dependent answers?” is already a benchmark question. Procedural action consequences or temporal revision would need an explicit additional comparison. |
| **P10. [Locas, 2602.05085v1](https://arxiv.org/html/2602.05085v1)** — abstract, introduction, §§2.1–2.2 | Develops locally supported parametric memory with initialization informed by the backbone. Describes expansion/compression and reports book-modeling and dialogue-QA evaluations. | Relevant to consolidation and initialization. Results and deployment lifecycle still need closer inspection before selecting it as a study implementation. |
| **P11. [TTCD, 2608.01672v1](https://arxiv.org/html/2608.01672v1)** — §§2–4, Tables 1 and Fig. 3 | Uses a longer-context teacher to supervise a shorter-context student's fast weights. Tests predictive retention, including recall and long-context reasoning. | Learning what to retain for later prediction is already the contribution. An unannounced change in the downstream goal is a possible narrower extension. |
| **P12. [Modular TTT, 2608.07110v1](https://arxiv.org/html/2608.07110v1)** — depth analysis, Appendices 8.4, 9.4–9.5, limitations | In its tested one-step setting, deeper learners remain behind shallow ones despite stabilization and initialization sweeps. External hybrid-model comparisons bundle several mechanisms. | Reconcile operating conditions with P2. A simple depth or initialization sweep would overlap with existing ablations. |
| **P13. [Self-Guided TTT, 2607.09415v1](https://arxiv.org/html/2607.09415v1)** — method and Algorithm 1; abstract | Selects training spans using the current question, retains full context at answer time, and resets after each instance. Reports gains over long-context baselines. | Selection of update text is already studied. Distinguish question-known selection from selection before a future need is known. |
| **P14. [VANE, 2608.09448v2](https://arxiv.org/html/2608.09448v2)** — §§3, 4.2; validation appendix | Adapts latent prompts on a shadow copy and validates candidates using subsequent observations before commitment. Reports task-dependent robotic results. | Validation and rollback of live updates are prior art. This is a related mechanism in a different modality, not an established solution for textual memory authority. |
| **P15. [Test-Time Training Undermines Safety Guardrails, 2605.22984v1](https://arxiv.org/html/2605.22984v1)** — abstract, §4.4 | Studies adversarial TTT and distinguishes substantive failures from degenerate outputs that fool safety judges. | “Weight updates introduce an attack surface” is already studied. Useful-learning preservation and evidence-specific authority would need their own comparison. |
| **P16. [ACE, 2510.04618v3](https://arxiv.org/html/2510.04618v3)** — §§3–4, Appendices A.1, A.3–A.4 | Supports incremental playbook updates, sequential prediction-before-update evaluation, multiple models, cost analysis, and harmful-reflection tests. Evaluation input cost can increase even when adaptation is cheaper. | Revision, robustness, model variation, and cost have existing evidence. Use it as an explicit-memory comparator rather than a new mechanism proposal. |

Additional existing background: [Reflexion v4](https://arxiv.org/html/2303.11366v4) §§3–4 explains bounded reflection buffers and repeated trials; [TT-SI v1](https://arxiv.org/html/2510.07841v1) Algorithm 1 restores the original parameters after instance-specific adaptation. [DeepSeek-R1 v2](https://arxiv.org/html/2501.12948v2), including Appendix F, provides training/distillation background. [Composer's developer report](https://cursor.com/blog/self-summarization) describes training summaries within rewarded trajectories. These establish useful mechanisms, with different evidence and reset boundaries.

The original SWE-agent, Voyager, compute-allocation, small-model, production, AgentDojo, and methods references remain background in [Perspectives](../notes/RESEARCH_PERSPECTIVES.md). They received abstract/source-summary review in the earlier pass; they are not newly audited in full here. Executable skills are not a proposed study priority.

## 4. What Construct and Formation already answered

The original-question table below uses the Construct synthesis. On 10 September 2026 we also read the local [Construct overview](../../construct/README.md), its M2 and GM findings, the [Formation overview](../../formation/README.md), and the two Formation evidence accounts linked below. This is a targeted reading of reported findings, not a new audit of raw requests, experimental ledgers, or scorers. Their external-memory results motivate comparisons but do not transfer automatically to neural mechanisms.

| Original area | What is already answered or substantially covered | What remains useful here |
|---|---|---|
| **T1: Access to stored information** | M1 demonstrates an eligibility effect with the same retained record. P8/P13 already study use of parametric context and selection of update text. | Background explanation of storage/write/read failures. Dynamic choice of update source becomes S1. Autonomous external retrieval is deferred. |
| **T2: Repair versus transferable learning** | M2 demonstrates a bounded cross-session lesson effect; GM joins old continuity with current state. P3/P4/P5/P6/P8 already distinguish or measure relevant forms of adaptation and retention. | Explain the distinct outcomes. Investigate a learned procedure's retention and revision under later updates in S2. |
| **T3: Knowledge placement/consolidation** | P1/P2 explain fast-weight memory; P7/P8/P10 provide parametric storage designs. R1 establishes a training/distillation background. | The workload-dependent value of carrying or consolidating an update becomes S5. Neural depth and update dynamics become S3. No universal placement rule is established. |
| **T4: Compression and recovery** | X2 shows a hot-store proxy benefit from recoverable eviction. P11 and Composer already learn retention policies. | A changed future goal becomes S4. Full archive/recovery engineering is deferred; its costs remain relevant to comparisons. |
| **T5: Correction** | Construct's retraction work covers a bounded correction. P7/P9 cover editing, locality, and dependent answers; P4/P6 address interference/retention. | Procedural exceptions after intervening learning become S2. General edit propagation is background, not a new proposal. |
| **T6: Total cost** | X2's metric is limited; warming-budget results depend on charging assumptions. P16 separates adaptation and evaluation costs. | Attach full accounting to every candidate; S5 studies the recurrence/revision tradeoff if a useful neural mechanism is available. |
| **T7: Capability and composition** | Engine-dependent engagement and Body-0's unengaged integration run limit Construct's claims. P3/P12/P16 examine model or component variation. | Use interaction comparisons within S1/S3. A general architecture-composition project is deferred. |
| **T8: Authority/security** | M3 already shows memory withholding/admission attacks. P14/P15 supply neural-update validation and attack evidence. | Authority is a factor in S1/S2. We are not proposing to rediscover that memory can be poisoned. |
| **T9: Measurement** | Construct scorer/admission audits and P5 already support separating instrument outcomes from behavioral evidence. | Background research method used throughout; no new generic framework is proposed. |

### Direct local evidence relevant to S1 and S2

- **Construct: using an earned record is already demonstrated.** [M2 findings](../../construct/notes/M2_FINDINGS.md) report a cross-session retraction lesson changing later answers, with removal comparisons and repeated draws. The bound is one hop and one retraction, not general procedural learning. [GM findings](../../construct/notes/GM_MEMORY_FINDING.md) report joining an earlier promise with current state: 24/24 relevant cases versus 6/24 state-only. This is explicitly an exploratory finding from a corrected replacement, not a formal validation claim.
- **Formation: selective revision is already demonstrated in a restricted setting.** The [composed revision successor](../../formation/evidence/composed-clerical-revision-engagement-successor-20260820T185545Z/README.md) reports 45/48 matching actions after admitting revised records, equal to supplied correct revisions; removal left the old versions active and scored 0/48. The account explicitly limits this to structured retrieval over model-written fields. It does not establish long-run interference resistance or general acquired competence.
- **Formation: producing a record and using it can fail separately.** In the [opaque-sink coding contact](../../formation/evidence/opaque-sink-coding-contact-20260822T031500Z/README.md), the clerk reversed the observed API fact and every learned record was quarantined. Supplying the correct fact still yielded 0/6 matching functions; most programs failed on field names before the remembered API behavior could matter. That comparison could not establish the intended memory benefit. It also does not show that neural adaptation would repair the failure.

**Implication for our studies:** S1 needs evidence that source selection affects useful downstream behavior, rather than merely changing training text or a reported rationale. S2 must distinguish successful acquisition from successful use and test scoped revision beyond an already-established lookup effect. Supplied-correct-information controls help locate failures, but are not a universal ceiling on what parameter learning can achieve: an update might change computation that a context-only control cannot. These are design implications we draw from the local results, not additional findings. Formation's [current state](../../formation/README.md#present-state) owns its broader thesis assessment and paused empirical route.

## 5. Narrower questions and candidate ancillary studies

The hypotheses below are our proposals. Each study names its intended addition, closest overlap, and a result that could change the theory. They are sketches for discussion; sample sizes, budgets, implementation versions, and exact protocols would be chosen with the investigating project.

**Workload choice.** For placement and repayment questions, a useful comparison needs a motivated workload, explicit information access, and measured costs that can distinguish the competing explanations. Context or retrieval is a comparator whose cost must be measured. An acquisition failure, an explicit-memory advantage, or a tie at lower total cost can each be informative. Bounded exploration may establish the workload; a subsequent test of a developed claim needs fresh evaluation material. The root motivates the question and assesses its implications; the study owns task and protocol design under the [ancillary-study approach](../notes/ANCILLARY_STUDY.md). S3's mechanism comparison can answer its narrower question without establishing an advantage over explicit context.

### S1. Can an agent choose which experience to train on during an episode?

**Related study:** See the update-source-selection project; read that study's own [README](../../ancillary-studies/update-source-selection/README.md) and publications for the latest. P3 explicitly identifies online selection/combination of update sources as unresolved in that paper. P13 and P14 narrow what we could claim as new.

**Root assessment of the 10 September 2026 report.** [Update Source Selection: A Local Feasibility and Behavioral Diagnostic](../../ancillary-studies/update-source-selection/output/pdf/update-source-selection.pdf) establishes a local route for reproducible LoRA interventions, with exact adapter resets, unchanged base weights, and measurable generation changes. Early first-action gains on 0.6B did not establish four-action episode success: all sources completed 0/24 legs in that diagnostic. The later native 4B reasoning comparison reached 24/24 for every source and no update. These are exploratory results from correlated synthetic cases; neither the floor nor the ceiling settles whether source selection can help elsewhere. No dynamic selector was tested.

The theoretical update is that **source reliability and source training value must be distinguished**. A verified correction can supersede an earlier plan without making its text the best material for a parameter update. This study did not demonstrate that the best training source changes across circumstances. Full historical context and explicit reliability rules also let the competent baseline solve every case without adaptation. No update used the fewest action-generation tokens in the final run, but those descriptive counts do not establish a general cost advantage. Source-dependent training utility, useful retention, and an agent's ability to choose remain unresolved.

We accept the report as completing the initial focused feasibility investigation. Further runs should follow a separately motivated question: **when does training on experience improve later performance or reduce total cost compared with retaining accessible evidence and reasoning over it?** A workload with meaningful context, retrieval, or repeated-use costs would give that comparison a purpose. Evidence that different sources help under different observable conditions—or that selective abstention saves cost—would then motivate selector development. This is a proposed direction for discussion, not a commissioned follow-up or a requirement to find a positive effect.

Assessment scope: we read the [manuscript source](../../ancillary-studies/update-source-selection/paper/update-source-selection.tex), its included results, the [results note](../../ancillary-studies/update-source-selection/notes/2026-09-10-interface-results.md), recorded analysis, and the diagnostic implementation. We did not rerun the experiments or independently rescore all raw traces. Methods, operational state, and the supporting evidence remain with the study.

**Question:** Does choosing between self-generated text, environmental observations, summaries, and no update improve later decisions when the most useful source changes during an episode?

**Competing explanations:** A source-selection policy identifies evidence relevant to the current failure; alternatively, it merely saves updates or picks the single source that is generally best for that model.

**Possible comparison:** Keep the base model, adapter, optimizer, and update budget fixed. Compare a selector with each fixed source, a fixed mixture, and a matched random selector. Choose the strongest static policy using development data, not the evaluation outcomes. Include no-update and same-information-in-context controls. First compare updates on common recorded prefixes, then test live trajectories, where selection changes subsequent experience.

**What it would add:** A prospective comparison of changing source usefulness, beyond selecting spans for an already-known question or suppressing repeated text. Crossing source reliability with novelty can supply candidate conditions, such as repeated verified corrections and novel incorrect assertions, but does not itself establish changing training utility. Any verification labels available to the selector must be equally available to its controls.

**Evidence to collect:** Task success, unnecessary/harmful updates, retention of corrections, selection cost, and update count. A tie with the best fixed source would weaken the case for dynamic selection. A gain that disappears after charging verification or matching update counts would support a simpler explanation.

**Reading/implementation needed:** P3's exact update and reset code; P13's selection baselines; P14's matched validation. The abstract-level [decision-theoretic TTT paper, 2606.15569v1](https://arxiv.org/abs/2606.15569v1) should be read for relevant assumptions about update selection. Build on existing implementations where usable.

### S2. Can a learned procedure survive later learning and accept a scoped correction?

**Status:** High-interest extension candidate with substantial prior overlap. The prospective combination matters; retention, multi-hop consequences, and locality are not individually new tests.

**Related study and scope:** [Procedure acquisition and reuse](../../ancillary-studies/procedure-acquisition-and-reuse/README.md) investigated acquisition, transfer to new inputs, and repeated-use costs. Its initial experiment and bounded follow-up are complete. S2's additional question concerns interference from later learning and scoped correction; neither was tested in that investigation. S5's broader consolidation comparison also remains open.

**Root assessment — 13 September 2026.** The [initial results](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-acquisition-results.md) report 12/12 training-call recall from a fixed twelve-demonstration LoRA adapter, but 26/64 correct new-input calls versus 41/64 with retained examples. The [fresh follow-up](../../ancillary-studies/procedure-acquisition-and-reuse/notes/2026-09-11-followup-results.md) reports 28/64 for the unchanged adapter versus 51/64 for examples, including 13/32 versus 31/32 on ordinary words. This is scored contact with acquisition and transfer, with a bounded result favoring retained examples. It does not establish a general limitation of parameter learning.

The lesson-construction method also failed: none of three candidates passed acquisition validation, and the selected fallback remained explicitly unvalidated. The supplied correct rule scored 64/64 in each evaluation but contained privileged information; it diagnoses execution ability without establishing acquisition from the same evidence. The intended compositional rule is not uniquely determined by the demonstrations, and inputs share identifier clusters. These limits constrain the transfer claim.

The theoretical implication is that **training recall, usable transfer, and acquisition-cost repayment need separate evidence**. The adapter reduced prompt tokens and measured inference time, but its lower accuracy prevented a repayment claim at comparable useful performance. Repeating its use does not by itself resolve the observed transfer deficit. This investigation already addresses the workload concern empirically; a further study needs a motivated acquisition method or different question, without an obligation to obtain an adapter win.

Assessment scope: we read the study README, initial results, follow-up addendum, and frozen follow-up protocol. We did not rerun experiments or independently rescore raw traces. Methods, evidence, and the completed investigation's operational state remain with that study.

**Question:** After an agent internalizes a procedure, can a correction to one condition change its later actions while preserving the rest of the procedure and unrelated abilities?

**Competing explanations:** The update retains a reusable conditional procedure; it instead memorizes the training answer, biases a familiar action, follows the latest statement indiscriminately, or loses unrelated knowledge during repair.

**Possible comparison:** Teach a small tool-use rule from checked examples; remove those examples from the later prompt. Present new compositions, then unrelated learning episodes, then a valid exception or a less-authoritative conflicting assertion. Compare reset versus carried adapters, a retention-oriented parametric method, and an explicit lesson using the same evidence. Use an independent environment to score actions and outcomes. A simple example is a routing procedure whose destination depends on two changing conditions; a correction changes only one condition's scope.

**What it adds:** Measure the joint sequence of acquisition, interference, scoped procedural revision, and subsequent action. Reuse P9's distinction between component knowledge and consequences, adapting it to actions. Do not present the resulting task format or a single successful edit as a new learning mechanism.

**Evidence to collect:** Initial acquisition, later compositional success, stale versus corrected actions, inappropriate application of the exception, and unaffected-task performance. If initial acquisition fails, the run informs acquisition rather than correction. Report that outcome; do not select only convenient successful writes without also reporting the full denominator.

**Reading/implementation needed:** P4's sequential-edit setup; P6/P7's retention and locality controls; P9's revised data and scoring. Read [LOKI, 2606.19679v1](https://arxiv.org/abs/2606.19679v1) and the closest procedural-editing literature before claiming a novel intervention. This first pass only reviewed LOKI's abstract. The study can still begin as an explicitly labeled replication-plus-extension.

### S3. When does deeper neural memory repay its harder update problem?

**Status:** [Neural memory depth](../../ancillary-studies/neural-memory-depth/README.md) was prepared on 13 September 2026 for an independent ancillary session. The investigation has not started. The ancillary agent owns the written comparison and its methods; the root will assess the resulting publication.

**First written output:** A comparison of P2 and P12 in common notation, with versioned section and configuration references. Identify the mutable memory, inner loss and update rule, number of update steps, initialization, normalization, reset boundary, and outer training objective. Put the depth comparisons alongside their task, context/chunk lengths, parameter counts, and training compute where reported; mark missing configuration facts explicitly. Explain which comparisons are commensurate and which differences could account for the reported depth trends. If a question survives alignment, sketch the smallest empirical comparison that could distinguish its explanations. This is the ancillary project's intended first deliverable; the alignment has not yet been performed.

**Question:** Which operating differences explain the favorable depth trend in P2 and unfavorable trend in P12?

**Competing explanations:** Additional depth provides useful capacity only when the write dynamics can exploit it; apparent gains instead arise from extra parameters, training compute, task distribution, or the surrounding architecture.

**Possible later empirical comparison:** If written alignment leaves a meaningful uncertainty, reproduce the relevant shallow/deep comparison and change one identified factor in a common implementation. Candidate factors include initialization, update rule, normalization, context length, memory capacity, and training schedule. Use both a parameter-matched comparison and a compute-matched comparison; neither can stand in for the other. This is a possible extension, not a training campaign commissioned by the project preparation.

**What it adds:** An explanation of a change in the direction of the depth effect across settings. Repeating P12's completed initialization/chunk-size sweeps, or plotting deeper models against unmatched shallow ones, would not answer this question.

**Evidence to collect:** Retrieval and predictive performance, interference, update/activation magnitudes, throughput, and training stability. A stable deep model that still loses points toward capacity being unnecessary under those conditions. An advantage that appears only with a changed update schedule supports an interaction between capacity and learnability.

**Reading/implementation needed:** P2 §5.5 and its actual configurations; P12 Appendices 8.4 and 9.4–9.5; P1 for the common formulation. We have identified an apparent tension, not established that the published implementations are directly comparable. If configuration alignment explains it, a background synthesis may be the complete useful result.

### S4. What does learned memory lose when the future goal changes?

**Status:** Medium-priority extension candidate. Requires a trained memory mechanism and a clearly specified change in the query distribution.

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

## 6. Suggested order for discussion

1. **B0: Completed above; discuss any unclear mechanisms first.** The worked examples distinguish fitting an observation, retaining information, and improving later behavior. They establish vocabulary without claiming new empirical findings.
2. **S1/S2: Discuss what the two completed investigations leave unresolved.** S1 did not establish source-dependent task benefit; the procedure-acquisition study found poor transfer and no repayment at comparable useful accuracy for its tested adapter. A next acquisition or placement question needs a motivated method and workload. Source selection, later-learning retention, and scoped correction remain separate questions.
3. **S3: Prepared for an ancillary agent; not started.** The [neural-memory-depth project](../../ancillary-studies/neural-memory-depth/README.md) contains the starting question, sources, and resources. Its ancillary agent will develop the written comparison before considering any experimental extension. The root will synthesize the published findings.
4. **S4 and S5: Keep as subsequent directions.** They become more informative once we understand a working memory mechanism and can account for its real costs.

Every empirical candidate needs gradient or state access for its neural treatment. An inference-only model endpoint can supply comparison answers or summaries but cannot substitute for inspecting the update. S1 established a native MLX training route on its 48 GB Apple M3 Max, and the procedure-acquisition study subsequently used native MLX for a fixed Qwen3-4B adapter comparison. These results do not establish feasibility or budgets for other neural mechanisms. Read each study's own documentation and applicable AGENTS.md for current resources; the [root resource notes](../AGENTS.md#model-resources) identify the newly commissioned Mac Studio as the preferred serving resource. S3's project preparation starts no investigation or experiments.

## 7. Search scope and remaining uncertainty

This is a focused map, not an exhaustive novelty review. On 10 September 2026, we followed the original bibliography, inspected the primary full-text sections identified above, and used the arXiv query API for adjacent discovery and version metadata. API requests used one connection at a time, were spaced by more than three seconds, and used the descriptive User-Agent `Construct-2 literature mapping (local research metadata cache)`. Temporary responses were cached outside the notes directory; the durable review is this file and its versioned citations.

The discovery searches were:

- `ti:"Self-Adapting Language Models" OR ti:"Test-Time Training" OR ti:"Lifelong Knowledge Editing"`, first 35 results by descending submission date.
- `ti:MQuAKE OR ti:Locas OR ti:PERK OR ti:MEMORYLLM`, first 15 results by descending submission date; unrelated name matches were excluded.
- A batch `id_list` query verified the selected adjacent versions, including WISE, TTT layers, SEAL, TT-SI, Beyond Perplexity, TTCD, VANE, Modular TTT, Self-Guided TTT, LOKI, the TTT safety paper, and the decision-theoretic paper.

B0 additionally uses the original [LoRA paper, 2106.09685v2, §4.1](https://arxiv.org/html/2106.09685v2) for its factorized update equation. Its scalar calculations and two-slot latent-memory illustration are educational constructions, not additional literature findings or experimental replications.

These bounded searches can miss older work, different terminology, and later follow-ups. In particular, procedural editing, continual meta-learning, and adaptive update-source selection deserve a focused search when we choose a study. “Explicitly open in P3” means open in that paper, not proven open across all subsequent literature. None of S1–S5 is labeled a confirmed novel contribution.

The earlier abstract review remains historical background. This file now owns the working paper/question/study map; subsequent assessments and discussion should update it here.
