# Software Factory Parallel Dispatch Packet Template v0

Status: template v0 / tool-backed parallel dispatch
Factory run ID: `<SF-ORCH-YYYY-MM-DD-SLUG>`
Owner/reviewer: `<human owner> / <operations or product reviewer>`
Scope: parallel Software Factory builder dispatch against isolated copies or worktrees

## 1. Dispatch Decision

GO/HOLD/NO-GO: `<GO | HOLD | NO-GO>`

Builders may be dispatched only after the file-scope lock manifest gate below passes. If the gate fails, the dispatcher must hold and update the packet or manifest before any builder writes.

## 2. Required Pre-Dispatch Lock Manifest Gate

Lock manifest: `<relative-path-to-lock-manifest.json>`
Lock checker command:

```bash
python3 tools/software_factory_file_scope_lock_check.py <relative-path-to-lock-manifest.json>
```

Required evidence before dispatch:

- Result: `pass`
- Evidence log: `<relative-path-to-pre-dispatch-lock-check.log>`
- Confirmed: every active builder has a unique `worker_id`, branch/worktree identity, assigned result path, and non-overlapping write scope.
- Confirmed: all read-only paths are inspection-only and do not imply sibling or root artifact write access.

If any scope overlaps, path escapes the workspace, worker/result identity is duplicated, or changed-file scope is ambiguous, dispatch state is `HOLD` until the Integrator or owning lane resolves it.

## 3. Run Context

- Root workspace: `<absolute-root-workspace>`
- Run folder: `<relative-run-folder>`
- TDE intake: `<relative-intake-path or n/a>`
- Quality gate matrix: `<relative-quality-gate-path or n/a>`
- Worker Result Contract: `<relative-worker-result-contract-path>`
- Evidence target: `<relative-evidence-path>`

## 4. Shared Builder Instructions

Each builder must:

1. read this packet, its role-specific packet, the Worker Result Contract, and the pre-dispatch lock-check evidence;
2. write only the artifact path and result path assigned to that builder;
3. treat shared specs, manifests, checklists, and other builder outputs as read-only unless explicitly locked for that builder;
4. stop with `blocked` or `decision-needed` if useful work requires an undeclared path, root final artifact edit, external send, deployment, release, push, merge, credential/access change, destructive cleanup, persistent agent, or prohibited product/customer-data mutation;
5. return a result file that follows the Worker Result Contract and lists every changed file.

## 5. Builder Assignments

### Builder `<worker-id>`

- Role packet: `<relative-role-packet-path>`
- Assigned artifact: `<relative-isolated-copy-or-worktree-artifact-path>`
- Assigned result: `<relative-worker-result-path>`
- Branch/worktree identity: `<branch>` / `<relative-worktree-or-isolated-copy-path>`
- Write scopes:
  - `<relative-path>` — `<create | modify | delete | replace>`; `<purpose>`
- Read-only paths:
  - `<relative-path>` — `<reason>`
- Assignment objective: `<one concise outcome>`

Repeat this subsection for each parallel builder.

## 6. Prohibited Paths and Actions

- No root final artifact edits unless explicitly assigned through a lock record.
- No edits to another builder's isolated copy, worktree, result file, or lock record.
- No credentials/access changes, external sends, deploys, releases, pushes, merges, persistent agents, destructive cleanup, or unrelated product/customer-data mutation.
- No PXS/PXS CRM, Vega Inquiry Engine, or client/customer-data changes unless the owning lane explicitly grants them in a separate authorized packet.

## 7. Validation Expectations

Allowed validation commands:

```bash
python3 tools/software_factory_file_scope_lock_check.py <relative-path-to-lock-manifest.json>
python3 tools/validate_software_factory_orchestration.py <relative-run-folder>
```

A worker may report validation as `not-run` only when the packet or current run state prevents safe execution; the reason must be explicit in the result file.

## 8. Integration Handoff

Integrator may consume builder outputs only when:

- each worker result exists and follows the Worker Result Contract;
- changed files are entirely inside that worker's assigned write scope;
- the lock manifest gate has passed and no unresolved overlap remains;
- validation is passing or clearly explained; and
- authority boundaries and risks are explicit.

Final integration authority remains with the human owner/reviewer and designated Integrator; builder recommendations are advisory.
