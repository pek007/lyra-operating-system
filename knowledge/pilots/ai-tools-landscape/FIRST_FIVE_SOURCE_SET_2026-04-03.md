# First Five Source Set

Pilot: AI Tools Landscape
Date: 2026-04-03
Status: proposed first ingestion set

## Selection logic
This first five-source set is designed to cover the five key pilot themes with minimal overlap:
1. knowledge compiler / wiki pattern
2. retrieval vs RAG tradeoff
3. provenance / integrity
4. agentic research workflow
5. output-oriented artifact workflow

The goal is not to pick the final best five sources in the world.
The goal is to create a good first corpus slice that will stress the compile/index/concept/synthesis workflow.

---

## Source 1 — Anchor pattern
### Karpathy — LLM Knowledge Bases
- **Theme:** knowledge compiler / wiki pattern
- **Status:** already ingested
- **Why first:** this is the conceptual anchor for the pilot itself
- **Path:** `raw/external/2026-04-03__karpathy-llm-knowledge-bases.md`
- **Expected compiled outputs:**
  - source summary
  - concept pages for `knowledge compiler`, `compiled wiki`, `query outputs as assets`, `LLM health checks`

---

## Source 2 — Retrieval/RAG tradeoff
### A strong practical source on when simple retrieval/indexing is enough before heavy RAG
- **Theme:** retrieval vs RAG tradeoff
- **Desired source type:** practical engineering note, strong blog post, or field-tested implementation write-up
- **Why include:** we need a grounded comparison against the temptation to overbuild vector/RAG infrastructure too early
- **Selection criteria:**
  - must discuss scale, tradeoffs, and implementation simplicity
  - should not be a vendor pitch
- **Expected compiled outputs:**
  - source summary
  - comparison candidate: `compiled markdown corpus vs vector-first retrieval`
  - concept pages for `lightweight retrieval`, `RAG threshold`, `index-maintained corpus`

---

## Source 3 — Provenance/integrity
### A strong source on provenance and trust in AI-assisted knowledge systems
- **Theme:** provenance / integrity
- **Desired source type:** architecture note, research article, or practical write-up on citation, traceability, or source-grounded synthesis
- **Why include:** this is the main counterweight to uncontrolled LLM-maintained knowledge layers
- **Selection criteria:**
  - should discuss traceability, trust, or source grounding in a serious way
  - ideally useful beyond academic abstraction
- **Expected compiled outputs:**
  - source summary
  - concept pages for `source traceability`, `compiled trust`, `grounded synthesis`
  - integrity-rule candidate for the pilot

---

## Source 4 — Agentic research workflow
### A strong source on tool-using agentic research / synthesis workflows
- **Theme:** agentic research workflow
- **Desired source type:** strong practical workflow description, engineering write-up, or research-agent field note
- **Why include:** helps shape how Lyra/Vega should traverse, query, and extend the compiled layer
- **Selection criteria:**
  - should include actual workflow mechanics, not generic hype
  - should involve multi-step research/synthesis, not just chat Q&A
- **Expected compiled outputs:**
  - source summary
  - concept pages for `research agent loop`, `query-to-artifact`, `tool-augmented synthesis`
  - comparison candidate with our nightly synthesis/reporting workflows

---

## Source 5 — Output-oriented workflow
### A strong source on generating durable artifacts (briefs, slides, charts, memos) from AI-assisted research
- **Theme:** output-oriented artifact workflow
- **Desired source type:** practical workflow note or field-tested pattern
- **Why include:** one of our key design goals is that outputs should compound back into the system, not vanish as chat replies
- **Selection criteria:**
  - should emphasize reusable deliverables
  - ideally markdown/slides/chart friendly
- **Expected compiled outputs:**
  - source summary
  - concept pages for `output-as-asset`, `artifact-first answers`, `file-back workflow`
  - synthesis candidate on how output workflows affect knowledge compounding

---

## Recommendation for next action
For each of Sources 2–5:
1. select one concrete candidate source
2. ingest into `raw/external/`
3. create a compiled source summary page
4. update source/topic/concept indexes

## Important note
At this stage, **selection quality matters more than volume**.
Five strong, conceptually distinct sources are better than fifteen repetitive ones.
