# TDE Phase Delegation Charter v1

Status: Active  
Date: 2026-03-02

## Mandate
`JOB-OWN-001` delegates phase-execution mandate to `JOB-PROD-001` to proceed into the next TDE phase and make operational decisions within approved scope.

## Delegated authority (JOB-PROD-001)
- Run day-to-day planning and execution for the phase
- Sequence backlog and WIP within phase boundaries
- Approve routine operational trade-offs (time/quality/scope) that do not cross reserved boundaries
- Trigger and manage standard implementation work in existing repos/processes

## Reserved authority (JOB-OWN-001 / Peter)
- Major decisions and boundary-changing choices
- Next major milestone gate decisions
- Involvement of 3PPs (Deep Research, Claude Code)
- GitHub repository setup/structure decisions

## Escalation triggers
Escalate to `JOB-OWN-001` when any reserved authority item is touched, or when risk class reaches High/Critical.

## Operating constraint
Scope remains **kernel slice only** until explicitly expanded by `JOB-OWN-001`.

## Audit
All escalations and approvals under this charter must be linked in gate/milestone notes.
