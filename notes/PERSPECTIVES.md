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
