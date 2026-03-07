# Security — Session Starter

## Product
- Name: Security
- Product ID / Assembly IDs: A-004
- Owner Session: Security Owner — Lyra

## Scope
- Owns: Product-specific planning, execution discipline, and artifacts for security.
- Does not own: Other product internals; cross-product exceptions without interface agreement.
- Current objective: Stabilize v0.1 operating rhythm and complete verification baseline.

## Interfaces
- Upstream dependencies: Governance + Security guardrails where applicable.
- Downstream consumers: PXS operational execution.
- Required approvers: Dominant counterparty product owner for interface-impacting changes.

## Operating Cadence
- Weekly review day/time: Friday 16:00 Europe/Stockholm
- Monthly boundary review: First business week of each month

## Priority Queue (Top 3)
1. Complete and evidence one full VERIFY cycle.
2. Identify top drift/risk and add one preventive control.
3. Define pinned-lane migration plan from interim-copy.

## Evidence & Artifacts
- Primary registry/docs: ASSEMBLY_REGISTRY.md + product assembly folder
- Verification checklist: `assemblies/.../VERIFY.md`
- Change evidence location: `knowledge/evidence/` + relevant logs

## Escalation Triggers
- Authority/security-impacting changes
- Cross-product boundary exceptions
- Repeated failure pattern (>=2)
