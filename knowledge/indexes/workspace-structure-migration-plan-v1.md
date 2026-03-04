# Workspace Structure Migration Plan v1

Status: active  
Date: 2026-03-01  
Owner: Peter + Lyra

## Implemented now
- Added skeleton directories for target taxonomy (`control/`, `registries/`, `governance/research/`, `os/*`, `integrations/*`).
- Preserved current paths (no destructive moves).
- Ingested deep research report on markdown workspace structure into `knowledge/reports/`.

## Next safe steps (recommended)
1. Define metadata frontmatter standard for non-bootstrap docs.
2. Add a link-check + registry-path validation script in `tools/`.
3. Move docs by artifact class in batches with redirect stubs.
4. Keep bootstrap files at workspace root (`AGENTS.md`, `SOUL.md`, etc.).
5. Keep `TASKS.md` compatibility until Trello sync is path-configurable.

## Guardrails
- No OpenClaw config changes as part of structure migration without config-change SOP.
- No file deletions without verified replacement path + updated links.
- Evidence path `knowledge/evidence/YYYY-MM/` remains stable.
