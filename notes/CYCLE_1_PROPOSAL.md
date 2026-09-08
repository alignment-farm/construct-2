# Cycle 1: Does learned memory utility survive a schema change?

2026-09-08 · Research proposal · No experimental results yet

## Recommendation

Reproduce a bounded MemRL comparison on the database component of
LifelongAgentBench, then introduce one extension: a controlled schema migration
after memory acquisition. Test whether retaining the learned utility scores
helps or impedes adaptation compared with resetting those scores while keeping
the same memory contents.

The scientific objective is to characterize when historical success remains a
useful basis for memory selection. The first cycle keeps model weights fixed
so that the intervention has a clear location. Direct training belongs in a
subsequent question that requires it. Learning resources are in the separate
[appendix](LEARNING_APPENDIX.md).

## Basis for the choice

MemRL selects semantically relevant memories using learned utility scores and
updates those scores from outcomes. Its stability analysis assumes a stationary
task distribution and a frozen inference policy. These features make a controlled
environment change an interpretable extension.
[Paper, v2](https://arxiv.org/html/2601.03192v2).

Construct's earlier work motivates examining the costs of inherited authority
and the distinction between stored information and offered context. Here the
agent acquires its memories through benchmark interaction. We can inspect the
entire path from an outcome to a score update, retrieval, SQL execution, and a
later outcome.

The literature already studies evolving state, tool changes, and memory credit
assignment. Our proposed contribution is the narrower comparison between
inherited and reset utility on identical starting memories during executable
schema migration. Novelty remains provisional; see the
[candidate and overlap review](CYCLE_1_LITERATURE.md).

## Reproduction

Use the authors' database runner and released task definitions. Pin the source,
environment, task IDs, prompts, model, embedding model, and all configuration
changes. The reviewed source is commit
`c1b322ca43de36ddf64c6712f89d0095bfc35ce0` of
[MemTensor/MemRL](https://github.com/MemTensor/MemRL/tree/c1b322ca43de36ddf64c6712f89d0095bfc35ce0).

The target is the benefit of learned retrieval utility in a recurrent task
setting. Compare:

| Condition | Persistent state and selection |
| --- | --- |
| No memory | Independent task attempts through the same action interface |
| Similarity retrieval | The same memory construction procedure, selected by similarity |
| MemRL | Memory construction plus outcome-driven utility and hybrid selection |

The two adaptive conditions acquire separate histories. Their comparison
estimates the effect of the complete policies; it does not hold all subsequent
memory contents constant. The extension below provides a shared-checkpoint
comparison to isolate the intervention on inherited scores.

Start from a task subset chosen using dataset metadata and a recorded seed,
before examining treatment outcomes. Cover several SQL skill combinations;
avoid taking the first task IDs or selecting only failures. Preserve recurrent
task exposure and score last-pass success and cumulative ever-solved success
separately. Improvement on repeated tasks does not establish novel-task transfer.

Prefer the paper's relevant settings where available. Any substitution of the
model, embedding model, data subset, or episode schedule must appear in a
deviation table. A changed model or reduced dataset yields an adapted
reproduction; it cannot reproduce the paper's numerical claim exactly.

## One extension: schema migration

After acquisition, clone each memory checkpoint into four core continuations:

| World | Retain utilities | Reset utilities |
| --- | --- | --- |
| Original schema | Preserve learned scores and continue updating | Set all scores to the configured initial value, then continue updating |
| Migrated schema | Preserve learned scores and continue updating | Apply the identical reset, then continue updating |

At the fork, memory text, IDs, embeddings, model, prompt policy, and budgets are
identical. Resetting changes only utility scores and any derived score caches.
Later histories may diverge as a consequence of the intervention; that is part
of the effect being measured.

The migration renames a predetermined subset of table or column identifiers.
For example, a column named `item_name` could become `product_name`, while rows,
types, and the requested logical operation stay the same. Update explicit
identifier mentions in task instructions consistently. Every condition receives
the current schema through the existing observation interface. Old memory text
retains its original identifiers. Unaffected tasks remain in the continuation
to expose collateral costs of resetting useful scores.

Use one migration family in this cycle. Extra types of drift, automatic change
detection, corrective memory rewriting, and a return to the old schema are
separate potential studies.

Verify migrations independently by executing transformed reference SQL and
checking equivalent logical results or final row states. Check round-trip
identifier mappings and incorrect-query cases. Keep reference answers out of
model prompts and memory construction inputs. A textual renaming script alone
is insufficient validation.

Add similarity-only and no-memory continuations as reference conditions in
both worlds. The former starts with the same checkpoint contents. These help
interpret whether an effect concerns inherited scoring, historical context
generally, or the difficulty of the changed task.

## Predictions and measurements

**Inertia hypothesis:** resetting scores helps more after migration than in the
unchanged world because historical successes favor obsolete instructions.

**Useful inheritance hypothesis:** retained scores remain beneficial because
memories contain reusable SQL procedures, or normal feedback updates them
quickly enough to preserve their advantage.

**Weak score influence:** resetting has little effect because scores rarely
change retrieval or because the model can reconcile retrieved advice with the
current schema. Retrieval traces distinguish these possibilities.

Let `S` be task success over a fixed continuation window. The primary contrast is:

```text
D = (S_reset,migrated - S_retain,migrated)
  - (S_reset,original - S_retain,original)
```

Positive `D` indicates a relative advantage for resetting after migration.
Report all four cell estimates and the direct migrated-world contrast: a
positive interaction alone does not establish that resetting improves migrated
performance. It could instead reflect different losses in the original world.

Secondary measurements: success on affected and unaffected tasks, invalid SQL
attempts, obsolete identifiers in executed actions, memory selections and score
trajectories, and input/output tokens, tool calls, and elapsed time. Include
acquisition, summarization, embedding, and retries in cost accounting. Separate
research-only audit costs from costs an operating agent would incur.

Freeze the continuation horizon and primary analysis before evaluation. A
cost benefit with an accuracy tie is a different finding from an accuracy gain.
An imprecise interval is not evidence of equivalence.

## Sampling and evidence

Use independently acquired memory histories with predeclared task orders and
sampling settings. Pair all branches within each history. Reset the database
between tasks and isolate memory stores between branches. Repeated attempts,
SQL calls, and tasks sharing an evolving memory are dependent observations.

Estimate the primary contrast per complete history, then summarize across
histories with uncertainty. Choose the number of histories and task coverage
using a prospective precision analysis and simulations of clustered outcomes.
Report individual histories as well as aggregates. Generalization to other
task families requires family coverage; extra decoder draws do not supply it.

Before the main run, freeze task IDs, migration mappings, exclusions, retry
rules, budgets, horizon, sample size, and the smallest effect considered useful.
Keep development tasks separate. Record every pilot, configuration change,
failed run, and missing outcome. Transport failures and scorer defects need
their own accounting, alongside task failures. No unrecorded reruns or silent
removal of inconvenient cases.

## Execution sequence

1. **Instrument audit.** Trace the active retrieval and update paths, reproduce
   deterministic score calculations, verify the database scorer, and resolve
   paper/configuration differences. Build a minimal task replay and cost logger.
2. **Bounded feasibility exploration.** Cap the first pilot at 100 episodes
   across conditions. Check task execution, memory construction, retrieval
   coverage, migration validity, context limits, and runtime. This cap is for
   development, not a statistically adequate final sample.
3. **Protocol and budget.** Use pilot timing and prospective precision analysis
   to specify the main run. Pin the participant before comparing final outcomes.
   Retain pilot findings and all adaptations in the report.
4. **Reproduction and extension.** Execute the frozen comparisons, retain raw
   traces, and audit a mixture of successes, failures, and unexpected outcomes.
5. **Synthesis.** Return the result, limitations, and any revised theory here,
   with direct links into the derivative's evidence.

A positive reproduction result is not required to report or interpret the
cycle. If the instrument works but memory has little influence, report that
boundary. If the design cannot distinguish the hypotheses, revise it explicitly
and evaluate on fresh material; do not search repeatedly for a favorable cell.

## Resources and unresolved choices

The local Docker model inventory includes gpt-oss-20B and Qwen3-14B; their
fitness for this interface has not been measured. gpt-oss-20B is a reasonable
first local participant to investigate, with its quantization recorded.
An embedding endpoint and the pinned MySQL environment still need verification.
No inference, training, benchmark execution, or paid compute has run for this
proposal. Runtime and monetary estimates remain pending the pilot.

The empirical work belongs in a derivative project; its path remains to be
chosen when execution starts. It should own the pinned environment, deviations,
protocol, raw evidence, scorer, analysis, and report. This root owns the question,
literature comparison, and resulting theory. The deliverable is a bounded,
reproducible finding even if the treatment loses or the proposed mechanism has
little influence.
