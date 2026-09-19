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
- Status: the learning memory worker's local publication is reviewed at `09f6683`
  on 19 September 2026; see the [latest review](#memory-worker-review--19-september-2026).
  The preceding investigator interface was reviewed at `9ffb10a` on 17 September.
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

The completed [weight-consolidation study](../studies/2026-09-17-weight-consolidation-findings.md)
used this revision unchanged for an independent environment, real adapter training,
fresh workers and corrected source-access confirmation. It found partial learning
but no added completion over its finite-language compiler. This is evidence of
useful instrument operation, not a runtime-wide quality or consolidation result.
Its workload and protocol belong to the study; runtime development continues independently.

The [database continuation](../studies/2026-09-18-continuing-consolidation-findings.md)
also uses this pin, with study-owned generation and lower-rate training adaptations.
Two cumulative updates produce shorter familiar execution without better fresh
completion. Runtime operation, teaching quality and useful consolidation remain
separate claims; the review does not change this derivative's implementation.

### Memory-worker development — 19 September 2026

The user authorized a learning memory worker within Construct Runtime. Root wrote
the [assignment](../../derivatives/construct-runtime/MEMORY_WORKER.md) and
[build plan](../../derivatives/construct-runtime/docs/MEMORY_WORKER_PLAN.md),
then supplied a prompt for the user to give the derivative agent. The initial
handoff recorded development underway with accepted code still at `9ffb10a`.
The subsequent review below advances that boundary.

The initial design uses one fixed primary model and one smaller memory model with
one active LoRA adapter, alongside explicit experience records. It separates
between-task learning, evaluation, snapshots and rollback; expanding archives do
not imply unbounded active adapter growth. Repeated learning must be assessed on
downstream complete work against a frozen memory worker and ordinary retrieval.
The derivative owns implementation and refinement. Root independently develops
[when checking a proposed lesson is worth its cost](../notes/FEEDBACK_DECISIONS.md#checking-a-reusable-lesson--19-september),
which could later use these instruments without prescribing another build phase.

### Memory-worker review — 19 September 2026

Accepted local publication: `09f66837ca76db1f674ee3372d734219ad0f3e27`, with a clean
working tree. Local `origin/main` remained at `9ffb10a`; no remote check or push
was performed. Read [Milestone 3](../../derivatives/construct-runtime/reports/MILESTONE-3.md)
and the [root review and evidence ledger](../sources/2026-09-19-runtime-memory-review/README.md)
for exact boundaries. Historical runs include earlier source snapshots; the
published implementation includes subsequent prompt and logging repairs.

The runtime now supplies a separate 1.5B memory model with real LoRA updates,
bounded evidence consultation, source observation, snapshots, activation and
correction-preserving restore alongside the fixed 4B primary. Two cumulative
training points acquire source read/deliver behavior. Original fresh blocks
complete 9/28 with frozen memory, 26/28 with learned memory, and 28/28 with ordinary
scope retrieval. The ordinary alternative is cheaper; no useful-cost advantage
for learned memory is established. Both updates start from base and fresh
optimizers, and the evidence concerns one authored account history.

The old adapter with the expanded current archive completes 5/16 phase-two
tasks; those unchanged weights do not demonstrate update-induced forgetting.
A joint record-ID/order change yields learned 0/4 versus ordinary 4/4. Software
blocks 12 attempted deliveries of uncertain/superseded records in that learned
diagnostic. Authority declarations and correction precedence are supplied by the
controller; learned authority judgment, autonomous writing and fact validation
remain untested. A separate primary-schema repair confirms 3/4 learned versus
4/4 ordinary on new cases without altering the original final scores.

Root re-ran the saved-record audit and independently regraded 176 task artifacts,
checked the representation transformation, reproduced published cost totals, and
ran 33 software tests and lint successfully. No fresh inference or training was
performed. The build and bounded phase are accepted. The
[root plan refinement](../notes/FEEDBACK_DECISIONS.md#runtime-review-refinement--19-september)
uses competent ordinary delivery to isolate the value of checking lesson
acceptance; independent-history robustness remains useful derivative development.
This review commissions no new run and adds no ancillary study.

## Relationship and retrieval

The [repository list](repos.txt) is separate from [ancillary studies](../studies/repos.txt).
There are fourteen ancillary studies with accepted bounded contributions;
weight-consolidation's [continuing-work follow-up](../notes/WEIGHT_CONSOLIDATION.md#assessment-after-continuing-work--18-september)
is now reviewed and complete.
The fifteenth, [lesson-acceptance](../studies/README.md#lesson-acceptance), is
prepared with an owned runtime copy at `09f6683`. Its acceptance-evidence question,
protocol and execution remain independent of derivative development.
This derivative remains outside
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
