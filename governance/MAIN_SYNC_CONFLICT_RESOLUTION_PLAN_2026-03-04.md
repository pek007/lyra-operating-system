# Main Sync Conflict-Resolution Plan — 2026-03-04

Owner: Lyra
Scope: Merge `lyra-forward-2026-03-04` into `main` without disrupting TDE progression.

## Situation summary

`main` advanced significantly with active TDE kernel work while the forward branch contains governance/bootstrap/pilot changes.
Primary conflict hotspots are shared operational files:
- `TASKS.md`
- `PROCESS_REGISTRY.md`
- `WO_TEMPLATE_V1.md`
- `CA_TEMPLATE_V1.md`
- `inventory/generated/repo_inventory.json`

## Merge strategy (safe order)

1. Use PR from `lyra-forward-2026-03-04` into `main`.
2. Resolve conflicts manually in this order:
   1) `TASKS.md`
   2) `PROCESS_REGISTRY.md`
   3) `WO_TEMPLATE_V1.md` / `CA_TEMPLATE_V1.md`
   4) generated inventory/index files
3. Run validation suite after conflict resolution.
4. Merge only when validation is green and TDE lane remains intact.

## Resolution rules by file

### 1) TASKS.md (highest risk)

Rule: keep **all active TDE tasks/state from `main` as canonical**, then append governance tasks from forward branch as additive entries.

Must preserve from `main`:
- Active/Done progression for `TDE-2026-*` series (S13–S16 chain)
- current TDE inbox items and sequencing

Must add from forward branch:
- `OPS-2026-048` closeout status
- `OPS-2026-049` closeout status
- `OPS-2026-050` pilot items (day-1 audit + outcome due)

No deletions of TDE entries allowed in conflict resolution.

### 2) PROCESS_REGISTRY.md

Rule: keep latest registry rows from `main`, then add only missing additive rows:
- `STANDARD_CHANGE_CATALOG_V1.md`
- `MILESTONE_0_1_MACHINE_CHECKABLE_GOVERNANCE.md`
- `governance/PLAN_EXECUTION_PORTFOLIO_2026-03-04.md`
- `STANDARD_CHANGE_PILOT_PROTOCOL_V1.md`

### 3) WO_TEMPLATE_V1.md and CA_TEMPLATE_V1.md

Rule: preserve any `main` template evolution; add standard-change routing fields only if absent:
- Change class
- Standard class
- Auto-promotion requested
- Exclusion trigger present

### 4) Generated files

After merge resolution, regenerate rather than manually resolve:
- `inventory/generated/repo_inventory.json`
- `knowledge/indexes/*.json`

## Validation gates before merge

Run:

```bash
python3 tools/validate_repo.py --fix
python3 tools/task_hygiene_check.py --file TASKS.md
```

Expected:
- validator pass
- no duplicate open task IDs
- standard-change policy check pass

## Post-merge checks

1. Confirm `TDE-2026-*` active chain unchanged.
2. Confirm OPS-048/049 closed and OPS-050 pilot remains active.
3. Confirm no TDE runtime scripts/contracts were modified by this merge unless explicitly intended.

## Rollback

If merge introduces TDE regression or task-state corruption:
- Revert merge commit
- Re-run validation
- reattempt with narrower commit subset (governance-only files first, generated files later)
