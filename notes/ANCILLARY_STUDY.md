# Independent investigations in a shared research program

Ancillary study manuscript · 10 September 2026

## Abstract

A research program can maintain a connected theoretical inquiry while allowing
individual investigations to develop independently. We propose a simple division:
the root project explores theories, reads literature, and synthesizes evidence;
ancillary studies pursue questions and publish their findings locally. A human
starts each study with a question, available resources, and an expectation
for the work. The investigator owns its methods and experimental protocols and
may revise the question as understanding develops. Publications connect the
projects without requiring a central operational workflow. This is a proposed
organization for Construct's research, not an experimentally validated method.

## Motivation

The guiding image is a large research vessel exploring theories and sending
smaller ships to investigate particular questions. Each ship can discover that
its original question was incomplete, encounter a different phenomenon, or
return with evidence that changes the larger map.

Construct's accumulated record motivates this separation. Its
[research synthesis](notes/RESEARCH_BRIEF.md) describes both useful findings
and instrument failures, including cases where admission rules limited contact
with the proposed phenomenon. Safeguards can protect scientific claims, but
carrying every local remedy into shared instructions risks making administration
the center of the work. Repeatedly loading the same historical interpretations
may also narrow what a new investigator considers. These are concerns motivating
the design; their effects on research quality and agent context have not been
measured here.

## The root project

The root maintains the broader inquiry. It develops competing explanations,
looks for relevant and emerging public research, identifies gaps, and connects
findings across projects. A question worth investigating can motivate a
study, but theory work need not always produce an experiment. Clarifying a
concept, finding an existing answer, or abandoning a weak conjecture is useful
progress.

The root reads ancillary publications as it reads other research: beginning
with the abstract, examining methods and results, and following supporting
evidence when the claim warrants it. It records its own assessment and the
implications for the broader account. Operational state, detailed protocols,
and experimental repair work remain with the investigating project.

## Starting an ancillary study

A study is a standalone research project whose starting question arose
from the shared program. Its launch is human driven and needs three things:

- **A question:** the uncertainty or observation motivating the investigation,
  with useful background and sources.
- **Resources:** the models, tools, services, and workspace available, together
  with any limits on their use.
- **An expectation:** the intended depth or effort, such as “quick look,”
  “take your time and figure this out,” or “spend at most X,” with the unit of
  any cap made explicit.

A short local `AGENTS.md` describes the project's responsibility, available
resources, working boundaries, and essential research practices. The agent
begins in a fresh session in that project's directory. It reads the background
needed for its question without requiring the root's entire research history.
The human's launch instruction supplies the immediate expectation; a separate
charter or orchestration system is unnecessary by default.

## Investigative autonomy

The study manages its research direction, experimental protocols,
implementation, analysis, repairs, and working documentation. The initial
question gives it a direction. Discoveries may justify revising that question
or pursuing another within the stated resources and expectation. Work beyond
those boundaries returns to the human for direction.

Scientific accountability remains local and inspectable. The investigator
explains consequential changes in methods, preserves the evidence behind its
claims, and distinguishes exploration from subsequent tests of a developed
claim. Failed attempts, adverse outcomes, and limitations remain part of the
record. The project chooses the detail and procedures needed for its particular
work. A remedy for one experiment does not automatically become a rule for
every project.

## Local publication

Projects share findings through research manuscripts kept alongside their
supporting work. A short investigation can produce a research note; a larger
one can produce a full paper. The account explains the question, relation to
prior work, methods, observations, interpretation, and limitations. Negative
and inconclusive results are publishable outcomes within the program.

The intended publication files follow established scholarly practice:
LaTeX source, bibliography, figures as needed, and a compiled PDF. This aligns
with arXiv's preference for TeX/LaTeX and its requirement to supply source for
papers produced with it. The choice of local filenames and directory layout
belongs to the project. [arXiv submission guidance](https://info.arxiv.org/help/submit/index.html#formats-for-text-of-submission)

The project README provides an abstract or short overview and points to its
manuscripts and supporting evidence. Code, data, saved outputs, and reproduction
instructions remain in the same project, referenced from the publication.
Revisions remain identifiable through version control. Publication here means
making findings available locally; submission to an external service is a
separate human decision. This concept manuscript remains in Markdown for review.

## Limits and expectations

Separate projects can reduce the operational material needed in root sessions,
but they do not guarantee independent reasoning. Investigators may share models,
sources, assumptions, or authored tasks. Root assessments should account for
those relationships when weighing evidence.

Likewise, a polished paper does not establish a reliable result. The scientific
value lies in what its evidence supports and what remains unresolved. Manuscript
length and effort should fit the investigation, so a quick look can communicate
a useful finding without becoming a publication production exercise.

The arrangement should be judged by whether investigations produce useful,
inspectable knowledge while the root remains able to explore and revise its
theories. Its organization can evolve with that experience.

---

**A locally published research manuscript is a familiar interface between projects and root.** It can replace our custom progress/final-return machinery.

For the files, LaTeX source, references, figures, and a compiled PDF are a sensible default. arXiv prefers TeX/LaTeX and requires the source when the paper was produced with it. [arXiv submission guidance](https://info.arxiv.org/help/submit/index.html#formats-for-text-of-submission)

For example:

```text
ancillary-study/
  AGENTS.md
  README.md
  paper/
    main.tex
    references.bib
    figures/
    main.pdf
  ... project-owned code, data, and experiments
```

The manuscript explains the question, related work, methods, results, limitations, and implications. Its methods and supporting material point to the evidence within the project. The README provides a short abstract and links to the manuscript and reproduction instructions. Those filenames and that layout would be our convention, not an arXiv requirement.

Root can then read the abstract, examine the paper, and follow evidence when needed—without reconstructing the investigator’s working conversation.

I would keep the length proportional to the assignment: a “quick look” can publish a short research note; a substantial investigation can publish a full paper. Negative and inconclusive findings belong in either. **Use the scholarly publication format without making publication polish a prerequisite for sharing a useful finding.**