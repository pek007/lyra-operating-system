# Risks

### R-001 — Verification debt through thin activation/evidence practice
- Description: Delivery may look mature in documentation while real activation, verification, and evidence capture remain weak or inconsistent.
- Consequence: False confidence, hidden delivery risk, and poor learning.
- Mitigation: Run a real pilot, require evidence packs, and strengthen fail-closed verification behavior.

### R-002 — Drift through interim copy distribution
- Description: Temporary interim-copy lanes can create silent divergence between Lyra OS and consuming workspaces if provenance and removal are weak.
- Consequence: Two delivery systems, unclear authority, and hidden work.
- Mitigation: Use a strict interim copy protocol and migrate to pinned-lane distribution as soon as practical.

### R-003 — Gate ambiguity
- Description: Delivery gates can become operator-specific interpretation rather than a compiled contract.
- Consequence: Inconsistent quality bar, weak comparability, and enforcement drift.
- Mitigation: Define risk classes, required evidence outputs, pass/fail logic, and machine-checkable hooks.

### R-004 — Security or authority regression under delivery pressure
- Description: Release/change pressure can weaken proper review of security or authority-impacting changes.
- Consequence: Higher downside changes pass without proportionate scrutiny.
- Mitigation: Keep medium/high change classes tied to explicit review, stop-the-line triggers, and escalation expectations.
