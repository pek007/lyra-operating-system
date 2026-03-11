# Canonical Repo Map v1

Status: Draft active map
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define the canonical local repo path and authority rule for active code-bearing products.

This artifact exists to prevent Git sync, rebase, and push decisions from being made against the wrong local clone.

## Operating rule
Before any Git sync action:
1. identify the intended product/repo
2. confirm the canonical local clone path below
3. confirm the active Git root matches that path
4. do not assume the workspace root is authoritative just because it is the active agent workspace

## Repo map

### Lyra Operating System / TDE
- Product(s): `A-007 Task Management` and shared Lyra OS code line
- Remote: `https://github.com/pek007/lyra-operating-system.git`
- Canonical local repo: `repos/lyra-operating-system`
- Workspace root authoritative? `No`
- Notes:
  - use this clone for TDE / Lyra OS code reconciliation, sync, rebase, and push decisions
  - workspace-root clone must not be assumed authoritative for code-lineage decisions

### Control Panel
- Product: `CP-001 Control Panel`
- Remote: `https://github.com/pek007/control-panel.git`
- Canonical local repo: `repos/control-panel`
- Workspace root authoritative? `No`
- Notes:
  - use this clone for Control Panel code work and sync decisions

## Workspace root status
- Path: `/Users/lyra/.openclaw/workspace`
- Role: global operating workspace, documentation, governance, models, memory, and shared artifacts
- Authority rule:
  - may contain a Git clone, but should not be treated as the default authoritative code clone for a product unless explicitly declared

## Review rule
Reassess this map when:
- a product gets a new repo
- canonical code location changes
- a nested clone is retired or replaced
- sync confusion or wrong-root incidents occur again

## Short rule
**Use the canonical product repo, not whichever clone you happen to be standing in.**
