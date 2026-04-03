# Knowledge Compiler Architecture Note

Date: 2026-04-03
Owner: Lyra / PXS Tools / Lyra OS
Status: Draft working note

## Purpose
Translate the "LLM knowledge base" pattern into a practical architecture direction for PX Strategy, PXS Tools, and Lyra OS.

This note assumes the key design move is not "build a knowledge database" in the abstract, but to build a **knowledge compiler** that converts raw source material into durable, queryable, compounding intelligence artifacts.

---

## 1. Core design view

### Working thesis
The right mental model is:
- **raw inputs** are collected,
- an LLM-assisted pipeline **compiles** them into structured markdown-based knowledge artifacts,
- users and agents query and extend that compiled layer,
- and useful outputs are filed back into the system so the knowledge base compounds over time.

### Why this matters
A generic knowledge database easily becomes a pile of retrieved fragments.
A knowledge compiler creates:
- summaries
- concept pages
- indexes
- cross-links
- comparison artifacts
- briefing outputs
- reusable syntheses

This is a stronger architecture for strategy, research, decision support, and operating-system continuity.

---

## 2. Recommended architectural layers

### Layer A — Raw
Purpose: hold source material in minimally transformed form.

Examples:
- web articles
- PDFs / papers
- reports
- datasets
- repo snapshots / specs
- screenshots / images
- transcripts
- imported notes
- meeting artifacts

Properties:
- evidence-first
- append-friendly
- provenance-preserving
- not optimized for human reading

### Layer B — Compiled knowledge
Purpose: turn raw material into usable intelligence artifacts.

Examples:
- source summaries
- topic pages
- concept pages
- entity pages
- comparison notes
- timeline notes
- thematic synthesis notes
- index files
- backlink maps
- "what changed" pages

Properties:
- LLM-maintained by default
- markdown-native
- heavily linked
- query-oriented
- designed for reuse

### Layer C — Operational truth
Purpose: hold canonical state that governs action, accountability, and continuity.

Examples:
- decisions
- plans
- top priorities
- backlog / tasks
- risks
- error artifacts
- run ledgers
- job state
- product / BU / department state

Properties:
- explicitly governed
- source-of-truth disciplined
- not casually rewritten by an LLM
- tied to ownership and review cadence

### Layer D — Output artifacts
Purpose: hold user-facing and decision-support deliverables generated from the system.

Examples:
- memos
- briefings
- decks / slide markdown
- charts
- research packets
- executive summaries
- client-ready drafts

Properties:
- can be generated from compiled knowledge
- should often be filed back into compiled knowledge if durable

---

## 3. What the LLM should own vs not own

### Good default: LLM owns the compiled layer
The LLM is well-suited to:
- summarization
- categorization
- cross-linking
- index maintenance
- concept-page drafting
- synthesis generation
- identifying gaps / inconsistencies
- proposing new knowledge artifacts

### Do not let the LLM unilaterally own operational truth
The LLM should not silently own:
- canonical decisions
- status-of-record for critical work
- governance commitments
- final risk posture
- task completion truth
- portfolio bottleneck declarations without accountable review

### Recommended rule
- **compiled knowledge**: LLM-maintained by default
- **operational truth**: LLM-assisted, but ownership-governed

This distinction is critical for PX Strategy.

---

## 4. Why this is better than “RAG first”

At our current scale, the better order is:
1. improve canonical artifacts
2. improve indexes and summaries
3. improve folder and concept structure
4. add lightweight search / retrieval helpers
5. only then add heavier RAG/vector infrastructure if genuinely needed

### Rationale
A well-compiled markdown corpus with strong indexes and summaries can often outperform a poorly structured vector-first knowledge system.

This is especially true when the real use case is:
- synthesis
- decision support
- reusable briefing outputs
- continuity over time
- artifact-driven operating work

---

## 5. What should compound

A strong system should ensure that:
- every serious research effort leaves reusable artifacts
- every major answer improves future answers
- every synthesis can become part of the compiled layer
- every recurring question creates pressure for better indexes/pages

