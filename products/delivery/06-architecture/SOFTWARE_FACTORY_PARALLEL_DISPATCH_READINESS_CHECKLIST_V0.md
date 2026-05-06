# Software Factory Parallel Dispatch Readiness Checklist v0

Status: draft v0 / operational checklist
Factory run ID: `<SF-ORCH-YYYY-MM-DD-SLUG>`
Owner/reviewer: `<human owner> / <operations or product reviewer>`
Scope: deciding whether a future Software Factory parallel dispatch is ready to run using the lock-manifest gate

## GO Checklist

Dispatch is ready only when every item below is true:

- [ ] A dispatch packet exists with explicit `GO/HOLD/NO-GO`, run folder, owner/reviewer, evidence target, Worker Result Contract, and allowed validation commands.
- [ ] The pre-dispatch lock manifest exists at the path named in the packet and covers every active builder exactly once.
- [ ] Every worker has a unique `worker_id`, branch/worktree or isolated-copy identity, assigned result path, and role packet.
- [ ] Every write scope is explicit, relative to the workspace, non-wildcard, non-overlapping, and limited to the worker's assigned artifact/result needs.
- [ ] Read-only paths are listed separately and do not imply permission to edit shared specs, root final artifacts, sibling builder outputs, manifests, or packets.
- [ ] The lock checker has been run from the root workspace with the exact manifest path:

  ```bash
  python3 tools/software_factory_file_scope_lock_check.py <relative-path-to-lock-manifest.json>
  ```

- [ ] The lock checker result is `[PASS]`, and the output is saved or referenced in the run evidence before any builder writes.
- [ ] Role packets match the manifest: assigned artifact paths, result paths, read-only paths, and authority boundaries are consistent.
- [ ] Builders are instructed to stop with `blocked` or `decision-needed` if work requires an undeclared path, root final artifact edit, external send, deploy, release, push, merge, credential/access change, destructive cleanup, persistent agent, or prohibited product/customer-data mutation.
- [ ] Integration authority is clear: workers only recommend; the designated Integrator and human owner/reviewer decide whether outputs are integrated.

## HOLD / NO-GO Triggers

Hold dispatch if any item below is true:

- [ ] Lock checker fails or has not been run.
- [ ] Worker IDs, result paths, branch/worktree identities, or write scopes are duplicated or ambiguous.
- [ ] Any write scope overlaps another worker, escapes the workspace, uses broad/wildcard paths, or conflicts with a read-only path.
- [ ] A builder would need to edit root final artifacts directly without an explicit lock record.
- [ ] Validation cannot be run or preserved as evidence, and the reason is not documented.
- [ ] The requested work would require credentials/access changes, external communication, deployment, release, push/merge, persistent agents, destructive cleanup, or mutation of prohibited products/customer data.

## Minimum Dispatch Evidence

Before dispatch, preserve:

- Lock manifest path.
- Exact lock checker command.
- Pass/fail output and timestamp.
- Builder-to-path assignment summary.
- Confirmation that role packets and manifest agree.
- Any known residual risk, owner decision, or reason for HOLD.
