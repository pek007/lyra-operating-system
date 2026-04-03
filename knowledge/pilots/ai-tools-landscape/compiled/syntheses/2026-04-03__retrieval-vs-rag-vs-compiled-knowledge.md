# Synthesis — Retrieval vs RAG vs Compiled Knowledge

Date: 2026-04-03
Status: synthesis note
Confidence: medium

## Purpose
Clarify the relationship between simple retrieval, retrieval-augmented generation (RAG), and a compiled knowledge layer in the context of the AI Tools Landscape pilot.

## Bottom line
These three ideas should not be treated as interchangeable.

- **Retrieval** is a capability: finding relevant material.
- **RAG** is a runtime pattern: retrieving material and injecting it into the model’s working context.
- **Compiled knowledge** is an architectural layer: maintaining durable summaries, concepts, indexes, and syntheses that improve future retrieval, reasoning, and output generation.

The key conclusion for this pilot is:

> compiled knowledge should be the primary architecture, retrieval should support it, and heavier RAG should be introduced only when the compiled markdown corpus and lightweight retrieval stop being sufficient.

## 1. What retrieval is
At the simplest level, retrieval means locating relevant information from a corpus.

This might be:
- lexical search
- semantic search
- index traversal
- link traversal
- manual or agent-guided browsing through summaries and topic pages

Retrieval is not a full solution by itself.
It is one capability in a broader knowledge system.

## 2. What RAG is
RAG is a specific pattern in which a system:
1. searches a knowledge source at runtime
2. retrieves candidate chunks or passages
3. places them into the prompt/context window
4. asks the model to answer using that injected context

This is useful when:
- direct source grounding matters
- the answer needs fresh or source-specific material
- the corpus is too large or too dynamic to rely on the model alone

But strong RAG is not trivial.
The current source set suggests real RAG quality depends on:
- chunking choices
- retrieval strategy
- data cleaning
- prompt design
- evaluation
- feedback/data loops

So RAG is not merely "vector search plus LLM".
It is its own system design problem.

## 3. What compiled knowledge is
Compiled knowledge is a maintained layer of derived artifacts such as:
- source summaries
- concept pages
- topic pages
- comparison pages
- synthesis notes
- indexes

It differs from RAG because its value is not only runtime retrieval.
Its value is that it reduces the amount of structure that must be rediscovered during each query.

In other words:
- RAG retrieves source fragments into working memory
- compiled knowledge stores prior intellectual work in durable form

## 4. Why compiled knowledge should come first here
For this pilot, compiled knowledge should be primary for several reasons:

### A. Our current scale is small enough
At the current size, we do not need to jump immediately into heavy retrieval infrastructure if the corpus is well-structured.

### B. We care about reusable artifacts, not only answers
The goal is not only answering the next question correctly.
The goal is building a compounding intelligence asset.

### C. Structure matters more than recall volume right now
The current bottleneck is not lack of documents.
It is lack of:
- summaries
- concepts
- indexes
- synthesis
- traceable structure

### D. Compiled knowledge improves retrieval quality indirectly
A well-compiled corpus creates better search and navigation surfaces even before advanced RAG is added.

## 5. Where retrieval still matters immediately
Saying compiled knowledge comes first does not mean retrieval is unimportant.
It means retrieval should be introduced in proportion to actual need.

Even now, the pilot benefits from retrieval in forms such as:
- traversing source summaries
- traversing indexes
- finding related concepts
- locating candidate synthesis inputs

So retrieval is still necessary.
It is just not yet the primary architecture.

## 6. When heavier RAG becomes justified
Heavier RAG becomes justified when one or more of these conditions appear:
- the corpus grows beyond easy manual/summary-based traversal
- important source details are repeatedly missed through summary-first querying
- cross-document search quality degrades
- source freshness matters more than compiled summaries can keep up with
- query latency from manual traversal becomes too high
- high-granularity citation/support checking becomes a dominant need

At that point, compiled knowledge still remains useful.
RAG should be added to support the compiled layer, not replace it.

## 7. The right relationship between the three
The strongest architecture suggested by the current pilot is:

### Compiled knowledge = primary layer
- durable structure
- summaries
- concepts
- syntheses
- indexes

### Retrieval = supporting capability
- search across raw and compiled layers
- finding related artifacts
- helping users/agents navigate the system

### RAG = runtime augmentation pattern
- used selectively when the query requires source-grounded runtime context beyond what the compiled layer can efficiently provide

This creates a healthier design than treating RAG as the entire knowledge strategy.

## 8. Main caution
A poor knowledge system can fail in either direction:

### Failure mode A — over-RAGing too early
- too much infrastructure
- weak compiled structure
- expensive retrieval over messy content
- recurring need to rediscover the same concepts each time

### Failure mode B — over-compiling without retrieval support
- beautiful summaries and concept pages
- but hard to find exact supporting material
- weak support for fresh, detailed, source-specific questions

The right path is staged:
1. build compiled structure
2. keep retrieval lightweight and useful
3. add heavier RAG only when justified by real scale or task complexity

## 9. Working design rule for the pilot
The current pilot should operate under this rule:

- **Default:** use the compiled markdown layer first
- **Support:** use lightweight retrieval over source summaries, concept pages, and indexes
- **Escalate:** add stronger RAG patterns only when the current layer demonstrably fails on real tasks

## Open questions
- What is the first concrete threshold at which the current markdown corpus becomes insufficient without stronger retrieval tooling?
- How should raw-layer retrieval and compiled-layer retrieval be balanced?
- When should concept/synthesis artifacts be refreshed instead of relying on runtime retrieval?
- What minimal retrieval helper would materially improve this pilot without overcomplicating it?

## Related sources
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)
- [Anthropic — Building Effective Agents](../sources/anthropic-building-effective-agents.md)
- [Stack Overflow Blog — Practical Tips for RAG](../sources/stackoverflow-practical-tips-for-rag.md)
- [FINOS — Citations and Source Traceability](../sources/finos-citations-and-source-traceability.md)

## Related concepts
- [Knowledge Compiler](../concepts/knowledge-compiler.md)
- [Workflow vs Agent](../concepts/workflow-vs-agent.md)
- [Source Traceability](../concepts/source-traceability.md)
- [Markdown as Intermediate Representation](../concepts/markdown-as-ir.md)
