# What Construct has learned

> previous project root for this file was `~/Developer/Projects/alignment-farm/construct/`

Research synthesis · 2026-09-08

**Construct's strongest result is that governing what becomes context can
improve later decisions, and that keeping memory recoverable can reduce the
cost of retaining it.** Those benefits have been demonstrated on bounded
tasks. The larger thesis—that memory architecture explains everything an agent
becomes after training—remains a research thesis, beyond what these experiments
establish.

Construct studies **agent-side memory**: persistent software around a language
model whose individual sessions do not retain their own context. These
experiments change external memory and its governance, rather than train new
model weights. The **harness** is the experimental software that supplies
context, records actions, and computes outcomes independently of the tested
model. An **oracle** is the rule or external evidence used to judge correctness.

This brief is self-contained and can be shared as a single Markdown file. It
summarizes the research record as of the date above; it creates no new
experimental verdict. Numbered source notes at the end identify the underlying
internal records for provenance. Reading those records is not required to
follow the findings, although independently reproducing the experiments would
require the original evidence and code.

The experiment names are identifiers: the M-track studies memory offered to
answers; the X-track studies memory management around and between answers.
A **branch** is the same model under a different memory condition; an
**ablation** removes a proposed cause to test its influence. A result marked
`not_engaged` means the cell's prerequisites for measuring the intended effect
were not met. A **loses condition** specifies where the mechanism should incur
a cost or perform worse.

## 1. Possessing information does not ensure that a model can use it

The central experimental intervention is the **offer**: the harness places
selected records into the model's context. The same engine runs under different
memory conditions, with foreground inputs held constant. This isolates the
effect of the memory boundary; it does not establish that an autonomous agent
would retrieve the same records itself.

M0 demonstrated a world-grounded governance win: on gpt-oss-20b, surfacing a
retraction notice in place of an attractive retracted claim changed a wrong
citation into a correct refusal. Claude's governed control already declined,
so the same cell was `not_engaged` there. The correction-notice loses-cell
also did not engage: the notice itself contained enough information to answer
correctly. Governance's value depended on what the baseline lacked.
(M0 findings [1],
harness contract [2])

M1 made the distinction between storage and usable memory sharper. An heir
inheriting consequence-earned authority surfaced a useful record that a cold
re-reader withheld. In the world-grounded HU1 case, both branches possessed
the same single record; an authority change from 1.0 to 1.1 moved it across a
deliberately calibrated eligibility threshold. Both tested engines then
answered correctly only in the heir branch. This is a causal demonstration
at a specific retrieval geometry, not a general budget frontier. The price was
also observed: over-pruning removed a record later needed, making the heir
wrong where the cold branch was right on both engines.
(M1 findings [3])

**Learned implication:** evaluate the path from retained information to offered
context. More accumulated records can crowd out the record that matters;
selective inheritance can help and can discard something valuable.

## 2. Experience can change a later session, but influence must be measured

M2 crossed a real session boundary. After a model incorrectly cited a retracted
finding, the harness minted a lesson from the externally checked correction
trace. In the later session, the resident received that lesson and its control
did not. Removing the lesson in a further counterfactual tested whether it
actually mattered.

The causal success cell passed **5/5 draws on gpt-oss-20b and 4/5 on Claude**.
Claude's one miss came from an ablation draw that still declined without the
lesson, rather than a wrong resident answer. A later five-sample ablation
supported the lesson's influence. The initial story of a consistently cautious
Claude was withdrawn after repeated draws: both controls cited the retracted
finding in all five runs. The demonstrated scope remains one hop, one
retraction, and lexical retrieval.
(M2 findings [4], draw ledgers [5])

M1.5 established a related accounting boundary: a contribution claim needed
resolvable artifact evidence; a presence-only, inflated claim was refused.
Yet the contribution ledger subsequently went unused through several
milestones. Its later audit recorded that gap instead of silently backfilling
it. A functioning instrument and sustained operational use are separate
achievements. (M1.5 findings and addendum [6])

**Learned implication:** a model's statement that it remembered, used, or caused
something cannot establish causality. Counterfactual influence also does not
establish correctness; an independent outcome check must supply that judgment.

