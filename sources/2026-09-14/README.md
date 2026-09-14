# Procedural learning: focused positive-demonstration reading

14 September 2026. This review supports the root's [procedural-learning theory note](../../notes/PROCEDURAL_LEARNING.md). It examines successful learning mechanisms relevant to the active acquisition question. It is a selected comparison, not a systematic review, local reproduction, or novelty claim.

| Source | Exact version and inspected scope | Use in the theory note |
|---|---|---|
| **P19. Lake and Baroni: meta-learning for compositionality** | Published *Nature* article, 25 October 2023, DOI [10.1038/s41586-023-06668-3](https://doi.org/10.1038/s41586-023-06668-3); [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/). Results, architecture, meta-training and productivity discussion. | Composition with episode evidence in context. |
| **P20. Transformers Can Do Arithmetic with the Right Embeddings** | [2405.17399v1](https://arxiv.org/html/2405.17399v1), §3 including setup and embedding/recurrence comparisons; introduction and limitations. | Representation and computation in length generalization; substantial training differs from local adaptation. |
| **P4. Self-Adapting Language Models (SEAL)** | [2506.10943v2](https://arxiv.org/html/2506.10943v2), §§3.2–4.2, Tables 1–2; revisits the existing methods review. | Learned preparation of updates; disclose task selection and the unit of success. |
| **P8. PERK: Long-Context Reasoning as Test-Time Learning** | [2507.06415v3](https://arxiv.org/html/2507.06415v3), §§3–4.1, §5.1 and Table 1; extends the existing methods review. | Adaptation trained for later use; context storage differs from learning an operation. |

Only these primary papers support the note's external empirical claims. The methods and results remain author-reported. Exact arXiv versions above are the ones read, without a latest-version claim. P19 uses the published journal article rather than an unverified arXiv version. P19/P20 extend the [paper map](../../studies/README.md#3-paper-map-what-we-can-build-on).

## Discovery and retrieval

One arXiv API title query returned HTTP 429 and no metadata results. Further API requests stopped. The [cached request and response headers](retrieval.json) and [error body](compositional-learning-query-error.txt) preserve that attempt; no Retry-After header was present. The request used a descriptive User-Agent. Full text was read through the web research tool, using existing P4/P8 citations and ordinary web title searches to locate the additional primary papers. The Nature page's direct open failed; its indexed text and the PMC copy supplied the published article. The title query also included *Show Your Work*; its discovery result was not developed into a supporting source in this note.

This reading does not cover all algorithm-learning curricula, compositionality critiques, or later follow-ups. It establishes specific positive demonstrations and their boundaries, not which is best or easiest to reproduce locally. The root did not inspect procedure-transfer's new diagnostic results or run models during this work.
