# Sandbox Governance Library

This folder contains the sandbox governance baseline derived from deep research and incident handling.

## Contents
- `deep-research-report.md` — full source report
- `SANDBOX_OPERATING_FRAMEWORK.md` — distilled operating framework
- `RUNBOOK_ENVIRONMENT_MISMATCH.md` — incident response runbook
- `PREFLIGHT_CHECKLIST.md` — fail-closed preflight baseline
- `WORKSPACE_MANIFEST.template.json` — template contract for required repos/runtime paths

## Operational scripts (repo root `tools/`)
- `tools/openclaw-env-doctor.sh` — one-command diagnostics bundle
- `tools/openclaw-preflight.sh` — fail-closed gate wrapper

### Quick usage
```bash
# Diagnostics (green/yellow/red style)
./tools/openclaw-env-doctor.sh --repo lyra-operating-system

# Fail-closed preflight for real work
./tools/openclaw-preflight.sh --repo lyra-operating-system
```

## Status
Baseline v1 created on 2026-03-04, with runnable diagnostics/preflight scripts.
