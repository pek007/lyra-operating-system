# Software Factory Worktree / Branch Lock Tooling Evidence Workspace

Status: completed / pass
Date: 2026-05-06
TDE intake: `control/tde-intake/software-factory-worktree-branch-lock-tooling-2026-05-06.json`
Predecessor: `control/execution-evidence/software-factory-phase3b-isolated-worktree-parallel-builder-proof-2026-05-06.md`

This workspace captures the bounded implementation cycle for the reusable Software Factory file-scope lock checker and expected-fail fixtures.

## Outputs
- `tools/software_factory_file_scope_lock_check.py`
- `tools/test_software_factory_file_scope_lock_check.py`
- `tools/fixtures/software_factory_file_scope_locks/pass-non-overlap.json`
- `tools/fixtures/software_factory_file_scope_locks/fail-overlap.json`
- `tools/fixtures/software_factory_file_scope_locks/fail-naming.json`
- `tools/fixtures/software_factory_file_scope_locks/fail-changed-file.json`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_FILE_SCOPE_LOCK_V0.md`
- `products/delivery/06-architecture/SOFTWARE_FACTORY_PARALLEL_BUILDER_INTEGRATION_CHECKLIST_V0.md`

## Validation logs
- `logs/file-scope-lock-pass-fixture.log`
- `logs/file-scope-lock-unit-tests.log`
- `logs/file-scope-lock-expected-fail-overlap.log`
- `logs/file-scope-lock-expected-fail-naming.log`
- `logs/file-scope-lock-expected-fail-changed-file.log`
- `logs/file-scope-lock-expected-failures-summary.log`
