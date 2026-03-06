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
