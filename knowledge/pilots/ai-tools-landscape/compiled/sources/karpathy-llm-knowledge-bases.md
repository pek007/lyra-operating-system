# Source Summary — Karpathy: LLM Knowledge Bases

- Source file: `../../raw/external/2026-04-03__karpathy-llm-knowledge-bases.md`
- Date compiled: 2026-04-03
- Theme: knowledge compiler / compiled wiki pattern
- Confidence: medium

## Summary
Karpathy describes a practical workflow in which raw materials are collected into a source directory and incrementally compiled by an LLM into a markdown wiki containing summaries, concepts, backlinks, and derived outputs. The system is then queried through the LLM, which produces reusable outputs such as markdown notes, slides, and visualizations. Those outputs are often filed back into the wiki, causing the knowledge base to compound over time.

## Why it matters
This source provides the anchor pattern for the pilot: treat knowledge work as a compilation process rather than a database lookup problem. It supports the idea that a useful internal system can be markdown-native, artifact-oriented, and query-enhancing without necessarily starting from heavy RAG infrastructure.

## Key ideas
- separate raw source material from the compiled wiki layer
- use the LLM to maintain summaries, concepts, and backlinks
- outputs should be durable artifacts, not just ephemeral answers
- health checks/linting can improve integrity over time
- queries should add to the system, not only consume it

## Relevance to this pilot
Direct conceptual anchor for the pilot architecture.

## Potential limits / cautions
- optimized for a personal research workflow, not necessarily a governed organizational system
- does not fully address operational truth, ownership, or governance boundaries
- may understate integrity and provenance challenges in multi-agent/shared systems

## Candidate links
- concept: `../concepts/knowledge-compiler.md`
- concept: `../concepts/output-as-asset.md`
- topic: `../topics/llm-knowledge-systems.md`
