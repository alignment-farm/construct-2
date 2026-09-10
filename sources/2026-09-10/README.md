# Source retrieval record

Retrieved 10 September 2026 for the [initial literature review](../LITERATURE_REVIEW.md).

`arxiv-query.xml` is the unmodified Atom response from one HTTPS GET to:

```text
https://export.arxiv.org/api/query?id_list=2405.15793,2303.11366,2305.16291,2510.04618,2501.00663,2607.03441,2501.12948,2408.03314,2506.02153,2512.04123,2406.13352&max_results=11
```

User-Agent: `Construct-2 literature review (local research; arXiv metadata cache)`.
The response contains all 11 requested records, with versioned identifiers,
titles, authors, dates, abstracts, and paper links. It preserves the metadata
read without requiring another API request. Paper PDFs and source archives
were not downloaded in this pass.

The review also used browser retrieval of these primary pages:

- https://cursor.com/blog/self-summarization
- https://metr.org/notes/2026-01-22-time-horizon-limitations/
- https://distill.pub/2017/research-debt/
- https://www.cos.io/initiatives/registered-reports
- https://arxiv.org/abs/2607.03441
- https://arxiv.org/abs/2512.04123
- https://arxiv.org/html/2512.04123v4#S5.SS2

These browser responses are not archived here. The dated review preserves
paraphrased reading notes and links, rather than a reproducible snapshot of
the unversioned web essays.