## 3. Memory governance is a security boundary

M3's most consequential attack changed what the resident could remember.
An attacker spoofed a fresh live-channel datum, causing the unauthenticated
yield gate to withhold an earned retraction lesson. Deprived of that lesson,
Claude cited the retracted finding: **3/3 answer-level breaches** in the close
run. Foreground framing attacks left the protected projection intact and
failed to induce the corresponding answer pathology across five draws.

The distinction was between **consequence-earned authority protected outside
the foreground** and **trust asserted at an attacker-accessible boundary**.
A separate ingestion attack showed that a chosen high trust field could also
clear eligibility. The `channel_trust` defense blocked the tested spoof and
restored the correct answer in its one-draw close check.
(M3 findings [7],
close evidence [8])

**Learned implication:** protect the inputs that govern withholding and
admission, as well as the text offered to the model. A robust answer policy
cannot compensate reliably for a compromised memory channel. This result is
bounded to one channel, one retraction, hand-authored attacks, and one frontier
engine for answer-level effects; it is not a general prompt-injection defense.
The trust-map mechanism also depends on trustworthy channel identity.

## 4. Forgetting can mean eviction with recovery

X2 found a measurable benefit outside the immediate answer boundary. It
compared keeping everything hot, pruning without recovery, and pruning with
rematerialization from immutable lineage: restoring an evicted record from a
preserved history. **Hot** records are currently materialized in the active
store; **cold** records remain recoverable from that history. Both gpt-oss-20b
and Claude produced the following results:

| Four-episode fixture | Keep hot: cost / correct | Prune only: cost / correct | Prune + recover: cost / correct |
| --- | ---: | ---: | ---: |
| Fictional Helix Basin | 312 / 4 | 105 / 3 | 135 / 4 |
| External DEP0033 reversal | 248 / 4 | 92 / 3 | 102 / 4 |

Recovery reduced the scored hot-store cost by **56.7% and 58.9%**, respectively,
while matching every baseline answer. Pruning without recovery was cheaper
still, but failed when an evicted fact became relevant again. The external
fixture concerned Node.js DEP0033, a deprecation subsequently revoked. It
additionally used cold ignorance probes—questions asked without the relevant
memory: both engines initially
answered with the outdated fact.
(X2 findings [9], verdicts and ledgers [10])

The metric matters: `hot_tokens` is a cumulative count over hot-store snapshots,
computed from whitespace-split record text. It is not a measured reduction in
API bills, latency, physical RAM, or total archival storage. Quality was sampled
once per engine per fixture, over one short recurrence pattern.
(Cost scorer [11])

**Learned implication:** the useful optimization is selective materialization
with a priced recovery path. Cheap deletion alone does not earn the same claim.

## 5. A distinct memory mechanism needs a distinct test

X1's use-driven temperature—a record eligibility multiplier, not the model's
sampling temperature—changed eligibility at offer time. Its proposed
win did not engage on three real engines, but the experiment had not established
offer dependence, so that null could not settle whether the mechanism helped.
The mechanism was retired as an implicit-memory organ on a structural argument:
it was another form of explicit offer selection.

The resulting design discipline was to require a new mechanism to change
something ordinary offer projection cannot explain, operate where the offer
gate cannot, and use a metric that gate cannot move. X2 met that challenge on
hot-store retention cost. (X1 correction [12],
X2 findings [9])

X4 exposed a measurement problem in a proposed watch for missing prior context.
Review found forgeable catch records, denominator gaps, unreliable session
inference, and a deeper problem: the scoreboard depended on which omissions
other participants named. It measured curation rather than independently
establishing sensing. The project consequently moved toward warming (restoring useful context) and
metabolism (managing memory retention and recovery costs) as an engineering
direction, without treating that direction as an earned mechanism. (X4 review in the specification [13],
thesis history [14])

## 6. A refusal tells us why a test stopped, not whether its conjecture is false

Several later lines produced useful but different kinds of closure.
**Admission** means checking that an engine and instrument can support an
interpretable test before running the memory treatment. The **epistemic-frame
check (EFC)** asked whether an earlier failure could trigger a useful external
check on a later task in a different domain. Warming-budget and pause/resume
work asked whether retained state could reduce the cost of resuming work.

