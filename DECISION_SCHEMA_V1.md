# DECISION_SCHEMA_V1.md

Status: Draft v1  
Owner: Peter + Lyra  
Purpose: Canonical contract for decision-centered, role-based control panel architecture.

---

## 1) Design intent
This schema defines the **unit of management** as a Decision, not a registry row.

Primary navigation is by **Role** (Security, Finance, Operations, etc.).
Secondary grouping can be urgency, risk, due date, and status.

---

## 2) Decision object (canonical)

```yaml
Decision:
  decision_id: string                # stable ID, e.g. DEC-2026-0012
  title: string                      # short human-readable label
  question: string                   # the decision to make
  role: enum                         # Security | Finance | Operations | Product | Research | Custom
  domain: enum                       # os | px | shared
  status: enum                       # proposed | ready | blocked | approved | rejected | deferred | expired
  urgency: enum                      # low | medium | high | critical
  risk_level: enum                   # low | medium | high | critical
  decision_type: enum                # approve | reject | choose | escalate | review
  options:                           # explicit choice set
    - option_id: string
      label: string
      impact_summary: string
      estimated_cost: number|null
      estimated_risk: enum|null      # low | medium | high | critical
  recommended_option_id: string|null
  recommendation_rationale: string|null

  required_evidence:
    - evidence_id: string
      type: enum                     # security_audit | cost_report | test_result | policy_check | human_note | external_signal
      title: string
      freshness_sla_hours: number    # max allowed age
      min_confidence: number         # 0..1
      source_ref: string             # path/url/object ref

  approvals:
    required: boolean
    required_by_role: string[]       # e.g. ["Security"]
    minimum_count: number            # e.g. 1
    granted_by:                      # audit-safe list
      - actor_id: string
        actor_role: string
        at: string                   # RFC3339

  constraints:
    max_cost_tier: string|null
    allowed_write_scopes: string[]
    deadline: string|null            # RFC3339

  links:
    runbook_ref: string|null
    policy_ref: string|null
    incident_ref: string|null

  telemetry:
    created_at: string               # RFC3339
    updated_at: string               # RFC3339
    last_evidence_refresh_at: string|null
    freshness_ok: boolean
    confidence_score: number|null    # 0..1

  audit:
    created_by: string
    last_decision_by: string|null
    last_decision_at: string|null
    change_ref: string|null          # git SHA / event id
```

---

## 3) JSON Schema minimum (for validation)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://lyra.local/schemas/decision.v1.json",
  "title": "DecisionV1",
  "type": "object",
  "required": [
    "decision_id", "title", "question", "role", "domain", "status",
    "urgency", "risk_level", "decision_type", "options",
    "required_evidence", "approvals", "constraints", "telemetry", "audit"
  ],
  "properties": {
    "decision_id": { "type": "string", "pattern": "^DEC-[0-9]{4}-[0-9]{4,}$" },
    "title": { "type": "string", "minLength": 3 },
    "question": { "type": "string", "minLength": 5 },
    "role": { "enum": ["Security", "Finance", "Operations", "Product", "Research", "Custom"] },
    "domain": { "enum": ["os", "px", "shared"] },
    "status": { "enum": ["proposed", "ready", "blocked", "approved", "rejected", "deferred", "expired"] },
    "urgency": { "enum": ["low", "medium", "high", "critical"] },
    "risk_level": { "enum": ["low", "medium", "high", "critical"] },
    "decision_type": { "enum": ["approve", "reject", "choose", "escalate", "review"] },
    "options": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["option_id", "label", "impact_summary"],
        "properties": {
          "option_id": { "type": "string" },
          "label": { "type": "string" },
          "impact_summary": { "type": "string" },
          "estimated_cost": { "type": ["number", "null"] },
          "estimated_risk": { "type": ["string", "null"], "enum": ["low", "medium", "high", "critical", null] }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": true
}
```

---

## 4) API surface (v1)

- `GET /api/roles`
- `GET /api/roles/:role/decisions?status=&urgency=&risk=&domain=`
- `GET /api/decisions/:decision_id`
- `POST /api/decisions/:decision_id/recommendation:refresh`
- `POST /api/decisions/:decision_id/approve`
- `POST /api/decisions/:decision_id/reject`
- `POST /api/decisions/:decision_id/defer`
- `GET /api/decisions/:decision_id/evidence`
- `GET /api/decisions/:decision_id/audit`

Write endpoints require capability checks and approval policy enforcement.

---

## 5) Mapping from existing artifacts (transition layer)

- `TASKS.md` -> candidate decisions (question + owner + due date)
- `RISK_REGISTER.md` -> risk_level + blockers/evidence requirements
- `PROCESS_REGISTRY.md` -> runbook_ref + constraints
- evidence files -> required_evidence entries
- policy files (`skills-policy.yaml`) -> approvals + constraints

Create a translator service in transition period; do not parse legacy registries directly in UI.

---

## 6) Non-negotiables

1. Role-first navigation is primary information architecture.
2. Decision object is the canonical contract.
3. Evidence freshness and confidence must be explicit.
4. All write decisions are audited with actor/time/reason.
5. UI should never silently drop parse/contract errors.

---

## 7) Schema alignment note (2026-03-06)
- `REGISTRY_SCHEMAS_V1.md` examples are now aligned to canonical snake_case and decision enums.
- Keep this document as the canonical source for decision naming and enum contract changes.
- 2026-03-07 daily sweep: no new duplicate decision enums/term aliases detected in this document; drift remains on evidence emitter field casing (`severitySummary`/`linkedTasks`) outside this schema.
- 2026-03-08 daily sweep: no new duplicate decision enums/term aliases detected; canonical decision contract remains stable and unchanged.
- 2026-03-09 daily sweep: no new duplicate decision enums, term aliases, or cross-schema contract drift detected; canonical decision contract remains stable, with only the already-tracked external evidence-emitter casing mismatch remaining outside this document.
