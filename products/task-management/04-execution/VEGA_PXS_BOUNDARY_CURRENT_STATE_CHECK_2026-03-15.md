# Vega/PXS Boundary Current-State Check

Date: 2026-03-15
Owner: Lyra
Linked overnight priority: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
Source selection chain:
- `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
- `tmp/overnight-2026-03-15-boundary-assignment.json`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_REMEDIATION_BRIEF_2026-03-15.md`
- `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

## Purpose
Execute the first overnight remediation step from the brief: reconfirm current Vega workspace/repo topology and distinguish live fail conditions from stale acceptance-sheet evidence before further remediation work.

## TDE state checked
Canonical TDE row at `os/runtime/tde_state.sqlite`:
- task_id: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
- status: `active`
- title: `Make Vega/PXS boundary PASS so downstream \`pxs\` consumption can proceed safely`
- updated_at: `2026-03-15T00:37:54.789115+00:00`

## Current-state findings
### 1. B1 (`pxs` repo in Vega workspace)
**Current result: no longer a live fail.**

Observed state under `/Users/lyra/.openclaw/workspace-px-internal-dev`:
- top-level `pxs/` directory exists
- `pxs/.git` exists
- Vega workspace root is present and active

Interpretation:
- Acceptance-sheet B1 is stale relative to the current workspace state.
- The overnight remediation path should stop treating repo placement as the lead blocker.

### 2. C1/C2 (pinned platform-core dependency)
**Current result: materially improved; acceptance sheet is stale/incomplete.**

Observed state:
- Vega workspace contains `.gitmodules` with:
  - submodule name: `platform-core`
  - path: `platform-core`
  - url: `/Users/lyra/.openclaw/workspace`
- `git submodule status` in Vega workspace reports pinned commit:
  - `d20cf2ade89d96c75a7279767a736d5d530e2583 platform-core (heads/main)`

Interpretation:
- A real submodule-backed dependency now exists, so the old blanket C1 fail is stale.
- However, the current URL points at the Lyra workspace working tree. That means the dependency is pinned at a commit but still anchored to a local-path source rather than a clearly packaged/distributed platform-core remote.
- C2 should therefore be reframed from `not implemented` to `implemented in a still-local coupling form; needs packaging/consumability review if Pattern A requires a cleaner distribution boundary`.

### 3. E2 (no direct cross-domain read by default)
**Current result: still the most credible live blocker.**

Evidence reviewed:
- Acceptance sheet records successful listing of `/Users/lyra/.openclaw/workspace` from Vega test.
- Current Vega session metadata under `agents/px-internal-dev/sessions/sessions.json` shows at least one runtime context using a sandbox workspace (`/Users/lyra/.openclaw/sandboxes/agent-px-internal-dev-36f5bae7`) and another using the direct Vega workspace root.
- No runtime-level control artifact was found tonight showing that default cross-domain filesystem reads are now denied outside explicit handoffs.

Interpretation:
- The main live issue is no longer simple repo placement.
- The remaining gating problem is enforcement: the declared no-direct-read boundary is still not evidenced as an active control.
- Until a deny-by-default control or equivalent tested guard exists, downstream `pxs` consumption cannot be claimed safe/repeatable under the intended boundary model.

## Resulting overnight execution stance
### What changed from the old acceptance picture
- **B1:** stale fail -> effectively resolved in current topology
- **C1:** stale fail -> partially resolved (pinned submodule exists)
- **C2:** should be narrowed from blanket fail to packaging/local-coupling concern
- **E2:** remains the lead live blocker

### Recommended next remediation step
Focus the next overnight execution move on the runtime/control surface for E2:
- identify where filesystem/tool-access boundary enforcement for Vega can actually be implemented or configured
- if enforceable now, make the smallest deny-by-default change and record proof
- if not enforceable now, publish the exact implementation gap and why the current declared boundary is still only documentary

## Why this matters
This checkpoint keeps the Control Tower-selected priority explicit while preventing wasted overnight effort on already-closed or mostly-closed fail conditions. It narrows the task from a three-fail remediation narrative to a more accurate current problem statement: **boundary enforcement evidence is still missing even though topology and dependency state have materially advanced.**
