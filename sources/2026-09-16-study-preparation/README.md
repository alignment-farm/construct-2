# Methods and workload preparation

16 September 2026. Follow-up to the [direction review](../2026-09-16-research-direction/README.md).
This pass inspected released implementation files and a candidate workload. It
ran no external code, installed no dependencies and invoked no models. Static
inspection establishes an implementation lead, not local runtime feasibility.

## What changes the proposed study

The preferred first implementation is **EARM's learned retrieval**, with evidence
remaining explicit. Its core needs NumPy; inference and memory extraction are
separate costs. The inspected online runner keys experience by memory ID and
scores previously unseen IDs. A content revision therefore requires a deliberate
choice about retaining or invalidating that experience. Changing an ID is not
cost-free: new IDs incur cold-start scoring. See the pinned `online.py`,
`matrix_completion.py` and reproduction guide below.

Cartridges and Doc-to-LoRA remain learned-content alternatives. The inspected
Cartridges attention path uses compiled FlexAttention; Doc-to-LoRA defaults to
CUDA/FlashAttention and declares GPU-oriented dependencies. Neither was verified
on Apple hardware. Doc-to-LoRA publishes Gemma, Qwen and Mistral checkpoints;
reusing one could avoid meta-training, but does not establish local compatibility.
The study should investigate a bounded port or smaller adaptation only if it
serves the comparison; reproducing a large training pipeline is not its purpose.

For maintenance decisions, the Jin–Ren repository supplies matrix-completion and
representation-based prediction implementations. Its matrix-completion script
exposes measured entries of a held-out task row. This supports a comparator that
uses a paid current-state observation; it is not a forecast before any update.

| Implementation | Revision inspected | Files most relevant to the decision |
|---|---|---|
| [EARM](https://github.com/FengQi-HITSZ/earm/tree/ea06cb9059e9ebf7ebd9bf036ff08e188c18f6e0) | `ea06cb9059e9ebf7ebd9bf036ff08e188c18f6e0` | `pyproject.toml`, `src/earm/online.py`, `src/earm/matrix_completion.py`, `docs/reproducibility.md` |
| [Cartridges](https://github.com/HazyResearch/cartridges/tree/ef34ba97a06049c34820506e2c283746284ae5f0) | `ef34ba97a06049c34820506e2c283746284ae5f0` | README, dependencies, attention implementation, example training configuration |
| [Doc-to-LoRA](https://github.com/SakanaAI/doc-to-lora/tree/baa85db4d5df9b29d618af432d6ebf28b3ad5a29) | `baa85db4d5df9b29d618af432d6ebf28b3ad5a29` | README, dependencies, Python API, model loader |
| [Forgetting prediction](https://github.com/INK-USC/lm-forgetting-prediction-code/tree/1a16c989b65142507b864277bccb4a6f3f2ca74f) | `1a16c989b65142507b864277bccb4a6f3f2ca74f` | README, `src/run_matrix_completion.py` |
| [τ-bench](https://github.com/sierra-research/tau2-bench/tree/2174a603f6d014ef94473ffa95957f6ce27100db) | `2174a603f6d014ef94473ffa95957f6ce27100db` | banking task schema and one document, release notes, MIT license |
| [MemoryData](https://github.com/OpenDataBox/MemoryData/tree/bdbe698f776d921ac791d1b07c0a7fc65a8bb4bb) | `bdbe698f776d921ac791d1b07c0a7fc65a8bb4bb` | README and repository inventory; harness not audited |

The [Doc-to-LoRA model repository](https://huggingface.co/SakanaAI/doc-to-lora/tree/7514da3cf18439265aef805f2a00170199e44456)
was inspected through metadata at revision
`7514da3cf18439265aef805f2a00170199e44456`; no weights were downloaded.
The checkpoint listing and workload counts are recorded in
[workload-inventory.json](workload-inventory.json).

## Workload lead and closer overlap

The pinned τ-bench banking corpus contains 698 document files and 97 task entries.
It supplies a concrete reference-and-request workload, including source-document
annotations. Those annotations are evaluator information, not free retrieval
answers. The first preparation inspected the schema and a sample, not every
task. Its release notes document grading and policy corrections: pin the release
and validate any edited cases. A controlled versioned subset would be an
adaptation, not a τ-bench leaderboard reproduction.

Three additional primary readings narrow the gap further. Results are
author-reported; these papers do not establish our proposed crossover.

| ID | Exact source and reading scope | Consequence for preparation |
|---|---|---|
| P36 | [Are We Ready For An Agent-Native Memory System?, 2606.24775v1](https://arxiv.org/html/2606.24775v1), §§3–4, especially 4.3 and 4.5 | Existing comparisons cover conflicting updates and construction/query costs. A general dynamic-memory cost benchmark would overlap. Our question must concern the useful lifetime of a learned component. |
| P37 | [Can Agent Memory Systems Track Evolving State?, 2608.19652v1](https://arxiv.org/html/2608.19652v1), §§4–5 | Typed changes, dependent consequences and anti-update controls already have a benchmark and explicit-state method. Use these distinctions rather than claim a new stale-memory taxonomy. Released-code feasibility was not checked. |
| P38 | [Supersede, 2606.27472v1](https://arxiv.org/html/2606.27472v1), §§2–4 and the reported training result | Learning supersession is already studied. Its no-refeeding condition differs from our accessible-evidence comparison; the reported single-run improvement leaves substantial failure. It is not evidence that learning universally resolves revision. |

The study can begin with document questions and decisions, avoiding a full user
simulator during workload development. It must say what this omits from complete
agent execution. Reuse should involve fresh requests, with answer caching allowed
for explicit controls; repeatedly asking an identical question is not sufficient.

## Retrieval record and limits

[implementation-retrieval.json](implementation-retrieval.json) records exact code
URLs, revisions, timestamps and content hashes. Source files remain in a temporary
cache. It records downloads, not a claim that every line was reviewed.
[workload-metadata.xml](workload-metadata.xml) and its
[retrieval record](workload-metadata-retrieval.json) pin P36–P38 through one
successful arXiv API request, after the earlier pass and using a descriptive
User-Agent. [web-discovery.json](web-discovery.json) records targeted searches;
results from secondary lists were only discovery leads.

The guessed τ-bench `banking_knowledge/policy.md` path returned 404; the domain
uses document and prompt files instead. No absent file is treated as reviewed.
These are selected implementation and workload checks, not an exhaustive novelty
search or a hardware benchmark. The first study still owns workload calibration,
the actual method adaptation and its experimental design.
