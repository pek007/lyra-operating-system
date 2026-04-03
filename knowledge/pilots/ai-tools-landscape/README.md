# AI Tools Landscape Pilot

Status: active pilot
Date created: 2026-04-03
Owner: Lyra / PXS Tools / Lyra OS

## Purpose
This pilot tests a markdown-native knowledge-compiler workflow for AI/tool landscape and tool/architecture research relevant to PX Strategy, PXS Tools, and Lyra OS.

## Scope
The pilot should:
- ingest raw source material
- compile reusable markdown knowledge artifacts
- support better synthesis and query outputs
- compound useful knowledge over time

The pilot should not:
- replace canonical operational truth
- silently rewrite governance/decision/state artifacts
- become a grand unified knowledge platform before the workflow is proven

## Key references
- `/Users/lyra/.openclaw/workspace/KNOWLEDGE_COMPILER_ARCHITECTURE_NOTE_2026-04-03.md`
- `/Users/lyra/.openclaw/workspace/KNOWLEDGE_COMPILER_FIRST_IMPLEMENTATION_PLAN_2026-04-03.md`

## Folder model
- `raw/` — minimally transformed source material
- `compiled/` — LLM-maintained summaries, topics, concepts, syntheses, indexes
- `outputs/` — durable briefs/decks/charts generated from the pilot
- `logs/` — compile/lint run traces and notes

## Working rule
Compiled knowledge is LLM-maintained by default. Operational truth remains explicitly governed elsewhere.
