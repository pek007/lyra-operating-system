# Preflight Checklist (Fail-Closed)

## Rule
If any required check fails: STOP and return `ENVIRONMENT_MISMATCH`.

## Required checks
- [ ] Docker available (if sandbox mode is on)
- [ ] `openclaw sandbox explain --json` captured
- [ ] `openclaw sandbox list --json` checked for drift
- [ ] Required host repo paths exist
- [ ] Required runtime repo paths exist
- [ ] Required binaries exist (`git`, `python3`, `jq` as needed)
- [ ] `workspaceAccess` supports intended operation
- [ ] Channel/profile trust policy passes

## After config changes affecting sandbox
- [ ] `openclaw sandbox recreate --all` (or targeted recreate)
- [ ] `openclaw security audit --deep`
- [ ] Rollback checkpoint documented
