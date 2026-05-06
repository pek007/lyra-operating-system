# Software Factory Parallel Builder File-Scope Lock v0

Status: draft v0 / tool-backed
Factory run ID: `SF-ORCH-2026-05-06-PHASE3B-ISOLATED-PARALLEL-BUILDERS`
Owner/reviewer: Peter Eklind / Lyra Operations
Scope: future Software Factory runs that execute multiple builders against isolated copies or worktrees before integration

## Purpose

This artifact defines the v0 file-scope lock/check discipline for parallel Software Factory builders. It is intended to prevent accidental write overlap, make read-only collaboration explicit, and give the Integrator enough evidence to decide whether builder outputs can be safely combined.

## Core Rule

Every builder must declare its intended write scope before making changes. A builder may write only files covered by its assigned lock and must return `blocked` or `decision-needed` rather than modifying an undeclared or conflicting path.

## Required Lock Record

Each builder packet or child task should include one lock record with these fields:

```yaml
lock_id: <factory-run-id>/<role-or-worker-id>
lock_owner: <role/worker/session label>
assigned_result_path: <relative worker result path>
write_scopes:
  - path: <relative file or directory path>
    mode: create | modify | delete | replace
    purpose: <one-line reason>
read_only_exceptions:
  - path: <relative path allowed for inspection only>
    reason: <why read access is needed>
conflict_policy: hold-for-integrator
issued_by: <orchestrator or owning lane>
issued_at: <timestamp with timezone>
```

## Scope Semantics

- **Exact file scope:** permits writes only to the named file.
- **Directory scope:** permits writes under the directory only when the packet explicitly grants directory scope.
- **Result scope:** every worker may write only its assigned result file unless the packet grants more.
- **Read-only exception:** permits inspection, grep, diff, or validation reads, but never edit, delete, move, or formatting changes.
- **No implied sibling access:** permission for one file does not permit changing adjacent files, generated indexes, root final artifacts, or another worker's result.

## Overlap Detection

Before work starts, the orchestrator or dispatcher should compare all declared `write_scopes` in the same factory run:

1. Normalize paths relative to the root workspace.
2. Treat a directory scope as overlapping every child path.
3. Treat exact file matches as overlapping regardless of write mode.
4. Treat delete/replace of a directory as overlapping every descendant file.
5. Flag any overlap between two active builders unless the same owner holds both scopes and the packet explicitly says the work is serial, not parallel.

A builder should also self-check its changed-file list before handoff. If any changed file is outside its lock record, the result must be `issue`, `blocked`, or `decision-needed` with the stray path named explicitly.

## Conflict / Hold Behavior

When overlap or ambiguity is found:

- The builder must stop before writing the disputed path.
- The worker result should record `Status: blocked` or `decision-needed`.
- The result should name the conflicting path, competing owner if known, and needed Integrator decision.
- The Integrator decides whether to serialize, split the scope, assign a new lock, or reject one output.
- Builders must not resolve conflicts by editing another builder's copy, result file, lock record, or root final artifact.

## Evidence Fields for Worker Results

Each worker result should include enough evidence for an Integrator to verify scope compliance quickly:

- assigned lock owner / worker role;
- assigned artifact and result paths;
- complete changed-file list from the worker;
- confirmation that no Builder B, root final artifact, credential, deploy, push, merge, release, external-send, persistent-agent, destructive-cleanup, PXS, or PXS CRM path/action was touched;
- validation command and result, when an allowed validation command exists;
- any conflict, ambiguity, or read-only exception used during the work.

## Minimal Integration Gate

The Integrator may accept a parallel builder output only when:

1. every changed file is inside that builder's declared write scope;
2. no active builder write scopes overlap unresolved;
3. the worker result follows the Worker Result Contract;
4. authority boundaries and prohibited actions are explicitly addressed; and
5. validation is either passing or any non-run/failing validation is explained.

## Worktree / Branch Naming Rule

For parallel builder runs that use git worktrees or equivalent isolated copies, each active worker should have a unique branch/worktree identity before dispatch:

- Branch: `sf/<factory-run-slug>/<worker-slug>`
- Worktree path: a relative path that includes both `<factory-run-slug>` and `<worker-slug>`
- Worker result path: one unique Markdown result file per worker

The naming rule is intentionally boring: it gives the orchestrator, Integrator, and Verifier a predictable way to identify which output came from which isolated lane.

## Machine-Check Manifest

Use `tools/software_factory_file_scope_lock_check.py` to fail closed before dispatch. The tool accepts JSON lock manifests with this shape:

```json
{
  "artifactType": "software_factory_file_scope_locks",
  "schemaVersion": "0.1.0",
  "factory_run_id": "SF-ORCH-YYYY-MM-DD-EXAMPLE",
  "workers": [
    {
      "worker_id": "builder-a",
      "branch": "sf/sf-orch-yyyy-mm-dd-example/builder-a",
      "worktree_path": "workspaces/software-factory/worktrees/sf-orch-yyyy-mm-dd-example/builder-a",
      "assigned_result_path": "workspaces/software-factory/dry-runs/yyyy-mm-dd-example/worker-results/BUILDER_A_RESULT.md",
      "write_scopes": [
        {
          "path": "products/delivery/06-architecture/EXAMPLE.md",
          "scope_type": "file",
          "mode": "modify"
        }
      ],
      "changed_files": [
        "products/delivery/06-architecture/EXAMPLE.md"
      ],
      "read_only_paths": [
        "products/delivery/06-architecture/SOFTWARE_FACTORY_WORKER_RESULT_CONTRACT_V0.md"
      ]
    }
  ]
}
```

Required pre-dispatch command:

```bash
python3 tools/software_factory_file_scope_lock_check.py <lock-manifest.json>
```

The helper rejects:

- missing artifact/schema/factory-run identifiers;
- missing or duplicate worker IDs;
- branch names that do not match `sf/<factory-run-slug>/<worker-slug>`;
- worktree paths that do not include both the factory run slug and worker slug;
- absolute, parent-escaping, or wildcard paths;
- overlapping exact-file, directory, or parent/child write scopes across workers;
- duplicate worker result paths; and
- changed files outside the declaring worker's write scopes.

Reference fixtures:

- pass: `tools/fixtures/software_factory_file_scope_locks/pass-non-overlap.json`
- expected fail: `tools/fixtures/software_factory_file_scope_locks/fail-overlap.json`
- expected fail: `tools/fixtures/software_factory_file_scope_locks/fail-naming.json`
- expected fail: `tools/fixtures/software_factory_file_scope_locks/fail-changed-file.json`

## Authority Boundary

This v0 discipline is an operational check, not permission to bypass product ownership. Final integration authority remains with the human owner/reviewer and designated Integrator. Builders must hold rather than expand access, mutate external systems, or make root-level final artifact changes without explicit assignment.
