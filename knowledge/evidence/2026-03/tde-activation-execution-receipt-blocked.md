# TDE Activation Execution Receipt

- Generated at: `2026-03-02T20:44:05.294992+00:00`
- Receipt ID: `actrcpt-ed63a673241d3748`
- Linked envelope ID: `env-95c7216a98a2562b`
- Linked envelope path: `knowledge/evidence/2026-03/tde-release-envelope-blocked.json`

## Decision Trace
- Decision: **BLOCKED**
- Decision source: `BLOCKED_ESCALATION`
- Rationale: Activation blocked by deterministic fail-closed guard due to escalation.

## Guard State
- status: `blocked`
- handoffAllowed: `False`
- escalationDetected: `True`
- blockOnEscalation: `True`
- failClosed: `True`
- escalationReason: simulated:pre_authorization_guard_test

## Execution Result
- executed: `False`
- route: `hold_fail_closed`
- nextAction: Escalate evidence packet; activation remains blocked until escalation is cleared.
