# Cold read of Construct-2 — 13 September 2026

A fresh Codex session recovered the project's current scientific state from its
documents and followed the links into ancillary results and supporting analyses.
This is one successful orientation probe, with minor omissions. It is a
documentation diagnostic, not an agent-memory finding or a controlled test of
whether the recent documentation edits improved performance.

The [prompt](prompt.txt) asked for the project's question, completed work,
evidential limits, weaknesses, and a useful next step. It supplied no study names,
results, or preferred recommendation. The [assessment notes](pre-run-notes.md)
were written before launch and kept outside the project directory. The agent
received neither those notes nor the parent conversation. This diagnostic
directory was created after the run; exclude it and previous diagnostic responses
from the inputs of any future independent cold-read probe.

The run used a new `codex exec` session, with read-only access, `--ephemeral`,
and memories, hooks, and delegation disabled. Normal CLI configuration and
general instructions remained available. This is cold relative to the current
conversation and saved agent memories, not a model without prior knowledge or
general instructions. The invocation follows the CLI's documented
[non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).

| Recorded property | Value |
| --- | --- |
| CLI | 0.154.0 |
| Configured model / reasoning | `gpt-6-astra` / `xhigh`; no model override |
| Elapsed time | 172.93 seconds |
| Completed commands | 19, all local discovery or reads; no failures |
| CLI input tokens | 630,987, including 561,920 cached input tokens |
| CLI output tokens | 4,193; reasoning-output field: 1,358 |

The token fields are the CLI's reported aggregates across the run, not the size
of one context window or a monetary cost estimate. See the exact [invocation and
timing](run.json), [event trace](events.jsonl), and [checks](checks.json).

The [full response](response.md) correctly recovered both completed bounded
investigations. It preserved S1's distinction between changed loss/generation and
task benefit, including the absence of a dynamic-selector test. It identified
the procedure study's weak adapter transfer, failed lesson construction,
privileged supplied-rule diagnostic, and lack of repayment at comparable
accuracy. It also distinguished the latest addendum from the initial PDF,
inherited Construct evidence from the newer investigations, and completed work
from unresolved interference, correction, consolidation, and changed-goal tests.

The recommendation was the proposed Titans–Modular TTT written synthesis, with
an explanation or discriminating hypothesis as its output. That is a defensible
reading of the current agenda. Since the documents already suggest this route,
the agreement demonstrates recovery of the agenda rather than independent
evidence that S3 is the best research investment. The response also supplied
substantive cautions about clustered inputs, underdetermined compositional rules,
and confounding a representation with the method used to construct it.

Some omissions deserve attention. The agent missed the then-present
contradiction between the supplied serving endpoint and the following sentence
claiming the endpoint was unrecorded. Its final sentence also tied later
experiments too broadly to mutable-state access on the new machine: access must
be checked on the hardware actually chosen, and the previously verified MLX
route remains a possible resource. Root/ancillary ownership was also implicit:
the agent recommended root-level synthesis but did not explain who owns
experimental protocols and evidence. The response was strong on scientific
scope but did not recover every operational detail.

The first post-run hash check found all 31 snapshotted documents unchanged. A
later archive check found that root `AGENTS.md` had been updated to remove the
endpoint contradiction; that [post-run change](post-run-document-change.diff)
is recorded separately. The [input snapshot](input-snapshot.tar.gz) and
[manifest](input-manifest.json) preserve the earlier documents. The snapshot
covers root Markdown and ancillary entry, notes, and protocol documents; the
event trace also preserves the returned excerpts from other local sources.
Neither this probe nor the parent assessment independently rescored the raw
scientific experiment outputs.

The result supports a narrow judgment: this agent could reconstruct the
project's state and make a grounded recommendation without the parent chat.
It does not establish consistency across agents, models, prompts, or future
work, and there was no comparison with the previous documentation.
