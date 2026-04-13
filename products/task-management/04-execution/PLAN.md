# Current Plan

## Planning horizon
Rolling near-term plan for the next 2–6 weeks.

## Current objectives
1. Keep the accepted Phase 1 Vega/PXS boundary posture explicit across compact steering surfaces and readiness language.
2. Stabilize the bounded-operational `pxs` consumption contract into a disciplined, inspectable downstream interface with an explicit machine-execution boundary and invocation rule.
3. Close the remaining substrate-to-runtime gap by wiring the producer/adapter path, forming proving-slice work into canonical runtime state, and forcing an explicit DB-cutover GO/NO-GO path.
4. Keep Task Management product boundaries explicit while downstream consumption and runtime hardening progress.

## Current workstreams
### Workstream 1: Compact current-state alignment
- refresh `PLAN.md`, `RISKS.md`, and `READINESS_SCORECARD.md` to match accepted Phase 1 posture and current evidence
- keep compact executive surfaces synchronized to canonical decisions, interface state, and readiness evidence
- reduce management-surface drift so product steering reflects current executable reality rather than older blocker framing

Current evidence anchors for this workstream:
- accepted Phase 1 boundary posture: `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` (**PASS (Phase 1)**)
- bounded-operational downstream interface: `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`
- assignment-acceptance substrate proof: `products/task-management/04-execution/TDE_ASSIGNMENT_ACCEPTANCE_TEST_EVIDENCE_2026-03-16.md` (**21/21 PASS**)
- canonical runtime projection / active TDE state: `os/runtime/TASKS_from_db.md`

### Workstream 2: Downstream interface stabilization
- tighten provider/consumer compatibility notes for the bounded `pxs` consumption path
- make the TDE machine-execution boundary explicit so it is clear what belongs in prompt-level work, executive/control-plane objects, and TDE
- define a usable invocation rule for when `pxs` should route work into TDE versus keeping it outside the execution plane
- strengthen the linking model so TDE executes against external domain objects rather than absorbing them into one blended task pool
- extend bounded handling, worked examples, and inspection clarity where needed
- accumulate evidence that `pxs` can consume the interface without hidden operator rescue

### Workstream 3: Runtime-path closure
- wire the Control Panel / producer path more tightly to canonical intake and assignment acceptance
- form the TDE self-UI experiment work into canonical DB-backed runtime state so the proving slice can reflect a real post-build runtime/state change
- make DB-cutover readiness a visible GO/NO-GO decision with evidence
- keep runtime hardening grounded in the already-verified assignment-acceptance substrate and the new self-UI proving evidence

## Immediate next steps
- refresh compact steering surfaces so they explicitly reflect: accepted Phase 1 boundary posture, bounded-operational `pxs` interface, and 21/21 assignment-acceptance evidence
- tighten `PXS_CONSUMPTION_INTERFACE.md` compatibility semantics, add an explicit boundary/invocation rule for `pxs`, and add the next bounded proof/example where inspection remains thin
- define and execute the explicit next runtime-path step from experiment-task runtime formation into DB-cutover readiness evidence
- keep Delivery’s accepted pilot contract integrated through the shared pilot flow without reintroducing mailbox-style coordination
- keep Task Management as the execution-side mapping owner for the shared As-Code Contract Pack into TDE intake classes, evidence expectations, and execution state transitions

## Added as-code rollout focus
- Task Management owns the execution-side mapping from cross-repo contracts into signal/work/decision handling
- the first bridge should stay minimal: decisions, active tasks, and evidence bundle ingest with explicit approval points for high-risk transformations
- avoid creating a separate planning layer; use product artifacts for intended structure and TDE for executable follow-through

## PxS Tools development execution integration
- treat PxS-side architecture work as input for absorbing repeated development-support execution patterns into TDE where machine execution adds reliability, continuity, and auditability
- prioritize stateful machine-execution patterns, recurring background runs, dependency/retry/handoff support, and structured execution support for repeated workflow families
- use recurring manual orchestration and operator-rescue patterns as input for TDE-side professionalization rather than leaving them outside the execution plane
- use `MINIMUM_AUTONOMOUS_DELIVERY_LOOP_V0_1_2026-04-03.md` as the target direction for shifting routine procedural progression out of chat and into workflow/execution logic
- first bounded proving case: CRM Core Slice 1 change-to-evidence loop, where TDE owns machine-execution support state around implementation/test/evidence progression without taking primary ownership of CRM feature implementation
- activation intake created: `control/tde-intake/crm-core-slice-1-change-to-evidence-pilot-2026-04-13.json`
- reference: `products/task-management/04-execution/2026-04-03_PXS_TOOLS_MACHINE_EXECUTION_INTEGRATION_NOTE.md`
- reference: `2026-04-13_DELIVERY_TDE_PXS_TOOLS_CRM_INTEGRATION_PILOT_NOTE.md`
- reference: `products/delivery/04-execution/CRM_CORE_SLICE_1_CHANGE_TO_EVIDENCE_PILOT_CONTRACT_V1.md`

## Out of scope for now
- re-litigating the accepted Phase 1 boundary as if it were still the main open blocker
- full commercialization packaging
- generalized multi-product schema enforcement
- heavy process expansion without evidence of need
