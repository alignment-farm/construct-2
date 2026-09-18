# Weight-consolidation review — 17 September 2026

This ledger supports the [root assessment](../../studies/2026-09-17-weight-consolidation-findings.md).
The accepted ancillary boundary is `491c0f8a745f48327f6d095d2c3fa7f07d768b44`,
following preparation at `a9e609a892fb8e34507e20b5fdf9b504c7c93170`.
The clean local checkout was fast-forwarded to the published remote `main`.
Construct Runtime remains pinned at `9ffb10a66180626b80127fb1892b2cf71e39d946`.

## Local inspection and independent checks

Read study instructions, README/brief, FINDINGS, REPRODUCE, both protocols,
resource provenance, accounting boundaries, methods inspection and Git history.
Inspected the compiler, transformation, fixtures, public source interfaces,
confirmation driver, audits and cost aggregation, together with selected raw
traces, training records, freeze manifests, source examples and overlap records.

The [root auditor](../../scripts/review-weight-consolidation.py) runs inspected
author analyses with file writes captured in memory, then independently interprets
public contracts, grades saved artifacts and counts raw usage. It executes only
deterministic compiler and source-reading tools in temporary workspaces. It
neither changes published evidence nor invokes models or training.

```sh
uv run --no-project python scripts/review-weight-consolidation.py
```

[checks.json](checks.json) records matching author audits/costs, 172 independently
graded executions, 24 compiler replays, 64 exact-source reads and 35 verified
freeze hashes. The manual paired outcomes are three adapter-only completions,
one base-only completion, two shared completions and six shared failures.
Full-source access is executable in all arms; no confirmation model chooses it.
Training used authored trajectories under the older manual interface. These
boundaries are material to interpreting the publication, not verification of
arbitrary contracts or fresh stochastic model performance.

## Public methods and consequences

All public outcomes below are **author-reported**. Selected methods were inspected;
no public implementation, checkpoint or experiment was reproduced. Exact-version
API metadata are in [metadata.xml](metadata.xml), with [retrieval provenance](retrieval.json).

**P89 — [HarnessForge, 2606.01779v1](https://arxiv.org/html/2606.01779v1).**
Read §§3.4, 4.3–4.4, limitations and Appendix G.1. Survivor harnesses receive
lineage-specific LoRA alignment using successful rollouts from harness selection.
The authors cross harnesses and policies to assess compatibility and report
advantages for matched pairs. **Answers** whether joint adaptation and compatibility
testing already have concrete precedents. **Narrows** any local follow-up to a
specific consequential interface change and its costs. **Redirects** interpretation
away from assuming a learned update transfers unchanged across execution routes.
This does not identify the cause of our malformed actions or justify retraining
where the explicit route already completes every case. Claims remain bounded by
the paper's models, tasks and constrained harness edits.

**P42 revisited — [Co-Evolving Harnesses and Models, 2609.09134v1](https://arxiv.org/html/2609.09134v1).**
Read §§3.3.3–3.4 against the [previous review](../2026-09-17-runtime-study-selection/README.md).
Its correction method edits a failing turn within the learner's rollout under
the evolved harness. Reported imitation failures and correction benefits
**narrow** the assumption that authored full trajectories provide compatible
training. Our adapter was trained before the compiler interface existed; the
local study does not compare these teaching methods or reproduce the paper's
planning explanation. This is a method donor for a justified future question,
not evidence that correction would add useful quality at the current ceiling.

## Discovery and selection boundary

Web discovery searched agent fine-tuning/harness compatibility and
agent/LoRA/compiler/memory combinations. Search hits were leads; only the exact
primary versions above entered this assessment. HarnessForge was also identified
in P42's references. One cached arXiv API request retrieved both versions; no
parallel API client or repeated request was used.

The preceding P87/P88 reading already distinguishes continuing task histories,
compositional reuse and feedback boundaries. The local confirmation has new
payloads but no independent history or later consolidation. Existing work and
this explained finite-grammar limitation favor workload/decision selection
before another mechanism or training sweep. No new study is commissioned here.
