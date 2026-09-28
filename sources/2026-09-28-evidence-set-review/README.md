# Evidence-set publication review — 28 September 2026

The [root assessment](../../studies/2026-09-28-evidence-set-findings.md) accepts
five bounded phases, with qualified natural-text scores and no demonstrated
complete LLM-work advantage over competent ordinary access. The expanded EBM
investigation remains open. This review issues no new commission.

## Publication and inspection boundary

- Study: `alignment-farm/evidence-set-memory`, private. Previous root boundary
  `5a0e8f78ab9ee570dd69b80928f39aae4b72f481` covered preparation only.
- Reviewed local HEAD and independently queried remote `main`:
  [`8ac9b694a32e53e5941912b65e2c8881ce0d7c4b`](https://github.com/alignment-farm/evidence-set-memory/tree/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b).
  The live tracked tree was clean. Root read an isolated Git archive, avoiding
  mutation of the active investigator's publications.
- Inspected AGENTS, README, START, the root brief, Git history, phases 1–5
  FINDINGS, relevant protocols/claims, phase-2 provenance, exposure, label and
  reader audits, phase-5 development, optimizer diagnosis and reproduction notes.
  Code inspection covered quote selection, neural features/energy, reader grading
  and fallback, relaxation, native configuration generation/representation/search,
  acquisition, revision/cache handling and audit paths.
- History separates phase 1 (`ad01b74`), initial neural development (`2c55bdf`),
  frozen QA/scaling (`dda88d9`), relaxation and subsequent qualifications through
  `480ad4a`, phase-5 development (`f9959c3`, `d263f86`), the pre-confirmation freeze
  `f8651b89a9ce7eb4301c363e7156a9e22348af2c`, publication `93ab8b6`, and the
  additional verification-cost supplement `8ac9b69`. The latter deliberately
  sits outside the unchanged 52-file phase manifest.

Study runtime/model provenance is author-recorded, except where independently
replayed below. Phase 1 investigator: Astra/medium; phases 2–5: Astra/high,
OpenAI, Codex CLI 0.158.0. Root: observed `gpt-6-astra`/`xhigh`, OpenAI, Codex
Desktop 0.158.0-alpha.2.1; [session record](reviewer-provenance.json). Neither
investigator record supplies an independent backend fingerprint. The phase-2
reader tag is `docker.io/ai/qwen3.8:27b-q4_K_M`, with published digest
`f04d0a543b642a6f0d06590973b124bc4e8700ddf7e99b669ec6c4ab1ef561ef`;
parameter count and quantization are tag claims, not root-inspected weights.

## Checks performed here

The cached review snapshot is
`.cache/evidence-set-review/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b/` in the
Construct-2 root. It has an isolated environment restored with `uv sync --frozen`.
Use a fresh output path for every replay.

1. **Phase 1:** the study's read-only audit regenerated development and later
   histories, replayed all confirmation outcomes, checked frozen hashes, and
   verified the suboptimal one-swap local optimum. The
   [saved report](root-phase1-audit.json) retains all checks and acquisition costs.
   No phase-1 learning or reader inference was rerun.
2. **Phase 5:** `scripts/phase5_audit.py --retrain` reproduced 2,448 executed
   feedback rows, 2,520 policy outcomes, 192 post-hoc diagnostic outputs and
   complete-pool/omission checks on 144 episodes. It made **6,185 native calls**
   and reproduced all five weight vectors bit-for-bit. This is execution of the
   author's audit, not an independently written native semantics implementation.
   See [replay report](phase5-audit.json) and
   [recomputed experimental cost ledger](phase5-native-costs.json).
   Root also reran frozen confirmation, including search and caching: all 504
   policy/episode rows match after excluding timing fields. This added 369 native
   executions, 11,520 inference gradient steps and 246,144 discrete evaluations;
   see the exact [confirmation replay record](phase5-confirmation-replay.json).
3. **Independent aggregation/regrading:**
   [verify_publication.py](verify_publication.py) reconstructs the original
   frozen QA scores from raw response contents, request paragraph IDs and
   restored labels. All **192 mapped outcomes / 166 unique responses** reproduce,
   including public fallback. It also checks 384 selection rows, aggregates all
   504 phase-5 confirmation rows, verifies 52 manifest files and all six input/
   label partition hashes, and totals all 262 saved phase-2 calls. See
   [root-regrade.json](root-regrade.json). Matching a metric does not validate its
   source semantics.
4. **Source grounding:** root inspected recovered supporting paragraphs for
   `double__48776_807969` (different Salah identities), `double__825727_584042`
   (different clubs/players), and `double__159903_154896` (year versus date).
   These selected cases substantiate the reported problem, not its frequency.
5. **Software/algebra:** all 18 supplied tests passed after restoring partitions,
   including the fixed-cardinality energy identity over 4,845 binary sets and
   50 fractional points at seven coefficients. The saved phase-3/4 sweeps and
   phase-2 neural acquisition were inspected, not regenerated.

The full raw MuSiQue development asset was reacquired from the author-linked
Google Drive URL in `scripts/phase2_assets.py`; **42,457,393 bytes**, 2,417 rows,
SHA-256 `76eb07a2cd7b60b3336374a28097e90867f979791023f5626e7397dc2d083dd5`.
`--rebuild-cache` reproduced every frozen partition hash. The study's existing
reconnaissance supplied the answer-alias mapping and scorer files; their copied
hashes are retained in the ignored review cache. The author repository identifier
is `922ac98f19a201998dbdae6d7f2887a5258dbdeb`; the Drive asset itself is unversioned,
so its content hash is the recovery boundary. Labels remain imported benchmark
supervision, not independently certified truth.

### Runtime and failed setup attempts

The published native runtime is Python 3.12.14; the local `uv` catalog returned
“No download found” for that exact version. Root used **3.12.12**, NumPy 2.5.3 and
PyTorch 2.14.0. Root's `configparser` SHA-256 is
`8d822edd41d1085e0c697f1926f3f98e5c7889b4072361ae88726464b37f6460`, different
from the study's `cf5318e0c45a2e206b4ec74d4d66493185ed26c3736a86b0ebdf8f3a3e365a1a`.
The replay is behaviorally successful on this material, not exact native-source
identity. Root's five replay fits took 3.606 seconds; the full audit 3.878 seconds.

An initial no-sync invocation assumed an existing study environment, created an
empty `.venv` and failed on missing NumPy before audit execution. Root relocated
only that newly created empty environment into its review cache; a conservative
first relocation assertion stopped on its virtualenv bytecode cache, then a
verified retry succeeded. The active study's tracked files were unchanged.
An initial test pass had 17 successes and one missing-partition error; after
hash-verified data recovery, all 18 passed. These are setup failures, not scientific
failures or unpublished learner attempts.

No serving endpoint, new reader call or pretrained-model download was used by
root. Root did rerun five tiny fits. The study's 4,481 phase-5 experimental native
executions, its own 6,185-call audit, its subsequent 369-call verification, and
root's 6,185-call audit plus 369-call confirmation replay are distinct cost
records, not independent evidence.
Phase-2 raw usage totals reproduce at 258,920 prompt and 64,888 completion tokens
across 262 physical calls. Investigator/authoring cost, power and full infrastructure
cost remain unknown; timing comparisons are small, host-dependent and partly
nested. Acquisition, representation, search, reader and repair units are not
interchangeable.

## Complementary public method: P118

**Belanger, Yang and McCallum, End-to-End Learning for Structured Prediction
Energy Networks**, ICML 2017, PMLR 70:429–439.
[Primary publication](https://proceedings.mlr.press/v70/belanger17a.html),
[paper](https://proceedings.mlr.press/v70/belanger17a/belanger17a.pdf),
[retrieval record](public-source.json). Read introduction, §§2.3, 3, 4.1–4.3 and 5.
The exact venue PDF is cached and hashed; no arXiv version is substituted.

**Inspected method:** training backpropagates through a finite unrolled inference
procedure. The paper discusses projection-related gradient problems, smoother
updates, losses along intermediate iterates and training/inference compatibility.
Its experimental superiority claims are author reports, not results reproduced
here; experimental tables, supplement and implementation were not audited.

**Root inference:** this narrows the interpretation of local failures after
binary-ranking training. Jointly trained practical inference is a distinct,
established method worth considering if complete-task headroom warrants it.
It neither resolves the local utility question nor commissions a new experiment.
This targeted complementary reading extends P105–P109/P116; it is not an
exhaustive or current-coverage claim about energy-based research.

## Reproduce the root regrade

From Construct-2, after restoring the pinned study snapshot and its partitions:

```sh
python3 sources/2026-09-28-evidence-set-review/verify_publication.py \
  --study .cache/evidence-set-review/8ac9b694a32e53e5941912b65e2c8881ce0d7c4b \
  --out .cache/evidence-set-review/root-regrade-replay.json
```

The script reads only the study snapshot and refuses an existing report path.
Detailed experimental methods and original raw traces remain in the study.
