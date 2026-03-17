# Canonical Repo Map v1

Status: Active
Owner: Peter / Lyra
Date: 2026-03-11
Last updated: 2026-03-16 (v1.1 — added lifecycle status, archived repo section, pre-edit authority gate)

## Purpose
Define the canonical local repo path, lifecycle status, and authority rule for all code-bearing repos in the workspace.

This artifact exists to prevent:
- Git sync/rebase/push decisions made against the wrong local clone
- Implementation work accidentally landed in archived or reference repos
- Forward-path progress attributed to non-authoritative code surfaces

---

## Pre-edit authority gate (MANDATORY)

Before making any non-trivial code edit to a repo:

1. **Identify the intended product/repo** by name or product ID
2. **Look up its status below**: is it Active, Archived, or Reference?
3. **If Archived or Reference**: do NOT proceed with implementation. Use only for inspection, learning, or reuse extraction.
   - To land code in an archived repo, a formal restart/revival decision must be made and recorded first.
4. **If Active**: confirm the canonical local clone path and proceed
5. **If multiple Active repos exist for a domain**: confirm which surface has authority for the specific change type before editing

This gate is a response to ERR-2026-03-15-ARCHIVED-REPO-MISUSE.

---

## Active repos

### Lyra Operating System / TDE
- Product(s): `A-007 Task Management` and shared Lyra OS code line
- Lifecycle status: **Active**
- Remote: `https://github.com/pek007/lyra-operating-system.git`
- Canonical local repo: `repos/lyra-operating-system`
- Workspace root authoritative? `No` (workspace root is documentation/governance, not the canonical code clone)
- Notes:
  - use this clone for TDE / Lyra OS code reconciliation, sync, rebase, and push decisions
  - workspace-root clone must not be assumed authoritative for code-lineage decisions

---

## Archived repos (reference/reuse only — no implementation)

### Control Panel
- Product: `CP-001 Control Panel`
- Lifecycle status: **Archived** — CLOSED 2026-02-28 (Sprint 6 closeout; insufficient demonstrated value at this stage)
- Remote: `https://github.com/pek007/control-panel.git`
- Canonical local repo: `repos/control-panel`
- Permitted uses:
  - Inspect code for reuse or learning
  - Extract patterns/contracts into active surfaces
  - Reference for architecture decisions
- NOT permitted (without formal restart decision):
  - New feature implementation
  - Forward-path producer adapter development
  - Treating as an active implementation lane for any product
- Restart criteria: see `repos/control-panel/docs/PROJECT_CLOSEOUT_2026-02-28.md`
- Notes:
  - Archived label is in `repos/control-panel/README.md` (first line)
  - The code remains technically relevant — this is what makes accidental misuse easy; always verify status before editing

---

## Workspace root status
- Path: `/Users/lyra/.openclaw/workspace`
- Role: global operating workspace — documentation, governance, models, memory, and shared artifacts
- Authority rule:
  - may contain a Git clone of the operating-system repo, but should not be treated as the default authoritative code clone for any product unless explicitly declared

---

## Quick status lookup

| Repo | Status | Permitted for implementation? |
|------|--------|-------------------------------|
| `repos/lyra-operating-system` | Active | Yes |
| `repos/control-panel` | Archived | No (inspect/reuse only) |

---

## Review rule
Reassess this map when:
- A product gets a new repo
- A repo's lifecycle status changes (closure, revival, new product)
- Canonical code location changes
- A nested clone is retired or replaced
- Sync confusion or wrong-root incidents occur

---

## Short rule
**Check lifecycle status first. If Archived: look, don't touch.**

---

## Change log

| Date | Change | Driver |
|------|--------|--------|
| 2026-03-11 | v1.0 — initial canonical repo map (active-clone authority rule) | GIT_TOPOLOGY_AND_SYNC_ERROR_REPORT_2026-03-11 |
| 2026-03-16 | v1.1 — added lifecycle status, archived repo section, pre-edit authority gate | ERR-2026-03-15-ARCHIVED-REPO-MISUSE corrective action |
