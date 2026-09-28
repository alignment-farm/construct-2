# Experience and evidence acquisition — 28 September 2026

Supports [the root conclusion](../../notes/EVIDENCE_ACQUISITION.md). The user
authorized a bounded methods-and-artifact investigation while evidence-set memory
is active. This work closes that root phase; it commissions no additional study.

## Provenance and retrieval

Root began at `f570b2d` on clean `main`. Actual investigator: `gpt-6-astra`,
reasoning `xhigh`, OpenAI provider, Codex Desktop `0.158.0-alpha.2.1`, read from
the current session metadata/turn context. No research agent was delegated.
[provenance.json](provenance.json) distinguishes investigation from participant
work. Investigator costs were not measured. No model endpoint or training job
was used. The deterministic Requests component replay is described below.

[retrieval.json](retrieval.json) records URLs, response times, headers, payload
sizes and SHA-256. Raw sources are cached under ignored
`.cache/evidence-acquisition/`. One arXiv selected-ID API request returned HTTP
406 with an empty body; no retry followed. Exact-version HTML supplied the two
arXiv readings. The two ACL papers use their published venue PDFs, rather than
an unverified equivalence to their arXiv counterparts. Full-text acquisition is
not a claim of complete reading. [discovery.json](discovery.json) records the
bounded searches; this is not an exhaustive or certified-novelty review.

## Inspected methods

**P110 — [InSCIt, TACL 2023, pp. 453–468](https://aclanthology.org/2023.tacl-1.27.pdf).**
Read §§3–5.2, including collection, alternative references and evaluation.
Paid workers create source-grounded conversations; testing uses gold previous
responses and passages. **Answers** availability of human mixed-initiative
examples. **Narrows** their use: the next-turn benchmark does not execute a new
policy's conversational consequences or test learning across sessions. The
independent development-data inspection in [CASES.md](CASES.md) confirms usable
artifacts and multiple reference strategies, without reproducing model scores.

**P111 — [Smart-Searcher, Findings of EMNLP 2025, pp. 13572–13586](https://aclanthology.org/2025.findings-emnlp.731.pdf).**
Read §§4–6.4, Tables 1–2 and 5. It trains retrieval behavior and internalizes
rewritten successful retrieval traces. **Answers** generic feasibility of learned
knowledge acquisition. Reported average judge accuracy and retrieval count improve,
while average F1 does not beat R1-Searcher; measures should remain distinct.
**Narrows** Construct's question toward new-work transfer beyond reusable answers
and full acquisition cost. The memory analysis compares seen/unseen QA, not a
matched external-answer store across changing tasks. Author results were not
reproduced. The linked repository at `3040f25` contains a README, figures and
packaging files, with model/data/start instructions still pending; no trainer or
evaluator was found in that pinned recursive listing. The README uses the earlier
R1-Searcher++ title. This inspection does not establish absence elsewhere.

**P112 — [Active Inference as Context Acquisition for AI Agents, 2608.19202v1](https://arxiv.org/html/2608.19202v1).**
Read §§3–5, §7 and §9; skimmed §8 and Appendix B's oracle. **Answers** the generic
costly-context formulation, including a Bayes-risk criterion. Information gain
is the special case of a logarithmic terminal loss, not a universal substitute
for useful decisions. Fixed attribute tables and clarification templates provide
controlled comparisons; synthetic clarification costs and supplied measurement
models limit direct import. **Narrows** the unresolved target to acquiring useful
observation strategies from earlier work. No code or reported outcome was replayed;
this is complementary theory/method evidence, not a competing EBM result.

**P113 — [Remember, Verify, or Ask?, 2608.19564v1](https://arxiv.org/html/2608.19564v1).**
Read §§III–VI. The memory-commitment benchmark distinguishes durable storage,
temporary use, verification and clarification. **Answers** novelty of that action
taxonomy and supplies a direct evaluation precedent. **Narrows** the empirical
claim: authored scenarios and rules supply gold choices; structured calls are
recorded without executing tools, obtaining user replies or measuring later task
utility. The paper explicitly states these limits. Prompt effects and label/tool
differences are author-reported; no artifact or model result was reproduced.

P102–P104 and the earlier AD1/decision-value readings retain their recorded
boundaries. They were consulted through root records rather than all reread.
Other related-work citations remain discovery leads.

## Artifact inspection and independent checks

[CASES.md](CASES.md) owns the detailed case record, provenance limits and selected
decision boundaries. [asset-audit.json](asset-audit.json) records the InSCIt counts
and selected record hashes. The Requests results are in
[requests-before.json](requests-before.json) and [requests-after.json](requests-after.json).
They establish an old implementation path and its repair, not agent acquisition
or the advantage of a learned source chooser.

The InSCIt author repository was inspected at commit
`2319fb85932b9528a13417223ffc6fc629ae8087`, verified through the commit endpoint.
The Smart-Searcher linked repository was inspected at
`3040f2591b7b7d962359ed9ca9b6116f4833db77`. These are accessible artifact revisions,
not verified reconstructions of each paper's submission-time code. Requests
uses the original merge and the exact base/merge revisions of the follow-up;
the case record resolves the stale PR-description/code discrepancy.

From the root, run:

```sh
uv run --no-project python sources/2026-09-28-evidence-acquisition/audit_assets.py
```

Add `--fetch` on a fresh checkout to retrieve missing immutable raw source/data
files and validate their recorded hashes. It does not reconstruct mutable API
captures, download the full Wikipedia corpus, or execute upstream setup scripts.

For the offline Requests probe, use Python 3.13.12 and the dependencies recorded
in each result. For example, the original execution commands were:

```sh
uv run --no-project --with 'requests @ https://github.com/psf/requests/archive/8bce583b9547c7b82d44c8e97f37cf9a16cbe758.tar.gz' --with simplejson==3.20.1 python sources/2026-09-28-evidence-acquisition/replay_requests.py before-followup
uv run --no-project --with 'requests @ https://github.com/psf/requests/archive/2d5517682b3b38547634d153cea43d48fbc8cdb5.tar.gz' --with simplejson==3.20.1 python sources/2026-09-28-evidence-acquisition/replay_requests.py fixed
```

Pin the other recorded dependencies as well for environment-matched replay;
the commands above allow their resolver-selected versions to change. Installation
uses network access; the probe itself constructs local Response objects and makes
no HTTP requests. The first probe attempt stopped before execution because its
AST guard compared differently indented docstring literals. The diagnostic showed
identical cleaned docstrings and executable ASTs; normalization repaired the guard.
[diagnostics.json](diagnostics.json) preserves this failed attempt and correction.

Source payload bytes are recorded; package/build downloads and investigator/tool
costs were not instrumented. There is no training, user simulation, full library
test run, deployment change, ancillary publication review or scientific model
result in this phase. [validation.json](validation.json) records final checks.
