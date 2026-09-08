# Agents, memory, and learning

> previous directory for this file was `~/Developer/Projects/alignment-farm/`

Research perspective · 4 September 2026

> Weights provide the policy; external stores provide the revisable declarative knowledge.

The working view is that the most promising agents will learn how to use external
state while keeping important parts of that state explicit and revisable. The
interesting question is where each improvement should live: context, a memory
store, executable code, model parameters, or an enforceable rule. Each choice
changes the cost of learning, using, inspecting, and correcting it.

Expect stronger models to remove some scaffolding and make other scaffolding
more valuable. A model that can reliably interpret a compact lesson makes that
lesson worth preserving. A model that already performs the procedure makes a
long corrective prompt unnecessary. Architecture should be reconsidered when
capability changes.

This is a dated research agenda. Results below are attributed to their sources;
the proposed division of responsibilities and research priorities are subjective.
Local findings remain owned by [Construct](../../construct/README.md) and
[Formation](../../formation/README.md).

## Model and harness design are converging

The useful unit of comparison is a model operating through a particular
interface, with particular tools, state, and compute. SWE-agent demonstrated
that changing the interface through which a model explores repositories, edits
files, and runs tests changes its effectiveness. A model benchmark alone cannot
settle an agent architecture decision.
[SWE-agent, 2024](https://arxiv.org/abs/2405.15793).

Cursor's self-summarization work provides a concrete example of training and
harness design meeting. Summarization occurs inside the training trajectory, so
the eventual task reward also trains the summaries that carried the work
forward. Cursor reports better results and shorter summaries than its prompted
compaction baseline on its internal coding benchmark. This is evidence from
the system's developer, with the corresponding limits on independent
verification. The architectural point is clear:
**a learned memory policy still operates through an external compaction mechanism.**
[Training Composer for longer horizons, March 2026](https://cursor.com/blog/self-summarization).

My expectation is that training will increasingly improve decisions about
search, tool use, summarization, and recovery. The runtime will still have to
execute those decisions, preserve state, and enforce access. The promising
research compares different allocations of responsibility and measures their
interaction.

## Frozen weights do not imply a system cannot learn

Three distinct questions often get compressed into the word “learning”: whether
the model's parameters changed, whether the surrounding system retained
something useful, and whether that retained change improves a new task. These
questions need separate evidence.

There is already relevant work on improvement without parameter updates:

- [Reflexion, 2023](https://arxiv.org/abs/2303.11366) retains textual reflections
on feedback to improve subsequent attempts. Improvement on a repeated task
needs to be distinguished from transfer to a new one.
- [Voyager, 2023](https://arxiv.org/abs/2305.16291) builds a library of executable
Minecraft skills through interaction and reports reuse in a new world. Its
retained competence includes code the system can execute.
- [Agentic Context Engineering, 2025; revised 2026](https://arxiv.org/abs/2510.04618)
develops and maintains contextual playbooks, reporting gains on agent and
domain-specific benchmarks without updating the model's weights.

These results do not establish Formation's full combination of acquisition,
selective transfer, revision, and net value. They do make “context engineering
is only clerical work” an inadequate starting assumption. A system can acquire
a useful procedure in executable code or a reusable contextual representation.
Whether a particular experiment demonstrates that is an empirical question.

The same standard should apply to weights. A parameter update is evidence that
training occurred; it does not by itself demonstrate useful generalization.
Copying, narrow memorization, and inappropriate transfer remain possible.

I would also avoid treating a task's unique correct solution as evidence of
answer leakage. Many meaningful tasks have one correct result. What matters is
whether the retained artifact supplies that result directly, or supplies
reusable knowledge that the participant must apply to new inputs. Changing
surface details alone is a weak transfer test; changing the required
composition of the knowledge is more informative.

## Choose storage by how the knowledge must change

My default allocation would be:


| What persists                                                   | Starting place                                                    | Reason                                                                |
| --------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| Current facts, promises, exceptions, and unresolved obligations | Explicit records with sources and revision state                  | Individual entries need correction and selective use                  |
| Reusable procedures with exact semantics                        | Tested code or tools                                              | Execution and failure can be inspected directly                       |
| Repeated judgments and broadly useful strategies                | Contextual lessons first; training when repeated use justifies it | Compare acquisition cost, reliability, and transfer before committing |
| Access rights and permission to take consequential actions      | Runtime enforcement                                               | A model's prediction of permission should not grant permission        |


This is a starting hypothesis, not a universal partition. External memories can
be badly organized; trained behaviors can be difficult to correct. Both can
contain facts and procedures. The practical question is which representation
gives the required precision, adaptability, and cost on the actual workload.

The research opportunity I find most compelling is selective consolidation:
identify which lessons recur across independent experiences, test their scope,
and determine whether moving some of their use into weights improves the
system while preserving correction of individual facts.

## Online adaptation is real, but its benefits need precise names

Titans introduces a neural memory module that learns to retain historical
context. It belongs in the discussion of memory architecture, but its mechanism
is different from fine-tuning a deployed agent's base model or installing a
LoRA for a particular task.
[Titans, 2024](https://arxiv.org/abs/2501.00663).

Agentic Test-Time Training updates LoRA parameters during live agent episodes.
The authors report improvements of up to 5.0 percentage points on ALFWorld and
4.9 on SWE-bench Lite, with overhead limited to 1.9 times the no-TTT cost. They
also find that repetitive self-training can amplify drift. Their interpretation
is especially relevant here: gains concentrate where a model already has task
competence but loses its way during a long trajectory.
[No Time Like the Present, July 2026](https://arxiv.org/abs/2607.03441).

Maintaining a strategy, remembering an episode, adapting to a distribution, and
acquiring a transferable skill are all valuable. They deserve different tests.
An adaptation method that improves the current episode may leave no useful
change for the next one. Conversely, a temporary adapter could be the right
design precisely because its contents should expire.

My main questions for online updates are what persists after the episode,
whether the benefit survives a change of task, and what happens when later
evidence contradicts the update. The strongest result would include successful
revision as well as successful acquisition.

## Training, inference, and specialization compete on total cost

DeepSeek-R1 provides evidence that reinforcement learning can improve reasoning
on verifiable tasks and that the resulting behavior can help train smaller
models. It supports taking post-training seriously; it does not establish that
an arbitrary collection of successful agent transcripts is a sufficient
training set.
[DeepSeek-R1, 2025; revised 2026](https://arxiv.org/abs/2501.12948).

More inference compute is another intervention. Research on its allocation
finds that the returns depend on task difficulty and the base model's existing
success rate. This argues for measuring a performance-versus-cost curve before
deciding that a task needs either a larger model or training.
[Scaling LLM Test-Time Compute Optimally, 2024](https://arxiv.org/abs/2408.03314).

NVIDIA's small-model agent paper makes a plausible case for specialists on
repetitive workloads. It is explicitly a position paper. I would test a small
specialist against a strong general model using cost per successful task,
including retries, routing, verification, training, and maintenance. A cheap
call that causes expensive repair is not a cheap system.
[Small Language Models are the Future of Agentic AI, 2025](https://arxiv.org/abs/2506.02153).

The production evidence also needs its denominator. Measuring Agents in
Production reports that 14 of its 20 interviewed systems used off-the-shelf
models without weight tuning. That supports a pattern of pragmatic deployment;
it is neither a census nor a controlled comparison of prompting and training.
[Measuring Agents in Production, revised June 2026](https://arxiv.org/abs/2512.04123),
[weight-tuning results](https://arxiv.org/html/2512.04123v4#S5.SS2).

For this lab, open weights are especially useful as an experimental affordance:
they permit controlled comparisons on the same base model. The model's
national origin or place on a leaderboard is less informative than its ability
to perform the required operation through the chosen interface.

I would retain trajectories with exact inputs, tool results, model versions,
external outcomes, corrections, and failed attempts. Selecting only apparent
successes can hide how much human or harness assistance produced them. A
trajectory becomes a useful training example after its target and evidence
have been examined.

## Longer tasks make recovery and authority central

A useful agent must recover from partial failure, recognize stale state, and
resume work after interruption. A single successful completion does not tell
us how reliably it does those things. METR's time-horizon work helps measure
capability growth, but its authors explicitly distinguish the human duration
of tasks an agent can solve at a given success rate from the time an agent can
operate independently. That distinction should survive every retelling.
[METR's limitations note, January 2026](https://metr.org/notes/2026-01-22-time-horizon-limitations/).

Security belongs in this same picture. AgentDojo evaluates agents using tools
over untrusted data and finds both ordinary task failures and successful prompt
injection attacks. A system needs to complete the authorized task while
resisting redirection. Refusing everything would satisfy only half the goal.
[AgentDojo, 2024](https://arxiv.org/abs/2406.13352).

My design judgment is that learned judgment should be paired with explicit
authority boundaries. A retrieved document may inform an action without
acquiring the right to authorize it. A generated summary may preserve useful
content without becoming the authoritative history. Greater capability makes
these distinctions more consequential because the model can act on more of
what it encounters.

Protocols and integrations matter when they improve access, observability, or
control. The number of connected tools or participating agents is not itself a
measure of competence. Evaluate the resulting behavior and the additional
failure paths.

## What I would investigate in this lab

Construct's [GM continuity finding](../../construct/notes/GM_MEMORY_FINDING.md),
[X2 recovery result](../../construct/notes/X2_FINDINGS.md), and
[M3 channel attack](../../construct/notes/M3_FINDINGS.md) motivate a practical program:
make useful history available, keep recovery affordable, and protect the
mechanisms that decide what the model receives. The immediate GM opportunity
is contact with actual play, including irrelevant memories, revised promises,
and obligations that become relevant much later.

For the broader learning question, I would first locate the failure:


| Observation                                                                       | What the next comparison should resolve                                         |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| The model succeeds when given a correct, reusable artifact, but not a learned one | Whether experience interpretation or artifact construction is failing           |
| The model fails even with a correct supplied artifact                             | Whether it can understand and apply that representation through this interface  |
| Ordinary retrieval and governed memory both succeed                               | Whether governance adds selectivity, correction, security, or lower cost        |
| A method helps new matching tasks but harms unrelated ones                        | Whether its applicability can be learned or enforced without losing the benefit |


These are diagnostic comparisons, not a new admission bureaucracy. Cheap
exploration should help find a tractable phenomenon. Once one exists, stronger
controls should determine what caused it and whether it generalizes.

The eventual harness/weights comparison should cross two choices: ordinary
retrieval versus governed memory, and frozen versus tuned versions of the
same base model. Use the same underlying experience and evaluation tasks,
disclose any extra training supervision, and account for the different compute
budgets. Include an information-matched control when isolating governance.
Measure transfer, non-transfer, correction, and total cost. This design can
reveal complementarity as well as substitution.

I would give both architectural complexity and model upgrades a burden of
proof. When a stronger model arrives, rerun a compact set of meaningful cases
with the existing system and a simpler baseline. Some old machinery may become
unnecessary; some previously unusable memories may become useful. A failure
with one participant is evidence about that participant and setup, not a
permanent ceiling on context engineering.

## The observations that would change my priorities

I currently favor explicit, revisable records for changing facts and selective
training for recurring procedures. Three kinds of evidence would change that
allocation:

1. A frozen model with a compact learned artifact repeatedly matches a tuned
  model on novel tasks at lower total cost. I would put more effort into
   artifact acquisition and use.
2. Tuning reliably improves the application of the same supplied artifact
  across unfamiliar settings. I would treat artifact consumption as a training
   target and retain the external memory system.
3. Online weight updates retain precise episodic information, support selective
  correction, and outperform explicit memory at comparable cost. I would
   reconsider how much episodic state should remain external.

The most valuable result would identify when to remember an experience, when
to turn it into a reusable procedure, when to train on it, and when to discard
its influence. That is a concrete research contribution even if the winning
system uses familiar components.

---

## Retained critique of earlier framing

The commentary below was already present in this repository's initial commit,
`b49fac2`. It discusses earlier wording and is retained as part of the research
record. Its exact review date and target revision were not recorded. The main
perspective above already incorporates several of its qualifications, including
the limits of the “clerk-work” framing and the production-study denominator.
References below to “TRENDS,” “current,” or work to do “now” describe the
critique's context, not a new assessment or assignment. Use the
[theory map](THEORY_MAP.md) and [cycle records](cycles/README.md) for the evolving
account and current work.

Construct has credible, bounded evidence that memory architecture improves an agent’s behavior. It does **not yet establish where harness improvements stop paying and weight updates become necessary**. That is an interesting open question, but the documents sometimes frame it as more settled than the experiments support.

I read both documents, followed the main findings, and checked Formation’s current account because TRENDS invokes its clerk/practitioner distinction. This is an assessment of the documented evidence, not a rerun of the experiments.

Three results stand out:

- **M3 is the strongest architectural lesson.** Manipulating the channel that determines which memories reach the model caused an actual wrong answer; protecting that channel prevented the tested attack. That gives a concrete reason to treat memory infrastructure as a security boundary. However, “frontier models resist framing” generalizes beyond the evidence: the answer-level tests used one model, one retraction, and a limited payload set. The narrower finding is useful enough without that extension. [M3 findings](/Users/macos-user/Developer/Projects/alignment-farm/construct/notes/M3_FINDINGS.md:65)
- **X2 demonstrates a useful engineering tradeoff.** Eviction with recovery preserved answer quality while reducing hot-store tokens by roughly 57–59%. The branch that evicted without recovery actually failed, which makes the comparison informative. But this is a small, oracle-gated experiment with one run per engine per fixture. Hot-store tokens also aren’t total operating cost. I’d read it as evidence that this recovery mechanism works under these conditions, not yet that the architecture saves 57% in production. [X2 findings](/Users/macos-user/Developer/Projects/alignment-farm/construct/notes/X2_FINDINGS.md:48)
- **The GM result is convincing enough to justify trying it in a game.** Going from 6/24 to 24/24 is substantial. But the baseline lacks the earlier promise, so the experiment primarily establishes the value of supplying missing historical information and joining it with current state. It doesn’t isolate how much *governance* adds over ordinary retrieval containing the same information. The finding correctly labels itself exploratory; “zero measured safety loss” covers only twelve safety cases. [GM finding](/Users/macos-user/Developer/Projects/alignment-farm/construct/notes/GM_MEMORY_FINDING.md:13)

I particularly respect the willingness to retire mechanisms and distinguish integration success from behavioral success. That makes the record more trustworthy. The corresponding risk is spending so much effort making experiments admissible that the apparatus receives more attention than the phenomenon. The README’s recognition of this selection effect is persuasive, and the move toward lightweight exploration seems warranted.

The thesis needs tightening. “After training, everything an agent becomes is memory architecture” is either too broad or almost definitional, depending on what counts as memory architecture. The testable claim is narrower: **which persistent changes improve later action, under which conditions, at what cost?** Supplying a missing fact, teaching a reusable procedure, and enforcing an authorization boundary are different accomplishments.

That distinction also weakens the harness-versus-weights framing. Training can improve how a model interprets evidence, retrieves memories, or follows a procedure while an external system remains responsible for current facts and permissions. “The harness is being absorbed into weights” bundles together several different changes. For example, the recent agentic test-time-training paper reports gains concentrated where models already possess competence but lose it during long trajectories; its authors interpret the effect mainly as preserving competence rather than acquiring new abilities. That is surprisingly close to Construct’s concerns. [aTTT paper](https://arxiv.org/abs/2607.03441)

TRENDS is useful as a research agenda, but its language sometimes prejudges the answer. Calling context engineering “clerk-work” doesn’t establish its capability ceiling. Likewise, Formation’s failures—even with supplied correct records—show that the tested participants could not use those artifacts successfully. They do not establish that weight updates are necessary. [Formation’s current evidence](/Users/macos-user/Developer/Projects/alignment-farm/formation/README.md:182)

One factual qualification: the “70% of deployed agents” figure comes from **14 of 20 interviewed case studies** in the cited production study. It supports a deployment pattern, not a population estimate or a verdict about which approach works better. [Original study](https://arxiv.org/html/2512.04123v1#S5.SS2)

The experiment I’d most want next would cross ordinary retrieval versus governed memory with frozen versus tuned versions of the same base model. Give the branches the same underlying experience, then measure novel-task success, inappropriate transfer, correction after facts change, and total cost. Include an information-matched retrieval control so governance earns its own contribution.

My working bet is that stable, repeatedly useful procedures are promising training targets, while changing facts, explicit obligations, provenance, and permissions benefit from external representation. Construct provides reasons to investigate that division. I would take the GM mechanism into actual play now; I would keep the claim that the experiments locate the boundary between harness and weights open.