| Line | What the record supports |
| --- | --- |
| Warming budget [15] | An analytic null under per-resume charging, restricted state contents, and a planner that reads the decisive status evidence first. Charging retained state once across many resumptions remains a different question. |
| Pause/resume [16] | Licensed behavioral losses and ties on one family; variance and admission refusals on others. No licensed cost win. Five identical pilots that read only the decisive sources do not establish a population distribution. |
| EFC v0 [17] | Free-text substring scoring failed fresh semantic counterexamples; no memory treatment ran. |
| EFC v1 [18] | The corrected baseline was 5/15 overall and 2/5 on the gate's subset. Statistical headroom, not a perfect baseline, explains refusal. |
| EFC v2 [19] | Two completed small-engine batteries failed admission with constant-policy and within-class selection problems; the treatment conjecture remained untested. |
| Body-1 [20] and frontier obligation [21] | Transport or commitment-format failures prevented scored treatment contact. |

EFC v1 is particularly instructive. The retrospective audit reproduces the
historical refusal, but withdraws the explanation attached to it. At five
cases, the frozen headroom rule accepted only 0/5 baseline successes and
refused 1/5 through 5/5. The broader story that several lineages independently
proved an unoccupied behavioral band was consequently withdrawn.
(Correction audit [22])

**Learned implication:** distinguish behavioral loss, absent treatment need,
statistical insufficiency, parser failure, and transport failure. Combining
them into one negative result creates knowledge the experiments did not earn.

## 7. Reliable components do not establish a useful whole

Body-0 composed M2's consequence record, M3's protected projection, and X2's
recovery. The deterministic integration worked. In the real run, however,
reference and composed branches returned empty answers while the ablations
answered correctly. The corrected scorer required reference and treatment
correctness before interpreting the ablations, closing `not_engaged` with no
integration claim. This neither establishes nor refutes beneficial composition.
(Body-0 findings [23])

Body Core's engineering lesson is narrower: durable event validation can be
separated from an explicitly selected lifecycle and placement policy, while
adapters preserve historical scorer results. That is useful replay and
integration engineering. It does not demonstrate new learning, reconstruction
cost savings, or writer authentication; a hash chain alone cannot supply the
last of these. (Projection boundary [24],
sketch limitations [25])

## 8. Governed continuity has a promising concrete use

The game-master (GM) exploration concerned a language model running a tabletop
role-playing game. **Canonical state** is the authoritative current game
record; continuity preserves earlier promises and obligations that state may
omit. The exploration tested a decision requiring two facts to be joined:
an earlier promise identified a consequence, and current canonical state
mapped that consequence to an available action. The memory did not simply
provide the action label.

On Bonsai 27B, governed continuity scored **24/24 relevant cases versus 6/24
for state only**, with 18 favorable paired differences and none adverse.
Both branches scored 6/6 when current state sufficed and 6/6 when it superseded
the older record. Continuity added about **99 input tokens per governed call**;
on those safety cases it bought no accuracy, supplying a concrete cost-only
loses condition. (GM finding [26])

This is explicitly a **bounded exploratory finding**. The original formal
attempt incorrectly assumed which response metadata the model server would
return; the owner superseded its zero-retry
rule and authorized a corrected 72-call exploratory replacement. It does not
establish a population success rate, whole-game benefit, another engine's
performance, or reliable model-authored memory.
(Replacement result and provenance [27])

**Learned implication:** a compact, sourced proposition can supply continuity
that current state omits, while current state remains authoritative. The result
motivates selective continuity in live play; it does not settle the retrieval
policy that should select those propositions.

## What the evidence asks of the next claim

Across the project, scorer audits changed substantive conclusions: markdown
normalization and negation bugs mis-scored correct answers, and admission
arithmetic supported a refusal without supporting its original explanation.
The evidence chain must therefore expose answers and scoring rules as well as
verdict labels.

The project's methodological response also matters. Strict admission protected
claims but selected for questions already easy to isolate and grade. The
exploration policy [28] permits bounded iteration
while reserving validation for a fresh prospective test. That is a policy
lesson, not proof that looser exploration produces better science.

