# OpenClaw Config Change Checklist v1

## Before apply
- [ ] Change scope defined
- [ ] Risk class assigned (low/medium/high)
- [ ] Exact diff prepared
- [ ] Peter approval received (required for high risk)
- [ ] Backup created (`openclaw.json.bak-...`)
- [ ] Rollback steps prepared

## Apply
- [ ] Apply only approved diff
- [ ] Restart/reload service if required

## Validate
- [ ] `openclaw gateway status` OK
- [ ] `openclaw status --deep` reviewed
- [ ] Channel health verified
- [ ] Affected workflow tested

## If something goes wrong
- [ ] Restore backup
- [ ] Restart gateway
- [ ] Re-run validation
- [ ] Log incident and follow-up action
