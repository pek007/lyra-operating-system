# Control Panel Capabilities

Status: Active draft v1
Owner: Lyra via Control Panel
Date: 2026-03-19

## Purpose
Make Control Panel capabilities explicit, governable, and linkable to delivery artifacts such as Skills.

## Capability records

## CP-001.C1 — Same-runtime coordination and bounded handoff orchestration
- Owning product: `CP-001` Control Panel
- Purpose: Coordinate bounded same-runtime intra-Lyra work by shaping clear handoffs, routing the next action to the right lane/session, and keeping continuity expectations explicit.
- Scope / boundary: Same-runtime coordination only. Does not replace product-lane execution, portfolio strategy judgment, cross-runtime transfer mechanisms, or canonical task/system-of-record rules.
- Primary consumers: Control Panel operating context; secondarily Lyra lanes receiving bounded handoffs.
- Delivery mode(s): `skill`, supported by protocol and product-local architecture artifacts.
- Entrypoint / interface: `skills/control-panel-coordination/`; `INTRA_LYRA_HANDOFF_PROTOCOL_V1.md`; Control Panel coordination workflows.
- Canonical artifacts:
  - `skills/control-panel-coordination/SKILL.md`
  - `skills/control-panel-coordination/references/handoff-examples.md`
  - `CONTROL_PANEL_COORDINATION_SKILL_SPEC_V1.md`
  - `SKILL_PORTFOLIO_REGISTRY.md`
- Dependencies: Intra-Lyra handoff protocol, job continuity artifacts, relevant product artifacts, session routing mechanisms.
- Constraints / guardrails: No cross-runtime handoffs via the lightweight protocol; no strategic portfolio decisions; no bypass of TDE or product system-of-record discipline.
- Readiness: `draft`
- Lifecycle state: `building`
- Evidence:
  - `SKILL_ARCHITECTURE_AUDIT_AND_PROPOSAL_V1.md`
  - validated operating pattern embodied in `CONTROL_PANEL_COORDINATION_SKILL_SPEC_V1.md`
- Known gaps / risks: Capability not yet tested as a fully governed skill; promotion criteria and representative live-run evidence still need explicit capture.
- Upgrade / retirement trigger: Upgrade when representative live runs show reduced coordination friction and correct continuity targeting; retire or replace if a stronger runtime-native orchestration mechanism supersedes skill-based handoff packaging.

## Version
- v1.0
- Date: 2026-03-19
