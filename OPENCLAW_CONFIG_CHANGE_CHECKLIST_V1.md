# OpenClaw Config Change Checklist v1

## Before apply
- [ ] Change scope defined
- [ ] Risk class assigned (low/medium/high)
- [ ] Exact diff prepared
- [ ] Peter approval received (required for high risk)
- [ ] Backup created (`openclaw.json.bak-...`)
- [ ] Rollback steps prepared
- [ ] If sandbox-mode change: run `python3 tools/openclaw_sandbox_preflight.py`
- [ ] If sandbox-mode change: confirm this is not the main execution lane, or an explicit change window + canary plan is approved

## Apply
- [ ] Apply only approved diff
- [ ] Restart/reload service if required

## Validate
- [ ] `openclaw gateway status` OK
- [ ] `openclaw status --deep` reviewed
- [ ] Channel health verified
- [ ] Affected workflow tested

## TDE runtime path discipline
- [ ] If this change affects TDE runtime behavior, confirm target environment (`dev`|`staging`|`prod`)
- [ ] Confirm DB/objective/binding/evidence paths are environment-scoped per `TDE_ENVIRONMENT_PATH_CONVENTION_V1.md`
- [ ] Confirm no cron-enabled environment is pointing at a shared runtime DB/path
- [ ] If this is a TDE runtime-path change, also apply `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`

## If something goes wrong
- [ ] Restore backup
- [ ] Restart gateway
- [ ] Re-run validation
- [ ] Log incident and follow-up action
