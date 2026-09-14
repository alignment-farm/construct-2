## Abstract

A research program can maintain a connected theoretical inquiry while allowing
individual studies to develop independently. We propose a simple division:
the root project explores theories, reads literature, and synthesizes evidence;
ancillary studies pursue questions and publish their findings in their own directories. Each study starts with a question, available resources, and an expectation for the work. The ancillary agent owns its methods and experimental protocols and may revise the question as understanding develops. Publications connect the projects without requiring a central operational workflow. This is a proposed organization for Construct's research, not an experimentally validated method.

## Motivation

Construct's accumulated record motivates this separation. Its
[previous research](PREVIOUS_RESEARCH.md) describes both useful findings
and instrument failures, including cases where admission rules limited contact
with the proposed phenomenon. Safeguards can protect scientific claims, but
carrying every local remedy into shared instructions risks making administration
the center of the work. Repeatedly loading the same historical interpretations
may also narrow what a new investigator considers. These are concerns motivating
the design; their effects on research quality and agent context have not been
measured here.

## The root project

This project maintains the broader direction. It develops competing explanations,
looks for relevant and emerging public research, identifies gaps, and connects
findings across projects. A question worth investigating can motivate a
study, but theory work need not always produce an experiment. Clarifying a
concept, finding an existing answer, or abandoning a weak conjecture is useful
progress.

The root reads ancillary publications as it reads other research: beginning
with the abstract, examining methods and results, and following supporting
evidence when the claim warrants it. It records its own assessment and the
implications for the broader account. Operational state, detailed protocols,
and experimental repair work remain within the ancillary study’s directory.

Independent questions can proceed concurrently. A study may reuse a published
method or result without waiting for another study's next phase. The root keeps
their distinct implications connected; investigators coordinate shared machine
use when heavy jobs or timing comparisons would interfere.

## Starting an ancillary study

A standalone research project that needs three things:

- **A question:** the uncertainty or observation motivating the investigation,
with useful background and sources.
- **Resources:** the models, tools, services, and workspace available, together
with any limits on their use.
- **An expectation:** an optional depth or effort.

A short local `AGENTS.md` describes the project's responsibility, available
resources, working boundaries, and essential research practices. The agent
begins in a fresh session in that project's directory. It reads the background
needed for its question without requiring the root's entire research history.
A prompt instruction supplies the immediate expectation; a separate
charter or orchestration system is unnecessary.

Preparing a new study includes its shared repository:

1. Create `../ancillary-studies/<study-name>/` with a question and starting
   expectation in `README.md`, local `AGENTS.md` instructions, and a `.gitignore`
   for environments, credentials, caches and model downloads. Keep evidence
   needed for the eventual claims trackable.
2. Initialize an independent Git repository on `main` and commit the preparation.
   Create the same-named repository under the `alignment-farm` GitHub organization,
   private by default unless a different visibility is requested. Set it as
   `origin` and push the initial commit with `main` tracking `origin/main`.
3. Add its `alignment-farm/<study-name>` entry to the root's
   [repository list](../studies/repos.txt) and connect the project to its question
   in the [study map](../studies/README.md). Keep completed studies in the list
   so contributors can retrieve the program's evidence as well as current work.
4. Verify the pushed branch matches the local commit and the working tree is
   clean. The prepared repository is then ready for an independent ancillary
   session; creating and pushing it does not itself launch experiments.

For a new directory with its preparation files ready, the repository step is:

```bash
study_name=$(basename "$PWD")
git init -b main
git add README.md AGENTS.md .gitignore
git commit -m "Prepare independent ancillary study"
gh repo create "alignment-farm/$study_name" --private --source . --remote origin --push
```

The [clone instructions](../studies/README.md#cloning-the-studies) use the same
repository list to retrieve all studies or a selected subset. Update that list
when a repository is added, renamed or moved; it is the maintained inventory
of Construct-2 ancillary repositories, rather than a list of every lab project.

## Autonomy

The study manages its execution, experimental protocols, implementation, analysis,
repairs, and working documentation. The initial question gives it a direction.
Discoveries may justify revising that question or pursuing another within the
stated resources and expectation.

Workload discovery can be part of bounded exploration. For a claim about
knowledge placement or repayment of learning cost, the investigator develops
a motivated workload and compares useful behavior and costs under explicit
information access. The comparison should distinguish the competing explanations;
an acquisition failure, an explicit-memory advantage, or equal performance at
lower cost can each inform the question. A treatment win is not an admission
requirement. The root assesses the question and its implications, while the
study owns workload and protocol design. A mechanism explanation may also
resolve a narrower question without a placement comparison or new experiment.

Scientific accountability remains local and inspectable. The ancillary agent
explains consequential changes in methods, preserves the evidence behind its
claims, and distinguishes exploration from subsequent tests of a developed
claim using fresh evaluation material. Failed attempts, adverse outcomes, and
limitations remain part of the record. The project chooses the detail and
procedures needed for its particular work.

**Research persistence — clarified 14 September 2026.** Acceptance of a
publication and retirement of its research question are separate decisions.
An unsuccessful treatment can reveal a limitation or distinguish explanations,
but failure of one minimally developed recipe is insufficient reason to move
on while plausible acquisition failures remain undiagnosed. In that situation,
continue bounded development within the available resources. Choose diagnostic
comparisons for the explanations their possible outcomes separate. Establishing
finite gradients or exact resets does not establish a functioning learner.
Listing possible causes or restating a recipe's failure does not meet that
explanatory expectation.

Calibration on development material is legitimate research. Preserve its
unsuccessful attempts and evaluate any resulting transfer claim on fresh
material; do not revise a completed protocol or select a checkpoint on its test
results. Closure should rest on explanatory progress, a demonstrated limitation,
or an actual resource constraint. If resources require stopping before the
question is resolved, record that constraint. This calls for more informative
experimentation, without requiring a positive treatment effect or indefinite
search for a winning configuration.

## Findings

The project README provides an abstract or short overview and points to its
supporting evidence. Code, data, saved outputs, and reproduction
instructions remain in the same directory, referenced from the README.
Revisions remain identifiable through version control.
