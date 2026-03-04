# IMP-AUTO Hygiene Bundle (Non-TDE) — Progress Note

Date: 2026-03-04
Scope: Non-TDE maintenance tasks during release monitoring window.

## Completed items

- `IMP-AUTO-20260302-01`
  - Added `tools/task_hygiene_check.py` for duplicate open task ID + duplicate normalized intent detection.
  - Wired into `tools/validate_repo.py` (fail-fast).

- `IMP-AUTO-20260304-01`
  - Added `tools/test_markdown_link_check.py` and wired execution in `.github/workflows/governance-machine-check.yml`.
  - Updated `CRON_SPEC_AUTONOMOUS_GOVERNANCE_SWEEPS.md` runbook to include markdown-link unittest gate.

- `IMP-AUTO-20260304-02`
  - Implemented `tools/markdown_link_check.py` with `--changed-only` mode (git-diff scoped).
  - Wired changed-only link check into `tools/validate_repo.py` and cron runbook.

## Verification

Commands run:
- `python3 -m unittest tools/test_markdown_link_check.py` (2/2 passing)
- `python3 tools/task_hygiene_check.py --file TASKS.md` (pass)
- `python3 tools/markdown_link_check.py --changed-only` (pass)
- `python3 tools/validate_repo.py --fix` (pass)

## TDE impact statement

No TDE runtime semantics, contracts, mutation behavior, or release logic were modified.
Changes are limited to documentation/tooling hygiene and CI/runbook wiring.
