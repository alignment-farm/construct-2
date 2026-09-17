# Executable artifact review — 17 September 2026

Follow-up to the [P60–P70 primary reading](../2026-09-17-executable-experience/README.md).
The root inspected two author repositories as static artifacts. No third-party
code, models, browser tasks or environment installation was run. These code
revisions are not asserted to be the papers' experimental revisions.

| Artifact | Exact revision | Files inspected for the consequential comparison |
|---|---|---|
| [AWM](https://github.com/zorazrw/agent-workflow-memory/tree/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1) | `8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1` | Root and two workload READMEs; `mind2web/run_mind2web.py`, `memory.py`, `utils/env.py`, action prompts; WebArena runner, workflow files and action configuration. |
| [SkillWeaver](https://github.com/OSU-NLP-Group/SkillWeaver/tree/f2a63d65d0f6ff46ac30e817cede8797f8f25b97) | `f2a63d65d0f6ff46ac30e817cede8797f8f25b97` | README; `agent.py`, `attempt_task.py`, `create_skill_library_prompt.py`, `sanity_check_code.py`, knowledge-base loader/retrieval/formatting, codegen templates, single-task/benchmark evaluators, locator recovery, LM/performance logging; five bundled libraries and task-configuration inventory. |

Repositories were cloned into ignored `.cache/executable-review/`. The
[inventory and checks](checks.json) contain pins, tracked-file inventories and
SHA-256 hashes. Reproduce after checking out those exact revisions:

```sh
uv run python scripts/review-executable-artifacts.py \
  --cache .cache/executable-review \
  --output sources/2026-09-17-executable-artifacts/checks.json
```

The [check script](../../scripts/review-executable-artifacts.py) parses source
without importing it. It confirms AWM's unimplemented action branch and missing
workflow module; SkillWeaver's 438 functions, absent companion verification
metadata and 812 WebArena configurations; production retrieval's reference-flag
behavior; and CSS/query-selector calls in 345 library functions alongside the
generated-action restriction. It does not prove current task success or model
behavior. Full acquisition and evaluation traces were not found in the inspected
pinned trees; benchmark task specifications are not such traces.

Revisited [SkillWeaver 2504.07079v1, §§3.3 and 4](https://arxiv.org/html/2504.07079v1)
to distinguish the paper's browsing/skill comparison from the code's reference-only
route. This adds implementation provenance to P65, not a new reproduced result.
P69's AWM table/prose discrepancy remains recorded in the prior ledger; exact
resolution is unnecessary because the corresponding runnable release path is
missing. P64's compute-control precedent remains primary-paper evidence only.

**Selection effect:** AWM is an incomplete donor for the requested paired
comparison. SkillWeaver is a closer starting method with identifiable access,
verification and cost issues. The [root assessment](../../studies/2026-09-17-executable-feasibility.md)
closes this artifact review and recommends bounded independent development of
the acquisition/persistence comparison. It distinguishes invocation with source
available from a genuine choice of retained representation. No experiment is
commissioned by this review.
