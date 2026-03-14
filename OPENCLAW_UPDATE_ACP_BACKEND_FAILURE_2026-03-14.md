# OpenClaw Update ACP Backend Failure — 2026-03-14

## Header
- Error ID: ERR-2026-03-14-OPENCLAW-ACP-BACKEND
- Date: 2026-03-14
- Title: ACP smoke test failed after OpenClaw update because ACP runtime backend is not configured
- Type: control_failure
- Scope: system_level
- Owning product or owner: Lyra OS / OpenClaw runtime operations
- Affected products/contexts: main runtime, OpenClaw update workflow, ACP/Codex smoke-test path
- Status: open
- Review / closure date: 2026-03-15

## Summary
OpenClaw was updated successfully to the latest available version (`2026.3.13`), but the required post-update ACP/Codex smoke test did not pass.

The attempted ACP smoke run failed with:
- `ACP runtime backend is not configured. Install and enable the acpx runtime plugin.`

This means the update is installed, memory search is healthy, and gateway connectivity is back, but the update cannot yet be treated as operationally complete under the post-update smoke-test standard.

## Impact
- Actual impact:
  - ACP smoke test failed.
  - ACP/Codex path is not currently verified as operational after update.
  - Update completion remains partial/pending.

- Potential impact:
  - ACP-dependent workflows may fail when invoked.
  - Future updates could silently degrade ACP capability unless the smoke-test path catches it.

## Detection
- How was it detected?
  - During formal post-update smoke testing after `openclaw update`.
  - Memory search passed.
  - Gateway probe succeeded with limited scope.
  - ACP smoke failed immediately with a backend-not-configured error.

- Detection gap, if any:
  - The update flow did not guarantee ACP backend availability or make the missing plugin obvious before smoke testing.

## Root cause
- Primary root cause:
  - ACP runtime backend (`acpx`) is not configured/enabled in the current runtime after the update path.

- Contributing factors:
  - No default ACP agent was configured, which initially obscured the true issue.
  - The OpenClaw update path can succeed at package-install level while leaving critical optional/runtime-path dependencies unavailable.
  - ACP capability depends on runtime/plugin configuration beyond the base package update itself.

## Immediate mitigation
- Confirmed package update completed to latest available version.
- Confirmed memory search availability after update.
- Confirmed gateway connectivity is back, though with limited `operator.read` scope for diagnostics.
- Stopped treating the update as fully complete and recorded this error formally.

## Corrective actions
- [ ] Identify the intended ACP backend/plugin installation path for this runtime.
- [ ] Install/enable the `acpx` runtime plugin or otherwise restore ACP backend availability.
- [ ] Re-run the ACP smoke test with an explicit ACP agent after backend restoration.
- [ ] Re-run the full post-update smoke checklist and record final pass/fail outcome.

## Preventive changes
- The OpenClaw post-update smoke-test/runbook should continue treating ACP verification as mandatory for this runtime.
- Update/release-delta handling should explicitly check whether ACP backend/plugin availability changed across versions or install paths.
- Consider making ACP backend presence/configuration more explicit in local runtime configuration/runbooks so the failure mode is easier to diagnose quickly.

## Linked artifacts
- Related tasks:
  - follow-up task needed for ACP backend restoration
- Related decisions:
  - `OPENCLAW_RELEASE_DELTA_SOP.md`
- Related evidence:
  - `os/runbooks/OPENCLAW_POST_UPDATE_SMOKE_TEST_CHECKLIST_V1.md`
- Related product/shared artifacts:
  - `AGENTS.md`
  - `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`

## Closure criteria
- ACP backend is configured and available.
- A lightweight ACP/Codex smoke test succeeds.
- Post-update smoke checklist is re-run and passes overall.
- Any required runbook/config clarifications are recorded.

## Closure note
- Final outcome / verification:
  - Pending.
