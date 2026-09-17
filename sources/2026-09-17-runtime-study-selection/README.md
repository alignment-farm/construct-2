# Runtime-enabled research selection — 17 September 2026

This targeted pass informs the [weight-consolidation comparison](../../notes/WEIGHT_CONSOLIDATION.md).
It adds P87–P88 and revisits P42. Exact-version API metadata are cached in
[metadata.xml](metadata.xml), with request provenance in [retrieval.json](retrieval.json).
All paper outcomes below are author-reported. No author implementation or public
experiment was reproduced; this is selected methods reading, not a novelty audit.

## Methods and consequences

**P87 — [AgentOdyssey, 2606.24893v1](https://arxiv.org/html/2606.24893v1).**
Read §4, §6 and Appendix 10. Its agent comparison includes LoRA-based SFT and
external-memory mechanisms in continuing text games. In the simpler Qwen3-4B
experiment, SFT with short-term memory outperforms short-term memory alone.
The appendix changes update frequency with the memory condition: every step
without it, every five steps with it. **Answers** the generic possibility of
combining external memory and test-time weight learning. **Narrows** our proposal
to comparable accumulated evidence and competent persistent examples/code, with
complete work through changed requirements and acquisition costs. Its game result
does not by itself answer that allocation question. It is a method donor for
continuing evaluation, not evidence that the local runtime has acquired the same
capability.

**P88 — [AgentCL, 2606.02461v1](https://arxiv.org/html/2606.02461v1).**
Read §§3.1–3.3 and the scope statement preceding §3. The authors evaluate
non-parametric memory using naive and deliberately compositional task streams.
They distinguish first-pass improvement, repeated-task reuse and held-out
generalization; memory construction excludes ground-truth guidance.
**Redirects** workload selection toward identifiable reusable components and
separate fresh probes. Our proposed corrected-trajectory acquisition has a
different feedback boundary and must disclose it. These memory-stream methods
already address generic evaluation of experience reuse; the additional local
question concerns the contribution of weight updates with retained artifacts
still accessible.

**P42 revisited — [Co-Evolving Harnesses and Models, 2609.09134v1](https://arxiv.org/html/2609.09134v1).**
Re-read §3.4 against the earlier [methods assessment](../2026-09-16-adaptation-decisions/README.md).
The reported correction method edits a failing turn in the learner's own rollout
and trains under its evolved harness. **Narrows** acquisition development toward
corrections compatible with the executor rather than assuming whole expert
trajectories are suitable. Teacher selection and correction work are acquisition
costs. This is a possible recipe, not a required treatment or a locally reproduced
explanation of planning-style interference.

## Discovery and local feasibility boundary

Supplementary web searches covered continual agents/LoRA/memory, the exact P42
title, and parametric/non-parametric continual memory. Primary full texts above
were then inspected; general search results were discovery leads only. The one
arXiv API request retrieved all three exact versions together. No parallel API
client or retry was used.

Runtime review advanced from `864b846e96c2733d2b8a607217fe905476542cd6` to
`9ffb10a66180626b80127fb1892b2cf71e39d946`: instructions, README, handoff,
investigator contract, Milestone 2 and implementation boundaries were inspected.
Local HEAD and remote main matched, with a clean tree. Root re-ran the release-gate
saved-record audit (verified), 25 software tests (passed) and lint (passed).
These checks reproduce recorded development outcomes and software behavior,
not fresh model learning. The release example already has a supplied complete
program; it should not become the scientific workload merely because it runs.
Training restarts from base, so continuing-adapter optimization is unavailable.

The review supports bounded workload/acquisition feasibility for the proposed
comparison. It does not yet establish a competent baseline, functioning learner
or affordable main study on the new workload. Those remain investigator work.
