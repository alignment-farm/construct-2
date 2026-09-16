# Learning adaptation decisions: public-research review

16 September 2026. Targeted reading for the root's
[adaptation synthesis](../../notes/ADAPTATION_DECISIONS.md), conducted while the
placement study runs independently. These are author-reported results and our
interpretations. No implementation, training run or local replication was performed.

## What this reading changes

Learned memory management, online memory-policy improvement, harness optimization
and model–harness interactions all have direct precedents. A general selector
among several kinds of change is also already proposed. The root's existing
hybrid hypothesis is consistent with this work; it is not a new architecture claim.
The remaining comparisons concern useful intervention choices, transfer across
changed recipients and selective reuse of experience. These sources narrow those
questions without establishing comprehensive novelty.

| ID and exact version | Reading scope | Finding and consequential limit |
|---|---|---|
| **P39 — [AgeMem, 2601.01885v3](https://arxiv.org/html/2601.01885v3)** | §§3.1–3.3; §4.2 tool use and §4.3 ablations | RL coordinates six provided memory operations across long- and short-term state. Staged training forces persistent-memory use. The action space and tool semantics are supplied; reported token reductions coexist with increased tool calls. This answers the broad feasibility question for learning memory operations, not their universal cost advantage. |
| **P40 — [Memory-R1, 2508.19828v5](https://arxiv.org/html/2508.19828v5)** | §3 method; §4.4 ablation overview; limitations | A manager learns memory edits from downstream answer rewards; an answer agent learns to select useful retrieved entries. The answer agent is frozen during manager training and the components are trained separately. Gold-answer supervision supplies the reward. This is direct prior art for learned admission and selection, not a demonstration of choosing weight versus harness changes. |
| **P41 — [Life-Harness, 2605.22166v2](https://arxiv.org/html/2605.22166v2)** | §§3–5, especially §4.4 adaptation and evaluation setup | An external coding agent improves a frozen executor's contract, skills, action realization and trajectory regulation using training trajectories. The harness is frozen for held-out evaluation. Reported transfer supports interface adaptation; it does not establish that the deployed executor learns an intervention policy during evaluation. |
| **P42 — [Co-Evolving Harnesses and Models, 2609.09134v1](https://arxiv.org/html/2609.09134v1)** | §§3.1–3.3, Table 1 and Appendices A–C | In the Qwen seven-task comparison, imitation reduces evolved-harness mean accuracy from 78.0 to 63.1; the correction recipe reaches 79.7, with some task declines. Gemma replication is WebArena only. The proposed planning-style explanation uses judged failure categories and examples, not uniquely identifying causal controls. Results establish compatibility concerns; the recipes do not isolate every data/objective difference. |
| **P43 — [HarnessBandit, 2609.13739v1](https://arxiv.org/html/2609.13739v1)** | §§3–5, Algorithm 1, setup and result tables | Selects among six fixed harnesses per GRPO step from previous advantage and gradient-alignment signals. Signals follow paid updates. Comparisons change scheduling and batch composition together; a uniform harness-pure scheduler would better isolate learned choice. Reported held-out gains are metric-dependent: Claw strict Pass3 ties the base. This supplies a method lead, not an isolated general benefit of adaptive intervention selection. |
| **P44 — [Interactive Memory Learning, 2609.17088v1](https://arxiv.org/html/2609.17088v1)** | §3, §4.1 setup, §4.2 ablations and §4.3 analysis | Saving and retrieval policies co-adapt online through shared actor–critic learning after supervised warmup. A buffer credits later response-quality judgments to retained memories. The paper's “truth reward” is judge-based, not a counterfactual causal measurement. Conversational metrics differ from complete procedural behavior. This answers the generic possibility of continued memory-policy learning; it narrows a contribution to decision transfer, feedback validity or another specified boundary. |
| **P45 — [Next-Generation Agentic RL, 2607.01120v2](https://arxiv.org/html/2607.01120v2)** | §5 proposed intervention selection; §§6–7 prototype scope | Explicitly proposes choices among memory, skills, harness, tools and weights using trajectory evidence. AReaL2.0 connects deployed trajectories to policy updates; the authors state that the prototype covers only the weight-update branch. It is direct conceptual overlap with a general adaptation selector, not empirical validation of the complete proposed system. |

These results concern different learners, action spaces, feedback and evaluation
conditions. We do not combine them into a performance ranking or infer one shared
mechanism. In particular, the broad fact of component interaction is already
studied; a later local comparison must specify what additional uncertainty it
resolves.

## Discovery and provenance

Three successful arXiv API requests are cached in
[selected-metadata.xml](selected-metadata.xml),
[additional-metadata.xml](additional-metadata.xml) and
[decision-discovery.xml](decision-discovery.xml). The last returned the latest
20 results for an agent/memory-management-or-harness/learning-or-adaptation query.
[retrieval.json](retrieval.json) records URLs, timestamps, headers, hashes and the
descriptive User-Agent. Requests used one connection at a time with at least
three seconds between requests. Supplementary searches are recorded in
[web-discovery.json](web-discovery.json).

[screening.json](screening.json) distinguishes targeted methods reading, inspected
abstract leads and title/date screening. DGM and MemGen metadata were retrieved
as adjacent leads, without new full-text reading. Recent leads include Modular
RSI, Ecdysis, Grounding Agent Memory: Environment-Probing Curation for Enterprise
Agents, and Code-to-Harness.
Their abstracts suggest useful follow-up on coordinated modules, recurring-failure
diagnosis, memory validation and experience-derived harnesses; no detailed claims
from their methods are adopted here.

[full-text-retrieval.json](full-text-retrieval.json) records the seven exact HTML
versions and hashes. Full-text copies are temporary local caches, not committed
paper mirrors; versioned public URLs are the durable references. Reading scopes
above are targeted rather than complete audits, and author code was not inspected.
The result limit, search vocabulary and selective follow-up leave coverage gaps.
A statement that this pass did not establish a working general selector is not
a claim that no such system exists.
