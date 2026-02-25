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

## Ambition–Pragmatism Principle
**State-of-the-art ambition, pragmatic execution.**

Rule:
- Set an ambitious target state and quality bar.
- Ship the smallest safe version that creates real value now.
- Do not block delivery on non-critical polish.
- Raise the bar in planned increments after each release.

Practical decision framing (required for major initiatives):
1. **Now bar (ship bar):** minimum level to deliver safely and credibly.
2. **Next bar (target bar):** state-of-the-art level to reach through iteration.

Escalation check:
- If “Now bar” compromises safety, trust, or decision quality, do not ship.
- If “Next bar” delays value without reducing meaningful risk, defer to roadmap.

## Make–Open Source–Buy Progression Principle
**Pragmatic sovereignty: optimize time-to-value now, increase ownership over time.**

Default preference order:
1. **Build** (best when strategically core and feasible)
2. **Adopt free open-source** (fast ownership without full build cost)
3. **Buy SaaS** (acceptable default when speed/quality advantage is clear)

Override rule (explicitly allowed):
- Start with **SaaS** when it materially improves time-to-value, quality/functionality, or near-term risk.

Strategic ownership triggers (favor Build or OSS sooner):
- Capability is core differentiation/IP
- Lock-in risk is high
- Long-term economics strongly favor ownership
- Compliance/privacy constraints require deeper control

Progression path (for non-core utilities and evolving capabilities):
1. **Phase 1 — Fastest credible start** (often SaaS)
2. **Phase 2 — Stabilize and learn real usage patterns**
3. **Phase 3 — Migrate to OSS/Build when justified**

Minimum evaluation checklist (before deciding):
- Time-to-value (now)
- Functional quality fit
- 12–24 month total cost
- Lock-in and migration cost
- Security/compliance posture
- Strategic ownership value

## Decision Quality Standard
A decision is “good” if:
- It matches the door type
- The process was proportionate
- Assumptions were explicit
- Reversal/mitigation path is clear
- Learning is captured for future decisions
- Ambition and pragmatism were explicitly balanced (Now vs Next bar)
- Make/OSS/Buy choice is explicit with rationale and progression path

## Version
- v1.2
- Date: 2026-02-25
- Owner: Peter + Lyra
