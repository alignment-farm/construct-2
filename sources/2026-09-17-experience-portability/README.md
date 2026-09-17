# Experience portability — 17 September 2026

Initial targeted reading for the proposed [root review](../../notes/EXPERIENCE_PORTABILITY.md).
This pass narrows the question; it is not a completed artifact review, a novelty
survey or a new experimental commission. Results are author-reported. No author
code, released evidence or local ancillary publication was inspected here.

## Inspected primary passages

**P75 — [Memory Transfer Learning, 2604.14004v1](https://arxiv.org/html/2604.14004v1).**
Read §§3.1–3.2 and 4.4, especially Tables 6–7. Memories from other models improve
reported average Pass@1 over no memory. Individual benchmark regressions remain;
Table 6 also contains a rounded cross/self-memory tie despite the prose's claim
of consistent self-memory superiority. Task-adaptive rewriting and reranking
underperform embedding retrieval in Table 7. **Answers** generic cross-model
reuse; **narrows** the case for automatic adaptation. These comparisons do not
establish a paid migration decision across a deployment sequence. Different
source memories do not isolate a receiving-model effect on one fixed archive.

**P76 — [Managing Procedural Memory in LLM Agents, 2606.23127v1](https://arxiv.org/html/2606.23127v1).**
Read §§2.1–2.3, 3.2, 4.3–4.4, limitations and Appendix B. The authors test
cross-model procedural-memory transfer and report negative cross-role transfer.
Skill annotations are supplied; retrieval is separated from skill quality.
The paper distinguishes partial-test credit from complete passes. Appendix B
describes validation-based revision and proposes context-specific prefixes,
explicitly leaving their empirical evaluation to future work. **Answers** broad
transfer and revision feasibility; **redirects** attention to recipient-specific
value and adaptation cost. It does not justify treating every transferred skill
as useful or a proposed prefix as a tested repair.

The previously inspected P41/P42 remain complementary evidence on harness
transfer and model–harness compatibility; see the
[adaptation ledger](../2026-09-16-adaptation-decisions/README.md). They were not
re-reviewed in this pass.

## Discovery leads only

- [Agent KB, 2507.06229v5](https://arxiv.org/abs/2507.06229v5): inspected metadata
  and abstract only. Follow its cross-framework experience sharing and
  disagreement mechanism before proposing a new selective-transfer comparison.
- [Portable Agent Memory, 2605.11032v1](https://arxiv.org/abs/2605.11032v1): inspected
  metadata and abstract only. A transport/provenance protocol is adjacent to,
  but does not by itself establish, useful behavioral inheritance. Its claimed
  demonstrations and implementation remain uninspected.

## Provenance and next step

Supplementary arXiv-domain web discovery used “agent memory transfer across
models cross model experience transfer memory” and “agent harness transfer model
upgrade memory compatibility”. These led to the four selected IDs in
[selected-metadata.xml](selected-metadata.xml). A single successful arXiv API
request supplied exact versions; [retrieval.json](retrieval.json) records its
URL, timestamp, descriptive User-Agent and hash. Versioned HTML was read through
the browser tool at the scopes above. No full-text mirror is committed.

Next inspect the closest selection/adaptation methods and their controls before
deciding whether a new experiment would add useful knowledge. A generic
portability demonstration already has direct precedents. This bounded discovery
does not establish the absence of a satisfactory migration comparison elsewhere.
