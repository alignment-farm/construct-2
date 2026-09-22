# Experience-guided investigation review — 21 September 2026

Supports the [root assessment](../../studies/2026-09-21-experience-investigation-findings.md).
The source publication is
[`47e5b284cf520bc89b0411ae2f0bf40e8cef046a`](https://github.com/alignment-farm/experience-guided-investigation/tree/47e5b284cf520bc89b0411ae2f0bf40e8cef046a),
following preparation `7717645b318d3f3e94673c814fd4acb001869dd3`. Remote `main`
matched that publication when reviewed. The sibling checkout remains clean at
preparation; root cloned a separate ignored review copy rather than modifying it.

## Local evidence boundary

Read instructions, README, starting prompt, protocol and both commits' history.
Inspected workload construction, scripted teacher traces, training rows, learning
and model-loop implementations, parsers, evaluator code, reset check, raw model
and tool events, environment/pins, training failure/retry, final hashes and
analysis. [replay.json](replay.json) records recomputed outcomes, costs and artifact
SHA-256 values. Hash inventory is provenance, not a claim that every byte was
independently interpreted or every model artifact re-executed.

The [review script](../../scripts/review-experience-investigation.py):

- Reconstructs four final participant programs from frozen successful edit actions
  and checks their hashes against the publication. Reproduces all four visible
  suites, six failed branch-case executions and two passed original diagnostic
  executions. These are repeated checks of four episodes, not independent samples.
- Runs four additional numeric/string predicate checks on the two submitted
  filter repairs. All fail the stated boolean-only contract; the original
  reference rejects those values correctly in two control executions.
- Rebuilds the researcher-authored branch implementation and verifies its recorded
  hash, six visible tests and three exact expected branch outputs.
- Recomputes all 34 saved model-call counts and native token/time totals. Replays
  action parsing: an ordinary composite response becomes done without an edit;
  eleven adapter responses hit the logged 384-chunk limit and remain unparsable.

Five six-test suites plus fifteen original/teacher/additional task checks and
two reference controls give **47 CLI executions** in this review. No model is
loaded, trained or queried. Additional contract checks qualify the submitted
code; they do not rewrite original scores or convert the examined pilot into
fresh confirmation. The study's recorded READY reset probe is inspected only.

To reproduce, clone the study at the exact publication into
`.cache/experience-investigation-review/study`, then run from Construct-2:

```sh
uv run --no-project python scripts/review-experience-investigation.py
```

The script verifies the revision and clean tracked state, uses disposable
reconstruction directories, and rewrites the root review report. It does not
write to the source publication or change experimental outputs.

## Public-method refresh

**P101 — [SWE-agent, `2405.15793v3`](https://arxiv.org/html/2405.15793v3).**
Read §§2–3 and §5.1, including Table 3. Compact edits, informative feedback and
handling malformed generations are established interface methods; author-reported
ablations show interface choices change task completion. **Answers:** interface
feasibility is an existing empirical subject. **Narrows:** this pilot's action
failures do not isolate memory value. **Redirects:** develop usable actions in
both arms before attributing complete-task differences to weights. This extends
the root's earlier background mention to selected primary-method inspection;
no author code or benchmark was reproduced. It does not identify this pilot's
cause or establish which editor its small learner can use.

**P42 revisited — [Co-Evolving Harnesses and Models, `2609.09134v1`](https://arxiv.org/html/2609.09134v1).**
Re-read §3.4: the method corrects a failing turn in the learner's own rollout and
retains surrounding actions under the same harness. Author-reported improvement
does not diagnose the ETL pilot. **Answers:** compatible learner-grounded teaching
has a concrete precedent. **Narrows:** two authored demonstrations are not that
method or evidence of learning from one's own attempts. **Redirects:** consider
bounded correction of actual learner failures, separating shared interface gains
from a learned contribution. The earlier [P42 reading](../2026-09-17-runtime-study-selection/README.md)
and its unreproduced-result boundary remain intact.

Targeted discovery searched the exact SWE-agent and P42 titles/IDs. Only the
versioned primary texts support this synthesis. This is a focused methods refresh,
not a systematic novelty search. One sequential arXiv query-API request with a
descriptive User-Agent returned both exact versions in [metadata.xml](metadata.xml).
[retrieval.json](retrieval.json) records URLs and hashes; full texts are cached in
ignored `.cache/experience-investigation-review/papers/`. No public result or
model experiment was reproduced.
