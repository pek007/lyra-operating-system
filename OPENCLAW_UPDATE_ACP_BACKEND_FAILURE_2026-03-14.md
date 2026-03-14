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

The ACP failure had two layers:
- first: `ACP runtime backend is not configured. Install and enable the acpx runtime plugin.`
- then, after enabling ACPX and wiring it to the bundled binary: `Authentication required`

Current state:
- ACPX runtime plugin is enabled and loaded
- bundled `acpx` CLI is present and invokable
- the Codex ACP agent launches via ACPX
- the remaining blocker is missing ACP/Codex authentication for the spawned Codex ACP agent

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
  - The Codex ACP agent requires ACP-side authentication, and no matching credentials are currently available to the spawned Codex ACP runtime.

- Contributing factors:
  - ACP runtime backend (`acpx`) was initially disabled.
  - The bundled `acpx` CLI was not being resolved automatically and required an explicit command override.
  - No default ACP agent was configured, which initially obscured the true issue.
  - The OpenClaw update path can succeed at package-install level while leaving critical optional/runtime-path dependencies unavailable.
  - ACP capability depends on both runtime/plugin configuration and ACP-agent authentication beyond the base package update itself.

## Immediate mitigation
- Confirmed package update completed to latest available version.
- Confirmed memory search availability after update.
- Confirmed gateway connectivity is back, though with limited `operator.read` scope for diagnostics.
- Stopped treating the update as fully complete and recorded this error formally.

## Corrective actions
- [x] Identify the intended ACP backend/plugin installation path for this runtime.
- [x] Install/enable the `acpx` runtime plugin.
- [x] Configure ACPX to use the bundled `acpx` binary explicitly.
- [ ] Restore ACP/Codex authentication for the spawned Codex ACP agent.
- [ ] Re-run the ACP smoke test with an explicit ACP agent after authentication is restored.
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
