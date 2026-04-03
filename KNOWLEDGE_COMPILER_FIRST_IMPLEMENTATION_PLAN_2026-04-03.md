# Knowledge Compiler — First Implementation Plan for Lyra OS

Date: 2026-04-03
Owner: Lyra / PXS Tools / Lyra OS
Status: Draft working implementation plan

Links:
- `./KNOWLEDGE_COMPILER_ARCHITECTURE_NOTE_2026-04-03.md`

## Purpose
Define the first practical implementation slice of a knowledge-compiler system inside Lyra OS.

This plan is intentionally narrow. The goal is not to build a grand unified knowledge platform immediately, but to prove a useful internal pattern that:
- ingests raw research/source material,
- compiles it into durable markdown-based knowledge artifacts,
- supports higher-quality query/synthesis,
- compounds over time,
- and preserves the boundary between compiled knowledge and governed operational truth.

---

## 1. Implementation objective

### Primary objective
Stand up the first bounded knowledge-compiler workflow for one internal research/problem domain inside Lyra OS.

### What success looks like
- raw materials are collected into a consistent source layer
- an LLM-assisted compile pass produces structured markdown artifacts
- a human or agent can ask meaningful questions against the compiled layer
- the answers produce reusable artifacts, not just ephemeral chat replies
- the process improves continuity and signal quality relative to ad hoc chat-based research

### What this is not yet
- not a full product
- not a full knowledge graph
- not a fine-tuned model pipeline
- not a replacement for canonical operational artifacts

---

## 2. Recommended first pilot scope

### Recommended pilot domain
**AI/tool landscape and operating-model research relevant to PX Strategy / PXS Tools**

### Why this domain
It is a strong first pilot because it is:
- high-value
- recurring
- research-heavy
- synthesis-heavy
- not too operationally dangerous
- likely to benefit from compounding summaries, comparisons, and concept pages

### Alternative pilot candidates
- strategy / market mapping
- investment/deal research
- client/account intelligence
- operating-model / governance concept library

### Recommendation
Start with **AI/tool landscape + tool/architecture research** because it is already active, likely to recur, and naturally aligned with PXS Tools.

---

## 3. First implementation slice

### Slice definition
Build a minimal but complete flow:

1. **Ingest** raw source documents into a bounded research area
2. **Compile** source summaries and concept/topic pages
3. **Index** the compiled layer with lightweight markdown indexes
4. **Query** the compiled layer through the agent
5. **File back** useful outputs into the compiled knowledge space
6. **Lint** the space for obvious integrity/staleness issues

This is enough to validate the model without overbuilding.

---

## 4. Proposed folder structure for the pilot

```text
knowledge/
  pilots/
    ai-tools-landscape/
      raw/
        external/
        internal/
        images/
      compiled/
        sources/
        topics/
        concepts/
        comparisons/
        syntheses/
        indexes/
      outputs/
        briefs/
        decks/
        charts/
      logs/
        compile-runs/
        lint-runs/
```

### Notes
- `raw/` is evidence-first, minimally transformed
- `compiled/` is LLM-maintained and queryable
- `outputs/` contains user-facing deliverables worth keeping
- `logs/` helps trace what compile/lint passes changed

---

## 5. Artifact types to support first

### Raw artifacts
- clipped articles in markdown
- copied notes/reports in markdown
- PDFs converted into markdown/text when practical
- image references where important

### Compiled artifacts
- `sources/<slug>.md` — source summary pages
- `topics/<slug>.md` — topic pages
- `concepts/<slug>.md` — concept definitions and recurring ideas
- `comparisons/<slug>.md` — side-by-side comparisons
- `syntheses/<date>-<slug>.md` — periodic synthesis notes
- `indexes/INDEX.md` — top-level browse/index surface
- `indexes/TOPICS.md`, `indexes/SOURCES.md`, etc.

### Output artifacts
- executive brief markdown
- internal memo markdown
- decision-support note
- slide markdown (e.g. Marp) when useful

---

## 6. Operating rules

### Rule 1 — Keep raw and compiled separate
The compile pass should not overwrite raw source material.

### Rule 2 — Preserve provenance
Compiled artifacts should link back to source materials.

### Rule 3 — LLM owns compiled layer by default
The agent may create/update summaries, concept pages, indexes, comparisons, and syntheses.

### Rule 4 — Do not silently rewrite operational truth
The pilot knowledge compiler must not silently edit canonical plans, priorities, decisions, or governance artifacts as part of compilation.

### Rule 5 — Query outputs should compound
If a query produces a useful durable insight, file it back into the compiled layer or outputs layer.

