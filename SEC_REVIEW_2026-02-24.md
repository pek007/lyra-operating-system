# SEC Review — 2026-02-24

## Scope
First baseline pass using:
- `SEC-001_BASELINE_CHECKLIST.md`
- `openclaw security audit --json`

## Summary
- Critical: 0
- Warnings: 3
- Info: 1
- Baseline status: **Partially compliant** (core controls in place; remediation required)

## Key Findings
1. `.openclaw` state directory permissions too open (`755`)  
   - Risk: local data exposure to other users on host
2. `gateway.nodes.denyCommands` has ineffective entries
   - Risk: false sense of restriction coverage
3. `gateway.trustedProxies` not configured
   - Risk: relevant only if UI is reverse-proxied (currently loopback local)
4. Manual verification pending: MFA/account access review and backup-path evidence

## Remediation Tasks
- **OPS-2026-004**: Harden state-dir permissions (`chmod 700 /Users/lyra/.openclaw`)
- **OPS-2026-005**: Clean ineffective `denyCommands` entries and re-audit
- **OPS-2026-006**: Complete MFA/access monthly review setup + backup evidence check

## Evidence
- Security audit JSON run at 2026-02-24
- Checklist updated in `SEC-001_BASELINE_CHECKLIST.md`
- Restore test evidence in `RESTORE_TEST_LOG.md` (RST-2026-001)

## Decision
Proceed with remediation tasks in normal priority order; no emergency response required.
