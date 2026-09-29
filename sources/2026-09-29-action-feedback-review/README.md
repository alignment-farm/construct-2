# Action and completion-feedback review — 29 September 2026

Evidence for the [joint root assessment](../../studies/2026-09-29-action-feedback-findings.md).
Read-only study review followed by root synthesis; zero participant calls, model
loads or new fits. Executable replays run in disposable local copies. Detailed
experimental methods and original evidence remain in the owning studies.

## Boundaries and provenance

[boundaries.json](boundaries.json) records previous/reviewed revisions, clean
initial study status and archive hashes. Root began clean at `ea166d5`. Both
ancillary `origin/main` heads were fetched and matched their publications before
inspection; no active checkout content was changed. Review snapshots live in
ignored `.cache/2026-09-29-study-review/`. Their public source clones and locked
Python environments are review resources, not participant preparation.

- EGI: `523eb3f` → `9380a564e104dbd766702a823a125f21ab55696a`, one publication
  commit. Read local instructions, README, autonomy-v3 protocol, publication,
  sources, acquisition/trainer/tool code, traces, manifests and evaluation.
- ESM: `8ac9b69` → `5e2d06a22f302ecfbd124f6f009b84274c39986b`, thirteen commits.
  Read local instructions, README, phase-6/7 findings, protocols/claims and
  reproduction/source records; inspect selector, grading, sandbox, self-check,
  documentation, repair and audit code plus relevant saved records.
- EGI phase protocol was reconstructed after accidental overwrite. ESM phase-6
  task definitions are already in the script at freeze `fa9f5e7`; serialized
  task files occur later. Phase-7 `transfer-tasks.json` is absent at `94bc951` and
  present at `368a61e`, after comparison freeze. Git establishes repository order,
  not independent wall-clock attestation or investigator blindness.
- Root investigator: `gpt-6-astra`, `xhigh`, OpenAI, Codex Desktop
  `0.158.0-alpha.2.1`, continuing session
  `01a0e7b0-fe8a-7c53-a0a8-23dde8a9c170`; previously observed session metadata,
  not independent backend verification. No delegated reviewer.
- EGI reports requested Astra with actual backend/effort unavailable. ESM reports
  observed Astra/high, Codex CLI `0.158.0`, session
  `01a0e7e4-68e2-7fb2-9a5d-2ea6873b86b8`. Do not substitute the root's setting.
- EGI participant identities remain its local 4B/7B model manifests and reported
  resident 27B service. ESM uses the reported Qwen3.8-27B Q4_K_M service digest
  `f04d0a543b642a6f0d06590973b124bc4e8700ddf7e99b669ec6c4ab1ef561ef`.
  Phase-7 runtime records a local serving binary `1 (72874f5)`; the remote endpoint
  is not independently attested. These are model provenance limits, not a claim
  that the tags are wrong.

## Root execution and what it establishes

[review_investigation.py](review_investigation.py) and
[investigation-review.json](investigation-review.json) record:

- All **428** EGI manifest file hashes and lengths verified.
- **12** saved programs re-evaluated against 18 established and 10 newer contract
  inputs each (**336** case executions), plus twelve public suite invocations.
  Per-case pass/fail, aggregate grades and public return codes match.
- All **42** tool actions in the three joint arms re-executed from their saved
  initial source, messages and complete history; non-timing results and final
  submitted hashes match. Python diagnostic formatting is not required identical.
  Root inspected the successful reference's post-edit verification chronology.
- **23** training targets matched to learner actions or executed investigator
  continuations; three masked edit indices checked. The teacher rows' source-event
  field points to the originating learner episode; their actual replacement actions
  reside in `acquisition/<task>/events.jsonl`. Root follows that distinction.
- Fifteen episode usage/elapsed records and completed-update counts reconciled
  against raw events. Paired 4B initial messages and first divergence checked.

EGI replay interpreter is **Python 3.14.6**; the study reports 3.14.7. Root's first
review-script attempts assumed a `tools` key and numeric teacher turns; those
schema assumptions failed after outcome replays and were corrected to the actual
`tool_schemas`/replacement-continuation records. They were reviewer errors, not
experimental failures. The final recorded run passes. Root inspects the
stopped-prefix-gradient implementation, but does not reproduce generation,
training gradients, adapter isolation or fresh transfer. Replay uses reviewed
local Python; this is not a proof of a general OS security boundary.

[review_evidence.py](review_evidence.py) collects the supplied audit reruns and
independent manifest/chronology checks in [evidence-review.json](evidence-review.json):

| Root replay | Scope |
|---|---|
| Phase 6 | 24 saved attempt/probe programs, 47 logical request identity/private-test-name checks, 33 frozen files, 48 pytest invocations |
| Phase 7 | 12 attempts, 15 public repair grades, 22 scratch grades, 61 logical request/boundary checks, 32 frozen files, 61 pytest invocations |
| Semantic/mutation diagnoses | Six additional pytest invocations reproduce the one-helper repair and unchanged self-test failures despite a new private failure |
| Requirement review | Eight documentation comparisons; root reads the actual request clauses and changed text, not only AST presence |
| Reviewed repair | One pytest invocation verifies 93 tests and a docstring-only AST change |
| Publication manifests | 299 phase-6 files at `cd2582c`; 239 phase-7 files at `5e2d06a` |

