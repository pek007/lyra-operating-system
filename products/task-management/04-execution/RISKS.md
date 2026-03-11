# Risks

## Purpose
Track the current risks that could prevent Task Management from becoming a reliable and reusable product.

## Current risks

### R-001 — Scope sprawl
- Description: The product may absorb adjacent coordination, governance, or delivery problems without a clear boundary.
- Consequence: The product becomes fuzzy, hard to operate, and difficult to improve.
- Mitigation: Keep product interfaces explicit; distinguish Task Management from general operating-system work.

### R-002 — Implicit downstream interfaces
- Description: `pxs` consumption may depend on tribal knowledge or workspace-specific assumptions instead of explicit contracts.
- Consequence: Adoption stays fragile and non-repeatable.
- Mitigation: Formalize downstream interface requirements and document what is internal versus consumable.

### R-003 — Governance drag
- Description: Governance artifacts may accumulate faster than practical value.
- Consequence: The product becomes heavy and discourages use.
- Mitigation: Keep controls proportionate to risk; require each artifact to support a real decision or control need.

### R-004 — Readiness ambiguity
- Description: It may remain hard to tell whether TDE is actually ready for broader operational use.
- Consequence: Either premature deployment or stalled progress.
- Mitigation: Tie product health and roadmap more explicitly to the readiness gate and evidence artifacts.

### R-005 — Shadow operating state
- Description: Important active work may continue to live in chat or side lists rather than the canonical operating substrate.
- Consequence: Lost visibility, weak traceability, and degraded control.
- Mitigation: Continue reinforcing TDE as the system of record for active product work.

## Risk posture
Current risk posture is manageable, but the main failure mode is not catastrophic breakage; it is slow drift into ambiguity, hidden coupling, and process weight.
