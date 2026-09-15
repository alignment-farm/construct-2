# Maintenance reliability: focused methods reading

15 September 2026, after the third-phase synthesis and the user's approval of
the next root focus. Supports [MAINTENANCE_RELIABILITY.md](../../notes/MAINTENANCE_RELIABILITY.md).
This is a methods comparison, not a reproduction or systematic novelty review.

| Source | Exact version and scope read | Relevance |
|---|---|---|
| **P23. Gradient Episodic Memory for Continual Learning** | [1706.08840v6](https://arxiv.org/html/1706.08840v6), §3, equations 5–8 and Algorithm 1; evaluation-metric context | Per-task remembered-loss constraints and local approximation assumptions. |
| **P24. Efficient Lifelong Learning with A-GEM** | [1812.00420v2](https://arxiv.org/html/1812.00420v2), §§2–4 and Appendix D.2 | Average versus per-task protection; cheaper sampled reference; separation of development and evaluation task streams. |
| **P25. Gradient based sample selection for online continual learning** | [1903.08671v5](https://arxiv.org/html/1903.08671v5), §§3.1–3.5 | Buffer population as constraint reduction, gradient diversity and the move from constraints to rehearsal. |

No reported benchmark gain from these papers is used as a local prediction of
method superiority. We did not inspect or run their author implementations.
MIR/P22 already has a local adaptation and author-code ledger in S1; P14/VANE's
candidate validation remains prior background, not new reading in this pass.
The root inference concerns what these surrogate objectives do and do not tell
us about complete procedural behavior. That relationship needs its own evidence.

## Retrieval and limits

One arXiv API title query succeeded, returning the first eight of twelve matches
ordered by relevance. [arxiv-query.xml](arxiv-query.xml) preserves the response;
[retrieval.json](retrieval.json) records its URL, timestamp, user agent, hash and
the exact full-text versions read. There was one API connection and one request;
no repeated requests or pagination. Full text was read through the web tool at
the versioned primary HTML URLs above, with no local full-text copies.

The query also returned unrelated Bayesian-optimization and later application
papers, a GEM quadratic-program correction, and a soft-constraint variant.
These were not developed into supporting sources. This pass establishes selected
method overlap, not coverage of subsequent continual-learning or decision-policy
work. A future implementation choice should inspect the relevant author code
and broaden the search for the concrete comparison.
