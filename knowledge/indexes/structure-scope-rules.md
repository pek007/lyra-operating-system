# Structure Scope Rules (Safe Migration)

Date: 2026-03-01  
Owner: Peter + Lyra

## Purpose
Keep core runtime docs stable while organizing self-added knowledge and research artifacts.

## Frozen (do not move for now)
- Workspace bootstrap/core docs at root: `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`, `TASKS.md`.
- Any file with known automation path dependency unless a compatibility stub is left.

## Safe-to-organize now
- `knowledge/reports/` (external analysis library)
- `knowledge/indexes/` (indexes, catalogs, migration plans)
- `governance/research/` (research references and business-case material)
- New docs created by us that are not referenced by critical scripts

## Migration rule
When moving a file from a legacy location:
1. Move to canonical location.
2. Leave a stub at old path with `Moved to: <new path>`.
3. Update relevant index (e.g., `knowledge/reports/INDEX.md`).
4. Batch-update links later.
