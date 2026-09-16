# Bounded remedy-choice review

16 September 2026. Supports the
[root assessment](../../studies/2026-09-16-remedy-feasibility.md).
Source code was inspected statically; no author model, retriever, preparation
pipeline or training procedure was executed. A root script reads published
artifacts and independently recalculates one released correctness slice.

## Pinned evidence

| Source | Revision / scope |
|---|---|
| [S4](https://github.com/alignment-farm/memory-under-goal-shift/tree/981719ffcda62fed0913461b50c0e97dbb4c10c8) | Local and remote HEAD match root's accepted `981719ffcda62fed0913461b50c0e97dbb4c10c8`; clean tree. Instructions, overview, FUTURE_USE brief, third-phase methods/publication, history, runner, costs and 10 evaluation files read. |
| [P52 CRAG author release](https://github.com/HuskyInSalt/CRAG/tree/de7c2961ae624a1483a138c5798e1f6d0c4fb0e0) | `de7c2961ae624a1483a138c5798e1f6d0c4fb0e0`; linked by exact paper **2401.15884v3**. README, launchers, inference, internal/external/combined preparation, evaluation and selected utilities read; context-file counts inspected. |
| [P53 Adaptive-RAG author release](https://github.com/starsuzi/Adaptive-RAG/tree/0c88670af8707667eb5c1163151bb5ce61b14acb) | `0c88670af8707667eb5c1163151bb5ce61b14acb`; linked by exact paper **2403.14403v2**. README, label construction/merging, postprocessing, evaluator normalization and success recording read; predictions archive sampled as described below. |

No AGENTS.md was present in either public checkout. Initial discovery also
cloned the AsH1605/Adaptive-RAG fork; after the paper identified starsuzi's author
release, only the latter was used as evidence. Public clones are temporary;
revision links and source hashes preserve the review boundary.

**CRAG implementation qualifications.** The launcher negates the supplied lower
threshold inside inference, so its positive CLI argument is not by itself a
paper/code contradiction. The combination script lacks an argparse import and
an initialized output list; its enumerate/zip loop also binds an integer and
tuple where strings are combined. Static defects were not repaired or run.
ARC's unequal context counts require an ID-based alignment check before reuse;
counts alone do not prove which rows are misaligned. Existing cached contexts
avoid preparation but do not make acquisition free.

## Added literature and selection effect

**P53 — [Adaptive-RAG, 2403.14403v2](https://arxiv.org/html/2403.14403v2).**
Read §3, Table 1, §5's training-data analysis/Table 4 and limitations. A small
classifier selects no, single or multi-step retrieval. Training prefers the
simplest successful strategy; dataset biases label cases without successful
outputs. Author-reported ablations trade quality against retrieval work. The
code's label construction and offline selection of cached predictions match
that account. **Answers** the generic outcome-to-strategy learning proposal;
**narrows** AD1 because the comparison is prior to answering and does not isolate
post-failure evidence acquisition from reading repair. Full training and reported
headline metrics were not reproduced. The root's 500-query recalculation is a
separate, limited check of released outputs.

Two focused web queries followed the access/action distinction:

- `site.arxiv.org adaptive retrieval augmented generation contextual bandit feedback routing strategies`
- `site.arxiv.org retrieval reasoning adaptive choose strategy outcome rewards Adaptive RAG`

Other returned work, including Process vs. Outcome Reward (2505.14069) and Online
Learning with LLM Experts from Limited Feedback (2609.05820), remains discovery
leads, not inspected methods or supporting evidence. No comprehensiveness claim.
One sequential arXiv API request retrieved P53 metadata. Exact URL, UTC time,
descriptive User-Agent, headers and SHA-256 are in [retrieval.json](retrieval.json);
the raw response is [metadata.xml](metadata.xml). Exact-version HTML was read
through the web tool; paper text is not stored here.

## Reproducible artifact check

[artifact-review.json](artifact-review.json) records per-seed S4 metrics, costs,
paired data/query hash checks, CRAG file counts, public source hashes and the
Adaptive-RAG slice. Its 500 NQ development queries were chosen as one bounded
single-dataset inspection, not selected for a positive result. All three arms
share IDs and ground-truth aliases. Recomputed normalized exact-match sets equal
the released labels. The union is a retrospective oracle; no policy was trained.
Full action outcomes and labels were available to this review, unlike online
partial feedback. No new inference was purchased or deployment cost estimated.

With the repositories checked out at the pins above:

```sh
uv run python scripts/remedy-feasibility-review.py \
  --s4 ../ancillary-studies/memory-under-goal-shift \
  --crag /tmp/construct2-crag-bounded-review \
  --adaptive /tmp/construct2-adaptive-rag-author-review \
  --output sources/2026-09-16-remedy-feasibility/artifact-review.json
```

The script requires only the standard library and checks each HEAD. It changes
only the requested output file. An initial archive-name filter also selected
sidecars and stopped at its uniqueness assertion; restricting it to the exact
prediction filename resolved this before any result was produced. S4's models,
sampled histories and original metrics were not regenerated in this pass.
