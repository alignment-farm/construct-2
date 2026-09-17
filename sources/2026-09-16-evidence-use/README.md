# Learning to use revisable evidence — 16 September 2026

Root selection reading for [reusable evidence use](../../notes/EVIDENCE_USE.md).
These are inspected primary methods and author-reported results, not local
replications. No author implementation was inspected. No new ancillary review
was performed; local synthesis uses the existing accepted root assessments.

## Exact versions and implications

### P54 — RAFT, 2403.10131v2

[Primary text](https://arxiv.org/html/2403.10131v2), §§3–5, Tables 1–2.
Training combines question, relevant/distractor documents and teacher-generated
reasoning with citations. Some training examples omit the relevant document
while retaining the answer target, deliberately encouraging memorization.
The authors report in-domain QA/API improvements and distractor robustness.
The §4.4 experiment supplies golden evidence plus distractors at evaluation;
§5 separately examines retrieved top-k inputs. Do not conflate these settings.

**Answers** whether supervised experience can improve document use.
**Narrows** the allocation claim: the recipe mixes reading and answer storage;
its reported gains do not isolate durable reading under successive corrections.
Teacher reasoning and answer-format effects also belong in the comparison.

### P55 — RA-DIT, 2310.01352v4

[Primary text](https://arxiv.org/html/2310.01352v4), §§2–3, §§5.1–5.2, Tables 4–6.
The model and query encoder are tuned separately; passage-conditioned predictions
are combined. Reader training includes irrelevant passages paired with correct
answers, allowing parametric fallback. Evaluation includes tasks outside the
training mix, with in-domain development selection for some tasks.
The five-shot ablation reports averages 53.8 for the base combination, 53.9 for
reader tuning alone and 54.6 for dual tuning. Larger zero-shot improvements must
not be presented as the isolated reader effect against a developed few-shot use.

**Answers** the broad possibility of learning useful evidence integration.
**Redirects** toward strong contextual controls and separate reader/retriever
claims. It does not establish repeated correction or acquisition repayment.

### P56 — Controlled ICL/finetuning generalization, 2505.00661v3

[Primary text](https://arxiv.org/html/2505.00661v3), Datasets, Methods,
Experiments and Limitations. Controlled novel factual structures separate
pretraining knowledge from supplied information. Main evaluation uses
multiple-choice likelihoods; context contains training documents, subsampled
for the largest cases. In-context inference augments the finetuning material.
The authors report stronger generalization from context than ordinary finetuning
in many comparisons, with augmentation improving finetuning substantially.

**Narrows** claims that a failed training recipe establishes an inherent storage
limit. Additional inferred training targets consume computation and alter the
experience presented to the learner. These are not direct complete-task,
successive-revision or cost-matched agent results.

### P57 — Context-Parametric Inversion, 2410.10796v3

[Primary text](https://arxiv.org/html/2410.10796v3), §§3–4 and theoretical setup
in §5 (not an independent proof check). The authors track context reliance during
instruction tuning and report a rise followed by decline across model/data
settings. Filtering for context-dependent inputs alone does not remove it.
Their context-critical distinction concerns whether the answer still has a
predictive route without the context, including teacher-forced answer prefixes.
Removing low no-context-loss examples mitigates decline with other-performance
tradeoffs. The simplified theoretical model is explanatory, not a general theorem
about agent maintenance.

**Answers** whether ordinary successful instruction tuning guarantees increasing
context reliance: it does not in these experiments. **Redirects** acquisition
diagnosis toward what experience actually requires the model to use. Our EU2
expectation extends that account to accumulated local experience and is untested.

### P58 — Context-faithful Prompting, 2303.11315v2

[Primary text](https://arxiv.org/html/2303.11315v2), §§3–4 and Limitations.
The methods change instructions and retrieve counterfactual demonstrations;
one prompt frames the answer relative to a narrator's statement. The authors
report improved conflict handling and selective answering, with limitations for
smaller models. Context reliability is assumed; intricate reasoning over updated
knowledge is outside their scope.

**Answers** whether an unchanged model with better context is a serious
alternative. **Redirects** the control toward developed lessons and appropriate
demonstrations rather than a default prompt. It supplies no guarantee for a new
model or complete procedural workload, and does not determine source authority.

### P59 — CARE, 2509.13683v1

[Primary text](https://arxiv.org/html/2509.13683v1), §§3–5 and Limitations.
Supervised training integrates labeled supporting facts into teacher reasoning;
GRPO then combines answer, format and literal-context-span rewards with a
curriculum. Answer labels remain necessary during RL. The authors report gains
on ordinary and counterfactual multi-hop QA; Qwen2.5-7B CofCA F1 is 64.56 versus
58.38 for the original model and 59.21 for SFT alone. These are F1 scores, not
complete-task success rates. Baselines include default prompting and other
retrieval systems, not a matched retained-lesson lifetime comparison.

**Answers** much of the generic proposal to learn reasoning over changed evidence.
**Narrows** remaining work to useful durability and cumulative costs through
corrections from an agent's inherited experience. Training used eight 80GB GPUs;
the published training recipe is not established feasible on our available Mac.
Its positive evidence is relevant without requiring a local reproduction.

## Discovery and provenance

Three successful sequential arXiv `id_list` requests, separated by more than
three seconds, used the User-Agent `Construct-2 literature mapping (local research
metadata cache)`. Responses are cached as [metadata.xml](metadata.xml),
[conflict-metadata.xml](conflict-metadata.xml) and
[care-metadata.xml](care-metadata.xml). They identify the six versions above.
Initial HTML inspection included RA-DIT v2 and the controlled study v2; the
selected reading was updated to v4/v3 before synthesis. A guessed RAFT v3 URL
returned 404; only v2 supports its entry.

Supplementary web discovery searched combinations of retrieval-augmented
finetuning, generalization, changing rules and knowledge conflicts. Main queries:

- `site.arxiv.org retrieval augmented fine tuning RAFT generalization unseen documents knowledge updates reasoning`
- `site.arxiv.org fine tuning versus in context learning reasoning generalization explicit knowledge procedures`
- `site.arxiv.org learning interpret policies structured rules semantic parsing changing rules generalization retrieval`
- `"Teaching LLMs How to Learn with Contextual Fine-Tuning" arxiv`
- `site.arxiv.org knowledge conflicts retrieval fine tuning counterfactual documents RAFT context adherence`
- `site.arxiv.org "RA-DIT"`
- `site.arxiv.org "context" "knowledge conflicts" "instruction tuning" 2025`
- `site.arxiv.org "context" "fine-tuning" "counterfactual" faithfulness`

Targeted RAFT/controlled-study and ICLR identifier searches resolved primary
pages. Secondary discovery summaries are not evidence for the conclusions.
Screened but not method-inspected leads include contextual fine-tuning
2503.09032, counterfactual-noise robustness 2305.01579, knowledge-reliance control
2503.15888, CLEAR 2510.12460 and Faithfulness-QA 2604.25313. They remain leads,
not accepted findings or grounds for claiming absence of overlap. This bounded
search selects a useful comparison; it is not an exhaustive novelty review.
