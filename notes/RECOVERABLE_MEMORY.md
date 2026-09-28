# Recoverable memory when the task changes

Root theory and literature assessment · 28 September 2026

**Conclusion:** compact working memory can coexist with preserved experience,
provided the agent can recover what a later task needs at an acceptable cost.
The relevant unit is all retained state and its access path. A short prompt,
a small active latent pool, and a small total store are different achievements.
Existing public methods already develop retrieval of archived latent states,
learned reconstruction, and construction of context from preserved sources.
The useful remaining question concerns reliable, economical recovery under
changed demands, beyond competent ordinary access.

This completes an independent root phase while the EBM study explores. It does
not reopen S4 or commission another study. The [reading ledger](../sources/2026-09-28-recoverable-memory/README.md)
records P114–P117, exact versions, inspection limits and provenance. No new
participant experiment ran; public results below remain author-reported.

## What the existing findings leave open

[S4](../studies/README.md#s4-what-does-learned-memory-lose-when-the-future-goal-changes)
separated omissions from unsuccessful reading, including later compositions
absent from writer training. It did not establish storage economy or acquisition
of unfamiliar read operations. [Construct's earlier recovery result](PREVIOUS_RESEARCH.md#4-forgetting-can-mean-eviction-with-recovery)
showed a bounded benefit from rematerializing evicted records; its hot-token
metric was not total storage, latency or an API bill. Together these motivate
asking what remains accessible after compression, rather than treating every
omission from active context as permanent forgetting.

## Three gaps, with explicit assumptions

Fix a distribution over past histories `H`, later questions `Q` and correct
outcomes `Y`, with a chosen task loss. Let `S` include **all** state retained from
the history: records, latent archives, learned parameter changes, generated
tools and indexes. Let `P` include everything the final reader can inspect after
the access procedure, including any retained state it can directly use. Hold
background knowledge fixed. Assume no fresh external evidence is obtained:
conditional on `Q`, the flow is `H → S → P → answer`, possibly with independent
randomization. A tool that consults a new source requires the additional
observation account in [evidence acquisition](EVIDENCE_ACQUISITION.md).

Write `R_H`, `R_S` and `R_P` for the minimum expected task loss of an unrestricted
reader given `(H,Q)`, `(S,Q)` or `(P,Q)`. If the actual reader has loss `R`, then

```text
R − R_H = (R_S − R_H) + (R_P − R_S) + (R − R_P)
           retention       access          reading
```

Each term is nonnegative under these assumptions. A reader with the earlier
information can simulate the later transformation and answering rule, so its
optimum cannot be worse. The identity then follows by adding and subtracting
the intermediate risks. These are explanatory optima, generally unknown in a
real system; a few failed decoders cannot measure them or prove information
absence. This is a standard decision-theoretic decomposition applied to our
question, not a new learning algorithm or a novelty claim.

The access term includes retrieval, eligibility, compression into the answer
packet and any budget-imposed omission. It can be split further when useful.
Keeping a raw archive can eliminate retention loss relative to that archive's
observed history while leaving substantial access and reading failures.
Archiving only an already compressed state cannot restore distinctions that
the complete retained state no longer contains. An actual fixed reader may
perform worse when given more material; the monotonic statement concerns the
unrestricted optimum, which can ignore it.

A constructed example makes the distinction exact. Let history contain two
independent fair bits `(x,y)`, let active memory retain `x`, and let the later
question ask for `y`. Under zero–one loss:

| Retained state and use | Retention gap | Access gap | Reading gap | Error |
|---|---:|---:|---:|---:|
| Only `x`; best answer | 1/2 | 0 | 0 | 1/2 |
| `x` plus another copy of `x`; best answer | 1/2 | 0 | 0 | 1/2 |
| Full `(x,y)` archived; access supplies only `x`; best answer | 0 | 1/2 | 0 | 1/2 |
| Full archive; access supplies `y`; reader returns `y` | 0 | 0 | 0 | 0 |
| Full archive; access supplies `(x,y)`; reader returns `x` | 0 | 0 | 1/2 | 1/2 |

All entries follow from the four equally likely histories. This is an analytic
illustration, not a measured workload or evidence that a model learns recovery.

For a deterministic writer and finite history space, exact support for a family
of deterministic questions requires only distinguishing histories with different
answers to at least one question in that family. If two such histories share
the same total retained state, no reader can answer both correctly. Conversely,
an unrestricted lookup reader can answer from a state that separates those
classes. Supporting every possible distinguishing question therefore requires
an injective retained representation; a narrower family can permit compression.
This says nothing about whether that reader is learnable or affordable. Count
actual representational capacity, including vector dimensions and precision;
fewer memory positions alone do not establish fewer stored bits.

## What the public methods change

| Inspected precedent | Consequence for this root question |
|---|---|
| [M+, P114](https://arxiv.org/html/2502.00592v2) | Archived latent states are a developed alternative. Moving a state out of active memory need not discard it; total capacity and access costs still matter. |
| [R³Mem, P115](https://aclanthology.org/2025.findings-acl.235.pdf) | Learned reconstruction is a concrete method. Reversible internal computation does not by itself establish exact recovery of source text from the deployed retained state. |
| [LazyMem, P116](https://arxiv.org/html/2607.22690v2) | A trained small context constructor is a close positive precedent. A generic proposal to train one would duplicate existing work. |
| [RD-Forget, P117](https://arxiv.org/html/2609.10263v1) | Preserving sources while changing current and historical evidence views is also developed public work. A rescue switch must be interpreted alongside other source-access paths. |

These methods make the hybrid hypothesis more concrete. They do not establish
that one substrate is generally best or that Construct has already achieved
their reported capabilities. The ledger distinguishes method inspection,
reported findings and our interpretation; no author code or checkpoints were
audited in this phase.

## When recovery is worth retaining

Compare a compact working representation with recovery (`h`) against broad
ready memory (`b`) at comparable complete-task quality over a stated horizon.
Let `A` be acquisition and construction cost, `M` maintenance plus storage cost
over that horizon, `u` ordinary cost per use, and `N` the number of uses. Suppose
recovery occurs on fraction `p` of uses and adds mean conditional cost `r` to the
compact path. Include failed attempts, checking and repair in the corresponding
costs. Under this stationary accounting approximation:

```text
C_h = A_h + M_h + N(u_h + p r)
C_b = A_b + M_b + N u_b

Recovery is cheaper when
N(u_b − u_h − p r) > (A_h − A_b) + (M_h − M_b).
```

This is a bookkeeping condition, not an estimated crossover. Different quality
requires reporting the quality–cost trade-off, rather than invoking this
equal-quality comparison. Real sequences with changing demands require summing
their actual costs. With a fixed positive premium on the right-hand side,
increasing the horizon cannot repay it if recovery removes the per-use saving.
Shared archive cost cancels only when both alternatives actually retain and
maintain it.

This also identifies where learning could help: reduce repeated access or
interpretation work while preserving useful distinctions and a functioning
recovery path. Weights, contextual lessons, indexes and executable access tools
can all contribute. The cost of developing or relearning that behavior belongs
in the comparison. Recovery need not reconstruct the whole history if a smaller
piece suffices for the new task.

## Research selection

Deprioritize a separate demonstration that raw retention permits later queries,
or that a trained specialist can shorten answer context. Existing results
already answer those generic feasibility questions. The selected root result
is the explanatory account above; it needs no new run to complete.

Retain as an independent candidate: **can accumulated experience reduce the
work needed to recover and use evidence after requirements change, at comparable
complete quality, beyond ordinary archive search and reuse of prior results?**
Relevant evidence would distinguish better persistent representation, better
access and better interpretation, while charging the archive and recovery.
A goal shift that only increases the archive's size is insufficient to establish
transfer to a changed evidence need. This is a research preference, not a new
protocol, claim of novelty or commission; feasibility remains for a study that
selects it.

LazyMem is also relevant background for evidence-set memory. Its existence
strengthens the rationale for small learned infrastructure while narrowing any
generic novelty claim. The EBM investigator's broader user-authorized latitude
remains intact; this root phase neither directs its execution nor changes its
review boundary. Original S4, CC and ES predictions remain preserved.
