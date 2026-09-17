# Executable experience — 17 September 2026

Focused root reading for [research selection](../../notes/EXECUTABLE_EXPERIENCE.md).
The earlier index included Voyager as abstract/source-summary background; this
round inspects its methods and follows adjacent library-learning, workflow and
migration research. Eleven primary texts receive selected method/result reading
below. All empirical results are author-reported; none was reproduced here.
No author implementation or unpublished ancillary evidence was inspected.

## Versioned reading and effect on selection

### P60 — Voyager, 2305.16291v2

[Primary text](https://arxiv.org/html/2305.16291v2), §§2.2–2.3, 3.3–3.4 and
Appendix B.3. Successful action programs enter a description-indexed library;
retrieved code and supplied primitives support subsequent generation. Environment
feedback, exceptions and an LLM critic drive refinement. Authors report transfer
to a new world and deterioration when the library is removed.
**Answers** the basic possibility of acquiring reusable executable experience.
A new world is not a change in API semantics, and removing the library is not
retaining equivalent procedural information for regeneration. The method combines
code execution with contextual exposure to code, rather than isolating them.

### P61 — LATM, 2305.17126v2

[Primary text](https://arxiv.org/html/2305.17126v2), §3, dispatcher in §4 and
§5.5. A capable maker synthesizes Python functions from three demonstrations;
three validation samples supply tests and usage examples for a cheaper user.
During verification, corrections target the test's function calls, not the
function body. The authors report cost/performance benefits from reuse and
model specialization. The CoT-transfer ablation tests two tasks; it does not
compare retained code with newly generated, executed code from matched lessons.
**Answers** generic tool synthesis and amortization; **narrows** the missing
control. Model asymmetry, wrapping demonstrations and verification are part of
acquisition, not free attributes of executable memory.

### P62 — LILO, 2310.19791v4

[Primary text](https://arxiv.org/html/2310.19791v4), §3, §4.1/Table 1, Appendix C.2.
LLM and enumerative search solve tasks; Stitch compresses solved programs into
abstractions; AutoDoc names and documents them. Libraries can be re-derived from
base primitives each iteration. Ablations show that readable descriptions matter;
naively exposing anonymous abstractions can impair synthesis. Results span REGEX,
CLEVR and LOGO, with heterogeneous effects and variability.
**Answers** whether useful abstractions must be supplied by investigators: they
can be acquired in these settings. **Redirects** from the false choice between
code and language: an executable library can depend on contextual documentation
for useful access. Refactoring here does not establish durability through changed
external contracts.

### P63 — TroVE, 2401.12869v1

[Primary text](https://arxiv.org/html/2401.12869v1), §3. An online library supports
IMPORT, CREATE and SKIP modes, each generating K candidates. Executable outputs
are selected by agreement and simplicity; low-use functions are periodically
trimmed. This is a concrete mechanism for acquiring and managing code without
ground-truth supervision during induction. **Answers** generic library growth
and pruning. Its empirical interpretation must be read with P64: generation and
selection compute are alternatives to spending effort on persistence.

### P64 — Compute-matched TroVE re-evaluation, 2507.22069v2

[Primary text](https://arxiv.org/html/2507.22069v2), §§2–4, Table 1.
The authors reproduce 3,201 MATH tasks with CodeLlama-7B over five seeds, match
15 generation calls and correct the selection mechanism. Their table reports
mean accuracy 0.24 for matched Primitive, 0.22 for reproduced TroVE and 0.25 for
corrected TroVE. This is call matching, not proof of equal tokens or wall time.
**Redirects** causal claims: the original large advantage mostly disappears
under this comparator. It does not negate useful libraries in other domains or
establish that all tool learning is mere resampling. This root did not re-audit
the reported implementation discrepancy.

### P65 — SkillWeaver, 2504.07079v1

[Primary text](https://arxiv.org/html/2504.07079v1), §2, §§3.1–3.4.
Exploration proposes tasks, successful trajectories become Python/Playwright
functions, and generated test invocations support honing. Docstrings carry
usage logs and prerequisites. Task success during acquisition uses an LLM
reward model; live-site evaluation is manually assessed. Official human-crafted
APIs are an additional comparator. The authors report improved web-agent success.
**Answers** acquisition through interaction and debugging, not just mathematical
function synthesis. **Narrows** the idea that executable syntax alone establishes
correctness: outcome checking and test coverage remain acquired or supplied
capabilities. The inspected sections do not isolate a lifetime comparison against
matched contextual experience under controlled interface revisions.

### P66 — PolySkill, 2510.15863v2

[Primary text](https://arxiv.org/html/2510.15863v2), §§3.2–3.5 and §4.1 setup.
Abstract domain classes separate skill intent from site-specific implementations;
successful trajectories supply methods, with replay verification before admission.
The authors report improved transfer and reuse. A counted step may be one primitive
or one entire skill invocation, so fewer steps are not automatically less execution
work. **Answers/narrows** the proposal to make reusable procedures portable by
separating interfaces and implementations. Such modular repair is a competent
alternative to both frozen monolithic code and complete regeneration. Cross-site
learning is not by itself a controlled history of contract changes.

### P67 — LLM Agents Making Agent Tools, 2502.11705v2

[Primary text](https://arxiv.org/html/2502.11705v2), selected workflow description,
§5 and Tables 2–3. ToolMaker adapts existing scientific repositories into callable
tools with environment setup and self-correction. Authors report 12/15 tools
correct, versus 3/15 for their OpenHands baseline, with substantially more actions
and higher average creation cost. **Answers** whether tool acquisition extends
beyond small utility functions. **Narrows** fairness claims: unequal creation
work and imported repository functionality matter. This is implementation and
integration of existing capabilities, not evidence of rediscovering their science
or of amortized maintenance under repeated changes. Full protocol/code audit is
outside this reading.

### P68 — Harness Continual Learning, 2608.19013v1

[Primary text](https://arxiv.org/html/2608.19013v1), §3.3.2, §§4.1–4.3, Appendix A.2.
Proposed harness edits face current-benefit, historical-anchor and validity checks.
Authors report acquisition/retention tradeoffs in controlled streams and capability
accumulation in Minecraft. The latter does not systematically replay every completed
task after every update. **Answers** generic proposals to retain tests and gate
harness changes. **Narrows** interpretation: passing historical anchors is not
complete retention, and whole-harness results do not isolate persistent code's
benefit over regeneration or charge a matched lifetime comparison. This is an
inspected method with reported experiments, not merely an architectural proposal;
no implementation or release availability claim is made here.

### P69 — Agent Workflow Memory, 2409.07429v1

[Primary text](https://arxiv.org/html/2409.07429v1), §2 and §§4–5.
Induced routines guide future actions; a variant wraps workflows into callable
sequences. §5 identifies lost intermediate observation as a failure mode.
**Answers** much of generic context-versus-executable-workflow comparison and
**redirects** attention to observation access. Programs with conditional reads
must remain eligible controls. The HTML Table 9 gives overall success 4.8 for AWM
and 3.6 for its action-space variant; accompanying prose instead says both 3.2.
Do not infer a precise whole-task advantage from that inconsistent statement.
The step metric and complete-task metric also differ. Resolving the discrepancy
would require a targeted artifact review, not inventing a reconciliation.

### P70 — SPELL, 2602.01107v1

[Primary text](https://arxiv.org/html/2602.01107v1), §§3–4, §§5.2–5.3.
Generated implementation/test/migration triples are filtered by shared tests and
coverage, then abstracted into reusable syntax-aware transformation programs.
Authors report transfer to sibling implementations and real repositories, with
substantial variation in preserved tests. **Answers** the generic possibility of
learning reusable repairs. **Redirects** the comparator: repair may itself be
amortized across a library rather than charged as independent regeneration of
every function. Passing generated tests is evidence, not proof of equivalence;
source-to-source API migration is not a complete agent lifetime evaluation.

## Discovery, versions and limits

Four sequential arXiv API requests used a descriptive User-Agent,
`Construct-2 literature mapping (local research metadata cache)`, one connection
and more than three seconds between requests:

- [discovery.xml](discovery.xml): title query `ti:SkillWeaver OR ti:"Large Language Models as Tool Makers" OR ti:LILO OR ti:CRAFT OR ti:Voyager`, first 35 by relevance. Many unrelated astronomy/craft/name matches; not comprehensive coverage.
- [adjacent.xml](adjacent.xml): title query `ti:TroVE OR ti:PolySkill OR ti:"LLM Agents Making Agent Tools" OR ti:"Harness Continual Learning" OR ti:"DreamCoder"`, first 15 by relevance.
- [metadata.xml](metadata.xml): selected identifier metadata for ten initial leads, including CRAFT.
- [comparison-metadata.xml](comparison-metadata.xml): AWM and migration leads. Exact versions above were confirmed; all inspected full texts use versioned primary HTML.

Supplementary web searches covered executable libraries and revision, SkillWeaver,
LILO, tools under API changes, CRAFT, workflow text/code comparisons, API migration,
and tool reuse versus regeneration. Key queries were
`site.arxiv.org "workflow memory" "code" "text" agents comparison`,
`site.arxiv.org "API migration" "large language"`, and
`site.arxiv.org "tool reuse" "regeneration"`. Secondary summaries only supplied
leads; they do not support findings recorded above.

Screened leads, not method-inspected here: DreamCoder 2006.08381v1,
CRAFT 2309.17428v2, Automatic Library Migration 2408.16151v3,
SkillMigrator 2606.17645, SMITH (author project page), and newer similarly named
TROVE/SkillWeaver papers. These remain candidates for focused follow-up. Older
program synthesis, macro-action learning, refactoring and regression testing
are substantial adjacent fields; this review does not claim novelty against them.

Selection: pursue the value of persistent implementation versus regeneration
from retained experience, initially through bounded artifact feasibility review.
Generic tool creation, portability and regression-gated repair are already
substantially answered. No new experiment or ancillary project is commissioned.


## Subsequent artifact assessment

The [pinned implementation review](../2026-09-17-executable-artifacts/README.md)
adds static code inspection for P65 and P69 after the primary reading above.
It finds an existing SkillWeaver reference-only route, missing bundled verification
metadata and access/primitive asymmetries; AWM's action branch is unimplemented.
These limits narrow the donor choice without refuting author-reported outcomes.
The [root assessment](../../studies/2026-09-17-executable-feasibility.md) closes
the bounded review and recommends independent acquisition/persistence development.
No public model result was reproduced and no experiment is commissioned.
