# Lesson-acceptance review — 20 September 2026

## Revision and inspection boundary

Reviewed **`cbe62b976e5a9d179a88edbd1a5f573eb0f29254`**, advancing from preparation
`60552288930555806cef042294ea27145753d1d8`. Local HEAD, origin/main and the remote
main advertised by `git ls-remote` matched. The working tree was clean. Read
study instructions, README/brief, Git history, the pilot report, initial and
amended protocols, failed-review and serving-repair records, runner, verifier,
cost accounting and relevant raw requests/responses. The root's initial tree was
also clean. No study or derivative files were changed.

The [root assessment](../../studies/2026-09-20-lesson-acceptance-findings.md) accepts
the bounded publication and phase closure, while preserving the broader question.
The investigator used stdlib SQLite/HTTP instead of the prepared runtime copy,
reported absent in its environment. The runtime review boundary stays `09f6683`;
this study supplies no evidence of its integration.

## Independent checks

[check_saved.py](check_saved.py) reads the saved artifacts and imports only the
inspected study fixture module. It executes SQL through its own SQLite connection
and independently computes expected aggregates from the declared obligations;
it does not call the study's executor or grader. [independent-check.json](independent-check.json)
records the output, case grades, costs and inspected-file hashes.

- **94 SQL executions:** four source/probe replays, 36 initial/final task
  executions, 36 additional behavioral executions and 18 fixed-program replays.
  All saved output and success checks matched. Raw final billing-801 reproduces
  the latent defect; curation arms pass every measured check.
- Recomputed standalone deployment accounts and all 53 response-artifact token/
  wall-time totals from raw responses, matching the report. The recorded extra
  interrupted request has unknown consumption; missing costs are not zero.
- Checked all 36 final requests for the same model/settings and intended retained
  source, proposal, curation and paid-probe access. Checked candidate/review identity
  against saved responses and each scored query against its actual model output.
- Verified 40 saved request hashes and all five protocol hashes in the evaluation
  manifest. Thirteen earlier requests retain full request bodies without separate
  saved hashes. The manifest's source snapshot matches its recorded hash.
  Recorded response timestamps put all four final curations before evaluation.
  These are artifact consistency checks, not independent historical timestamps.

Initial phases saved source hashes without full source snapshots; later phases
include snapshots. The current runner adds evidence-path and budget conveniences
after execution. One early competence manifest mislabeled the model; actual
request bodies identify final 27B use. The review does not equate current code
with an exact reconstruction of every historical run.

From the root, reproduce the read-only check without model access:

```sh
uv run sources/2026-09-20-lesson-acceptance-review/check_saved.py \
  ../ancillary-studies/lesson-acceptance
```

Root SQLite was 3.50.4; the final execution manifest records 3.53.1. All replayed
rows agreed despite that version difference. This check reuses the published
fixture generator and validates the small declared task, not an external
real-world specification. No live model call or training was launched. Root did
not run the author's scripts in place because they rewrite saved analysis files.

## Public-method refresh

**P95 — Semantic Evaluation for Text-to-SQL with Distilled Test Suites**, Ruiqi
Zhong, Tao Yu and Dan Klein, **2010.02840v1**, submitted 6 October 2020. Read
§§2–4 of the [exact arXiv PDF](https://arxiv.org/pdf/2010.02840v1); the
[published EMNLP paper](https://aclanthology.org/2020.emnlp-main.29/) supplies a
second stable citation. [Cached metadata](arxiv-2010.02840v1.xml) came from one
version-specific query API request with a descriptive User-Agent.

**Inspected method:** generate neighboring mutations of a gold query, sample
databases satisfying schema constraints, and retain databases that distinguish
additional neighbors. Evaluate predicted queries against the gold on the resulting
suite. Agreement approximates semantic equivalence; finite testing is not a
proof. **Root inference:** this answers the general measurement concern behind
single-output false positives and narrows any novelty claim for extra SQL checks.
Its gold-query dependence does not establish an affordable deployment checker
when requirements or source authority are uncertain. This redirects selection
toward unresolved decision information rather than another generic verifier.
No implementation or reported benchmark result was reproduced.

The earlier [P48/P94 selection reading](../2026-09-19-lesson-acceptance-selection/README.md)
already establishes environment-probing curation and separates artifact checking
from lesson validity. That overlap remains; the local incremental contribution
is the competent cheap comparator, ordinary repair, direct acquired-code reuse and
explicit cost/claim boundaries. The study's own reading remains separately owned.

## Review decision

Accept the bounded findings and closure. Paid checks added no measured benefit
once visible-schema reasoning worked. Preserve the weak-reviewer failures,
serving failures, scope qualifications and raw-repair result. The unresolved
question is when observation changes a useful decision beyond competent ordinary
review; neither selective acquisition nor a learned acceptance policy was tested.
[review.json](review.json) records the exact boundary and review artifacts.
