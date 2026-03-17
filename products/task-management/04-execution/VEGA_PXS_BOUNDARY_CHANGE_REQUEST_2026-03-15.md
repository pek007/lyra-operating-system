# Vega/PXS Boundary Change Request

Date: 2026-03-15
Owner: Lyra
Linked overnight priority: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
Selected-by policy: `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
Gate artifact: `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
Primary precursor evidence:
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_REMEDIATION_BRIEF_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CURRENT_STATE_CHECK_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_ENFORCEMENT_SURFACE_CHECK_2026-03-15.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`

## Purpose
Execute one concrete next step on the top overnight portfolio priority by converting the live E2 blocker into an approval-ready, minimal-diff change pack. This keeps the link explicit from:
1. Control Tower overnight selection
2. active TDE work (`TASK-20260314-VEGA-PXS-BOUNDARY-PASS`)
3. current blocker evidence
4. exact morning decision/action required

## Why this is the next step
Overnight evidence narrowed the acceptance picture:
- B1 repo-placement fail is stale/resolved in current topology.
- C1/C2 are no longer blank; they are narrowed to packaging/local-coupling review.
- **E2 remains the live blocking fail** because `px-internal-dev` is still configured with broader filesystem access than the declared boundary model allows.

That means the shortest path to an acceptance rerun is now a config-decision/change pack, not more exploratory analysis.

## Current live config state (observed)
Observed from `~/.openclaw/openclaw.json` during overnight inspection:

```json
{
  "id": "px-internal-dev",
  "workspace": "/Users/lyra/.openclaw/workspace-px-internal-dev",
  "sandbox": { "mode": "off" },
  "tools": {
    "exec": { "host": "gateway", "security": "full", "ask": "off" },
    "fs": { "workspaceOnly": false }
  }
}
```

Global defaults currently relevant:

```json
{
  "agents": {
    "defaults": {
      "sandbox": { "mode": "off" }
    }
  },
  "tools": {
    "fs": { "workspaceOnly": true }
  }
}
```

## Blocking interpretation
The declared Vega/PXS boundary says direct reads into Lyra-host workspace content should not be the default transfer path. But the current per-agent override explicitly disables the workspace-only read boundary for Vega. Under the acceptance sheet, E2 therefore cannot PASS credibly until one of the following happens:
1. the override is removed/tightened and the acceptance check is rerun, or
2. the boundary claim is formally narrowed to admit that Vega runs with a wider filesystem exception.

## Proposed minimal diff
### Recommended change
Remove the Vega-specific filesystem exception and let Vega inherit the global `tools.fs.workspaceOnly=true` posture.

### Before
```json
{
  "id": "px-internal-dev",
  "sandbox": { "mode": "off" },
  "tools": {
    "exec": { "host": "gateway", "security": "full", "ask": "off" },
    "fs": { "workspaceOnly": false }
  }
}
```

### After
```json
{
  "id": "px-internal-dev",
  "sandbox": { "mode": "off" },
  "tools": {
    "exec": { "host": "gateway", "security": "full", "ask": "off" }
  }
}
```

Equivalent acceptable explicit form:

```json
{
  "id": "px-internal-dev",
  "sandbox": { "mode": "off" },
  "tools": {
    "exec": { "host": "gateway", "security": "full", "ask": "off" },
    "fs": { "workspaceOnly": true }
  }
}
```

## Change classification
Per `OPENCLAW_CONFIG_CHANGE_SOP_V1.md` this is a **High-risk** config change because it alters runtime tool/file-access policy.

## Expected behavior impact
### Intended impact
- Vega should no longer be able to read arbitrary paths outside its own workspace by default.
- Acceptance item E2 can be rerun against a real deny-by-default posture.
- The declared Vega/PXS boundary moves closer to an actual enforced control rather than documentation only.

### Expected side effects to verify
- Existing Vega workflows that silently depended on direct reads into `/Users/lyra/.openclaw/workspace` will fail and must use explicit handoffs or local dependencies instead.
- If any hidden cross-workspace dependency remains, the acceptance rerun or smoke workflow should surface it immediately.

## Validation plan
Immediately after approved change application:
1. `openclaw gateway status`
2. `openclaw status --deep`
3. Launch or use `px-internal-dev` and attempt the non-handoff cross-domain read from acceptance E2
   - expected result: denied / inaccessible outside Vega workspace
4. Reconfirm normal Vega-local work still functions inside `/Users/lyra/.openclaw/workspace-px-internal-dev`
5. Update `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
   - B1: refresh from stale FAIL to current state
   - C1/C2: refresh from stale FAIL to narrowed current state
   - E2: mark PASS only if denial is observed and evidenced
6. Publish post-change validation artifact with command outputs and result summary

## Rollback plan
If Vega loses required safe operation or gateway/runtime behavior regresses:
1. restore the timestamped pre-change backup of `~/.openclaw/openclaw.json`
2. restart gateway
3. rerun validation commands
4. record rollback outcome and any newly discovered hidden dependency

## Decision required in the morning
### Recommended decision
**Approve the minimal filesystem-boundary change for `px-internal-dev` and immediately rerun the Vega acceptance sheet.**

### Why this is the recommended path
- It is the smallest change that directly addresses the only clearly live acceptance blocker.
- It converts the overnight analysis into a falsifiable control test.
- If it breaks something, that failure is useful: it reveals the exact remaining hidden dependency preventing clean downstream consumption.

### Alternative decision
If Peter does **not** want Vega narrowed yet, then the acceptance claim must be revised instead of pushed to PASS. In that case the next step is not a rerun-to-pass but a formal exception record stating that Vega currently operates with a broader filesystem boundary than the declared model.

## Evidence chain summary
- Selected overnight priority: Control Tower synthesis -> priority #1 -> `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
- Current execution evidence: remediation brief -> topology refresh -> enforcement surface check
- Concrete next step executed here: approval-ready change request with exact diff, risk class, validation plan, and rollback path

## Overnight conclusion
The highest-value authorized overnight move after narrowing the blocker was **not** to flip a high-risk runtime control without approval, but to reduce morning decision latency to a single explicit choice with a ready-to-run minimal diff.