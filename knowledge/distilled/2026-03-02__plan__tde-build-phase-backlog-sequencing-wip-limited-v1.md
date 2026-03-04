# TDE Build Phase Backlog Sequencing (WIP-Limited) v1

Status: Approved-for-execution baseline  
Date: 2026-03-02
Owner: JOB-PROD-001

## Objective
Sequence build work to maximize flow and reduce drift using strict WIP limits for kernel-slice execution.

## Sequencing model
1. **Now (WIP cap: 1 major item)**
   - WO-2026-TDE-KERNEL-S1 implementation
2. **Next (WIP cap: 2 queued items)**
   - Canary-readiness wiring for T7
   - Build evidence pack + closure artifact template
3. **Watch (uncommitted)**
   - Post-kernel expansion candidates (deferred)

## Rules
- Do not start a new major item while `Now` is in progress unless blocker severity is Critical.
- All work items must map to at least one acceptance test or risk-control objective.
- Any scope addition requires Product Owner re-sequencing and Architect concurrence if safety-impacting.
- Owner escalation required for reserved boundaries (major decisions, milestone gate, 3PP use, repo setup/structure changes).

## Entry criteria for Now
- Gate note approved GO
- Architecture/safety checks approved by JOB-ARC-001
- Product readiness checks approved by JOB-PROD-001

## Exit criteria for Now
- T1–T6 pass with evidence
- T7 canary-readiness hooks implemented
- Audit linkage and idempotency enforcement demonstrated

## Cadence
- Daily check: progress, blockers, risk shifts, WIP integrity.
- Milestone check: end of kernel slice -> gate packet to JOB-OWN-001 in executive format.
