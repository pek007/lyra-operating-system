# Software Factory Parallel Dispatch Gate Runbook v0

Status: draft v0 / tool-backed pre-dispatch gate
Factory run ID: `SF-ORCH-2026-05-06-TOOL-BACKED-PARALLEL-DISPATCH-GATE`
Owner/reviewer: Peter Eklind / Lyra Operations
Scope: operating `tools/software_factory_file_scope_lock_check.py` before parallel builder dispatch

## Purpose

Use this runbook to confirm, before dispatch, that parallel Software Factory builders have unique identities, non-overlapping write scopes, and unique worker result paths. The gate is fail-closed: if the check fails, hold dispatch until the manifest or packet boundaries are corrected.

## Inputs

- Lock manifest: `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/manifests/pre-dispatch-lock-manifest.json`
- Builder packets and assigned write/result paths.
- Worker Result Contract: `products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md`
- Optional evidence log: `workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/logs/pre-dispatch-lock-check.log`

## Pre-Dispatch Procedure

1. Confirm every active worker is represented in the manifest with:
   - `worker_id`;
   - branch shaped as `sf/<factory-run-slug>/<worker-slug>`;
   - worktree path containing the factory run slug and worker slug;
   - one unique `assigned_result_path`;
   - explicit `write_scopes` with relative, non-wildcard paths;
   - any read-only inspection paths listed separately.
2. Run from the root workspace:

   ```bash
   python3 tools/software_factory_file_scope_lock_check.py workspaces/software-factory/dry-runs/2026-05-06-tool-backed-parallel-dispatch-gate/manifests/pre-dispatch-lock-manifest.json
   ```

3. Save or reference the command output in run evidence before dispatching builders.
4. Dispatch builders only when the result is `[PASS]` and all packet authority boundaries still match the manifest.

## Interpreting Outcomes

### PASS

A pass means the manifest is structurally valid for dispatch: worker IDs, branch/worktree identities, result paths, path syntax, and cross-worker write-scope overlap checks succeeded.

Operational action:

- Proceed with bounded parallel dispatch.
- Tell builders to write only their assigned artifact and result paths.
- Preserve the pass output as evidence for the Integrator.

### FAIL

A fail means dispatch is not safe under the declared locks. The tool prints one or more specific errors, such as duplicate workers/result paths, invalid branch naming, absolute or parent-escaping paths, wildcard paths, read-only/write-scope overlap, write-scope overlap, or changed files outside a declared scope.

Operational action:

- Do not dispatch the affected builders in parallel.
- Correct the manifest and/or role packets, or switch the work to a serial/manual integration path.
- If a worker has already started, instruct it to stop before writing outside its lock and return `blocked` or `decision-needed` with the conflicting path.
- Re-run the exact gate command after correction and record the new output.

## Integrator Handoff Minimum

Before integration, the Integrator should receive:

- the lock manifest path;
- the exact gate command and pass/fail output;
- each worker result path;
- each worker changed-file list;
- confirmation that changed files stayed inside declared scopes;
- any unresolved conflict, failed validation, or authority exception.

## Authority Boundary

This gate validates declared file-scope locks only. It does not authorize credentials/access changes, external sends, deploys, releases, pushes, merges, destructive cleanup, persistent agents, root final artifact edits by workers, PXS/PXS CRM mutation, Vega Inquiry Engine intervention, or client/customer data changes. Final integration authority remains with the assigned Integrator and human owner/reviewer.
