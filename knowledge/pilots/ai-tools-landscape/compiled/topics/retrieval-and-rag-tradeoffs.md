# Topic — Retrieval and RAG Tradeoffs

Status: initial topic page
Date: 2026-04-03
Confidence: medium

## Topic summary
This topic covers the relationship between retrieval, retrieval-augmented generation (RAG), and compiled knowledge. The pilot’s current stance is that retrieval is a necessary capability, RAG is a useful runtime pattern, but neither should be confused with the broader architecture of a knowledge compiler.

## Why this topic matters
This is one of the central design questions for the pilot. If we reach for heavy RAG too early, we risk building infrastructure around an under-structured corpus. If we underinvest in retrieval too long, we risk a compiled layer that is elegant but hard to navigate or verify in detail.

## Current understanding
The current source set suggests:
- simple retrieval is often enough earlier than people assume
- production-quality RAG is more demanding than it first appears
- retrieval quality depends on source cleaning, search design, prompting, evaluation, and iteration
- compiled artifacts can reduce repeated rediscovery of structure

## Major subthemes
- lightweight retrieval
- RAG as a runtime pattern
- retrieval vs compilation
- RAG threshold
- source cleaning and chunking
- retrieval evaluation

## Current design stance in this pilot
- compiled markdown knowledge is primary
- lightweight retrieval should support navigation and query work
- stronger RAG should be introduced only when current methods fail on real tasks

## Key open questions
- what concrete failure signals should trigger stronger retrieval tooling?
- how should raw-layer and compiled-layer retrieval interact?
- how much search capability can be added without overcomplicating the pilot?

## Related sources
- [Stack Overflow Blog — Practical Tips for RAG](../sources/stackoverflow-practical-tips-for-rag.md)
- [Anthropic — Building Effective Agents](../sources/anthropic-building-effective-agents.md)
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)

## Related concepts
- [Knowledge Compiler](../concepts/knowledge-compiler.md)
- [Workflow vs Agent](../concepts/workflow-vs-agent.md)
- [Markdown as Intermediate Representation](../concepts/markdown-as-ir.md)