**116 pytest invocations** in the recorded ESM replay, with no reader calls.
The latest checkout's README differs from the phase-6 publication: verify that
manifest against its owning historical commit, not silently against the latest
README. Both pinned upstream commits and source manifests were verified after
clone: python-dotenv `d6c0b9638349a7dd605d60ee555ff60421c1a594` (39 files),
python-slugify `f85f9488520148d5f6899b5639199882b605e30a` (19 files).
Phase-local `uv sync --frozen` selected Python **3.12.12**, versus the study's
3.12.14; dependency locks were unchanged and grades agree. No phase-6 fit or full
repository test suite is rerun here. Author-reported bit-identical refits and
boundary tests remain author evidence. Root outcome replays reuse inspected study
graders and are not a second independent specification implementation. They
cannot certify every omitted requirement or exclude every possible information
leak. Timings vary; archived experimental costs are not replaced by replay costs.

From the respective extracted snapshots:

```sh
# EGI; invoke the root script with the snapshot and a fresh output path.
python3 /path/to/construct-2/sources/2026-09-29-action-feedback-review/review_investigation.py . /fresh/investigation-review.json

# ESM, on macOS; each --out directory must be absent.
uv sync --project phase6 --frozen
uv sync --project phase7 --frozen
phase7/.venv/bin/python scripts/phase7_fetch.py
phase6/.venv/bin/python scripts/phase6_audit.py --out .cache/root-review-phase6
phase7/.venv/bin/python scripts/phase7_audit.py --out .cache/root-review-phase7
phase7/.venv/bin/python scripts/phase7_documentation_audit.py --out .cache/root-review-docs
phase7/.venv/bin/python scripts/phase7_finalize.py --out .cache/root-review-repair
phase6/.venv/bin/python scripts/phase6_semantic_diagnosis.py --out .cache/root-review-semantic
phase7/.venv/bin/python scripts/phase7_check_diagnosis.py --out .cache/root-review-mutation
python3 /path/to/construct-2/sources/2026-09-29-action-feedback-review/review_evidence.py . /path/to/evidence-set-memory-git /fresh/evidence-review.json
```

The fetch script reads public GitHub source; remaining replay commands call no
participant or external model. Frozen current source, later unpublished work and
model-server processes in the active studies remain untouched.

## Public-method comparison

Targeted discovery for generated-test agreement and execution-based correction,
not a comprehensive or current-coverage claim. Search results were discovery aids;
claims below use the exact primary PDFs. One arXiv API request retrieves both
records, with a descriptive User-Agent and local caching. No concurrent arXiv
metadata client was started. [metadata.xml](metadata.xml) and
[public-sources.json](public-sources.json) preserve query, versions, dates and
SHA-256 values; PDFs and extracted text remain in ignored cache.

**P124 — Bei Chen et al., CodeT: Code Generation with Generated Tests**,
[2207.10397v2](https://arxiv.org/abs/2207.10397v2), updated 23 November 2022.
Inspected introduction, §§2–3, Table 2 and selected §4.1 discussion in the versioned
PDF; no repository, proof or experiment reproduction. The method separately
samples code and tests, executes their pairs and ranks agreement groups. It
assumes incorrect solutions rarely agree by chance. Authors report higher
HumanEval/MBPP selection accuracy, including HumanEval 47.0% to 65.8% with
code-davinci-002. **Root inference:** this narrows a generic “add generated tests”
proposal toward evaluating their discriminating quality and the cost of multiple
candidates. It does not validate the current agent's possibly correlated checks,
non-executable clauses or accumulated experience across tasks.

**P125 — Xinyun Chen et al., Teaching Large Language Models to Self-Debug**,
[2304.05128v2](https://arxiv.org/abs/2304.05128v2), updated 5 October 2023.
Inspected introduction, §§2–4, selected setup/decoding paragraph and MBPP framing;
no appendix prompt inventory, repository or experiment reproduction. Prompted
code explanation and execution feedback guide repair without finetuning;
termination uses correctness feedback or a turn cap. MBPP exposes one of three tests and still asks the model to infer correctness
after it passes. Authors report gains and improved sample efficiency.
**Root inference:** this supplies a competent ordinary method family to consider,
not proof that feedback is comprehensive. It narrows the case for learned control
to improvements beyond capable feedback use; it does not resolve the local
acquisition failure or documentation omissions.

These methods neither answer the continuing-experience question nor justify
retiring EBM exploration. They redirect an immediate generic self-check proposal
toward feedback validity and complete outcomes. P119 (learner-state aggregation),
P101 (agent interfaces), P108/P109 (set selection) and P118 (inference-aware energy
learning) retain the inspection boundaries in their earlier root ledgers; they
were not all reread or reproduced during this review.
