# Vega/PXS Boundary Morning Apply Runbook

Date: 2026-03-15
Owner: Lyra
Linked overnight priority: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`
Selected-by policy: `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
Predecessor artifacts:
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_REMEDIATION_BRIEF_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CURRENT_STATE_CHECK_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_ENFORCEMENT_SURFACE_CHECK_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CHANGE_REQUEST_2026-03-15.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`

## Purpose
Execute one more concrete step on the top overnight portfolio item without crossing the approval boundary: convert the approved-change request into a ready-to-run morning execution sequence with explicit commands, evidence capture targets, and acceptance-sheet refresh instructions.

This artifact keeps the bridge explicit from:
1. Control Tower overnight selection
2. active TDE work (`TASK-20260314-VEGA-PXS-BOUNDARY-PASS`)
3. narrowed live blocker (E2 runtime/config boundary exception)
4. morning execution evidence path

## Decision gate
This runbook is **not authorization to apply**.
It is the operator packet to use **if Peter approves** the recommended minimal filesystem-boundary change for `px-internal-dev`.

## Recommended approved change
Remove the per-agent Vega filesystem exception so `px-internal-dev` inherits the global `tools.fs.workspaceOnly=true` posture.

## Pre-change confirmation checklist
Before touching config, re-read:
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CHANGE_REQUEST_2026-03-15.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`

Confirm all of the following are still true:
- Target agent is `px-internal-dev`
- Only approved change is the filesystem-boundary narrowing
- No unrelated OpenClaw config work is bundled into the same window
- Rollback path is available

## Exact execution sequence

### 1. Backup current config
```bash
TS=$(date +%Y%m%d-%H%M%S)
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak-$TS
```

### 2. Inspect target stanza before edit
```bash
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home()/'.openclaw'/'openclaw.json'
obj = json.loads(p.read_text())
for agent in obj.get('agents', {}).get('list', []):
    if agent.get('id') == 'px-internal-dev':
        import pprint
        pprint.pp(agent)
        break
else:
    raise SystemExit('px-internal-dev agent not found')
PY
```

### 3. Apply minimal diff only
Preferred result: remove the `tools.fs.workspaceOnly` override under `px-internal-dev`.

Safe edit target:
- before: `"fs": { "workspaceOnly": false }`
- after: remove that override entirely, or set `"workspaceOnly": true` explicitly if removal is operationally awkward.

### 4. Restart/apply runtime if required by the live config path
Use the standard OpenClaw gateway restart path after the approved config edit.

```bash
openclaw gateway restart
```

### 5. Immediate validation
```bash
openclaw gateway status
openclaw status --deep
```

### 6. Boundary validation for E2
Attempt the non-handoff cross-domain read that previously succeeded.

Validation target:
- expected: Vega can no longer directly read `/Users/lyra/.openclaw/workspace` outside its own workspace boundary by default
- failure signal: direct list/read still succeeds unchanged

### 7. Vega-local smoke check
Verify Vega still works inside its own domain:
- Vega workspace root accessible
- `pxs/` repo usable
- normal local git/document operations still function

## Evidence capture requirements
Publish a post-change validation artifact with:
- backup filename used
- exact config delta applied
- `openclaw gateway status` result
- `openclaw status --deep` result summary
- E2 boundary test result
- Vega-local smoke result
- final verdict: PASS / FAIL / ROLLBACK

Recommended artifact path:
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md`

## Acceptance-sheet refresh instructions
After successful validation, update `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` explicitly:

### B1
Refresh from stale FAIL to current observed state:
- `pxs` repo exists in Vega workspace
- normal git operations observed

### C1
Refresh from blanket FAIL to current pinned-dependency reality:
- `platform-core` submodule exists
- pinned commit evidenced
- note remaining local-source coupling if still present

### C2
Refresh from `not verifiable` to a narrowed status based on the current dependency form:
- if dependency remains local-path coupled, record that exact packaging concern
- do not leave as the old pre-implementation fail statement

### E2
Mark PASS **only if** the direct cross-domain read is now denied and evidence is captured.
If denial is not observed, keep FAIL and record the exact observed behavior.

## Rollback sequence
Trigger rollback immediately if:
- gateway restart fails
- runtime health regresses
- Vega loses required local safe operation unexpectedly
- current live state becomes unclear

```bash
cp ~/.openclaw/openclaw.json.bak-$TS ~/.openclaw/openclaw.json
openclaw gateway restart
openclaw gateway status
openclaw status --deep
```

Then publish rollback outcome and newly discovered dependency/failure mode.

## Why this is the right overnight next step
The overnight loop already narrowed the portfolio bottleneck to one live blocker and produced the approval-ready change request. The highest-value remaining action before morning is to eliminate execution ambiguity:
- no searching for the right commands
- no mixing decision and implementation logic
- no broken evidence chain between selected priority, TDE task, applied change, and acceptance refresh

## Bottom line
If Peter approves the minimal boundary change in the morning, this runbook should let the top overnight TDE item move immediately from decision to controlled application and evidence-backed acceptance rerun.