### Anti-pattern
Ephemeral chat answers that disappear after the immediate conversation.

### Desired pattern
Research and Q&A should produce durable artifacts that strengthen the knowledge system.

---

## 6. Knowledge “linting” / health checks

This is one of the most valuable implications.

We should run periodic LLM-assisted health checks over compiled knowledge to detect:
- stale pages
- inconsistent facts
- missing backlinks
- duplicate concepts
- conflicting summaries
- weak provenance
- uncompiled raw materials
- missing comparison pages
- missing topic indexes
- unresolved contradictions across artifacts

### For Lyra OS / PX Strategy specifically
Health checks could also detect:
- decision/evidence mismatch
- model/artifact drift
- stale operational surfaces
- unresolved boundary ambiguity
- repeated questions that indicate a missing canonical page

---

## 7. Suggested folder model

Illustrative structure only:

```text
knowledge/
  raw/
    external/
    internal/
    images/
    datasets/
  compiled/
    topics/
    concepts/
    entities/
    comparisons/
    timelines/
    syntheses/
    indexes/
  outputs/
    briefs/
    decks/
    charts/
  tools/
    ingest/
    compile/
    lint/
    search/
```

### Important boundary
This knowledge tree should not absorb canonical operational state that already belongs in product/BU/department/job artifacts.

Instead:
- operational artifacts stay where they belong
- compiled knowledge may reference or summarize them
- but should not replace them as system-of-record surfaces

---

## 8. Practical operating model

### Ingest
- collect source material into raw
- preserve provenance and source references
- prefer automation for routine ingestion

### Compile
- summarize new raw inputs
- update topic/index/concept pages incrementally
- generate comparisons and synthesis notes where useful
- add backlinks and source references

### Query
- ask questions against the compiled layer
- have the agent traverse indexes, summaries, and key source pages
- emit markdown-based artifacts rather than only chat replies

### File-back
- important query outputs should be filed back into the compiled layer or outputs layer
- repeated useful answers should become maintained artifacts

### Lint
- run periodic checks for integrity, completeness, contradictions, and stale structure

---

## 9. PXS Tools implications

This is a strong candidate domain for **PXS Tools**.

### Why
The pattern has clear internal value first:
- research acceleration
- better synthesis
- better continuity
- better decision support
- compounding organizational intelligence

And it also has clear product potential later:
- knowledge compiler for strategy/research teams
- internal-to-external productization path
- output-oriented alternative to generic RAG stacks

### Likely first internal use cases
- strategy and market research compilation
- AI/tool landscape tracking
- client/account intelligence packs
- investment/deal research notes
- operating-model knowledge maps
- research support for BU discovery loops

---

## 10. What to automate first

Recommended first moves:
1. raw ingest + provenance discipline
2. source summaries
3. canonical index generation
4. concept/topic page generation for a bounded domain
5. query-to-markdown output filing
6. linting for stale/missing/inconsistent compiled pages

### What not to over-automate yet
- automatic rewriting of operational truth surfaces
- autonomous decision closure in canonical governance artifacts
- large-scale synthetic data generation / finetuning
- grand unified knowledge graph ambitions before basics work

---

## 11. Design principles to keep

1. **Raw and compiled must remain distinct**
2. **Compiled knowledge should be artifact-first, not chat-first**
3. **Outputs should compound back into the system**
4. **Operational truth must remain governed**
5. **Retrieval should support compilation, not replace it**
6. **Health checks are part of the product, not an afterthought**
7. **Prefer lightweight markdown-native systems before heavy infrastructure**

---

## 12. Bottom line

The strongest takeaway is:

> We should think less about building a knowledge database and more about building a knowledge compiler.

For PX Strategy / Lyra OS, the best version of this idea is likely:
- markdown-native
- source-traceable
- LLM-compiled
- output-oriented
- compounding over time
- but clearly separated from governed operational truth

That architecture is likely more useful internally and more productizable externally than a generic vector-search-first knowledge stack.
