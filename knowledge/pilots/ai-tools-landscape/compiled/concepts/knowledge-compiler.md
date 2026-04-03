# Concept — Knowledge Compiler

Status: initial concept page
Date: 2026-04-03
Confidence: medium

## Working definition
A knowledge compiler is a system that transforms raw source material into structured, reusable, queryable knowledge artifacts rather than merely storing or retrieving source fragments.

## Why this concept matters
This is the central concept of the pilot. It defines the difference between:
- a passive knowledge database
- and an active system that summarizes, organizes, links, synthesizes, and compounds knowledge over time

## Core properties
- starts from raw source material
- produces compiled artifacts such as summaries, concept pages, syntheses, and indexes
- treats outputs as reusable assets
- is designed to improve future queries and synthesis, not only answer current ones
- often benefits from periodic linting and integrity checks

## In this pilot
The intended architecture is:
- raw layer
- compiled layer
- output layer
- explicit separation from governed operational truth

## Related distinctions
### Knowledge compiler vs knowledge database
A knowledge database emphasizes storage and retrieval.
A knowledge compiler emphasizes transformation, structure, synthesis, and compounding reuse.

### Knowledge compiler vs RAG system
A RAG system may retrieve source fragments into context.
A knowledge compiler may use retrieval, but its main value comes from creating durable compiled artifacts.

## Risks / cautions
- can produce markdown volume without real insight
- can drift away from source grounding if provenance is weak
- should not silently absorb operational truth that belongs in governed artifacts

## Related sources
- [Karpathy — LLM Knowledge Bases](../sources/karpathy-llm-knowledge-bases.md)
- [FINOS — Citations and Source Traceability](../sources/finos-citations-and-source-traceability.md)
