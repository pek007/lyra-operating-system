# Vega/PXS Boundary Post-Change Validation — 2026-03-15

Owner: Lyra  
Linked task: `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`

## Purpose
Record the first validation pass after enforcing `px-internal-dev.tools.fs.workspaceOnly=true`, and capture what is actually improved versus what still leaves the boundary incomplete.

## Change applied
Approved config change was applied so that:
- `px-internal-dev.tools.fs.workspaceOnly=true`

Gateway/runtime restart/apply completed successfully.

## Runtime health after change
### Gateway status
- `openclaw gateway status` returned healthy/running
- RPC probe: ok
- runtime reachable

### Deep status
- `openclaw status --deep` returned normally
- no new gateway-level breakage observed from this change

## Validation result summary
### 1. Filesystem-tool boundary
**Result: PARTIAL PASS**

What is now true:
- `px-internal-dev` no longer has the explicit per-agent filesystem-tool exception.
- The live config now shows `tools.fs.workspaceOnly=true` for `px-internal-dev`.
- This should block direct cross-workspace access via filesystem tools (`read` / `write` / `edit`) outside the Vega workspace.

What was not directly runtime-probed yet:
- a live in-agent `read` tool denial transcript from the Vega side

### 2. True cross-domain boundary enforcement
**Result: FAIL**

Why it still fails:
- `px-internal-dev` still has:
  - `sandbox.mode=off`
  - `tools.exec.host=gateway`
  - `tools.exec.security=full`
  - `tools.exec.ask=off`
- That means Vega/PXS can still use shell execution to access arbitrary host paths outside its workspace, even if filesystem tools are narrowed.

### Key interpretation
The boundary has been tightened, but not fully enforced.

We removed the convenience path through filesystem tools, which is useful.
But the stronger cross-domain access path still exists through unsandboxed gateway exec.
Therefore the claim:
- “PXS no longer has default cross-workspace access”

is only true for filesystem tools, not for the overall runtime capability surface.

## Acceptance-sheet implication
### E2 — No direct cross-domain read by default
**Current judgment after this validation pass: KEEP FAIL**

Reason:
- direct cross-domain reads are still operationally possible through `exec`, even if narrowed through `fs` tools
- therefore the OS↔PXS boundary is still not yet a deny-by-default enforced control in the full runtime sense

## What improved
- Hidden dependency discovery will now surface sooner for workflows that relied on filesystem-tool reads
- We now have a cleaner distinction between:
  - productized/artifact-delivered access
  - convenience reads through `fs` tools
- Access surface documentation is now explicit in `PXS_ACCESS_SURFACE_BASELINE_2026-03-15.md`

## First concrete gap list
### Gap 1 — Boundary enforcement is broader than filesystem tools
- Type: control gap
- Description: `fs.workspaceOnly=true` is not sufficient while unrestricted gateway `exec` remains available.
- Consequence: boundary remains porous even after the approved change.

### Gap 2 — Acceptance criteria must distinguish tool-surface narrowing from true runtime isolation
- Type: evidence/model gap
- Description: the previous E2 framing was too coarse; it treated cross-domain read as a single condition rather than separating `fs`-tool access from `exec`-based access.
- Consequence: boundary progress can be overstated if only one surface is checked.

### Gap 3 — Capability-delivery gap mapping is still pending live Vega workflow checks
- Type: productization gap
- Description: we have not yet catalogued which Lyra OS capabilities Vega actually loses at the workflow level under the narrowed `fs` surface.
- Consequence: we know the boundary is still incomplete, but we do not yet have the workflow-by-workflow missing-capability inventory.

## Recommended immediate next steps
1. Update `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
   - refresh B1/C1/C2 from stale evidence
   - keep E2 as FAIL
   - explicitly note that `fs` narrowing landed but exec-based cross-domain access remains open
2. Decide whether E2 should require:
   - sandboxing/tighter exec restrictions, or
   - a narrower acceptance statement limited only to filesystem-tool access
3. Run the next live Vega workflow check set to identify actual missing capability-delivery gaps at the product level

## Bottom line
The approved change was worth doing and did improve the boundary.
But it did **not** fully close it.
The first real post-change result is:
- **filesystem boundary tightened**
- **true runtime boundary still not fully enforced**
- **E2 remains FAIL until exec/sandbox posture is addressed or the acceptance claim is narrowed honestly**
