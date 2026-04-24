# Canonical Repo Map v1

Status: Active
Owner: Peter / Lyra
Date: 2026-03-11
Last updated: 2026-04-24 (v1.2 — re-pointed `lyra-operating-system` authority to workspace root, added `pxs` + `pxs-crm`, and downgraded nested Lyra clone to legacy local status)

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

### Lyra Operating System / workspace root
- Product(s): shared Lyra OS operating workspace, governance/model/docs line, and the currently active `lyra-operating-system` mainline
- Lifecycle status: **Active**
- Remote: `https://github.com/pek007/lyra-operating-system.git`
- Canonical local repo: `/Users/lyra/.openclaw/workspace`
- Workspace root authoritative? `Yes`
- Notes:
  - use this clone for `lyra-operating-system` fetch / status / sync / rebase / push decisions unless a later explicit decision changes repo authority
  - current operating reality is that the workspace root is the maintained and pushed mainline for this remote
  - do not assume the nested clone under `repos/lyra-operating-system` is authoritative

### PXS
- Product(s): `PX Strategy` operating repo
- Lifecycle status: **Active**
- Remote: `https://github.com/pek007/pxs.git`
- Canonical local repo: `/Users/lyra/.openclaw/workspace-px-internal-dev/pxs`
- Notes:
  - use this clone for `pxs` fetch / status / sync / push decisions
  - keep local nightly/report work bounded so committed history reaches GitHub in small increments

### PXS CRM
- Product(s): `PXS CRM`
- Lifecycle status: **Active**
- Remote: `https://github.com/pek007/pxs-crm.git`
- Canonical local repo: `/Users/lyra/.openclaw/workspace-px-internal-dev/pxs-crm`
- Notes:
  - use this clone for `pxs-crm` fetch / status / sync / push decisions
  - current baseline is clean and synced; preserve that as the standard

### Lyra Operating System nested clone
- Product(s): legacy/local secondary clone of `lyra-operating-system`
- Lifecycle status: **Legacy local clone — non-authoritative**
- Remote: `https://github.com/pek007/lyra-operating-system.git`
- Local repo: `/Users/lyra/.openclaw/workspace/repos/lyra-operating-system`
- Permitted uses:
  - inspect divergence
  - extract reusable code or notes intentionally
  - reconcile or retire the clone under an explicit cleanup step
- NOT permitted:
  - treat as the default source for sync / rebase / push decisions
  - assume its local divergence represents the current authoritative repo state
- Notes:
  - this clone is materially divergent from the active mainline and should be reconciled or retired rather than silently used

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
- Role: global operating workspace — documentation, governance, models, memory, shared artifacts, and the current authoritative local clone for the `lyra-operating-system` remote
- Authority rule:
  - for the `lyra-operating-system` remote, this workspace root is the default authoritative clone unless a later explicit decision changes it
  - for other repos, defer to the canonical local repo listed above

---

## Quick status lookup

| Repo | Status | Permitted for implementation? |
|------|--------|-------------------------------|
| `/Users/lyra/.openclaw/workspace` | Active | Yes |
| `/Users/lyra/.openclaw/workspace-px-internal-dev/pxs` | Active | Yes |
| `/Users/lyra/.openclaw/workspace-px-internal-dev/pxs-crm` | Active | Yes |
| `/Users/lyra/.openclaw/workspace/repos/lyra-operating-system` | Legacy local clone | No (inspect/reconcile only) |
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
| 2026-04-24 | v1.2 — re-pointed `lyra-operating-system` authority to workspace root, added `pxs` + `pxs-crm`, and downgraded nested Lyra clone to legacy local status | GitHub hygiene + repo-authority reconciliation |
