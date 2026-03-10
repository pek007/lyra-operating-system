# Task/Decision Engine Interface Contract v1

Date: 2026-02-28
Owner: Peter/Lyra
Status: Draft-Active

## Purpose
Define what operational state belongs in the task/decision engine vs workspace memory/docs.

## Ownership boundaries
- Operational task state -> canonical TDE runtime/task system of record
- Decision records -> decision artifacts + linked ADRs
- Identity/preferences/long-term context -> MEMORY files
- Runtime behavior rules -> AGENTS/policies
- Coordination/handoff context -> supporting artifacts/messages only; not canonical execution state

## Minimum decision record fields
- Decision ID
- Context
- Options considered
- Decision
- Rationale
- Owner
- Date
- Review trigger/date
- Linked work artifacts (WO/CA/ADR)

## Agent obligations
1. Check current canonical task/decision state before starting multi-step work.
2. Write back significant decisions and task transitions.
3. Do not treat chat transcript as authoritative operational state.
4. For durable job-shaped work, prefer job-bundle continuity over transcript continuity.
5. Use artifact-backed handoffs when work crosses lanes or requires same-runtime coordination.

## Frontier preflight rule
Before resuming TDE work, the session must first establish:
- the current canonical TDE store,
- the latest TDE frontier/active phase,
- whether the intended slice is already superseded.

If these cannot be answered confidently, implementation should fail closed into frontier reconstruction.

## Integration note
Until dedicated engine exists, maintain these fields via the current canonical TDE/runtime artifacts rather than transcript memory alone.