The remaining scientific gap is scale and generality: longer histories,
multiple recurrences, broader corpora and engines, autonomous retrieval,
end-to-end costs, and useful composition in live tasks. The existing record
supports pursuing those questions without assuming their answers.

---

**Read-in and verification scope.** This synthesis reviewed project findings,
governing contracts, and selected implementation and evidence. It incorporates the 2026-09-06 EFC corrections. M2 draw counts and
M3 close evidence were checked in retained artifacts; all four cited real X2
ledgers were rescored without modifying them, using the pruning scorer
identified in the source notes, preserving their verdicts.
GM numbers are reported from its current finding and result documents: the
underlying MÖRK BORG game-project evidence was unavailable in the workspace
used to prepare this synthesis, so it was not independently inspected. No new model calls or experimental ledger writes were made.

## Source notes

These are internal Construct research records, identified by title and experiment
rather than by links or machine-specific paths. They preserve attribution when
this brief travels independently; they are not an attached reproducibility
package. All substantive results and limits used here are stated in the brief.

1. M0 findings — first scored verdicts against an un-authored oracle. Retraction and correction experiments.
2. Construct Plan v1 — Branch-and-Offer Harness. Experimental controls, offer boundary, and outcome-oracle contract.
3. M1 findings — inheritance, scored on two engines. Includes HU1 and the over-pruning loses-cell.
4. M2 findings — the resident substrate, run on the retraction chain. Includes repeated-draw and ablation corrections.
5. M2 repeated-draw primary ledgers. Five session-pair runs each for Claude and gpt-oss-20b.
6. M1.5 findings — the contribution ledger, computed on the M1 backfill. Includes the July 2, 2026 audit of the logging gap.
7. M3 findings — the adversarial air gap. Includes the corrected negation oracle and channel-trust defense.
8. M3 close-evidence summary, June 15, 2026. Five framing draws, three channel-spoof draws, and one defended draw.
9. X2 findings — prune-to-cold-store, cost at matched quality. Helix Basin and DEP0033 experiments.
10. X2 primary ledgers and computed verdicts. Real runs a30695 and d6aede (Helix); e10cef and f4e7ab (DEP0033).
11. X2 pruning scorer, score_prune. Replays hot-store membership and recomputes cumulative whitespace-token cost and quality comparisons.
12. X1 findings — decay dynamics. Includes the correction distinguishing an inconclusive null from the structural placement argument.
13. Specification X4 — Sensory Occlusion Watch, section 12. June 26, 2026 review and retracted measurement claims.
14. Construct project overview, “How the thesis changed.” Project-level interpretation, current at preparation of this brief.
15. Warming-budget findings. Analytic null under the v0.1 state and pricing contract, July 6, 2026.
16. Pause/resume findings — the pay-window question. Distinguishes behavioral outcomes from instrument and admission refusals.
17. EFC v0 findings — the oracle refused the experiment. Semantic scoring failure before treatment contact.
18. EFC v1 findings — calibration closed confounded(menu_ceiling). Closing interpretation corrected September 6, 2026.
19. EFC v2 findings — Part I contact stage. Admission-battery outcomes and corrected cross-lineage interpretation.
20. Body-1 admission findings. Transport and output-surface refusals; no scored treatment contact.
21. Frontier obligation admission findings. Artifact-qualified commitment failures before memory treatment.
22. EFC v1 retrospective closing audit, September 6, 2026. Preserved pilot counts, historical-rule replay, and five-case acceptance sweep.
23. Body-0 findings — earned-property composition. Corrected not_engaged verdict and limits of integration evidence.
24. Body Core v0.3 — explicit projection boundary. Structural kernel and selected policy separation; engineering claim boundary.
25. NEXT substrate embodiment sketch — evidence boundary and limitations. Replay, authentication, and maturity disclosures.
26. Governed continuity changes GM decisions, August 4, 2026. Bounded exploratory finding and token costs.
27. GM governed-continuity validation result, August 3, 2026. Corrected exploratory replacement, 72 calls, and bound artifact identities.
28. Frontier exploration and claim promotion, August 3, 2026. Two-lane exploration and prospective-validation policy.
