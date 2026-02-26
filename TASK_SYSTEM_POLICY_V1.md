# TASK_SYSTEM_POLICY_V1.md

Status: Active (v1)  
Owner: Peter (decision owner), Lyra (operating support)

## Purpose
Create a clear, low-noise task operating system that improves flow, prioritization, and decision quality without adding unnecessary process overhead.

## Scope
Applies to all operational work tracked in the workspace task system and rendered in the control panel.

---

## 1) Workflow model

### Canonical statuses
- `inbox`
- `triage`
- `active`
- `waiting`
- `done`
- `archived`

### WIP limits (mandatory)
- **Active:** max 3
- **Triage:** max 10
- **Waiting:** max 10

Rules:
1. No item may move to `active` if Active WIP is at limit.
2. Exception only via **Expedite** class (must be explicitly labeled), and one Active item must be de-prioritized or moved out.
3. WIP violations must be visible in review and corrected same day.

---

## 2) Triage policy (mandatory)

Every inbox item must be resolved into one of:
1. **Next action** (single concrete action)
2. **Project/Epic** (multi-step work; create first next action)
3. **Someday/Maybe** (defer intentionally)
4. **Archive/Trash** (remove from active system)

No indefinite inbox parking.

### Triage SLA
- Inbox item age should not exceed 7 days.
- Items older than 7 days are flagged for forced triage in weekly review.

---

## 3) Definition of Ready (DoR)

An item may move from `triage` to `active` only if all required fields are present:
- [ ] Owner assigned (single accountable owner)
- [ ] Clear outcome or acceptance criteria
- [ ] Dependency status recorded (`none` is valid)
- [ ] Scope is realistically executable in current horizon
- [ ] Priority basis documented (e.g., WSJF rationale or explicit override)

If any required field is missing, the item remains in `triage`.

---

## 4) Definition of Done (DoD)

An item may move to `done` only when:
- [ ] Agreed outcome is met
- [ ] Quality checks for item type are complete
- [ ] Evidence note exists (what changed, where, and why)
- [ ] If external/destructive action was involved: approval reference is linked

If work is complete but evidence is missing, item remains in `active` until documented.

---

## 5) Prioritization policy

### Primary method
Use **WSJF** as default sequencing method for operational backlog.

WSJF = Cost of Delay / Job Size

### Scoring inputs (lightweight)
- Cost of Delay (relative): low/medium/high/critical
- Job Size (relative): XS/S/M/L/XL
- Confidence note: low/medium/high

### Policy guardrails
1. Scores inform decisions; they do not replace judgment.
2. Any manual override must include a short rationale.
3. If confidence is low, score should be treated as provisional.

### Secondary method (optional)
RICE may be used for product/feature bets, not required for daily ops flow.

---

## 6) Role-based decision queue policy (primary navigation)

Primary control panel split is by role:
- **Security**
- **Finance**
- **Operations**
- (optional) Product / Research

Now/Next/Watch may exist as supporting filters only.

### Decision queue minimum fields
- Decision ID
- Decision question
- Recommended option
- Risk level
- Urgency
- Evidence freshness
- Required approver(s)
- Deadline
- Status

### Decision classes
- **Two-way door (reversible):** faster decision cadence, lightweight review
- **One-way door (hard-to-reverse):** explicit rationale + evidence + required approval

---

## 7) Review cadence

### Daily (5–10 min)
- Check Active WIP and blockers
- Resolve WIP limit violations
- Confirm urgent waiting follow-ups

### Weekly (30–60 min)
- Triage Inbox to SLA
- Refine top backlog slice to DoR-compliant state
- Prune stale items
- Review aging WIP and unblock plan

### Monthly (60–90 min)
- Review objective alignment and backlog mix
- Re-evaluate prioritization assumptions
- Archive stale work and reset focus

---

## 8) Automation behavior policy (Lyra)

Lyra defaults to **advisory mode**:
- can propose prioritization, triage outcomes, and splitting/merging suggestions
- can generate checklists and decision drafts
- does not silently execute external/destructive actions

Any high-risk or external action requires approval-gated execution and audit linkage.

---

## 9) Metrics

Track weekly:
- Active WIP compliance rate
- Inbox >7 days count
- % triage items meeting DoR
- Aging WIP count
- Done items with evidence link (% target: 100)
- Reopen rate (Done -> Active)

---

## 10) Exceptions and overrides

Temporary exceptions are allowed only if:
1. Reason is documented
2. Owner is assigned
3. Expiry date is set
4. Follow-up action is created

No permanent exceptions without explicit policy update.

---

## 11) Versioning

- This policy is versioned; updates require dated changelog entry.
- Any future automation changes must remain consistent with this policy unless explicitly revised.
