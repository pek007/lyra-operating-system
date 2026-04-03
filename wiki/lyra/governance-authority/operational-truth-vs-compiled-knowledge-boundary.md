# Operational Truth vs Compiled Knowledge Boundary

Status: draft wiki page
Date: 2026-04-03
Domain: Governance & Authority

## Summary
This boundary distinguishes between:
- **compiled knowledge**: reusable intelligence artifacts such as source summaries, concept pages, topic pages, syntheses, and query outputs
- **operational truth**: canonical surfaces for plans, priorities, risks, decisions, task state, and governance commitments

This distinction is one of the most important architectural rules in Lyra OS.

## Why it matters
Without this boundary:
- knowledge artifacts can quietly become a second system of record
- state and accountability become ambiguous
- generated structure can compete with explicitly governed truth
- the system becomes easier to browse but less trustworthy to operate

## What belongs in compiled knowledge
Examples:
- source summaries
- concept pages
- topic pages
- comparison pages
- synthesis notes
- reusable query outputs

## What belongs in operational truth
Examples:
- canonical plans
- top priorities
- task status of record
- formal risk posture
- governance commitments
- authoritative decision records unless explicitly designed otherwise

## Rule of use
Use compiled knowledge where raw evidence needs to become reusable intelligence artifacts.
Use operational truth where ownership, review, and canonical state must remain explicit.

Compiled knowledge may support operational truth.
It should not silently replace it.

## Current importance
This boundary is especially important as Lyra moves in the direction of a more visible compiled wiki, because a richer wiki must not be mistaken for the system of record.

## Related pages
- [Knowledge Compilation](../capabilities/knowledge-compilation.md)
- [Prompt Injection Defense](../controls-security/prompt-injection-defense.md)
