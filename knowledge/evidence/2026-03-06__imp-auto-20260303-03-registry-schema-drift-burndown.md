# IMP-AUTO-20260303-03 — Registry schema drift burn-down (2026-03-06)

## Scope
Normalize legacy camelCase registry example fields and confirm canonical decision enum alignment between:
- `REGISTRY_SCHEMAS_V1.md`
- `DECISION_SCHEMA_V1.md`

## Changes applied
Updated `REGISTRY_SCHEMAS_V1.md` example keys to canonical snake_case:
- `allowedTools` -> `allowed_tools`
- `readScope` -> `read_scope`
- `writeScope` -> `write_scope`
- `approvalRequiredFor` -> `approval_required_for`
- `defaultModelLane` -> `default_model_lane`
- `handoffTemplate` -> `handoff_template`
- `lastReviewed` / `nextReview` -> `last_reviewed` / `next_review`
- `severitySummary` -> `severity_summary`
- `linkedTasks` -> `linked_tasks`
- `rollbackPlan` -> `rollback_plan`
- `linkedArtifacts` -> `linked_artifacts`

Decision enum alignment status:
- `decision_type: approve|reject|choose|escalate|review` (aligned with `DECISION_SCHEMA_V1.md`)

## Validation
- Manual contract recheck completed against `DECISION_SCHEMA_V1.md` canonical section.
- Drift source (legacy camelCase examples in registry schema examples) removed.

## Outcome
- Residual schema-doc drift for this task is reduced from recurring to baseline-monitoring.
- Task can move to Done with this evidence artifact as closeout reference.
