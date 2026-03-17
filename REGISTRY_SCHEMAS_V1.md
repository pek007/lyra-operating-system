# REGISTRY_SCHEMAS_V1.md

## Purpose
Machine-readable schema contracts for Control Panel MVP registries.

## Format Decision
Use **YAML frontmatter in Markdown files** for human+machine readability.

## 1) Agent Contract Schema
```yaml
id: AGENT-<slug>
name: <display name>
mode: persistent|spawned|external-workbench
mission: <one-line mission>
owner: <person/role>
allowed_tools: ["web_search", "exec", "read", "write"]
read_scope: ["path/glob"]
write_scope: ["path/glob"]
approval_required_for:
  - external_send
  - destructive_change
default_model_lane: ops|research|build|premium
handoff_template: standard-v1
review:
  last_reviewed: YYYY-MM-DD
  next_review: YYYY-MM-DD
```

## 2) Routing Rule Schema
```yaml
id: ROUTE-<slug>
enabled: true
priority: 100
match:
  task_type: ["ops", "research", "build", "content"]
  risk_level: ["low", "medium", "high"]
  decision_type: ["approve", "reject", "choose", "escalate", "review"]
  data_class: ["public", "internal", "confidential"]
route:
  championModel: <model-ref>
  challengerModel: <model-ref>
  fallbackModels: [<model-ref>]
  maxCostTier: low|medium|high
  maxLatencyMs: 120000
governance:
  anti_thrash_window_days: 30
  change_gate: approval_required|normal
review:
  last_reviewed: YYYY-MM-DD
  next_review: YYYY-MM-DD
```

## 3) Evidence Record Schema
```yaml
id: EVID-<slug>
source: doctor|security_audit|restore_test|incident|review
timestamp: 2026-02-25T08:30:00+01:00
status: pass|warn|fail
severity_summary:
  critical: 0
  warn: 1
  info: 1
artifacts:
  - path: <file>
  - path: <file>
linked_tasks: ["OPS-2026-005"]
owner: Lyra
```

## 4) Change Record Schema
```yaml
id: CHG-<slug>
timestamp: 2026-02-25T09:00:00+01:00
type: policy|config|runbook|routing
summary: <what changed>
reason: <why>
decision_type: approve|reject|choose|escalate|review
owner: <who>
rollback_plan: <how to revert>
linked_artifacts:
  - path: <file>
linked_tasks:
  - OPS-2026-00X
```

## Storage Convention
- Agent contracts: `knowledge/registries/agents/*.md`
- Routing rules: `knowledge/registries/routing/*.md`
- Evidence records: `knowledge/evidence/YYYY-MM/*.md`
- Change records: `knowledge/changes/YYYY-MM/*.md`

## Version
- v1.1
- Date: 2026-03-06

## Compatibility Note
- This document now uses canonical snake_case and decision enums aligned with `DECISION_SCHEMA_V1.md`.
- Transition-layer migration guidance remains in `REGISTRY_DECISION_COMPATIBILITY_MAP_V1_1.md` for legacy artifacts.
- **Drift flag (2026-03-07):** `tools/evidence_ingest.py` still emits `severitySummary` and `linkedTasks` (camelCase), while this schema contract is `severity_summary` and `linked_tasks` (snake_case). Keep transition handling fail-closed and normalize emitter output.
- **Daily sweep (2026-03-08):** No new duplicate term aliases or enum drift detected in this schema contract; residual emitter casing drift remains open under task `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-09):** No new duplicate term aliases, enum drift, or registry-shape divergence detected in this schema contract; residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged mismatch and is already tracked under `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-10):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths, and no new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged mismatch and stays tracked under `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-11):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths, and no new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged mismatch and continues to be tracked under `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-12):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths; `knowledge/reports/INDEX.md` was regenerated and the library remains at 69 indexed report artifacts (including the weekly synthesis). No new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged mismatch and stays tracked under `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-13):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths, but one already-present report (`2026-03-12__deepresearch__best-practices-for-an-intent-to-execution-service-feeding-lyra-openclaw-tde__v1.md`) was normalized with canonical frontmatter so it now indexes correctly; `knowledge/reports/INDEX.md` was regenerated and the library now indexes 70 report artifacts (including the weekly synthesis). No new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged mismatch and stays tracked under `IMP-AUTO-20260307-03`.
- **Daily sweep (2026-03-14):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths; `knowledge/reports/INDEX.md` was regenerated and the library remains at 70 indexed report artifacts (including the weekly synthesis). No new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged cross-schema mismatch already tracked under `IMP-AUTO-20260307-03`; a separate metadata-maintenance follow-up (`IMP-AUTO-20260314-02`) was opened because 18 legacy reports still lack canonical report frontmatter fields and therefore continue to index as `source: unknown`.
- **Daily sweep (2026-03-15):** No new external-analysis ingest artifacts were found in the current workspace inbox/dropzone paths; `knowledge/reports/INDEX.md` was regenerated and the library remains at 70 indexed report artifacts (including the weekly synthesis). No new duplicate term aliases, enum drift, or registry-shape divergence were detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged cross-schema mismatch already tracked under `IMP-AUTO-20260307-03`, while legacy report-frontmatter drift remains tracked separately under `IMP-AUTO-20260314-02`.
- **Daily sweep (2026-03-16):** No new external-analysis ingest artifacts found in inbox/dropzone paths; no new inbox items pending ingest. `knowledge/reports/INDEX.md` confirmed accurate at 72 indexed report artifacts (including the weekly synthesis) — library count stable after 2026-03-15 ingestion of two new reports. No new duplicate term aliases, enum drift, or registry-shape divergence detected in this schema contract. Residual emitter casing drift (`severitySummary`/`linkedTasks` -> `severity_summary`/`linked_tasks`) remains the only flagged cross-schema mismatch, tracked under `IMP-AUTO-20260307-03`. Legacy report-frontmatter backfill (18 legacy artifacts, `source: unknown`) remains tracked under `IMP-AUTO-20260314-02`. Process-discovery dead link (`INFORMATION_MANAGEMENT_PROCESS_V1.md` missing) tracked under `IMP-AUTO-20260315-01`.
- **Daily sweep (2026-03-17):** No new external-analysis ingest artifacts found in inbox/dropzone paths, repos, or pxs library — all candidate sources checked (inbox, external-analysis-dropzone, pxs/docs library, repos/lyra-operating-system/library). `knowledge/reports/INDEX.md` confirmed accurate at 72 indexed report artifacts (including the weekly synthesis); file count in directory matches index count. No new duplicate term aliases, enum drift, or registry-shape divergence detected in this schema contract. Three open follow-ups unchanged: emitter casing drift (`IMP-AUTO-20260307-03`), legacy report-frontmatter backfill (`IMP-AUTO-20260314-02`), missing process doc (`IMP-AUTO-20260315-01`).
