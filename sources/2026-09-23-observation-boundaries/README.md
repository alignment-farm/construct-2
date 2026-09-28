# Observation boundaries and lesson acceptance — 23 September 2026

Root question: which observation can resolve a consequential uncertainty about
reusing a lesson after competent ordinary review? The
[conclusion and selection note](../../notes/OBSERVATION_BOUNDARIES.md) separates
implementation evidence, intended requirements and reusable investigation.

## Retrieval, provenance and inspection boundary

Root began at `f68f34c` on clean `main`. Read governing instructions, the overview,
ancillary approach, current study assessments, source guide, perspectives and
previous-research synthesis, then the lesson/feedback/decision-value records.
No ancillary repository was newly inspected; accepted publication boundaries
remain `cbe62b9` for lesson acceptance and `47e5b28` for the investigation pilot.
This is root theory and primary-method reading, not another publication review.

Investigator: **`gpt-6-astra`, reasoning `xhigh`**, OpenAI provider, Codex CLI
`0.156.1`. These fields were read from this session's local `session_meta` and
`turn_context`, rather than inferred from output or the requested policy.
[provenance.json](provenance.json) records the minimal fields and scope. There
were no participant/teacher model runs or delegated research agents. Investigator
token and monetary costs are not measured in this record. The 22 September
Astra-only investigator policy remains in force; participant models remain
scientific choices for a future study.

The title-discovery query and subsequent selected-ID API request both returned
HTTP **406**, with empty bodies and no metadata. They were sequential, more than
three seconds apart, with a descriptive User-Agent; no retries followed.
[retrieval.json](retrieval.json) and
[metadata-retrieval.json](metadata-retrieval.json) preserve requests, times,
headers and empty-body hashes. The empty `.xml` files are failed-response
artifacts, not valid metadata or evidence of zero search hits.

Supplementary web discovery located the primary papers.
[discovery.json](discovery.json) records the queries and lead disposition.
Exact-version arXiv HTML was inspected and cached locally under ignored `.cache/`;
[primary-retrieval.json](primary-retrieval.json) records URLs, timestamps, headers
and SHA-256. Version identity comes from the versioned HTML, not the failed API.
This bounded search does not establish exhaustive coverage or that v1 is each
paper's latest revision. No public author code, dataset instance or model result
was independently reproduced. Downloading full text does not mean every section
was reviewed.

## Inspected methods

**P102 — [Structured Uncertainty guided Clarification for LLM Agents,
2511.08798v1](https://arxiv.org/html/2511.08798v1).** Read §§3–7, selected §8
results and Appendix A.4.3. SAGE-Agent scores questions over candidate tool
arguments, with domain-based beliefs and a redundancy penalty. Its simulator
receives intended calls; its GRPO experiment trains clarification decisions on
When2Call. Authors report improved call matching and question efficiency.
**Answers** generic feasibility of structured and learned clarification.
**Narrows:** matching tool calls and modeled question costs do not establish
complete continuing-task benefit or lifetime cost. Belief factorization and
finite candidate/domain assumptions matter; these scores are not independently
calibrated uncertainty estimates. No learning from an agent's own accumulating
cross-session history was established by this inspection.

**P103 — [ClarEval, 2603.00187v1](https://arxiv.org/html/2603.00187v1).** Read
§3 and appendix Tables 4–8. Construction removes goals or premises or replaces
precise terms; scripted trigger/response pairs restore intended requirements.
Evaluation emphasizes question coverage, recovered premises and interaction
turns. **Narrows** novelty for ambiguous coding tasks and gives an inspectable
oracle-design lead. **Redirects:** constructed information withholding is not
evidence that ordinary specifications leave consequential uncertainty in our
work. Script coverage and communication scores do not establish complete program
correctness, transfer or retention value. No headline model ranking is adopted.

**P104 — [When Search Agents Should Ask: DiscoBench for Clarification-Aware
Deep Search, 2606.27669v1](https://arxiv.org/html/2606.27669v1).** Read §§3–5,
limitations and Appendix B. It inserts ambiguity into retrieval chains, supplies
discriminating clues through a simulated user, and scores both checkpoint
behavior and final answers. **Narrows** generic search-versus-clarify proposals.
**Root inference:** §5.4's higher success among SearchThenAsk trajectories is a
behavioral association, not an assigned-policy causal contrast; profile choice
can select different situations. The search-removal ablation addresses another
question. LLM-mediated answers and simulated users limit imported guarantees.
The inspected study does not test retained cross-session experience or establish
a generally optimal rule for when to ask.

P47's costly-observation framework and P48/P94/P95's previous reading boundaries
remain unchanged. They were consulted through existing root records, not reread
in full. The oracle-problem survey and Angluin's query-learning paper were
metadata/abstract discovery leads only; neither supports a new imported theorem
or receives a paper-map entry here.

## Consequence and verification

The root's indistinguishability argument is an analytical deduction with explicit
assumptions. Its row-count illustration is constructed, not measured evidence
or a validated workload. It explains why some acceptance questions require a
different source of information, rather than more execution of the same program.

The selected candidate is experience-informed evidence-source choice with
competent ordinary review and retained source answers. Further artifact inspection
would have to establish its empirical value; no new study is prepared or launched.
Original LA1–LA3, AD1–AD3 and CC1–CC3 remain unchanged.
[Documentation validation](validation.json) passed for local links, paper
numbering, preserved predictions, JSON records and primary-cache hashes;
`git diff --check` also passed. There is no new empirical test to score.
