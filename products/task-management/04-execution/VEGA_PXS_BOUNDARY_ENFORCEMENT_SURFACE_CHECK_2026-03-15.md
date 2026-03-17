# Vega/PXS Boundary Enforcement Surface Check

Date: 2026-03-15
Owner: Lyra
Linked overnight priority: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
Source selection chain:
- `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
- `tmp/overnight-2026-03-15-boundary-assignment.json`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_REMEDIATION_BRIEF_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CURRENT_STATE_CHECK_2026-03-15.md`
- `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

## Purpose
Execute the next Control-Tower-authorized remediation step after the current-state check: identify the actual runtime/config enforcement surface behind acceptance item E2 and determine whether the Vega/PXS no-direct-read boundary is currently enforced, enforceable immediately, or still only documentary.

## TDE state this step is serving
Canonical TDE assignment: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`

Task intent from assignment packet:
- "Make Vega/PXS boundary PASS so downstream pxs consumption can proceed safely"
- next required outcome: "acceptance sheet rerun to PASS with committed evidence"

## Evidence reviewed
### 1. Current gateway config
Read-only config inspection of `~/.openclaw/openclaw.json` showed:
- global default: `tools.fs.workspaceOnly=true`
- agent override for `px-internal-dev`: `tools.fs.workspaceOnly=false`
- `px-internal-dev.sandbox.mode=off`
- global default sandbox: `agents.defaults.sandbox.mode=off`

### 2. Current security baseline
`repos/lyra-operating-system/products/A-004/management/PXS_SECURITY_DEPLOYMENT_BASELINE.md` already records:
- the main trusted boundary is constrained by `tools.fs.workspaceOnly=true`
- open issue O2: `px-internal-dev` has broader filesystem posture than main
- recommendation: verify whether `px-internal-dev` still needs broader filesystem scope

### 3. Acceptance-sheet evidence
`governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` records E2 fail because Vega successfully listed `/Users/lyra/.openclaw/workspace` directly.

## Findings
### A. The E2 blocker is real and config-backed
This is not just a stale test artifact.

The current runtime/config state explicitly preserves broader filesystem access for Vega than for the main trusted boundary:
- main boundary: workspace-only reads
- Vega boundary: workspace-only restriction disabled
- sandbox isolation: disabled for Vega

That means the observed cross-domain read success is consistent with current configuration, not an accident.

### B. The live enforcement surface is OpenClaw config, not missing prose
The practical enforcement levers visible tonight are:
1. `tools.fs.workspaceOnly`
2. per-agent override under `agents.list[].tools.fs.workspaceOnly`
3. sandbox mode / workspace visibility posture

The declared boundary can only be treated as enforced if those runtime controls narrow Vega to its own workspace or an equivalent explicitly governed handoff path.

### C. No deny-by-default control is active for Vega right now
Given:
- `px-internal-dev.tools.fs.workspaceOnly=false`
- `px-internal-dev.sandbox.mode=off`

there is no evidence tonight of an active deny-by-default filesystem boundary preventing Vega from reading Lyra-host paths outside its own workspace.

### D. Minimum closure path is now narrower and clearer
The minimum credible closure path for E2 is no longer "investigate boundary somehow." It is:
1. decide whether Vega still truly needs broader-than-workspace filesystem scope
2. if not, tighten the per-agent config to workspace-only or equivalent deny-by-default posture
3. if yes, explicitly document the exception and stop claiming the no-direct-read boundary is enforced
4. rerun the acceptance sheet after the runtime posture is changed or the claim is narrowed

## Result for overnight execution
### What this step accomplished
It converted E2 from a loosely described boundary concern into a specific, inspectable configuration gap with named enforcement levers.

### What remains blocked
Acceptance E2 cannot PASS under current configuration because Vega is still explicitly configured with broader filesystem access than the main trusted boundary.

### Why I did not change config overnight
Changing OpenClaw boundary/sandbox/filesystem controls is a material runtime/security change with restart implications. Under current guardrails and the config-change SOP posture, that should not be flipped casually during the overnight loop without an explicit approved change decision/window.

## Recommended next step
Use this artifact as the bridge into the morning decision/action:
- either approve the narrowing change for `px-internal-dev` and rerun the acceptance sheet
- or record that Vega currently operates under an intentional wider-scope exception, which means the existing E2 acceptance claim must be revised rather than marked PASS

## Bottom line
The top overnight portfolio item is now narrowed precisely:
**the remaining live blocker is a currently active OpenClaw config exception (`px-internal-dev.tools.fs.workspaceOnly=false`, with sandbox off), so the Vega/PXS boundary is still documentary rather than deny-by-default enforced.**
