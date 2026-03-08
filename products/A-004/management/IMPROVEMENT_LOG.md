# A-004 — Improvement Log

Status: Active v1
Product Name: Security
Product Owner: Lyra
Last updated: 2026-03-08

## Entry A-004-L1 — Security product activation
- Trigger: Portfolio shift to explicit product ownership and Product Owner roles.
- Observation: Security work existed across evidence, governance, and research, but lacked a single activated product boundary and management pack.
- Hypothesis: Turning Security into an explicit product will improve prioritization, traceability, and follow-through on security posture work.
- Change made: Activated A-004 as Security, populated the management pack, created a boundary document, and updated the product portfolio registry.
- Result: Security now has a defined home for strategy, goals, plans, decisions, scorecard, and continuous improvement.
- Decision (adopt/revert/continue-test): Adopt
- Follow-up: Establish the recurring research/posture review loop and review whether `px-internal-dev` still requires broader filesystem scope than the main trusted boundary

## Entry A-004-L2 — First PXS security deployment baseline
- Trigger: Need for a concise product-owned posture statement for the current customer environment.
- Observation: Security evidence and decisions existed, but the current posture still required too much reconstruction across multiple files.
- Hypothesis: A single baseline artifact will improve review speed, residual-risk visibility, and future change control.
- Change made: Created `PXS_SECURITY_DEPLOYMENT_BASELINE.md` summarizing active controls, accepted residual risks, open non-blocking issues, and refresh triggers.
- Result: Security now has a single current baseline for PXS deployment posture.
- Decision (adopt/revert/continue-test): Adopt
- Follow-up: Use the baseline as the standing reference point for future posture changes and refresh it after material config changes
