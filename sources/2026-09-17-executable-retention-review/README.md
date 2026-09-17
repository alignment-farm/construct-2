# Executable-retention publication review — 17 September 2026

Review of `alignment-farm/executable-experience-retention` at
`baf4d764cb4e571551a2b69d45751bb7f3281eaf`, advancing the root boundary from
preparation `34a902fedf99a22fff3c9429d49146809af8a86a`. Local main and remote
main agree; the study tree is clean at review. The
[root assessment](../../studies/2026-09-17-executable-retention-findings.md)
accepts the publication and closes the bounded stable-use phase.

## Reading and evidence depth

Read AGENTS.md, README with its preserved brief, REPORT.md, REPRODUCE.md,
protocol/initial.md and amendments 01–03, results/methods-and-limits.md,
results/tables.md, acquisition/environment notes, source provenance and Git
history. Inspected experiment.py, workload.py, worker.py, test_harness.py,
verify_evidence.py and publish_accounting.py, acquired source and both lesson
versions. The evaluation code is unchanged from `3328619` through publication.

The consequential uncertainties were whether complete answers really agree,
whether reconstruction sees retained source, and whether checking or omitted
failed work explains the cost difference. The independent
[audit script](../../scripts/review-executable-retention.py) reads saved evidence
without importing the study's code or executing generated programs:

```sh
uv run python scripts/review-executable-retention.py \
  --study ../ancillary-studies/executable-experience-retention \
  --output sources/2026-09-17-executable-retention-review/checks.json
```

[checks.json](checks.json) records the results and manifest hash:

- All 122 manifest entries match; ready and archive source agree exactly.
- An independent integer-cent calculation matches eight fresh gold answers and
  all 32 saved current outcomes. Six requests have positive outputs.
- All ten saved candidate-check batches and invocation-time development outputs
  match the same five supplied examples; candidate/source identities agree.
  Ten generated source files and both lesson versions match their raw responses.
- Nine reconstruction prompts contain the contract, development examples,
  corrected lesson and request/page-size metadata. They contain no acquired
  implementation, hidden answer or full fresh dataset. Model mode and cap agree.
- Raw-response tokens, attempts and measured waits reproduce the arm and selected
  deployment accounting. Every policy makes 698 page reads, including checks;
  two timeouts have no token usage. All 12 structured successful responses end
  with `stop` and report the same backend fingerprint.

The study's own offline verification and 32-case container replay logs were
inspected. Root checking is saved-evidence rescoring, not an independent rerun of
model acquisition, generated code or timing. The initial capability probe is a
transcription; timeout tokens and investigator work cannot be reconstructed from
the ledger. Source availability and gold separation also rely on the inspected
runner and container invocation. No ancillary files were edited.

## Focused public follow-up

**P64 revisited — [A Compute-Matched Re-Evaluation of TroVE on MATH,
2507.22069v2](https://arxiv.org/html/2507.22069v2).** Revisited §§3, 4.1 and 4.3.
Its call-budget matching and selection correction distinguish toolbox claims
from sampling effects. **Narrows** local attribution: equal useful checking
and recorded incurred work matter, but a study of reconstruction avoidance
should not require needless generation merely to equalize call counts. The
MATH result is author-reported and not replicated here; its sampling experiment
does not answer this local archive/cache comparison.

**P85 — [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented
LLM Agents, 2608.19662v1](https://arxiv.org/html/2608.19662v1).** Read §§3–4 and
§6's reuse/model comparisons, Tables 2–4. The method changes attention and
positions, fine-tunes models, and caches schema representations. Evaluation
uses invocation F1; cache-hit prefill timing excludes offline construction.
Compression has quality costs, especially for unseen resources. **Answers**
generic modular schema-cache proposals; **narrows** a future contextual-cost
claim. It neither retains executable implementations nor measures complete
reconciliation tasks. No code was inspected and no local serving support for
this method was established. These are author-reported methods/results.

This follows the ReCache discovery lead in the
[persistence-control ledger](../2026-09-17-persistence-controls/README.md).
P71/P74's prior artifact and delivery assessments remain applicable; they were
not re-audited. Disk source caching, model prefix caching and reusable resource
KV blocks retain different objects and avoid different work. A future comparison
should specify which is available and charge its setup; this review does not
select a new cache experiment or reopen stable reuse.

## Retrieval boundary

Focused arXiv-domain web searches resolved the ReCache and TroVE identifiers;
the similarly named diffusion ReCache and provenance TROVE are unrelated leads
and supply no claim. One serialized query-API request verifies both exact versions
in [selected-metadata.xml](selected-metadata.xml). [retrieval.json](retrieval.json)
records timestamp, descriptive User-Agent and SHA-256. Versioned HTML was read
through the web tool; no new full-text mirror or author implementation is stored.
This targeted follow-up does not establish exhaustive novelty or current coverage
of every cache mechanism.
