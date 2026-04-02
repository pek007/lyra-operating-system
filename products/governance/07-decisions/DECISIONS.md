# Decisions

### D-001 — Governance is treated as a distinct product for now
- Decision: Governance remains a standalone product in the current portfolio, even though it overlaps conceptually with a future broader control-plane model.
- Why it matters: This preserves current ownership continuity while sharper boundaries are established.

### D-002 — Shared governance policies should be implemented model-first through workspace adoption surfaces
- Decision: Shared governance policies intended to apply across Lyra OS and downstream workspaces should first be anchored as explicit Governance capabilities, then expressed through canonical Governance artifacts, and finally adopted through local workspace authority surfaces rather than assumed to apply automatically everywhere.
- Why it matters: This prevents governance drift into loose documents, preserves local authority clarity, and gives policies an explicit architecture -> distribution -> adoption path.

### D-003 — Personal-data minimization / naming discipline is the first shared-policy implementation family
- Decision: The first concrete implementation of Governance shared-policy distribution will be a policy family for personal-data minimization and identifier discipline, starting with forward-looking naming/reference behavior and lightweight local adoption in `pxs`.
- Why it matters: This creates an immediate live test of the new Governance capability on a real cross-workspace policy question with clear compliance/privacy value.
