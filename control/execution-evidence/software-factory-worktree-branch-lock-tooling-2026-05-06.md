# Software Factory Worktree / Branch Lock Tooling Evidence

Status: completed / pass
Date: 2026-05-06
TDE intake: `control/tde-intake/software-factory-worktree-branch-lock-tooling-2026-05-06.json`
Predecessor evidence: `control/execution-evidence/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.md`
Evidence workspace: `workspaces/software-factory/dry-runs/2026-05-06-worktree-branch-lock-tooling/`

## Objective
Formalize reusable Software Factory worktree/branch naming and file-scope lock-check tooling before larger parallel-builder scale-up.

## Boundary
No persistent agents, PXS/PXS CRM mutation, deploy/release, credential/access changes, external sends, destructive cleanup, broad repository status sweep, or Vega Inquiry Engine intervention.

## Implemented outputs
- `tools/software_factory_file_scope_lock_check.py` — JSON lock-manifest validator for parallel builder dispatch.
- `tools/test_software_factory_file_scope_lock_check.py` — direct unit/fixture test harness.
- `tools/fixtures/software_factory_file_scope_locks/pass-non-overlap.json` — passing non-overlap fixture.
- `tools/fixtures/software_factory_file_scope_locks/fail-overlap.json` — expected-fail overlapping directory/file fixture.
- `tools/fixtures/software_factory_file_scope_locks/fail-naming.json` — expected-fail branch/worktree naming fixture.
- `tools/fixtures/software_factory_file_scope_locks/fail-changed-file.json` — expected-fail changed-file-outside-lock fixture.
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md` — updated to tool-backed status, branch/worktree naming rule, JSON manifest schema, command, and fixtures.
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_INTEGRATION_CHECKLIST_V0.md` — updated to require lock-manifest validation for parallel builders.

## Helper behavior
The checker fails closed on:
- missing artifact/schema/factory-run identifiers;
- missing or duplicate worker IDs;
- branch names not matching `sf/<factory-run-slug>/<worker-slug>`;
- worktree paths missing the factory run slug or worker slug;
- absolute, parent-escaping, or wildcard paths;
- overlapping exact-file, directory, or parent/child write scopes across workers;
- duplicate worker result paths;
- changed files outside the declaring worker's write scopes.

## Validation
- `python3 tools/software_factory_file_scope_lock_check.py tools/fixtures/software_factory_file_scope_locks/pass-non-overlap.json` — pass.
- `python3 tools/test_software_factory_file_scope_lock_check.py` — pass.
- Expected-fail fixtures were run and failed closed:
  - `tools/fixtures/software_factory_file_scope_locks/fail-overlap.json`
  - `tools/fixtures/software_factory_file_scope_locks/fail-naming.json`
  - `tools/fixtures/software_factory_file_scope_locks/fail-changed-file.json`

Validation logs are stored in `workspaces/software-factory/dry-runs/2026-05-06-worktree-branch-lock-tooling/logs/`.

Additional gates:
- `python3 tools/tde_cockpit.py --check --summary-json /tmp/tde-summary-after-sf-lock-tooling.json` — pass; parity true, closure-required debt 0.
- `python3 tools/validate_repo.py --fix` — pass; same known warning remains for `workspaces/software-factory/dry-runs/2026-05-04-isolated-copy-preflight` placeholder-looking snapshot text.

## Result
Completed / pass. Future parallel builder runs now have a reusable pre-dispatch lock manifest checker and expected-fail fixtures for overlap, naming, and changed-file boundary violations.

## Residual limitations
- The helper validates declared lock manifests; it does not create git worktrees or branches.
- It does not inspect real git diffs unless changed files are supplied in the manifest.
- It does not replace Integrator/Verifier semantic review.

## Exactly one next control object
Use the helper in the next Software Factory parallel-builder dispatch packet as a required pre-dispatch gate, then decide whether to add automatic worktree creation only after one tool-backed run passes.
