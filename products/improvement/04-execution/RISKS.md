# Risks

### R-001 — Improvement execution state is split across multiple systems of record
- Description: Improvement work can still leak into legacy or generated views instead of staying anchored in the canonical Task Management / TDE substrate.
- Consequence: weak traceability, poor metrics, inconsistent ownership, and slower automation-safe improvement loops.
- Mitigation: make improvement intake and follow-through TDE-first and remove legacy routing dependencies.

### R-002 — Deployment drift between Lyra OS and consuming workspaces
- Description: Improvement capability may remain verified only through interim-copy lanes instead of pinned-lane distribution with version truth and rollback semantics.
- Consequence: silent drift, unclear installed state, and weak confidence in downstream adoption.
- Mitigation: implement a pinned lane with machine-checkable installed-version truth and explicit rollback/verification behavior.

### R-003 — Improvement signals do not convert reliably into owned execution
- Description: incidents, repeated misses, and synthesis outputs may be visible but still fail to become explicit linked execution artifacts with owners and evidence.
- Consequence: recurring friction remains narrative instead of compounding learning.
- Mitigation: deploy a minimum improvement interface across active products and make incident-to-improvement conversion mandatory for material cases.

### R-004 — Status truth drifts inside the improvement product itself
- Description: scorecards, logs, automation specs, and operational summaries can become internally inconsistent.
- Consequence: the improvement product undermines trust in its own control loop.
- Mitigation: reconcile product-local status artifacts against verified evidence and keep automation specs free of integrity defects.
