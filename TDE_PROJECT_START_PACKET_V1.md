# TDE Project Start Packet v1.0

## 1) Product Goal (Why)
Establish a Task & Decision Engine (TDE) definition baseline that enables continuous, policy-governed operation in Lyra without human micro-management, while integrating natively with OpenClaw and enabling Trello retirement.

**Vision addendum:** Build the capability to autonomously pursue high-level goals.

## 2) Top 3 Decision Use-Cases
1. Should a task transition be allowed now (DoR/DoD, authority, risk gates)?
2. Which items require escalation/approval vs autonomous execution?
3. Is the system converging toward high-level goals or drifting (WIP/aging/blocker control), including anti-stall auto-follow-up so no important item remains indefinitely stuck?

## 3) Explicit Non-Goals
- Full UI-first control panel rebuild in this phase.
- Replacing OpenClaw scheduler/session/routing primitives.
- ML-dependent prioritization as a prerequisite for governance correctness.

## 4) Success Metrics
- Metric: Thin-slice governance flow completeness
  - Baseline: Not implemented end-to-end
  - Target: Trigger → evaluate → decision packet → approval gate → idempotent action → audit link implemented and testable
  - Time window: 2026-03-02 to 2026-03-20

- Metric: Contract stability
  - Baseline: Partial drift risk across task/decision/evidence semantics
  - Target: Stable canonical definitions for Task, Decision, EvidenceRecord, ChangeRecord, Action/Approval with explicit ownership
  - Time window: 2026-03-02 to 2026-03-20

- Metric: Trello retirement readiness
  - Baseline: Trello still operational dependency
  - Target: Documented migration + cutover conditions + Trello-free steady-state definition
  - Time window: 2026-03-02 to 2026-03-20

## 5) Kill Criteria
- Core entity semantics continue drifting without compatibility strategy.
- Mutation authority remains ambiguous.
- No safe idempotent contract for side-effecting actions can be specified.
- Trello cutover remains undefined.

## 6) Boundary Summary
- System of record: TDE governance state (Task/Decision/Evidence/Change/Action-Approval contracts)
- Derived view scope: role views, now/next/watch queues, decision packet outputs, optional Trello projection during migration
- Out of scope: full platform replacement, broad UI productization, unrelated infrastructure expansion

## 7) First MVP (Decision-first)
- Artifact/report/job to ship first: Daily decision-control packet for active high-priority items with evidence freshness, blockers, approvals, and recommended actions
- Cadence: Daily
- Freshness requirement: <=24h for evidence and queue status

## 8) Acceptance for Sprint 1
- Start Packet approved.
- Prioritized use-case set complete and mapped to objectives.
- Information architecture baseline complete (canonical objects + IDs + ownership).
- Architecture baseline complete (C4-style diagrams + OpenClaw integration map).
- Trello retirement design complete (migration + cutover + steady state).

## Approval
- Approver: Peter
- Date: 2026-03-01
