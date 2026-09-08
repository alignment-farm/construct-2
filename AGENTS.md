This is the third research project in the Construct series.
```text
workspace_root=`~/Developer/Projects/alignment-farm/`
0 - workspace_root/construct/notes/previous/
1 - workspace_root/construct/
2 - workspace_root/construct-2/ # you are here
```

Read the [Research synthesis](notes/RESEARCH_BRIEF.md).
Read the [Research perspective](notes/TRENDS.md).

The task is to combine the synthesis with the perspective to continue agent memory research. Form theories here, then breakout empirical experiments into other projects over time.

### Research focus and division of work

- Keep this root project focused on theories, competing explanations, literature, and synthesis across the research program. Maintain the connections in the [Theory map](notes/THEORY_MAP.md).
- The user directs empirical agents in derivative projects. Derivatives own implementation, experiment execution, instrument repairs, and their evidence reports; pursue that work here only when the user explicitly redirects the task.
- Evaluate returned findings by what they change in the broader account, including what remains unresolved. A derivative's next engineering task does not automatically become the root project's next research priority.
- Keep failures and limitations visible. Distinguish evidence about the proposed mechanism from evidence about the instrument, and preserve alternative explanations.

### Model resources

- Open weight models with `docker model`
- OpenAI models with `codex`
- SpaceXAI models with `agent`

### Research sources
Look for existing public research for theories and experiments to avoid overlap and inspire new ideas.

- [arXiv.org](https://arxiv.org/) — paper discovery, full text, and metadata.

  - **Search and paper metadata:** Use `https://export.arxiv.org/api/query`
    with `search_query` (fields such as `ti:`, `au:`, `abs:`, and `cat:`, combined
    with Boolean operators) or `id_list` (comma-separated arXiv IDs). Paginate
    with `start` and `max_results`; order with `sortBy` and `sortOrder`.
    Responses are Atom 1.0 XML containing titles, authors, abstracts, categories,
    submission/update dates, and paper links. Example:
    `https://export.arxiv.org/api/query?search_query=abs:agent+AND+abs:memory&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending`.
    [API manual](https://info.arxiv.org/help/api/user-manual.html).

  - **Paper content and LaTeX source:** Retrieve PDFs at
    `https://arxiv.org/pdf/{id}` and submitted source at
    `https://arxiv.org/src/{id}`. TeX/LaTeX submissions typically download as a
    gzipped TeX file or a tar archive containing TeX and supporting files;
    PDF-only submissions do not provide LaTeX source. The query API supplies
    metadata and links; source is a separate download. Record the exact version
    read (for example, `{id}=2303.11366v1`) for reproducible citations.
    [Content access](https://info.arxiv.org/help/ir.html#step-3-copy-the-pdf-andor-source-files),
    [source unpacking](https://info.arxiv.org/help/unpack.html),
    [versioned identifiers](https://info.arxiv.org/help/arxiv_identifier_for_services.html).

  - **Bulk and incremental metadata:** Use the Open Archives Initiative
    Protocol for Metadata Harvesting (OAI-PMH 2.0) at
    `https://oaipmh.arxiv.org/oai`. This returns XML metadata, with formats
    `oai_dc` (Dublin Core), `arXiv` (structured authors, categories, and license),
    and `arXivRaw` (including version history). Each item represents the latest
    paper version. Use `Identify`, `ListMetadataFormats`, and `ListSets` for
    discovery; `GetRecord` for one item; `ListRecords` or `ListIdentifiers` for
    harvesting. Example:
    `https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:2303.11366&metadataPrefix=arXiv`.
    Filter harvests with `set` (for example, `cs:cs:AI`) and `from`/`until`.
    These dates select metadata modifications, not original submission dates.
    Continue paginated requests using only the same `verb` and the returned
    `resumptionToken`; tokens expire daily. Prefer this interface for maintaining
    a local metadata index.
    [arXiv OAI-PMH guide](https://info.arxiv.org/help/oa/index.html),
    [protocol specification](https://www.openarchives.org/OAI/openarchivesprotocol.html).

  - **Programmatic access:** Cache responses and use a descriptive `User-Agent`.
    For the query API and OAI-PMH, use one connection and at most one request
    every three seconds across clients under our control; honor `Retry-After`.
    For large PDF/source collections, use the documented bulk access options.
    [API terms and rate limits](https://info.arxiv.org/help/api/tou.html),
    [bulk data access](https://info.arxiv.org/help/bulk_data.html).

### Dependency management

- Use `uv` for Python package and project management.
- Use `docker` for local models and `compose`/Dockerfile(s) for complex resources, if/when needed.
