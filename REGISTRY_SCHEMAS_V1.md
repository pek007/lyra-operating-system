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
allowedTools: ["web_search", "exec", "read", "write"]
readScope: ["path/glob"]
writeScope: ["path/glob"]
approvalRequiredFor:
  - external_send
  - destructive_change
defaultModelLane: ops|research|build|premium
handoffTemplate: standard-v1
review:
  lastReviewed: YYYY-MM-DD
  nextReview: YYYY-MM-DD
```

## 2) Routing Rule Schema
```yaml
id: ROUTE-<slug>
enabled: true
priority: 100
match:
  taskType: ["ops", "research", "build", "content"]
  riskLevel: ["low", "medium", "high"]
  decisionType: ["type1", "type2"]
  dataClass: ["public", "internal", "confidential"]
route:
  championModel: <model-ref>
  challengerModel: <model-ref>
  fallbackModels: [<model-ref>]
  maxCostTier: low|medium|high
  maxLatencyMs: 120000
governance:
  antiThrashWindowDays: 30
  changeGate: type1-required|normal
review:
  lastReviewed: YYYY-MM-DD
  nextReview: YYYY-MM-DD
```

## 3) Evidence Record Schema
```yaml
id: EVID-<slug>
source: doctor|security_audit|restore_test|incident|review
timestamp: 2026-02-25T08:30:00+01:00
status: pass|warn|fail
severitySummary:
  critical: 0
  warn: 1
  info: 1
artifacts:
  - path: <file>
  - path: <file>
linkedTasks: ["OPS-2026-005"]
owner: Lyra
```

## 4) Change Record Schema
```yaml
id: CHG-<slug>
timestamp: 2026-02-25T09:00:00+01:00
type: policy|config|runbook|routing
summary: <what changed>
reason: <why>
decisionType: type1|type2
owner: <who>
rollbackPlan: <how to revert>
linkedArtifacts:
  - path: <file>
linkedTasks:
  - OPS-2026-00X
```

## Storage Convention
- Agent contracts: `knowledge/registries/agents/*.md`
- Routing rules: `knowledge/registries/routing/*.md`
- Evidence records: `knowledge/evidence/YYYY-MM/*.md`
- Change records: `knowledge/changes/YYYY-MM/*.md`

## Version
- v1.0
- Date: 2026-02-25
