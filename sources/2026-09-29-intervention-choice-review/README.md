# Intervention-choice publication review — 29 September 2026

Supports the [root assessment](../../studies/2026-09-29-intervention-choice-findings.md).
Review scope: first experiment and source-parser follow-up, through
`cb25d5c64bd64859e0e9abbcfc41f0e8f44762df`, from preparation
`3cabc29aa1b784ec8a9129c568224d90badb9cd6`. Accept the reported bounded limitation;
the broader research question remains open. No participant calls or new task
cases were generated for this review.

## Publication and provenance

[boundary.json](boundary.json) records the five publication/development commits,
archive hash and clean study status. Read local AGENTS, README, BACKGROUND, START,
phase-1 report, both protocols, source ledger, provenance, all four implementation
files and all three test files. Examine saved generations, policy records, costs,
source hashes and relevant historical versions. Fetch confirmed local and remote
`main` at the same reviewed revision. The active study checkout was not edited;
replay used an ignored archive under `.cache/2026-09-29-intervention-review/study`.

Root began at `ea166d581e0101b3cf92b17bae1a1308cd5a69a9` with the preceding EGI/ESM
review uncommitted. That work remains preserved. Root investigator is
`gpt-6-astra`, `xhigh`, OpenAI, Codex Desktop `0.158.0-alpha.2.1`, continuing session
`01a0e7b0-fe8a-7c53-a0a8-23dde8a9c170`, as previously observed in session metadata;
no independent backend fingerprint or delegated reviewer.

Study investigator reports `gpt-6-astra`, **medium**, OpenAI, Codex CLI `0.158.0`,
session `01a0ebca-8395-75d0-a7a3-10439f6a4f8a`. Its evidence is local harness
metadata, not backend attestation. The participant is the reported Docker
Qwen3 8B service, manifest
`79fa56c07429f64f41950fe2f524937cf3ae9ea9bd3d7ada72170b036ea3cc85`, reporting 8.19B
parameters and mixed `IQ2_XXS/Q4_K_M`. Model weights, serving identity and speed
are not independently validated by root. There is no neural update in this phase;
mutable experimental state is the policy JSON table.

## Replay and material checks

[review.py](review.py) and [review.json](review.json) retain the independent root
checks. `uv sync --frozen` creates a dependency-free Python 3.13.12 environment
in the archive, versus the study's reported 3.14.7. All **nine** published unit
tests pass; those test grammar examples, adapters, validity and repair boundaries.
The root script then:

1. Verifies **nine** final source hashes, experiment/protocol bytes at each run's
   recorded Git revision, and policy/parser freezes before their outcome files.
2. Re-parses **84 raw model responses**, applies the actual adapter/validator,
   and compares exact scores and field failures. Root reconstructs expected minor
   units with integer-string arithmetic, separately from the treatment's Decimal
   adapter. All request objects equal the specified source-and-contract prompts;
   all recorded responses ended with `stop`.
3. Reconstructs all acquisition counts, C/C/D choices, the C global winner and
   frozen policy hashes. No new training or policy write is performed.
4. Re-executes **36 source-order repairs** and independently recomputes all
   decisions and charges in both eight-policy comparison tables, including
   fallback's failed initial calls. Raw and repaired values match publication.
5. Re-executes source parsing and adaptation on **72 development and 36
   confirmation API tasks**, checks source-derived canonical values against gold,
   and checks final payloads against the root reconstruction. Cohort invoice IDs
   are disjoint; saved datasets reproduce from the specified generator seeds.
6. Reconciles phase usage and request-time totals against all raw responses.
   Ten failed complete tasks remain included. No conversion to dollars or
   exclusive device time is made.

The original follow-up protocol hash intentionally differs from the final prose:
root resolves it at `9eb5073`, where the parser is already frozen and follow-up
outcome files are absent. Publication clarifies that structural unit tests had
instantiated future seeds before parser evaluation. The tests did not invoke the
parser on seed 440 or emit its source/model outcomes. This is an auditable
qualification to freshness, not a reason to pretend those values had never been
constructed. Commit order does not independently attest wall-clock chronology.

The supplied `audit.py` checks several original records but does not reparse raw
responses, rerun the parser, or fully recompute policy costs. Root adds those
checks rather than relying solely on the saved audit. Reusing the inspected
adapter/parser/validator still means this is outcome reproduction, not a second
independent language specification or a model regeneration. Synthetic source/gold
construction is inspected; natural-source label reliability remains untested.
No broad security or production API execution claim is made.

Reproduce from an extracted archive of the reviewed revision:

```sh
uv sync --frozen
uv run python -m unittest discover -s tests -v
uv run python /path/to/construct-2/sources/2026-09-29-intervention-choice-review/review.py . /path/to/intervention-choice-transfer-git /fresh/review.json
```

The Git repository argument supplies immutable historical protocol/source bytes.
The root script writes only its output path. Use a separate output to preserve
this record. It neither invokes `request()` nor writes acquired policy files.

## Public-method comparison

A targeted comparison of algorithm-selection evaluation and structured-output
correctness, not exhaustive discovery or a newly established literature gap.
One cached arXiv API query retrieves ASlib, JSONSchemaBench and LLMStructBench
metadata using a descriptive User-Agent; no concurrent metadata requests.
[metadata.xml](metadata.xml) and [public-sources.json](public-sources.json) preserve
versions, URLs, hashes and acquisition failures. Full paper assets stay in ignored
cache. An arXiv ASlib PDF request returned 406, and one author-mirror browser
request timed out; a second author's PDF and versioned JSONSchemaBench HTML
succeeded. No study benchmark implementation or external model was run.

**P126 — Bischl et al., ASlib: A Benchmark Library for Algorithm Selection (2016).**
Read the [author-hosted PDF](https://www.cs.uwyo.edu/~larsko/papers/bischl_aslib__2016.pdf):
§2.1 definition, §3 workflow, §4 opening and §6.2–6.3. The retrieved author-copy
hash identifies the exact inspected document; arXiv metadata reports 1506.02465v3,
but those PDF bytes were not obtained from arXiv. The method separates fixed and
perfect per-instance choices and charges feature/probe work. Its examples permit
features to solve the task before selection. **Root inference:** the local oracle
gap is conditional on the available actions; a source check that solves the task
changes that comparison. This narrows further selector proposals without testing
agent-change transfer. No benchmark results reproduced.

**P127 — Geng et al., JSONSchemaBench**, [2501.10868v3](https://arxiv.org/html/2501.10868v3),
27 February 2025. Read introduction, §2 constrained-decoding description and
§6 quality setup/results. Unlike the study's v1 reading, root's claims refer to
v3. It evaluates coverage/compliance separately from downstream task accuracy;
authors report constrained-decoding gains on three reasoning tasks. **Root
inference:** constrained generation is a credible untested structural remedy,
but a schema-compliant amount need not match source evidence. These methods
narrow interpretation of the local validator fallback; they do not guarantee
semantic repair or demonstrate acquired intervention decisions. No engine or
published experiment reproduced.

LLMStructBench 2602.14743v1 was metadata-checked, not independently method-reviewed
by root in this turn. The study's inspection and Self-Refine site reading retain
those author-reported boundaries. P120–P123 remain previously inspected root
background; none was re-reviewed or treated as fresh evaluation data here.
