# CONTROL_PANEL_VNEXT_EXECUTION_PLAN.md

Status: Proposed v1  
Owner: Peter (product + governance), Lyra (execution coordination)

## Objective
Deliver the next Control Panel phase as a **decision-support control plane** with enforceable contracts, domain isolation, and governed action paths.

## Guiding principle
Build in this order:
1. Contract integrity
2. Domain isolation
3. Decision ergonomics
4. Governed write path
5. SLO-oriented operations

---

## 1) Scope and non-goals

### In scope
- Contract alignment between OS artifacts and Control Panel schemas
- Role/domain-aware read surfaces
- Decision-first UX improvements (drill-down, freshness, provenance)
- Policy-enforced action path for high-risk changes
- CI gates, eval gates, and operational metrics

### Out of scope (for this phase)
- Full autonomous write-back without approvals
- Multi-tenant external SaaS deployment
- Complete replacement of existing views before parity

---

## 2) Phase plan (4–6 weeks)

## Phase 0 — Foundation lock (Week 1)
### Deliverables
- Canonical contract set frozen for vNext (`DecisionV1` + aligned evidence/agent/routing schemas)
- Compatibility matrix: current artifacts vs target schema
- Migration policy for enum/status differences (e.g., evidence statuses)

### Acceptance criteria
- Contract docs versioned and approved
- Fixture suite covers expected and invalid payloads
- Every known mismatch has an explicit mapping or deprecation note

### Risks
- Hidden drift in real workspace data

### Mitigation
- Use real workspace snapshot fixtures in CI

---

## Phase 1 — Contract alignment + domain isolation (Weeks 1–2)
### Deliverables
- API reads normalized through translator layer (legacy docs -> canonical schema)
- Domain-first config (`os`, `px`, optional `shared`) with separate roots
- Domain selector in API/meta responses
- Cross-domain read protection by default

### Acceptance criteria
- `GET` endpoints return domain-tagged meta and canonical schema
- Parsing succeeds for both domains with deterministic errors
- Cross-domain access attempts are denied and logged

### Risks
- Breaking existing UI assumptions

### Mitigation
- Keep legacy endpoints in compatibility mode during transition

---

## Phase 2 — Decision ergonomics (Weeks 2–3)
### Deliverables
- Role-first navigation shell (Security/Finance/Ops primary)
- Decision queue view with required fields
- One-hop drill-down to source evidence + policy + change provenance
- Freshness and confidence indicators in decision details

### Acceptance criteria
- Operator can reach source evidence from any flagged decision in <=1 click
- All decision cards display freshness state and risk/urgency
- Missing evidence/freshness blocks “ready” state deterministically

### Risks
- UI complexity creep

### Mitigation
- Strict high-signal design; no “analytics sprawl” in this phase

---

## Phase 3 — Governed write path (Weeks 3–5)
### Deliverables
- Action endpoints for `approve/reject/defer` guarded by policy checks
- Approval-card workflow for high-risk actions
- Policy Enforcement Point (PEP) implementation hook
- Structured audit records for every action (actor, reason, evidence, rollback ref)

### Acceptance criteria
- High-risk actions cannot execute without policy-valid approval path
- Denied actions are logged with reason code
- Every state-changing action emits an immutable audit event

### Risks
- Over-blocking legitimate actions

### Mitigation
- Start with monitor mode + progressive enforcement toggles

---

## Phase 4 — SLO-oriented operations + hardening (Weeks 5–6)
### Deliverables
- “Now” redesigned around 2–5 decision-critical health indicators
- Alert semantics tied to thresholds/error-budget-like burn conditions
- CI quality gates finalized (contracts/tests/security checks/evals)
- Rollback drills for schema and policy regressions

### Acceptance criteria
- “Now” is signal-dense and traces each signal to evidence path
- Alert runbook links present for each critical indicator
- Rollback tested for one contract break and one policy misconfiguration

### Risks
- Alert fatigue

### Mitigation
- Tune thresholds with weekly calibration review

---

## 3) PR and CI gate checklist

Every PR touching control-plane behavior must pass:

### A) Contract gates
- [ ] Schema validation passes
- [ ] Fixture compatibility tests pass
- [ ] Contract versioning/deprecation notes updated

### B) Code quality gates
- [ ] Lint/type checks pass
- [ ] Small deterministic tests pass
- [ ] Integration tests pass for affected paths

### C) Safety gates
- [ ] Policy checks updated/tested if action path changed
- [ ] Approval-card requirements validated for high-risk actions
- [ ] Audit event emission verified

### D) Security gates
- [ ] No new permissive network/auth regressions
- [ ] Execution path safety checks pass (no shell-injection regressions)
- [ ] Secrets handling unchanged or improved; documented if changed

### E) Evals/behavior gates (agent-impacting changes)
- [ ] Targeted eval suite passes
- [ ] Trace grading for high-risk scenarios reviewed
- [ ] Regression deltas acknowledged

---

## 4) Success scorecard

Track weekly and at phase end.

### Delivery performance (DORA-aligned)
- Deployment frequency
- Lead time for changes
- Change failure rate
- Time to restore service

### Decision efficiency
- Median time-to-decision (by role)
- % decisions with complete evidence package
- Evidence distance (interactions from signal to source evidence)

### Governance quality
- % high-risk actions with valid approval-card + audit
- Policy-deny rate (and false-positive review)
- % actions with rollback reference attached

### Flow quality
- Active WIP limit compliance
- Aging decision count
- Freshness SLA compliance for required evidence

---

## 5) RACI-lite

- **Peter**: product/governance decisions, policy exceptions, phase acceptance
- **Lyra**: plan orchestration, artifact drafting, gate tracking, evidence hygiene
- **Engineering implementation role**: schema/API/UI/policy code changes
- **Reviewer role**: final approval on high-risk changes and rollout readiness

---

## 6) Release strategy

- Trunk-based, small batch PRs
- Feature flags for new action paths
- Progressive rollout:
  1. Read-path changes first
  2. Decision UX changes
  3. Action paths in monitor mode
  4. Enforced mode after validation

Rollback rule:
- Any phase introduces hard failures -> revert to previous known-good contract version and disable affected feature flag.

---

## 7) Immediate next actions (this week)

1. Freeze vNext contracts and publish schema bundle
2. Create real-workspace fixture pack
3. Implement translator skeleton (legacy -> canonical)
4. Add domain config and API meta tagging
5. Define initial decision queue UI contract with role-first routes

---

## 8) Definition of done (vNext)

vNext is done when:
1. Contracts are aligned and enforced in CI.
2. Domain isolation is active and tested.
3. Role-first decision UX is operational with drill-down and freshness.
4. High-risk action paths are policy-enforced with approval cards and audit logs.
5. Operational dashboards are decision-oriented and linked to runbooks/evidence.
6. Rollback and restore paths are tested and documented.
