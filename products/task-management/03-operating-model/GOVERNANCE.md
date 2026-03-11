# Governance

## Purpose
Define the oversight model for Task Management so the product can evolve quickly without losing control over risk, boundary discipline, or real-world consequences.

## Governance posture
Task Management should operate with medium governance intensity:
- explicit enough to support trust, readiness, and auditability
- light enough to avoid slowing routine product improvement

## Governance principles
1. Keep operational state explicit.
2. Keep interfaces and responsibilities visible.
3. Keep deployment and readiness evidence-backed.
4. Escalate material trust-boundary, strategic, or real-world-impact changes.
5. Avoid creating shadow systems outside the canonical operating substrate.

## Core governance controls
### Product-owner operating control
Task Management should use TDE as the canonical operational layer for active work, decisions, evidence, and improvement capture.

### Production readiness control
Any production-active TDE capability must pass the defined readiness gate, including runtime safety, state integrity, security/trust-boundary review, verification, and operational readiness.

### Boundary control
No hidden cross-workspace coupling. Downstream consumers should interact through explicit interfaces and documented operating expectations.

### Evidence control
Meaningful completion should produce useful evidence where appropriate, not just status claims.

## Escalation triggers
Escalate to Peter when changes involve:
- material real-world impact
- trust-boundary or access expansion
- strategic shifts in product direction
- significant dependency or deployment risk
- governance exceptions with meaningful downside

## Review model
- weekly product review for health, blockers, and improvement opportunities
- gate review when deployment/readiness decisions are involved
- milestone review when product boundaries, interfaces, or distribution shape materially change

## Key references
- `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`
- `TDE_PRODUCTION_READINESS_GATE_V1.md`
- `PRODUCT_PORTFOLIO_REGISTRY.md`
