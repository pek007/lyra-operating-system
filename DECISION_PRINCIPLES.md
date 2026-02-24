# DECISION_PRINCIPLES.md

## Purpose
Improve decision quality and speed by matching effort to decision impact.

## Decision Taxonomy

## Type 1: One-way door (hard/expensive to reverse)
Examples:
- Core architecture choices
- New paid vendor commitments
- Security/privacy posture changes
- Client-critical methodology changes

**Rule:** Slow down, deepen analysis, and seek external signal.

Required before decision:
1. Problem definition and success criteria
2. 2–3 options with trade-offs
3. Risk analysis (downside, failure modes, mitigations)
4. Cost/benefit and opportunity cost
5. External perspective (e.g., Deep Research or expert review)
6. Explicit decision owner and review date

## Type 2: Two-way door (reversible)
Examples:
- Workflow tweaks
- UI/layout experiments
- Draft templates
- Low-risk tooling experiments

**Rule:** Decide fast, test in production, and iterate.

Required before decision:
1. Hypothesis (what we expect to improve)
2. Small safe-to-fail scope
3. Timebox (e.g., 1–2 weeks)
4. Rollback trigger

---

## Decision Effort Allocation Rule
- **Two-way door:** minimize analysis, maximize speed and learning.
- **One-way door:** maximize clarity and external input before committing.

Target split:
- Spend little time on reversible decisions.
- Spend substantial time on critical irreversible decisions.

---

## Decision Process (standard)
1. Classify: Type 1 or Type 2
2. Choose effort level accordingly
3. Capture in `DECISIONS.md` using template
4. Set review date (especially for Type 1)
5. Evaluate outcomes and update principles if needed

## Escalation Trigger (force Type 1 treatment)
If any condition is true, treat as one-way door:
- High reputational downside
- Material recurring cost
- Security/compliance impact
- Hard migration/reversal cost
- High dependency lock-in risk

## External Input Policy
For Type 1 decisions, gather at least one external perspective:
- OpenAI Deep Research synthesis, and/or
- Domain expert input, and/or
- Vendor-neutral benchmark material

External input should inform, not replace, final judgment.

## Decision Quality Standard
A decision is “good” if:
- It matches the door type
- The process was proportionate
- Assumptions were explicit
- Reversal/mitigation path is clear
- Learning is captured for future decisions

## Version
- v1.0
- Date: 2026-02-23
- Owner: Peter + Lyra
