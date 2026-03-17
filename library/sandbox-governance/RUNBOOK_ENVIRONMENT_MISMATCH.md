# Runbook: ENVIRONMENT_MISMATCH

## Trigger
Agent runtime cannot see expected repos/tools, or appears to be in stale/minimal sandbox context.

## 1) Diagnose (read-only first)
1. `openclaw status`
2. `openclaw sandbox explain --json`
3. `openclaw sandbox list --json`
4. Verify host paths (`~/.openclaw/workspace/repos/...`)
5. Verify in-runtime paths (`/workspace/repos/...` or configured bind targets)

## 2) Typical root causes
- `workspaceAccess: none` (minimal sandbox is expected)
- missing/incorrect binds
- stale container after config/image change
- missing Docker/toolchain in runtime
- channel/profile policy mismatch

## 3) Fix sequence
1. Backup config (`openclaw.json.bak-<timestamp>`)
2. Apply intended sandbox/workspace/bind policy
3. Recreate sandbox container(s)
4. Run preflight
5. Run security audit

## 4) Rollback
1. Restore last known-good config
2. Recreate sandbox containers
3. Re-check status and repo visibility

## 5) Exit criteria
- required repos visible where expected
- required binaries available
- no critical audit findings
- channel/session profile matches trust boundary
