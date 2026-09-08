# Cycle 1: Candidate selection and overlap review

2026-09-08 · Targeted review for choosing a first cycle

This is a selection memo, not a systematic literature review or an experimental
verification of the papers. Sources below are primary papers and author code.
The review examined relevant methods, limitations, and implementation sections;
it did not rerun any published results. The recommendation is developed in the
[proposal](PROPOSAL.md).

## Reproduction candidates

| Candidate | Relevant mechanism | Decision for this cycle |
| --- | --- | --- |
| [Reflexion, v4](https://arxiv.org/html/2303.11366v4), [author code](https://github.com/noahshinn/reflexion) | Retains textual reflection on feedback between attempts | Useful foundational reading and a viable reproduction; learned retrieval utility offers a more direct continuation of Construct's authority question |
| [Agentic Context Engineering, v2](https://arxiv.org/html/2510.04618v2), [author code](https://github.com/ace-agent/ace) | Generation, reflection, and curation maintain evolving playbooks | Strong candidate for a later study of memory construction; this first question benefits from an intervention on explicit scalar scores |
| [MemRL, v2](https://arxiv.org/html/2601.03192v2), [author code](https://github.com/MemTensor/MemRL) | Outcome feedback changes memory utilities used in retrieval | Preferred: the score state can be cloned, retained, or reset independently of the memory text |

This choice prioritizes an identifiable comparison with executable outcomes.
It does not depend on a method being new, large, or favorable to our hypothesis.

## Related work that narrows the question

- [On the Fragility of Self-Improving Agents, v1](https://arxiv.org/html/2608.18066v1)
  examines repeated runs and task order for Agent Workflow Memory and
  ReasoningBank on web tasks. It motivates treating an entire acquired memory
  history as a source of variation. A claim that we first discovered order
  sensitivity would overlap this work.
- [Can Agent Memory Systems Track Evolving State?, v1](https://arxiv.org/html/2608.19652v1)
  studies current versus superseded state in multi-session histories. Broad
  claims about obsolete memory are already occupied. Our planned outcome is
  executable task performance after changing a database interface.
- [MCPEvol-Bench, v1](https://arxiv.org/html/2607.14642v1)
  evaluates agents against evolved MCP tools. Tool evolution is an existing
  evaluation axis. The proposed distinction is the intervention on inherited
  retrieval utility at a shared memory checkpoint.
- [HiMPO](https://arxiv.org/abs/2606.16285) and
  [AttriMem](https://arxiv.org/abs/2607.21106) address credit for memory
  construction. Their abstracts already rule out treating counterfactual
  memory credit as an untouched topic; their full methods need review if we
  later pursue that direction.

The contribution to investigate is therefore specific: whether preserving
historical utility scores changes the cost or success of adaptation to a
schema migration, relative to retaining the contents while resetting the
scores. This search did not establish that the exact comparison is absent
from the literature. Repeat the closest-work check before finalizing a
novelty claim or a publication submission.

## Source inspection and reproduction risks

Inspected selected source files from MemRL commit
`c1b322ca43de36ddf64c6712f89d0095bfc35ce0` without executing them.
Temporary review copies are outside the project; the pinned upstream links
below identify the sources to retain in the derivative.

| Source | Observation from inspection | Required follow-through |
| --- | --- | --- |
| [Database task](https://github.com/MemTensor/MemRL/blob/c1b322ca43de36ddf64c6712f89d0095bfc35ce0/3rdparty/LifelongAgentBench/src/tasks/instance/db_bench/task.py) | Constructs prompts with table/column names; scores query answers or final-state hashes | Execute reference and incorrect cases; independently validate migrated outcomes |
| [LLB runner](https://github.com/MemTensor/MemRL/blob/c1b322ca43de36ddf64c6712f89d0095bfc35ce0/memrl/run/llb_rl_runner.py) | Replays ordered task lists and performs memory updates between batches | Pin ordering and batch semantics; prevent evaluation-state contamination |
| [Memory service](https://github.com/MemTensor/MemRL/blob/c1b322ca43de36ddf64c6712f89d0095bfc35ce0/memrl/service/memory_service.py) | Contains hybrid normalized scoring in the retrieval path | Trace the invoked path; do not assume the standalone selector is the benchmark policy |
| [Value updates](https://github.com/MemTensor/MemRL/blob/c1b322ca43de36ddf64c6712f89d0095bfc35ce0/memrl/service/value_driven.py) | Stores scalar utility updates in memory metadata | Verify numeric transitions and score-cache behavior after cloning/reset |
| [LLB configuration](https://github.com/MemTensor/MemRL/blob/c1b322ca43de36ddf64c6712f89d0095bfc35ce0/configs/rl_llb_config.yaml) | Contains 20 sections, while the paper's main comparison reports 10 epochs | Resolve and record the chosen schedule before running |

Source availability is established. Runtime compatibility, participant
competence, adequate memory influence, benchmark correctness, and feasible
statistical precision remain empirical questions. The present inspection is
enough to motivate a bounded feasibility pilot, not a reproduction verdict.
