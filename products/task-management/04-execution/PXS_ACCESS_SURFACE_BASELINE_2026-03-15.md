# PXS Access Surface Baseline — 2026-03-15

Owner: Lyra  
Purpose: document what `px-internal-dev` / PXS currently has access to, what will be removed by the boundary-enforcement change, and what gaps this is expected to expose.

## Context
Peter approved enforcing the Vega/PXS boundary now rather than staying in a temporary-design state. As part of that enforcement, we need an explicit baseline of current access so we can quickly identify and close capability-delivery gaps after the change.

## Runtime in scope
- Agent ID: `px-internal-dev`
- Bound Telegram account binding: `vega`
- Workspace: `/Users/lyra/.openclaw/workspace-px-internal-dev`

## Current relevant config state (pre-change)
Global default:
```json
{
  "tools": {
    "fs": { "workspaceOnly": true }
  }
}
```

Per-agent override currently in force:
```json
{
  "id": "px-internal-dev",
  "tools": {
    "exec": { "host": "gateway", "security": "full", "ask": "off" },
    "fs": { "workspaceOnly": false }
  },
  "sandbox": { "mode": "off" }
}
```

## Effective current access picture (pre-change)
### PXS currently has
- normal filesystem read/write/edit behavior not restricted to only its own workspace
- ability to directly inspect files under Lyra OS workspace paths when it knows or discovers them
- unrestricted operational convenience for reaching internal OS docs, runbooks, standards, governance docs, and other repo-local artifacts
- gateway-host exec enabled with broad security posture inside the Vega runtime (`exec.host=gateway`, `security=full`, `ask=off`)

### PXS currently does **not** necessarily have as explicit productized interfaces
The following may exist as knowledge/assets in Lyra OS, but are not yet guaranteed to be delivered to Vega through narrow downstream product interfaces:
- governance policies and standards
- security posture and compliance guardrails
- GDPR-related guidance and operating rules
- runbooks / ways of working / operating protocols
- shared architecture decisions and source-of-truth conventions
- product-local standards not yet exported as assemblies/packages/contracts

## What the boundary-enforcement change does
### After change
`px-internal-dev` will inherit the global filesystem restriction:
```json
{
  "tools": {
    "fs": { "workspaceOnly": true }
  }
}
```

### Practical meaning
PXS should no longer be able to directly read outside its own workspace by default.

## What PXS should still have after change
- access to its own workspace at `/Users/lyra/.openclaw/workspace-px-internal-dev`
- ability to work normally on local PXS repos/content already present there
- ability to use explicitly provided artifacts, handoffs, packages, local dependencies, or governed interfaces that live inside its workspace or are intentionally delivered to it

## What PXS should lose after change
- default direct read access into `/Users/lyra/.openclaw/workspace`
- implicit dependence on internal Lyra OS files as if they were a local library
- undocumented cross-boundary convenience reads that bypass the intended product/interface delivery model

## Expected gap classes to surface quickly
Once the boundary is enforced, any breakage is useful evidence. The likely gap classes are:
1. **Policy knowledge gap**
   - Example: Vega needs GDPR or security guidance that exists only in Lyra OS docs.
2. **Operating-process gap**
   - Example: Vega relies on Lyra OS runbooks/standards directly rather than a productized downstream package.
3. **Architecture / source-of-truth gap**
   - Example: Vega expects to inspect central architecture or decision artifacts directly.
4. **Packaging gap**
   - Example: needed capability exists, but only as internal documentation and not as an installable/consumable product.
5. **Hidden local-coupling gap**
   - Example: a workflow silently reads central files rather than using explicit inputs.

## Immediate post-change working rule
When Vega/PXS fails after the boundary change, do **not** treat that as proof the change was wrong.
Treat it as one of the following:
- a required capability is missing from the downstream delivery model
- a governed interface is missing
- a package/assembly/export surface is incomplete
- a hidden dependency has just become visible

## What to do with each surfaced gap
For each failure surfaced after enforcement, capture:
- what Vega tried to access
- why it needed it
- whether the need is legitimate or convenience-only
- what product/package/interface should carry that capability in the end state
- the smallest short-path fix that preserves the enforced boundary

## Success condition for this baseline artifact
This artifact is successful if it lets us move fast after enforcement by answering:
- what PXS used to be able to access
- what was intentionally removed
- what category each newly exposed gap belongs to
- what to productize next