### Rule 6 — Lightweight first
Prefer markdown conventions, simple indexes, and explicit compilation routines before introducing heavier infrastructure.

---

## 7. First workflows to implement

### Workflow A — Ingest
Human or agent places new source materials into `raw/`.

Minimum requirements:
- stable file naming
- source URL/reference where applicable
- source date if known
- origin type (article, repo, paper, note, etc.)

### Workflow B — Compile new source summaries
For each new raw artifact:
- generate a concise source summary page
- extract main ideas / claims / relevance
- identify candidate topic/concept links
- update source and topic indexes

### Workflow C — Topic/concept compilation
Across multiple source summaries:
- identify recurring concepts
- draft/update concept pages
- draft/update topic pages
- create backlinks and "related pages"

### Workflow D — Query to artifact
When a user asks a serious question:
- traverse compiled pages and relevant raw sources
- create a reusable markdown answer artifact
- optionally store it in `outputs/` or `compiled/syntheses/`

### Workflow E — Lint / health check
Periodic pass to identify:
- missing source summaries
- broken/missing backlinks
- duplicate concept pages
- stale syntheses
- weakly linked source pages
- missing comparison opportunities

---

## 8. What to automate first

### Phase 1 automation
1. ingest conventions and folder structure
2. source-summary generation
3. index regeneration/update
4. topic/concept suggestion
5. output filing for major answers
6. basic lint pass

### Phase 2 automation
1. comparison-page generation
2. synthesis-page generation from multiple sources
3. image-aware compilation where important
4. local lightweight search helper over compiled layer

### Defer for later
- embeddings/vector DB as the center of the design
- synthetic dataset generation
- finetuning against the corpus
- broad autonomous rewrite loops across the whole knowledge tree

---

## 9. Suggested first success metrics

### Quality metrics
- percentage of raw sources with compiled summaries
- percentage of compiled pages with source links
- number of reusable output artifacts produced from the pilot
- reduction in repeated re-research on the same topic
- subjective signal quality of answers vs previous ad hoc workflow

### Integrity metrics
- unresolved duplicate concept count
- orphaned source pages
- stale index count
- missing-link findings from lint pass

### Practical outcome metrics
- time to answer a recurring research question
- quality of briefing/memo output
- number of outputs worth filing back into the system

---

## 10. First implementation steps

### Step 1 — Create the pilot directory structure
Set up the bounded research pilot under `knowledge/pilots/ai-tools-landscape/`.

### Step 2 — Add the first raw corpus
Ingest a small but meaningful batch, e.g. 10–25 source items.

### Step 3 — Compile source summaries
Generate source summary pages for the initial corpus.

### Step 4 — Build first indexes
Create at minimum:
- source index
- topic index
- concept index

### Step 5 — Compile first topic/concept pages
Identify the top recurring themes and generate a first concept/topic layer.

### Step 6 — Run first real query cycle
Use the compiled layer to answer 3–5 meaningful internal questions and file the outputs back into the system.

### Step 7 — Run first lint pass
Identify missing summaries, weak links, duplicate concepts, and improvement candidates.

### Step 8 — Review the pilot
Assess whether the system is actually compounding useful knowledge or just producing more markdown.

---

## 11. Risks and watchpoints

### Risk 1 — Markdown bloat without real knowledge gain
Mitigation: judge success by usefulness and reuse, not page count.

### Risk 2 — LLM-generated artifacts become ungrounded
Mitigation: require provenance links and explicit source traceability.

### Risk 3 — Compiled knowledge drifts into operational truth
Mitigation: keep operational source-of-truth surfaces outside the compile loop.

### Risk 4 — Overengineering too early
Mitigation: keep the first pilot bounded and markdown-native.

### Risk 5 — Compiled layer becomes stale
Mitigation: include a lint/refresh workflow from the beginning.

---

## 12. Decision recommendation

### Recommended decision
Proceed with a bounded Lyra OS pilot for a markdown-native knowledge compiler focused on AI/tool landscape research.

### Why
This is the smallest meaningful implementation that can test whether the knowledge-compiler architecture actually creates compounding value for PX Strategy and PXS Tools.

### Decision trigger for next stage
If the pilot produces clearly better reusable research artifacts, faster recurring-question handling, and better synthesis quality, then move to:
- broader internal rollout, and/or
- a formal PXS Tools product concept note.

---

## Bottom line

The first implementation should be:
- narrow
- source-traceable
- markdown-native
- artifact-oriented
- LLM-compiled
- and explicitly separate from governed operational truth.

If that works, we will have evidence for both a stronger internal knowledge system and a credible future PXS Tools product direction.
