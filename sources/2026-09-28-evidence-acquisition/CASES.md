# What the inspected decisions reveal

28 September 2026. Purposive inspection of one public maintenance lineage and
three decisions in two elicited human conversations. These cases identify
mechanisms and evaluation limits; they are not a representative sample or a
test of agent learning. All descriptions below are paraphrases.

## Requests: requirements, checks and later reuse

The source chain is [issue 5794](https://github.com/psf/requests/issues/5794),
[PR 5856](https://github.com/psf/requests/pull/5856),
[issue 6084](https://github.com/psf/requests/issues/6084) and
[PR 6097](https://github.com/psf/requests/pull/6097).
The issue/PR bodies, comments, inline reviews and final file diffs were inspected.
API snapshots, timestamps and hashes are in the ignored cache and retrieval log.
Comments are a retrieved public history, not immutable contemporary snapshots;
historical edits to their text cannot be ruled out.

| Decision | Available information and subsequent evidence | Root interpretation |
|---|---|---|
| Preserve a backend or replace it? | The original report identifies exception types varying with installed JSON libraries. A contributor proposes removing `simplejson`. A [July 3 compatibility response](https://github.com/psf/requests/issues/5794#issuecomment-873413571) explains preserving existing callers; [review](https://github.com/psf/requests/pull/5856#discussion_r664037480) rejects the incompatible removal. | Executing one environment reveals behavior; it does not by itself select the project's compatibility policy. The decision record can supply that policy to later work. This does not prove that policy was otherwise unavailable in documentation. |
| Ask again or test a proposed implementation? | A [July 9 review](https://github.com/psf/requests/pull/5856#discussion_r667121799) identifies an exception class missing in Python 2. A [July 12 response](https://github.com/psf/requests/pull/5856#issuecomment-878482999) directs the contributor toward local environment/CI testing. | Once the requirement is established, implementation evidence can be obtained through a relevant environment. The record supports this distinction, but does not supply counterfactual costs or all test outputs. Root did not reproduce Python 2. |
| Reopen the policy or check an uncovered path? | The later report identifies the no-encoding path escaping the wrapper. A [maintainer response](https://github.com/psf/requests/issues/6084#issuecomment-1080988069) acknowledges the omission and points to a focused test and fix. | The earlier requirement remains usable. The new uncertainty is branch coverage. Keeping the resolved contract and inspecting relevant branches is a competent ordinary alternative to another source-selection learner. |

Revision history matters. PR 5856's body describes replacement of `simplejson`,
but its merged code at `db575eeedcfdb03bf31285afd3033e301df8b685` preserves the
backend choice and wraps one decoding route. The final code and review, rather
than the stale PR description alone, establish what landed. PR 6097 adds wrapping
to the earlier inferred-encoding route and adds a regression test. Its base is
`8bce583b9547c7b82d44c8e97f37cf9a16cbe758`; merged revision is
`2d5517682b3b38547634d153cea43d48fbc8cdb5`.

### Bounded independent replay

Root installed the two exact PR-6097 source revisions with `uv`, using Python
3.13.12 and `simplejson` 3.20.1. Both source snapshots report Requests 2.27.1;
the commit IDs distinguish them. The installed `Response.json` AST matches its
cached source after docstring-indentation normalization. Seven offline Response
objects exercise valid and malformed UTF-8/UTF-16, explicit/inferred encoding,
and a short malformed body. No HTTP service was called by the probe.

Before the fix, the two malformed inferred-encoding cases raise the backend's
exception without the Requests wrapper. The explicit-encoding and short-body
cases already satisfy the wrapper contract. After the fix all four malformed
cases have the wrapper and remain catchable through both relevant parent types.
All three valid-input controls parse identically at both revisions. This is
14 deterministic component executions, not independent samples, full-library
validation, historical-environment reproduction or an agent repair score.

The cases were chosen after reading the report and patch. They confirm the
mechanism; they cannot establish how readily an unassisted agent would discover
the missing check. Complete histories, old runtime coverage and learning from
earlier attempts remain outside this replay.

## InSCIt: a question can narrow the task without being uniquely necessary

Pinned author repository: [2319fb8](https://github.com/ellenmellon/INSCIT/tree/2319fb85932b9528a13417223ffc6fc629ae8087).
Inspected `README.md`, all development-record schemas, `eval/eval.py`, the human
evaluation README, and selected dialogue contexts, labels, passages and following
turns. Only the 4.18 MB development JSON was downloaded; train/test, the full
Wikipedia corpus, pretrained models and prediction bundles were not acquired.
These are paid, elicited human dialogues, not naturally deployed assistant logs.

The audit finds **86 conversations, 502 turns and 835 reference annotations**.
333 turns have two references; **77 of those have different response types**.
All 416 within-conversation continuations preserve the preceding context and
continue from one supplied reference response. This counts annotation structure,
not the benefit of asking or a population frequency. The official evaluator
matches recorded contexts and scores evidence/response agreement; it does not
execute alternative queries or score their later outcomes. No official model or
full evaluator run was performed.

Selection was diagnostic: inspect the first clarification in sorted development
IDs, its following turn, and the next conversation with a clarification. These
examples were not reserved for confirmation. Exact IDs, reference types, evidence
IDs and record hashes are in [asset-audit.json](asset-audit.json).

| Decision | What the recorded continuation establishes | What remains unidentified |
|---|---|---|
| `food_level1_dial28`, turn 4: commercial versus homemade egg substitutes | Both references ask the user to choose between these categories. The following user turn selects homemade options. Retrieved passages describe both categories, so factual availability does not supply the user's preference. | A concise answer covering both categories might also have served the request. No downstream comparison shows that asking was necessary or worth its cost. |
| Same conversation, turn 5: answer after that preference is known | One retained reference gives a direct answer; another supplies examples and offers further narrowing. Both use the previously available homemade-substitute passage. The recorded user then changes topic. | A single action label would discard a retained alternative. The next message cannot be replayed as the user's response to an arbitrary new clarification. Re-asking the already answered category question would be unnecessary. |
| `food_level1_dial33`, turn 2: historical origin of sausages | Retrieved passages describe several traditions. The agent asks which tradition interests the user, who chooses one. The subsequent response gives a historical mention while retaining uncertainty about the first origin. | Narrowing the user's interest changes scope but does not resolve the earliest-date uncertainty. A responded-to question is not proof that the original factual goal was completed. |

## What is obtainable versus missing

The maintenance source provides chronological requirements and a reproducible
implementation distinction. The dialogue source provides source-grounded
responses, alternative annotations and actual continuations along one branch.
Neither provides a matched comparison of source-answer reuse against a strategy
acquired from earlier agent work. Neither measures all alternative observations,
human interruption cost or later repair cost. Missing counterfactual outcomes
must not silently become labels saying which source an agent ought to choose.

These assets support the root's narrowed selection. They do not warrant a new
standalone classifier experiment or establish that learned investigation lacks
value. Fresh independent histories would be needed for a transfer claim; the
existing investigation study owns any subsequent experimental implementation.
