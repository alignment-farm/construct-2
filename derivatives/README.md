# Applied derivatives

Derivatives apply Construct's research in working experimental prototypes. They
own implementation, workloads, resources and local evidence in independent
repositories outside this root. Their primary deliverable is usable software;
an ancillary study's primary deliverable is an answer to a bounded question.
Either can inform root theory without becoming the root's operational work.

The user authorized the first derivative on 17 September 2026, preferring an
owned execution environment with complete access to experimental instruments,
a machine-to-machine interface and model-side adaptation. An end-user harness
and a skill-first memory architecture are not the target.

## Construct Runtime

- Repository: [alignment-farm/construct-runtime](https://github.com/alignment-farm/construct-runtime), private.
- Local project: [README](../../derivatives/construct-runtime/README.md),
  [agent instructions](../../derivatives/construct-runtime/AGENTS.md),
  [first assignment](../../derivatives/construct-runtime/START.md).
- Purpose: own the model/tool execution loop, persistent experience and real
  adapter training/loading path behind a thin machine-facing interface.
- Initial organization: one project with distinct execution and learning
  responsibilities; split only when development identifies a useful boundary.
- Status: local build and investigator reuse interface reviewed on 17 September
  2026; see the [latest review](#investigator-interface-review--17-september-2026).
  The original preparation boundary remains in [preparation.json](preparation.json).

The development brief targets a machine-driven agent doing useful work across sessions,
with a real acquired adapter, a meaningful change, independently checked outcomes
and a competent baseline. Skills, code and explicit records are possible
comparators rather than presumed answers. The project owns workload and method
selection. It can borrow ideas from Hermes while controlling its own runtime.

### Initial build review — 17 September 2026

Reviewed revision: `864b846e96c2733d2b8a607217fe905476542cd6`, advancing from
preparation `eb21303afe9fafe841ebfdaf08431f29cf401390`. The build was published in
`5aa02016396d14f55ae48692f1c34e14fac4887e`; the subsequent commit removes local
log fragments. The working tree was clean and remote `main` matched the reviewed
revision. Read the pinned
[milestone report](https://github.com/alignment-farm/construct-runtime/blob/864b846e96c2733d2b8a607217fe905476542cd6/reports/MILESTONE-1.md)
and [implementation contract](https://github.com/alignment-farm/construct-runtime/blob/864b846e96c2733d2b8a607217fe905476542cd6/docs/IMPLEMENTATION.md)
for evidence and operational details.

**Implemented:** owned context assembly and model/tool execution, isolated task
workspaces, persisted events and artifacts, a local HTTP client/service, and
native MLX LoRA training, saving and loading in fresh executor processes. The
machine interface is `construct-json/0.1`; A2A interoperability is not implemented.
Adapter selection is explicit, and optimizer continuation is unsupported. These
capabilities make both external experience and model weights accessible to
controlled experiments in one environment.

**Measured:** the supplier-ledger workload uses a pinned quantized Qwen3-4B model
and six authored, checked source demonstrations. The 128-step adapter completes
6/6 source tasks against a matched base's 3/6, but only 3/4 development tasks;
it misses the declared readiness gate and remains unpromoted. Its predeclared
diagnostic evaluation completes 5/8 fresh tasks, versus base 2/8 and retained
examples in context 5/8, across an explicit refund-policy change. No training
occurs between those policy phases. This is bounded source acquisition and
incomplete transfer; it does not establish autonomous accumulation from successful
learner trajectories, adapter superiority, acquisition-cost repayment or production
usefulness. The single seed and four correlated synthetic schema families limit
generalization.

**Root checks:** read instructions, assignment, publication, implementation
contract and Git history; inspected the execution, training and loading paths
and saved selection/isolation records. Re-ran the derivative's saved-record audit,
reproducing final grades, token/error totals and artifact hashes, then ran its
software checks: 12 tests passed and lint passed. This was a code and saved-evidence
review; no fresh model execution or training was performed by the root. Runtime
`succeeded` means artifact production and termination; semantic correctness is
checked separately. The build supplies an experimental instrument while useful
continuing capability remains an open development objective.

### Investigator interface review — 17 September 2026

The review advances to `9ffb10a66180626b80127fb1892b2cf71e39d946`, matching
local HEAD and remote main with a clean working tree. This revision includes
the research handoff and implements external investigator environments, portable
state forks, separate model/context/tool controls and source export. The pinned
[Milestone 2 report](https://github.com/alignment-farm/construct-runtime/blob/9ffb10a66180626b80127fb1892b2cf71e39d946/reports/MILESTONE-2.md)
records a release-gate example run from an independent directory.

Root re-ran its saved-record audit, 25 software tests and lint successfully.
The final example has base 1/4, context 4/4, adapter 2/4 and code 4/4, all on
repeatedly inspected development cases; these are not fresh-test findings.
The adapter remains unpromoted and the supplied program already solves the job.
The interface is useful infrastructure, while new-workload acquisition and utility
remain to be established. Warm-start adapter training and optimizer continuation
are still unsupported.

The newly prepared [weight-consolidation study](../notes/WEIGHT_CONSOLIDATION.md)
uses this revision as its starting instrument. Its workload and scientific
protocol belong to a separate investigator; runtime development continues independently.

## Relationship and retrieval

The [repository list](repos.txt) is separate from [ancillary studies](../studies/repos.txt).
There are thirteen ancillary studies with accepted bounded contributions and
one newly prepared study, weight-consolidation. This derivative remains outside
that registry and does not reopen any completed phase.
Root theory, literature and independent research selection continue.

From this root checkout, clone the derivative outside the root:

```sh
mkdir -p ../derivatives
gh repo clone alignment-farm/construct-runtime ../derivatives/construct-runtime
```

Derivative agents keep code, experiments and detailed operational records in
their own repositories. They publish meaningful milestones with reproducible
evidence and exact revisions. The root reviews those when scientifically useful;
routine polling and a shared implementation board are unnecessary. Preparation
creates a repository ready for an independent agent session; it does not itself
start that session.
