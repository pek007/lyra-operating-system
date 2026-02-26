# MODEL_ROUTING_POLICY.md

## Purpose
Provide a practical default for model selection in OpenClaw so we optimize for quality, reliability, speed, and cost.

## Principles
1. Default to the simplest model that can reliably do the job.
2. Escalate model capability only when task complexity or risk justifies it.
3. Keep high-cost models for high-value outputs.
4. Always have a fallback path.
5. Review routing decisions monthly based on real outcomes.

## Current Environment Assumptions
- Primary API path: OpenAI (active)
- Other subscriptions (Claude Pro, Google AI Pro, Grok, Copilot) are interactive plans, not automation APIs by default
- Optional future APIs: Anthropic, Google, etc.
- Optional local fallback model may be added later

## Routing Tiers

### Tier 1 — Default Operational Model (Primary)
**Use for:**
- Daily admin and operations
- Summaries, extraction, formatting, drafting internal notes
- Standard planning and coordination tasks

**Default model:** current OpenAI default in OpenClaw

**Success criteria:**
- Fast turnaround
- Good enough quality with minimal edits
- Stable tool use

---

### Tier 2 — High-Reasoning / High-Stakes Model (Premium lane)
**Use for:**
- Client-facing strategy memos
- Complex synthesis across multiple sources
- Difficult decision frameworks where errors are costly
- High-ambiguity analysis needing stronger judgment

**Candidate model:** Anthropic Opus API (when/if enabled)

**Trigger to route up from Tier 1:**
- Task is client-critical, novel, or high downside risk
- Tier 1 draft quality would require heavy rewrite
- User explicitly asks for "deep-dive" quality

**Guardrail:**
- Use selectively, not as default

---

### Tier 3 — Local Fallback / Utility Model (Resilience lane)
**Use for:**
- Basic summarization and classification
- Simple transformations and cleanup
- Backup operations during API outages
- Privacy-sensitive first-pass drafts (when appropriate)

**Candidate:** small local model (to be selected later)

**Guardrail:**
- No high-stakes final outputs without review

## Task-to-Model Routing Matrix (v1)

- **Inbox/calendar triage:** Tier 1
- **Daily OpenClaw improvement brief (12:00):** Tier 1 (upgrade to Tier 2 only if explicitly requested)
- **Internal process docs / SOP drafts:** Tier 1
- **Client-ready strategic memo:** Tier 2
- **Investment/strategy hypothesis generation:** Tier 1 -> Tier 2 review pass if high importance
- **Data extraction from docs:** Tier 1 (Tier 3 optional for bulk low-risk jobs)
- **Contingency when cloud API fails:** Tier 3

## Escalation Rules
Escalate from Tier 1 to Tier 2 if at least one is true:
1. Deliverable is client-facing and strategically important
2. Subject is highly ambiguous or cross-domain
3. Error cost is high
4. User asks for top-quality/deep-dive output

## Cost & Quality Governance
- Track weekly:
  - Number of Tier 2 invocations
  - Estimated added value (time saved, quality gain)
  - Any quality failures by tier
- Monthly review:
  - Keep / expand / reduce Tier 2 usage
  - Re-evaluate local model utility

## Business Case Rule for Paid API Additions
Adopt a new paid API only if at least one is true:
1. Saves >= 2–3 hours/month of high-value work, or
2. Produces materially better quality on client-critical outputs, or
3. Reduces operational risk (fallback diversity) enough to justify spend

Include in recommendation:
- Monthly cost estimate
- Primary use cases
- Expected benefit
- Decision: adopt now / pilot / defer

## Fallback Policy
If preferred model/provider is unavailable:
1. Retry once on same provider/model
2. Fallback to Tier 1 default
3. If cloud path unavailable, use Tier 3 local (if installed)
4. Mark output as fallback-generated when quality may differ

## Initial Next Steps
1. Keep OpenAI as default for all tasks now.
2. Run this routing policy for 2 weeks.
3. Collect examples where Tier 1 underperforms.
4. Pilot Tier 2 (Opus API) on a narrow set of high-stakes tasks only.
5. Evaluate a local model for resilience and low-cost utility work.

## Codex Reasoning-Effort Rules (operational default)
When routing to GPT-5.3-Codex:
- `medium` for routine coding/ops tasks
- `high` for architecture/security/significant cross-file changes
- `xhigh` only for high-ambiguity, high-consequence long-horizon work

Reasoning effort is a routing/lane decision, not a prompt-writing substitute.
Escalations should be noted in task artifacts with short rationale.

## Version
- v1.1
- Date: 2026-02-26
- Owner: Lyra + Peter
