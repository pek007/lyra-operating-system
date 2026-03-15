# Security Research Sources

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Make source hierarchy explicit so Security research quality does not depend on ad hoc browsing choices.

## Source hierarchy

### Priority 1 — Internal canonical sources
Use first when understanding current posture or product impact.
- `products/security/**`
- relevant product artifacts in adjacent products when they affect security boundaries or execution surfaces
- `governance/**`
- `knowledge/evidence/**`
- `knowledge/reports/**`
- local OpenClaw docs under `docs/`

### Priority 2 — Official product and vendor sources
Use next for technical truth about capabilities, controls, and intended behavior.
- OpenClaw documentation and source-linked documentation
- vendor security docs for runtimes, models, browsers, dependencies, and hosting surfaces
- official release/change notes where behavior or exposure may have changed

### Priority 3 — Standards and primary references
Use for stable external guidance and control design framing.
- relevant standards/frameworks
- regulatory or assurance references where operationally relevant
- primary technical specifications when they materially affect our setup

### Priority 4 — High-quality security research
Use for emerging patterns, defensive techniques, and architecture implications.
- serious technical writeups
- high-signal security analysis
- incident/postmortem analysis when directly relevant to agentic or adjacent environments

### Priority 5 — Discovery channels
Use only as weak-signal discovery, never as a sole basis for doctrine.
- curated newsletters
- industry summaries
- social/media discussions

## Rule
Any finding that materially changes doctrine or product implications should be linked back into canonical Security artifacts rather than left as a source note.
