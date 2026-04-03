# Topic — LLM Knowledge Systems

Status: initial topic page
Date: 2026-04-03
Confidence: medium

## Topic summary
This topic covers systems in which LLMs help ingest, structure, summarize, synthesize, query, and improve a body of knowledge over time. The current pilot is exploring one specific form of this: a markdown-native knowledge compiler with a raw layer, compiled layer, output layer, and explicit separation from governed operational truth.

## Why this topic matters
This is the umbrella topic that holds together the pilot’s core concerns:
- knowledge compilation
- artifact-oriented outputs
- retrieval and RAG tradeoffs
- provenance and integrity
- workflow vs agent design choices

## Current understanding
The current source set suggests that a useful LLM knowledge system is not simply a chatbot over documents. It is a maintained system of intermediate artifacts that improve future work. The strongest version of that idea is a system that preserves sources, compiles reusable structure, produces output artifacts, and remains auditable.

## Major subthemes
- knowledge compiler vs knowledge database
- workflow vs agent operating model
- retrieval vs RAG vs compiled knowledge
- source traceability and trust
- markdown-native intermediate representations
- linting and health checks

## Current design stance in this pilot
- compiled knowledge is primary
- retrieval is supportive
- heavier RAG is conditional
- provenance matters
- compiled knowledge should not silently replace governed operational truth

## Key open questions
- what scale threshold justifies stronger retrieval infrastructure?
- what level of provenance granularity is enough at pilot scale?
- how much of the compiled layer should be fully LLM-maintained versus more tightly controlled?

## Related sources
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)
- [Anthropic — Building Effective Agents](../sources/anthropic-building-effective-agents.md)
- [Stack Overflow Blog — Practical Tips for RAG](../sources/stackoverflow-practical-tips-for-rag.md)
- [FINOS — Citations and Source Traceability](../sources/finos-citations-and-source-traceability.md)
- [Microsoft Research — VeriTrail](../sources/microsoft-veritrail.md)

## Related concepts
- [Knowledge Compiler](../concepts/knowledge-compiler.md)
- [Workflow vs Agent](../concepts/workflow-vs-agent.md)
- [Source Traceability](../concepts/source-traceability.md)
- [Markdown as Intermediate Representation](../concepts/markdown-as-ir.md)
