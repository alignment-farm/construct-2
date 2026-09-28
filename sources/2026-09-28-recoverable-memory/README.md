# Recoverable memory — 28 September 2026

Supports [the root assessment](../../notes/RECOVERABLE_MEMORY.md). This bounded
reading revisits S4's recovery question independently of active ancillary work.
It concludes with theory and research selection, without a new experiment.

## Provenance and discovery

Root began at `f570b2d` on `main`, with the preceding evidence-acquisition work
and expanded EBM direction uncommitted. Those changes were preserved. Investigator:
`gpt-6-astra`, `xhigh`, OpenAI provider, Codex Desktop `0.158.0-alpha.2.1`, verified
from session metadata and current turn context; see [provenance.json](provenance.json).
No delegation, participant calls, training, code execution from publications,
or ancillary-repository inspection occurred. Investigator costs are unmeasured.

One cached arXiv API discovery request returned HTTP 406 with an empty body and
no Retry-After header. It supplied no search results and was not retried. Targeted
web searches and versioned primary full text supplied the readings. The query
and supplemental search strings are in [discovery.json](discovery.json).
[retrieval.json](retrieval.json) records downloaded primary URLs, times, bytes
and SHA-256; raw payloads remain in ignored `.cache/recoverable-memory/`.
Acquisition of a full document does not imply full inspection. This is a focused
comparison, not comprehensive coverage or a certified literature gap.

## Inspected methods and consequences

**P114 — [M+, 2502.00592v2](https://arxiv.org/html/2502.00592v2).** Read §§3.1–3.2.3,
4.1–4.4, 4.6.3 and Appendix E.2–E.5. Promotes the earlier abstract-only S4 lead.
The method archives displaced latent vectors, retrieves them with trained
projectors, and evicts the oldest at its archive limit. **Answers** feasibility
of learned latent retrieval beyond an active pool. Reported longer retention
uses added CPU storage with similar GPU cost; this is not equal total storage.
Appendix E.2 calls compression lossless, but the inspected material supplies no
exact source-decoding validation. **Narrows** the claim to demonstrated task
retention and capacity/access trade-offs. We do not infer either guaranteed
losslessness or inevitable information loss from the number of latent positions.
No implementation or reported result was reproduced.

**P115 — [R³Mem, Findings of ACL 2025, pp. 4541–4557](https://aclanthology.org/2025.findings-acl.235.pdf).**
Read §§2.1–2.3, experimental setup, §§3.1–3.3 and Appendix C's reversibility
argument. Uses hierarchical compression, virtual memory tokens, adapters and
bidirectional/cycle training. **Answers** availability of a concrete reconstruction
method. **Narrows** the meaning of recovery: an invertible transformation of
complete internal streams does not prove source reconstruction from whatever
subset survives compression. The inspected evaluations use perplexity, QA and
dialogue measures, not exact source round trips. Its reconstruction claims
remain author claims; we have neither reproduced nor refuted the architecture's
empirical performance. A lossless-archive comparison would need to identify all
retained streams and check recovery at that boundary.

**P116 — [LazyMem, 2607.22690v2](https://arxiv.org/html/2607.22690v2).** Read §§3–4.5,
Appendices C.1–C.2 and D.1. Preserves raw messages and trains Qwen3-4B through
SFT/GRPO to select and compress retrieved windows for a fixed answer model.
**Answers** generic feasibility of the small-specialist proposal. Authors report
0.85 judged accuracy on their 100-question LongMemEval test split and 213
answer-context tokens; LoCoMo's selected test subset scores 0.68. These are not
full-benchmark results. Mean online latency is 40.86 seconds versus NanoMemory's
55.35 and RAG Top50's 30.24: fewer answer tokens need not mean faster total use.
Parallel windows and different constructor sizes contribute to the comparison;
offline costs are excluded. **Redirects** our question toward useful recovery
and lifetime cost after changing needs. Its error attribution already separates
retrieval, editing and answering. No code, data, checkpoints or raw outcomes
were audited; training repayment and continuing deployment adaptation remain
unestablished by this reading.

**P117 — [What Should an Agent Forget? / RD-Forget, 2609.10263v1](https://arxiv.org/html/2609.10263v1).**
Read §§3–6, Algorithm 1 and Tables 1–3. Retains sources, then uses a frozen
curator, scoped replacements and query-conditioned eligibility to form evidence
views. **Answers** existence of an explicit source-preserving alternative.
**Narrows** interpretation: its 2,048-token budget covers the final view, with
upstream source reading separate; some evaluation supplies oracle sessions or
task-type metadata. Disabling rescue excludes non-active entries but still
allows fresh curation from the archive, so it does not remove every recovery
path. Reported scores support the evaluated configurations; they do not isolate
the value of preserving raw history or establish total-cost superiority.
No implementation or outcomes were audited.

## Selection and limits

The four methods support a comparison of what persists, how it becomes
accessible, and what the reader can do with it. They narrow generic proposals
for latent archives, reconstruction or trained context construction. The root
note's risk decomposition, finite-history argument, two-bit illustration and
cost condition are our analytical synthesis, not claims of a novel theorem or
new experimental evidence. They preserve uncertainty about learnability and
practical recovery cost.

Memento, MemRefine, CMT and papers in the inspected references remain discovery
leads; no conclusion here relies on their methods. Secondary discovery summaries
were not used as evidence. The LazyMem repository landing page was encountered
during discovery but no commit was pinned or implementation inspected; it is
not a reproducibility assessment. P8/P10/P11/P13 and earlier Construct/S4 findings
retain their prior review boundaries. No ancillary acceptance, prediction or
commission changed.

Validation: primary-cache hashes and version markers, local document links,
paper numbering, preservation of pre-existing research files and `git diff
--check`. See [validation.json](validation.json). This is document/source checking,
not model evaluation.
