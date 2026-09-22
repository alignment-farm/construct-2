This is the third research project in the Construct series.

```text
workspace_root=`~/Developer/Projects/alignment-farm`
0 - workspace_root/construct/notes/previous/
1 - workspace_root/construct/
2 - workspace_root/construct-2/ # you are here
```

## Research organization

The root develops theory, reads literature, and synthesizes findings. The
[studies directory](studies/README.md) owns current questions and root assessments.
Ancillary studies own their methods, protocols, evidence, and local publications,
following the [ancillary-study approach](notes/ANCILLARY_STUDY.md). Workload
discovery can be part of their bounded exploration; useful progress includes
negative results and explanations that resolve a question without new runs.

Use `gpt-6-astra` for root and ancillary research agents, including research
reviewers, until the user changes this policy. This 22 September 2026 decision
prioritizes consistency; record the actual reasoning setting and model provenance.
Models used as experimental participants, learners or teachers remain scientific
choices within each study. Include this investigator policy when preparing studies
or handing off further work; comparisons with other investigator families are deferred.

Independent ancillary questions proceed concurrently. A local acquisition or
implementation problem in one study does not block the others. The root keeps
the larger question in focus through theory, predictions and synthesis; each
study owns its experimental work and coordinates use of shared resources.

During ancillary execution, the root continues public-research discovery, theory
and selection of independent questions. As local findings sharpen a question,
check the closest public results and complementary methods before selecting
further work. Record whether they answer, narrow or redirect it. Review local
publications to judge their claims and implications; deepen evidence checks when
a material uncertainty warrants it. A study's latest follow-up receives priority
through its scientific value to the program, not merely its recency.

A negative result alone is not a stop condition. When a learning treatment has
not acquired even its development cases, pursue bounded diagnostic development
to distinguish plausible causes or establish a functioning learning regime.
Finite gradients and verified updates establish mechanics, not successful
acquisition. Accepting a publication does not close its unresolved research
question. Stop on explanatory progress, a demonstrated limitation, or a concrete
resource constraint; a neural advantage is not required. Preserve failed runs
and use fresh evaluation material to test claims developed through diagnosis.

## Research sources

Study existing public research for theories and experiments to avoid overlap and inspire new ideas.

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

## Model resources

- Dedicated Mac Studio M1 (64 GB unified memory), commissioned for model serving
  over Tailscale backed by docker model runner (preferred).
  `curl https://mac-studio-7hr7.taile71f88.ts.net/engines/v1/chat/completions ...`
  Verify gradient or mutable-state access separately before using a serving resource for a neural treatment.
- Local open-weight models with `docker model`
- OpenAI models with `codex`
- SpaceXAI models with `agent`

## Dependency management

- Use `uv` for Python package and project management.
- Use `docker` for local models and `compose`/Dockerfile(s) for complex resources, if/when needed.
