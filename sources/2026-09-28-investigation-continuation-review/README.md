# Investigation continuation review — 28 September 2026

The [root assessment](../../studies/2026-09-28-investigation-continuation-findings.md)
accepts a bounded diagnostic phase with qualifications. Conditional filter repair
is established on development; autonomous acquisition and transfer remain open.
No model inference, training, serving request or fresh confirmation was run here.
[Integration checks](integration-checks.json) verify new local links, preservation
of original predictions and changes limited to the intended root records.

## Revision and inspection boundary

The previous experimental review was `47e5b284cf520bc89b0411ae2f0bf40e8cef046a`.
The user-authorized handoff was `121242ca597c607f06d9f9084d88b1fa90a458ff`.
The new local HEAD and independently queried remote `main` both resolve to
[`523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6`](https://github.com/alignment-farm/experience-guided-investigation/tree/523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6).
The live tracked checkout was clean. Root reviewed an isolated Git archive at
`.cache/investigation-continuation-review/523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6/`.
The continuation is one new publication commit; a separate prospective Git freeze
for its adaptive steps is not verified.

Read local AGENTS, README, CONTINUE, `protocol/continuation-v2.md`, the complete
`evidence/continuation-02/README.md`, the local source ledger and revision history.
Inspected runtime/workload, preparation, all episode launchers, conditional replay,
correction/bridge construction, history delivery, training, evaluation, report,
validation and load/reset scripts. Checked environment, history manifests,
context audit, saved isolation and harness controls, training events and summaries,
raw episode events, frozen submissions and correction lineage. The unused fresh
extension's status was read; its cases were not executed to guide selection.

Study investigator provenance: requested `gpt-6-astra`, OpenAI, Codex CLI 0.158.0;
actual backend identity and reasoning effort unavailable. Participant:
`mlx-community/Qwen3-4B-Instruct-2507-4bit` at
`50d427756c6b1b2fe0c0a10f67fbda1fc8e82c1b`, author-recorded file hashes;
original upstream checkpoint not reverified. Study reports Python 3.14.7,
MLX 0.32.2, mlx-lm 0.32.0, transformers 5.17.0. Root replay uses Python 3.13.12
and the standard library via `uv`; no model dependencies are installed for review.
Root session: observed Astra/xhigh, OpenAI, Codex Desktop 0.158.0-alpha.2.1;
[provenance](reviewer-provenance.json). No independent backend fingerprint exists.

## Root checks

The independent orchestration in [review.py](review.py) produces
[review.json](review.json). It imports the inspected ancillary runtime, workspace
builder and contract evaluator, so semantic execution is not an independent
implementation of those components. It never writes published evidence or loads
participant weights. Its final successful audit:

- Verifies all **737 published manifest entries**, byte sizes and SHA-256 hashes.
- Reconstructs all twelve initial workspaces; verifies task/tests and initial
  source identity; checks full-history parity in all six pairs.
- Rebuilds all 135 generation prompts from saved transcripts, reparses every raw
  action and replays **152 tool results**, including injected prefixes, the
  executed teacher correction and bridge target. Final source hashes match both
  frozen submissions and evaluated workspaces.
- Reproduces **234 external checks** (12 submissions plus the teacher, 18 each)
  and thirteen six-test public-suite evaluations. These are overlapping checks,
  not independent observations. All saved scores and suite outcomes match.
- Verifies the conditional first prompt equals its taught probe context, both
  correction source hashes, all seven first-stage training targets and the bridge
  context/target, and the reported adapter-hash continuity into bridge training.
- Recounts all 32 saved training steps and episode/training cost fields. Token
  totals sum reported fields; tokenizer execution and live tensor hashes are not
  reproduced.
- Adds two executions of one root value-preservation probe. Base rename retains
  whitespace inside string values; the adapted submission improperly strips it.
  Both still score 16/18 on the published evaluator. The report preserves exact
  input, expected output and observed results.

Elapsed tool times, unittest durations and absolute test traceback paths are
normalized; other fields must match. An initial audit stopped at the rename
suite's absolute traceback path despite matching case outcomes; a focused check
identified the path difference. After explicit path normalization, replay passed.
The audit was rerun after adding lineage and training-cost checks. The counts above
describe one final successful audit, not all root verification work or new learner
samples. No timings from this replay support model-efficiency claims.

To reproduce, create the pinned archive separately, then run from the root:

```sh
uv run --no-project --python 3.13.12 python \
  sources/2026-09-28-investigation-continuation-review/review.py \
  .cache/investigation-continuation-review/523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6 \
  /tmp/investigation-root-review.json
```

Published model reset checks are inspected evidence, not root-reproduced isolation.
The shared tool guard restricts paths but is not an OS sandbox. Recorded actions
and submitted changes do not show hidden-material access. Passing evaluator
coverage does not prove the complete ETL specification or investigation procedure.

## Complementary public method: P119

**Ross, Gordon and Bagnell, A Reduction of Imitation Learning and Structured
Prediction to No-Regret Online Learning**, AISTATS 2011, PMLR 15:627–635.
[Primary publication](https://proceedings.mlr.press/v15/ross11a.html),
[venue PDF](https://proceedings.mlr.press/v15/ross11a/ross11a.pdf),
[retrieval hash and version](public-source.json).
Read introduction, §§2–3, Algorithm 3.1 and §4's assumptions; no proof audit,
implementation inspection or experiment reproduction. This is a targeted closest
method check, not a claim of current exhaustive literature coverage. No arXiv API
request was needed for this known venue publication.

**Inspected method:** sequential predictions change later inputs. DAgger labels
learner-visited states using an expert, accumulates them across iterations and
repeatedly trains on the aggregate. Its performance guarantees depend on learning
and loss assumptions; they do not certify arbitrary neural optimization.

**Root inference:** this narrows a future acquisition comparison toward visited
contexts and complete rollouts, not merely lower teacher-forced loss. The local
bridge tests neither iterative aggregation nor recovery across a distribution of
failed states. Failure at the exact supplied training context also keeps imperfect
acquisition in view. DAgger does not settle the local cause or guarantee a remedy.
P42's learner-grounded correction and P101's interface methods remain relevant
[prior inspected methods](../2026-09-21-experience-investigation-review/README.md#public-method-refresh);
the multi-turn authored correction here does not replicate either.
