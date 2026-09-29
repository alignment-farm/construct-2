# What can experience teach an agent about changing itself?

**Subsequent evidence — 29 September:** The commissioned
[intervention-choice study](../studies/2026-09-29-intervention-choice-findings.md)
now has an accepted first phase at `cb25d5c`. An acquired chooser adds no benefit
beyond ordinary reuse, and a source-only parser resolves its authored grammar.
This illustrates why the available remedies matter to the decision-value
comparison; it does not estimate that value on broader language distributions.
The original reading below remains historical; the study's broader remit is open.

**Subsequent approval — 28 September:** The user approved continuing this
selection. The [intervention-choice commission](INTERVENTION_CHOICE_STUDY.md)
now assigns bounded feasibility to a prepared independent study. The completed
reading and recommendation below remain the basis for that later decision.

28 September 2026. Completed root literature-and-theory phase during ancillary
execution. This develops [AD1–AD2](ADAPTATION_DECISIONS.md#three-predictions-and-their-possible-failures)
without changing their predictions or commissioning work.

**Conclusion:** choosing where to intervene is already a public research problem
with reported experimental results. A generic demonstration of model/harness
co-evolution would add little. The more consequential remaining question is
whether accumulated intervention outcomes improve decisions beyond competent
current diagnosis, and whether that experience remains useful when the receiving
agent changes. A better remedy, a better decision and cheaper continuing work
are separate achievements.

## What the new reading changes

The [source ledger](../sources/2026-09-28-adaptation-selection/README.md) records
exact versions, inspected sections and limitations. It adds four methods and
checks two pinned public implementations. Results below remain author-reported;
root ran no participant models or published experiments.

| Method | What determines the change? | Consequence for selection |
|---|---|---|
| P120, Qwen-Planner-Agent | Prescribed alternation of model training and harness editing. | Co-development alone does not test learned allocation. |
| P121, MetaRSI | An experience-revised policy schedules data, harness and model operators. | Direct precedent for improving the improvement policy; generic feasibility is no longer merely an architectural proposal. |
| P122, Ecdysis | Reviewed failure patterns guide harness edits, with the task model fixed. | Diagnosis and edit scope matter; recurring failure alone does not locate its cause. |
| P123, ModularRSI | Predefined modules evolve separately and are integrated; functions are selected at use time. | Localized construction and runtime selection differ from learning which substrate to change. |

The earlier P41/P43/P45 readings remain valid assessments of those versions.
Their metadata versions have not changed. The newer comparison changes the
program-level assessment, not the history of what was known on 16 September.
ModularRSI advances from a discovery lead to inspected methods.

The most relevant reported MetaRSI comparison forks one improved starting system
and compares its original and revised improvers. That is substantially closer
to AD1 than an end-to-end gain over an unchanged agent. The inspected public
release does not supply an independently reproduced version of that comparison.
Neither publication acceptance nor an implementation gap establishes the result's
truth or falsity. The ledger distinguishes the paper claim from the artifact.

## Three objects that can improve

Consider an agent that repeatedly mishandles a tool result. Retaining the correct
contract may help; a scoped tool wrapper may enforce it; training may improve
the agent's interpretation. A later combination may work better than any single
change. Calling the failure a model weakness does not uniquely determine where
the useful remedy should live. A wrapper can be a sound response to a model
weakness, provided it preserves valid uses and remains worthwhile to maintain.

Separate three retained objects:

1. **The capability:** an acquired lesson, implementation, adapter or rule that
   changes what the agent can do.
2. **The decision information:** records of the state receiving an intervention,
   what actually changed, subsequent outcomes and the work consumed.
3. **The decision policy:** the mapping from available observations and experience
   to an intervention, a sequence, a diagnostic check or leaving the system alone.

Experience can improve any of them. A policy can learn through revised explicit
instructions; parameter training is not required. Conversely, a frozen model
making different choices from current observations does not by itself establish
that experience improved its decision policy.

This distinction matters when a system both changes its selector and learns to
generate better candidate edits. Its total gain is useful, but cannot automatically
be assigned to better selection. The marginal comparison needs the same starting
agent and available remedy generators, with the decision policy varied. A
separate comparison can measure better generators and their interaction with
selection. These are attribution needs, not a requirement to freeze all components
throughout a practical deployment.

## When decision experience has something to offer

Let `o` denote currently available observations, `h` earlier intervention outcomes,
and `a` an available action or bounded sequence. For a declared future workload
and an explicitly chosen utility, let `u(a)` be its potential outcome from the
same starting state. An idealized value of the additional information is:

\[
V_H = \mathbb{E}_{o,h}\!\left[\max_a\mathbb{E}[u(a)\mid o,h]\right]
      -\mathbb{E}_{o}\!\left[\max_a\mathbb{E}[u(a)\mid o]\right].
\]

This is a decision-theoretic ceiling under known conditional outcomes and a
shared feasible action set, not an estimator or a promised learning result.
The ideal decision maker can ignore history, so the ceiling is nonnegative.
Actual acquisition, observation and decision costs can make a learned policy
less useful than its alternative. Without a justified utility conversion, keep
complete quality, latency, tokens, training and maintenance work separate.

Two conditions make the ceiling zero: current observations already supply all
outcome information in history, or the same action remains best for every history
consistent with those observations. Thus differences between remedy outcomes
are insufficient. Experience must change a useful decision beyond what a
competent present-state rule already knows. Even a positive ceiling need not be
learnable from the available histories or large enough to repay learning.

Our [remedy-feasibility assessment](../studies/2026-09-16-remedy-feasibility.md)
already encountered the second limitation: ordinary explicit access solved the
candidate workload without a useful remedy-choice problem. Reopening that
workload unchanged would not test AD1. Equally, the
[maintenance-decision study](../studies/2026-09-16-maintenance-transfer-findings.md)
shows why a better chooser is insufficient when available actions leave the
complete task unresolved. Finding either limitation is a valid feasibility
conclusion; a selector advantage is not an admission requirement.

## Transfer depends on what changed

A historical intervention outcome remains evidence about its original state.
Its relevance to a new state is conditional. For example, adding logging without
changing task behavior need not invalidate a useful remedy preference. Replacing
a parser, changing a tool contract or teaching the model the missing behavior
can change that preference. A component revision alone proves neither continued
applicability nor universal obsolescence of prior experience.

This gives accumulated experience a possible role in deciding **what needs to
be rechecked**, as well as what to change. The alternative is substantial:
unchanged reuse can remain fully effective. The
[migration assessment](../studies/2026-09-17-migration-lineage-findings.md)
already shows that paid adaptation need not repay its cost after an agent change.
These local findings motivate AD2; they do not establish cross-substrate decision
transfer.

Interventions can also change one another's value. Improving a reader may remove
the need for a recurring instruction; obtaining evidence may make training
possible; a tool wrapper may alter what an existing adapter must produce. The
comparison therefore includes competent fixed sequences where appropriate.
Selecting one permanent winning substrate would miss the original question.

## Research selection

**Complete this root phase; do not open a general co-evolution study.** The public
precedents narrow that proposal. Retain **transfer of intervention-choice
experience** as the next independent feasibility recommendation from this review:

> Can outcomes from earlier interventions improve the next adaptation decision
> on fresh work after the receiving agent or interface changes, beyond competent
> current diagnosis and unchanged reuse of the old decision policy?

This sharpens existing AD1–AD2 rather than claiming a new problem. A bounded
ancillary exploration could establish whether there are functioning alternatives,
consequential decision differences and observable information from which to learn.
Two credible remedies may suffice; a five-substrate competition is unnecessary.
Its scientific target would separate decision experience from improving the
remedies themselves, and assess complete subsequent work including preserved
obligations. Current observations and source access belong to the competent
comparators as well. Claims developed during diagnosis require fresh material.

The public methods support this question but do not supply a validated local
workload or a ready reproduction of the closest policy-update comparison. We
therefore recommend bounded feasibility, not an immediate controller benchmark
or broad training campaign. Closure can follow an explained lack of decision
value, a demonstrated method limitation or a concrete resource constraint.
If commissioned, the ancillary investigator owns workload discovery, methods
and execution under the standing `gpt-6-astra` investigator policy, with actual
reasoning settings and model provenance recorded.

This is a **recommendation, not a commission**. It neither waits on nor redirects
the active investigation and EBM agents. Their latest root review boundaries
remain `523eb3f` and `8ac9b69`; original predictions remain intact. The present
phase adds a literature-grounded distinction and research selection, with no new
learner result, ancillary phase or demonstrated cost advantage.
