# IR-001: Incident Mini-Runbook

## Purpose
Provide a fast, repeatable response process for operational/security incidents.

## Scope
Applies to OpenClaw runtime, channels, credentials, data handling, and automation failures.

## Severity Levels
- **SEV-1 Critical:** Active data leak, account compromise, major outage, legal/reputational risk
- **SEV-2 High:** Significant functionality loss, suspected credential exposure, repeated failed automations
- **SEV-3 Medium:** Degraded service with workaround
- **SEV-4 Low:** Minor issue, low impact

## Immediate Response (First 15 Minutes)
1. **Stabilize**
   - Stop harmful activity (disable affected channel/job/tool if needed).
2. **Contain**
   - Revoke/rotate exposed credentials.
   - Isolate impacted component.
3. **Assess**
   - Classify severity.
   - Identify affected systems/data.
4. **Log**
   - Create incident entry in `INCIDENT_LOG.md`.
5. **Escalate**
   - Notify Peter immediately for SEV-1/SEV-2.

## Communication Rules
- SEV-1/SEV-2: immediate alert to Peter with:
  - What happened
  - Current impact
  - What is contained
  - Next action and ETA
- Do not speculate; state knowns/unknowns explicitly.

## Containment Playbooks (quick)
### A) Suspected credential leak
- Rotate token/key immediately
- Restart affected service
- Verify health (`openclaw status --deep`)
- Review logs for misuse window

### B) Channel outage (Telegram)
- Check channel status + logs
- Re-auth/reconfigure token if needed
- Re-run pairing if needed
- Validate with test message

### C) Data exposure risk
- Stop external messaging/actions
- Identify exposed content scope
- Remove/restrict access where possible
- Document exactly what may have been exposed

## Recovery
- Restore normal operations in controlled steps
- Verify core paths:
  - Gateway health
  - Channel health
  - Cron critical jobs
  - Task/document integrity

## Post-Incident Review (within 24–48h)
Record in incident log:
1. Root cause
2. Detection gap
3. Response timeline
4. Corrective actions
5. Preventive controls
6. Owner + due date

## Evidence Artifacts
- `INCIDENT_LOG.md`
- Relevant logs/commands used
- Any credential rotation confirmation
- Follow-up task IDs in `TASKS.md`

## Version
- v1.0
- Date: 2026-02-24
