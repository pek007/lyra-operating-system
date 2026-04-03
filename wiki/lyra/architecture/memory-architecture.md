# Memory Architecture

Status: draft wiki page
Date: 2026-04-03
Domain: Architecture

## Summary
Memory architecture describes how Lyra maintains continuity across sessions, jobs, workspaces, artifacts, and knowledge layers.

## Why it matters
Lyra cannot rely on transient chat context alone. A usable system needs explicit memory layers with different roles and authority.

## Current memory layers
- agent identity and durable guidance
- recent session continuity
- job memory and handoff artifacts
- curated long-term memory
- knowledge artifacts and compiled research layers
- coordination memory and runtime state

## Current practical understanding
Memory is already layered in Lyra OS, but different forms of memory serve different purposes:
- some guide identity and behavior
- some preserve personal continuity
- some preserve job state
- some preserve knowledge
- some preserve governance or evidence

## Key architectural distinction
Knowledge memory and operational truth are not the same thing.
Likewise, transcript memory and job continuity are not the same thing.

## Related pages
- [Knowledge Compilation](../capabilities/knowledge-compilation.md)
- [Operational Truth vs Compiled Knowledge Boundary](../governance-authority/operational-truth-vs-compiled-knowledge-boundary.md)
- [Runtime Model](./runtime-model.md)
