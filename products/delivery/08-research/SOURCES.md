# Delivery Research Sources

Status: Active
Product: Delivery (`A-006`)
Owner: Lyra
Date: 2026-03-15

## Source hierarchy

### Priority 1 — Internal canonical sources
- `products/delivery/**`
- `assemblies/devsecops-delivery/**`
- relevant adjacent product artifacts when they affect delivery constraints or interfaces
- `governance/**`
- `knowledge/evidence/**`
- `knowledge/reports/**`
- local OpenClaw docs under `docs/`

### Priority 2 — Official product and vendor sources
- OpenClaw documentation and source-linked documentation
- vendor docs for runtimes, verification tools, packaging/deployment surfaces, and hosting environments
- official release/change notes where delivery behavior or risk changed

### Priority 3 — Standards and primary references
- relevant engineering standards/frameworks
- primary technical specifications when they materially affect delivery controls or evidence expectations

### Priority 4 — High-quality engineering and reliability research
- serious technical writeups on release engineering, verification, change safety, and evidence-backed operations
- incident/postmortem analysis when directly relevant to delivery design

### Priority 5 — Discovery channels
- curated newsletters
- engineering summaries
- social/media discussions for weak-signal discovery only

## Rule
Any finding that materially changes doctrine or product implications should be linked back into canonical Delivery artifacts rather than left as a source note.
