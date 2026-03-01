# Decision Memo — Task & Decision Engine (Project Definition Gate) v1

Status: Proposed for approval  
Date: 2026-03-01  
Decision Owner: Peter  
Prepared by: Lyra

## 1) Decision requested
Approve a **2–3 week Project Definition Sprint** for a Task & Decision Engine (TDE) with tightly bounded scope.

This is **not** approval to start full product build.

## 2) Why now
Multiple deep research analyses converge on the same conclusion:
- We need a durable **task + decision governance layer** more than a UI-first control panel.
- Existing artifacts already provide strong primitives (policy, schemas, decision framing, process guardrails).
- The highest risk is now **scope drift**, not feasibility.

## 3) What we are deciding
### Approve now
- Project Definition Sprint focused on one thin vertical slice:
  1. trigger/wakeup
  2. task+decision state update
  3. decision packet generation
  4. auditable decision action

### Not approving now
- Full control panel/UI build
- Full workflow-platform replacement
- Broad infra expansion beyond slice needs

## 4) Scope for the definition sprint (v1 kernel)
In scope:
- Task
- Decision
- EvidenceRecord
- ChangeRecord
- RoutingRule (task_decision only)
- Cadence checks: triage/replenishment/aging

Out of scope:
- Full read/write UI productization
- ML-based autonomous prioritization
- Multi-tenant architecture

## 5) Success criteria (go/no-go)
Go if all are true:
1. End-to-end slice works reliably under normal and retry conditions.
2. Transition/approval rules are machine-checkable and traceable.
3. Evidence + decision packet quality is usable for human sign-off.
4. Cross-links (task↔decision↔evidence↔change) are intact for sample flow.

No-go if any persists:
- repeated schema drift across core entities,
- broken traceability in normal operation,
- unresolved mutation authority/approval ambiguity.

## 6) Recommended architecture stance
Adopt **hybrid governance architecture**:
- centralized governance state + audit trail,
- decentralized execution through OpenClaw agents/tools,
- reconciliation loops for convergence.

Use OpenClaw primitives (cron, isolated runs, routing) rather than duplicating scheduler responsibilities.

## 7) Risks and mitigations
- Scope creep → lock kernel + explicit out-of-scope list.
- Retry/duplicate side effects → idempotency keys + transition guards.
- Process overhead without value → monthly audit function and keep/change/retire decisions.

## 8) 30-day output plan
Week 1: finalize contracts + authority matrix + glossary.  
Week 2: implement and test thin slice + evidence packet format.  
Week 3 (optional): hardening tests and go/no-go recommendation.

## 9) Recommendation
**Approve the Project Definition Sprint now** with the above constraints.

---

## Evidence base (selected)
- `knowledge/reports/2026-03-01__deepresearch__feasibility-study-for-a-task-and-decision-management-engine-in-lyra-openclaw__v1.md`
- `knowledge/reports/2026-03-01__deepresearch__first-version-information-model-for-the-lyra-openclaw-system__v1.md`
- `knowledge/reports/2026-03-01__deepresearch__task-and-decision-management-engine-for-lyra-openclaw-job-based-work-orchestration-and-use__v1.md`
- `knowledge/reports/2026-03-01__deepresearch__best-practices-for-task-and-decision-management-engines-for-lyra-openclaw__v1.md`
- `CONTROL_PANEL_TERMINATION_ACTION_PLAN_V1.md`
- `TASK_SYSTEM_POLICY_V1.md`
- `DECISION_SCHEMA_V1.md`
