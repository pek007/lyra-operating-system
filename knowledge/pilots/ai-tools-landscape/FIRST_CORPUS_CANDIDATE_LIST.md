# First Corpus Candidate List

Pilot: AI Tools Landscape
Date: 2026-04-03
Status: draft ingestion queue

## Purpose
Define the first bounded source corpus for the AI Tools Landscape knowledge-compiler pilot.

This list is intentionally mixed:
- foundational thinking pieces
- practical workflow/tooling pieces
- architecture/system-design pieces
- integrity/provenance/linting pieces

The goal is not exhaustive coverage. The goal is to assemble a small corpus that is rich enough to test compilation, indexing, concept extraction, comparison, and synthesis.

---

## Recommended first-corpus target size
- **Minimum viable corpus:** 10 sources
- **Good first pilot corpus:** 15–20 sources
- **Upper bound for initial ingest batch:** 25 sources

---

## Bucket A — Knowledge compiler / knowledge-base pattern

### A1. Karpathy — LLM Knowledge Bases
- Status: already captured
- Why include: anchor source for the pilot pattern itself
- Path: `raw/external/2026-04-03__karpathy-llm-knowledge-bases.md`

### A2. Additional commentary / discussion on the Karpathy pattern
- Why include: helps separate core insight from implementation specifics
- Desired source type: thoughtful commentary, not hype reposts

### A3. Good piece on "wiki as compiled knowledge" or "markdown-native research system"
- Why include: triangulate the raw→compiled idea beyond one source

### A4. Strong article or post on personal/team research systems using LLMs
- Why include: compare personal knowledge workflows vs organizational knowledge workflows

---

## Bucket B — Retrieval, RAG, and alternatives

### B1. A strong practical piece on when simple retrieval/indexing beats fancy RAG
- Why include: directly relevant to our architectural stance

### B2. A strong piece on failure modes of RAG / retrieval systems
- Why include: helps define what to avoid in our first implementation

### B3. A useful explanation of context engineering vs knowledge-base engineering
- Why include: clarify boundaries between prompt/context workflows and compiled knowledge workflows

### B4. A practical article on embeddings/vector search tradeoffs
- Why include: we likely want to defer heavy RAG, but not ignore it

---

## Bucket C — Agent/tool architecture for knowledge work

### C1. Strong source on agentic research workflows
- Why include: relevant to how Lyra/Vega should traverse and extend compiled knowledge

### C2. Strong source on tool-using agents for research/synthesis
- Why include: helps design the query and file-back workflows

### C3. Strong source on notebook/wiki/search hybrid systems
- Why include: useful for output/view layer design

### C4. Strong source on markdown as an AI-native intermediate representation
- Why include: validates or challenges our markdown-first approach

---

## Bucket D — Integrity, provenance, and linting

### D1. Strong source on provenance / source traceability in AI-assisted knowledge systems
- Why include: critical for trust and governance

### D2. Strong source on knowledge-base integrity / consistency checks
- Why include: directly relevant to linting design

### D3. Strong source on hallucination control in synthesis systems
- Why include: helps define constraints for compiled knowledge generation

### D4. Strong source on stale knowledge / update discipline
- Why include: highly relevant to our recurring stale-surface issues

---

## Bucket E — Output-oriented workflows

### E1. Strong source on generating reusable knowledge artifacts instead of ephemeral answers
- Why include: aligns with our output-as-asset goal

### E2. Good example of markdown -> slides / charts / memos workflow
- Why include: supports the output layer design

### E3. Good source on filing outputs back into the knowledge system
- Why include: directly relevant to compounding behavior

---

## Bucket F — Productization / PXS Tools angle

### F1. Strong source on productizing internal knowledge workflows
- Why include: connects Lyra OS internal pilot to future PXS Tools logic

### F2. Strong source on research tooling as a product category
- Why include: useful for build-vs-product framing

### F3. Strong source on team knowledge workflows in high-signal environments
- Why include: helps move from personal workflow patterns to organizational use

---

## Recommended first ingest order

### Phase 1 — anchor corpus (first 5)
1. Karpathy source (already captured)
2. one strong retrieval/RAG tradeoff source
3. one strong provenance/integrity source
4. one strong agentic research workflow source
5. one strong output-oriented workflow source

### Phase 2 — comparison corpus (next 5)
6. second knowledge-compiler / wiki-like workflow source
7. second retrieval-failure-mode source
8. second integrity/linting source
9. markdown-as-IR or notebook/wiki hybrid source
10. productization/research-tooling source

### Phase 3 — expansion corpus (next 5–10)
Add only if the pilot is already producing meaningful compiled artifacts.

---

## Selection criteria

Prefer sources that are:
- high signal
- practical
- specific
- architecture-relevant
- grounded in real use rather than hype
- reusable for comparisons and concept extraction

Avoid sources that are:
- shallow reposts
- generic AI trend summaries
- purely promotional tool pages unless used as comparison inputs
- repetitive takes that do not add conceptual distinction

---

## Expected early compiled artifacts from this corpus

After the first 10–15 sources, the pilot should be able to produce at least:
- 10–15 source summary pages
- 3–5 topic pages
- 5–10 concept pages
- 2–4 comparison pages
- 1–3 synthesis notes

---

## Immediate next step
Select the first 5 concrete sources and ingest them into `raw/`.

Recommended starting themes:
1. knowledge compiler / wiki pattern
2. retrieval vs RAG tradeoff
3. provenance/integrity
4. agentic research workflow
5. output-oriented artifact workflow
