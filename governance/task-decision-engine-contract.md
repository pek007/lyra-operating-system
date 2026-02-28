# Task/Decision Engine Interface Contract v1

Date: 2026-02-28
Owner: Peter/Lyra
Status: Draft-Active

## Purpose
Define what operational state belongs in the task/decision engine vs workspace memory/docs.

## Ownership boundaries
- Operational task state -> task engine / TASKS system of record
- Decision records -> decision artifacts + linked ADRs
- Identity/preferences/long-term context -> MEMORY files
- Runtime behavior rules -> AGENTS/policies

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
1. Check current task/decision state before starting multi-step work.
2. Write back significant decisions and task transitions.
3. Do not treat chat transcript as authoritative operational state.

## Integration note
Until dedicated engine exists, maintain these fields via existing markdown/task artifacts.
