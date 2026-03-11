# Milestone 0.1 — Machine-checkable governance bootstrap

Date: 2026-03-04
Scope: additive governance checks only (no TDE runtime behavior changes)

## Local run

```bash
python3 tools/validate_repo.py
```

## What this validates

1. Regenerates deterministic derivatives:
   - `inventory/generated/repo_inventory.json`
   - `knowledge/indexes/inbox_index.json`
   - `knowledge/indexes/decisions_index.json`
   - `knowledge/indexes/report_decision_index.json`
   - `knowledge/indexes/observations_index.json`
   - `knowledge/indexes/indexes_manifest.json`
   - `knowledge/reports/INDEX.md`
2. Validates schema files include `$schema` and `$id`.
3. Validates evidence JSON artifacts against schema registry (`schemas/_registry.json`) when `artifactType` is present.
4. Validates decision memo frontmatter in `knowledge/decisions/`.
5. Validates decision-impacting report mapping:
   - if `decision_impact: true` in report frontmatter, report must include either `decision_id` or `no_decision_marker`.
6. Fails on generated-output drift unless run with `--fix`.

## CI behavior

Workflow: `.github/workflows/governance-machine-check.yml`

- PR/push runs `python tools/validate_repo.py`.
- Fails on schema violations and generated-drift.

## Non-disruption clause (TDE)

- This milestone intentionally does **not** modify TDE execution semantics, task mutation logic, approval gates, or job-tick runtime contracts.
- All changes are validation/indexing/policy-surface additions around existing artifacts.
