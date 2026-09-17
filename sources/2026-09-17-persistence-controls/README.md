# Persistence controls — 17 September 2026

Root discovery after the completed [executable artifact review](../../studies/2026-09-17-executable-feasibility.md).
Four additional primary texts narrow the [comparison](../../notes/EXECUTABLE_COMPARISON.md).
Paper results below are author-reported. Static release inspection is separate;
no experimental result was reproduced or ancillary publication re-reviewed.
Section ranges identify targeted method and result passages, not exhaustive
reading of every passage or appendix.

## Inspected primary texts

**P71 — [SkillCraft, 2603.00718v2](https://arxiv.org/html/2603.00718v2).**
Read §§2–4, §5.1's composition comparison, Appendix B and D.2. Parameterized
tool compositions are acquired, stored and executed. D.2 already compares a
library with generated single-use scripts, answering the broad proposal to add
an executable reconstruction control. However, Table 7's caption describes
direct execution of existing skills without agent intervention, while the prose
describes new hardcoded scripts discarded after execution. The prose also
attributes failures to removal of the agent loop. These descriptions do not
identify one unambiguous intervention. Success permits a score of at least 90%;
efficiency averages use tasks on which both compared methods succeed, with
potentially different subsets across contrasts. Neither is an all-request,
complete-obligation lifetime measure. **Narrows** the comparison to retained
experience and cumulative value, rather than rediscovering code execution.
No precise persistence effect is adopted from Table 7.

**P72 — [CodeMem, 2512.15813v1](https://arxiv.org/html/2512.15813v1).**
Read §§4–7. The architecture explicitly retains validated functions to avoid
planning, coding and debugging again; code can enter both executor and model
context. A case study illustrates acquisition, and a 25-task evaluation compares
three models using trajectory-aware LLM judgment. This is an architectural
proposal with reported execution/evaluation evidence, not merely a hypothetical
design. The inspected evaluation does not isolate retaining a function from
reconstruction using the same accumulated procedural knowledge. Its approximate
reuse-time expression is not a measured full lifecycle saving. **Answers** the
conceptual reconstruction-avoidance proposal; **narrows** the empirical claim.
Deterministic execution alone establishes neither correct applicability nor
correctness under changed requirements. Distinct from the similarly named
CodeMEM repository-generation paper, 2601.02868v1, screened only as metadata here.

**P73 — [PANDO, 2605.24785v2](https://arxiv.org/html/2605.24785v2).**
Read §§3–6 and the limitations; targeted skill-dynamics reading. Explicit rules
and parameterized routines accumulate during the task stream, with progress
reflection, merging and confidence-based demotion. The cost account includes
induction and checking; component ablations distinguish skill additions from
routing, visual compression and cache layout. The library begins with seed
routines, so absence of a pre-evaluation discovery campaign must not be retold
as absence of supplied capability. **Answers** broad proposals for online
library maintenance and reporting induction costs. **Redirects** allocation
analysis toward the whole maintained arrangement. These bundled comparisons
do not isolate code retention against matched procedural experience, nor a
controlled sequence of changed external contracts. No code, raw trajectory,
backbone equivalence or dollar-accounting audit was conducted here.

**P74 — [Skill Blocks, 2608.14943v1](https://arxiv.org/html/2608.14943v1).**
Read §§1, 3–7 and Appendix C. Content-preserving loading compares full text,
requested blocks, references and hybrid stubs. Reported gains depend on unused
content, loading overhead, outputs and cache treatment. The effective-input
discount is a sensitivity assumption, not measured billing; missing historical
telemetry and development on final cases limit inference. Undetected paired
quality differences do not prove equivalence. **Answers** generic conditional
lesson-loading proposals and **redirects** the explicit comparator: competent
contextual reconstruction need not resend an uncached full lesson. This studies
delivery of supplied skills, not acquisition or executable persistence. No
implementation was inspected, and no local cache benefit is inferred.

## SkillCraft release: the consequential distinction

Inspected [author revision](https://github.com/shiqichen17/SkillCraft/tree/0a9ba8808ba49bbc7bd40ad2e853896b8c3d4764)
`0a9ba8808ba49bbc7bd40ad2e853896b8c3d4764`, cloned into ignored
`.cache/persistence-controls/SkillCraft`. It is not verified as the paper's
experimental revision. The [check record](artifact-checks.json) hashes the seven
read files and inventories the tracked tree. Static checks are reproducible:

```sh
uv run python scripts/review-persistence-controls.py \
  --repo .cache/persistence-controls/SkillCraft \
  --output sources/2026-09-17-persistence-controls/artifact-checks.json
```

The runner disables the skill cache and enables `local-exec_script` for
`direct-exec`. That tool executes model-supplied Python through the library's
`ToolBridge`/`ToolCallQueue`, returns results or detailed exceptions, and is loaded
into the ordinary agent interaction loop. The prompt explicitly requests
hardcoded parameters. Thus the current release supplies a concrete generated-script
method with feedback, rather than only automatic replay of an existing skill.
This establishes implementation affordances, not actual model repair behavior
or a reconciliation of Table 7's historical experiment.

Two defaults matter for an adaptation. Script bodies and results are saved in
workspace logs, despite lacking library registration; no registration is not
literal erasure of code. The library execution path applies a low-quality-output
heuristic and returns a warning, whereas Direct Exec does not call that check.
The library also records the warned execution as successful in its statistics.
Consequently, execution-rate counters are not independent correctness labels,
and unequal feedback can contribute to a quality difference. The heuristic
itself is not a task oracle. These observations come from inspected source,
not benchmark execution.

SkillCraft is an additional method donor beside SkillWeaver, especially for
programmatic tool chaining. Neither release is accepted as a ready matched-history
experiment. We did not reconstruct paper results from traces, install dependencies,
run public APIs or select a workload. This focused inspection resolves the donor
question sufficiently; another generic release inventory is not selected.

## Discovery record and limits

One successful arXiv query used the descriptive User-Agent
`Construct-2 literature mapping (local research metadata cache)` and one
connection. [discovery.xml](discovery.xml) retains all seven results for
`ti:SkillCraft OR ti:CodeMem OR ti:PANDO OR ti:"Skill Blocks"`, up to 15 by
relevance. It verifies the four versions above; unrelated Pando results were
excluded. Only one query-API request was made in this round.
[retrieval.json](retrieval.json) records the request and hashes of versioned HTML
cached under ignored `.cache/persistence-controls/papers/`.

Supplementary web queries included `site.arxiv.org agent code reuse regeneration
"ReCode"`, `site.arxiv.org agent "procedural memory" "code" reuse cost`,
`site.arxiv.org "skill" "caching" agents code`, and title checks for SkillCraft,
CodeMem and PANDO. Secondary results supplied leads only. ReCode 2510.23564,
ReCache 2608.19662, Search2Skill 2608.05245 and ASI remain discovery leads, without
method assessment here. This bounded search does not certify novelty or survey
older program synthesis comprehensively.

**Selection effect:** retain the independent allocation question with a stronger
competitor and a smaller claim. Public work already studies ephemeral execution,
online maintenance and efficient lesson delivery. Develop retention versus
reconstruction from shared acquisition with equal checking; do not manufacture
reconstruction work when existing source can simply be loaded. No experiment,
new repository or continuation of a completed study is commissioned.
