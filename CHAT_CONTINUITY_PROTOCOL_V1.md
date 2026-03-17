# CHAT_CONTINUITY_PROTOCOL_V1.md

Status: Active (v1)
Owner: Peter (A), Lyra (R)

## Purpose
Preserve key decisions and context from live chats so work can continue across channels and long threads without losing signal.

## What gets captured (high-signal only)
1. Decisions made (what, why, by whom).
2. Commitments and next actions (owner + due date if present).
3. Preferences or constraints that affect execution.
4. Open questions/blockers that need follow-up.
5. Links to artifacts created (docs, tasks, code, reports).

## Where it is stored
- **Daily raw log:** `memory/YYYY-MM-DD.md`
- **Curated long-term memory (main/private sessions only):** `MEMORY.md`
- **Operational tasks:** canonical TDE state (`os/runtime/tde_state.sqlite`) and generated projection (`os/runtime/TASKS_from_db.md`)
- **Formal decisions/process updates:** relevant `*_V1.md` or governance docs

## Capture rule
After each substantial exchange or decision point, append a short note to the daily memory file using this format:

- Context:
- Decision/Signal:
- Action:
- Owner:
- Due/Trigger:
- Artifact links:

## Channel handoff rule
When switching channel/thread, start with a compact handoff summary:
- Current objective
- Last confirmed decisions
- In-flight tasks
- Immediate next step

## Quality bar
- Prefer concise factual notes over long transcripts.
- Do not copy sensitive material into shared contexts.
- If uncertain whether something matters later, log it briefly.

## Cadence
- Real-time: capture during work.
- Daily: quick consolidation pass.
- Weekly: promote durable lessons/decisions into canonical docs.

## Sprint 2 metrics (OPS-2026-043)

### 1) Handoff completeness score (HCS)
Purpose: measure whether handoff summaries are decision-ready.

Scoring per handoff summary (0-4):
1. Current objective present
2. Last confirmed decisions present
3. In-flight tasks present
4. Immediate next step present

Formula:
- `HCS = (sum points / (4 * number_of_handoffs)) * 100`

Target:
- Green >= 85
- Watch 70-84
- Red < 70

### 2) Stale-context drift signal (SCD)
Purpose: detect when active work diverges from documented continuity state.

Definition (weekly):
- Count notable active items (open tasks/decisions in active execution)
- Count items missing fresh continuity capture (no update in memory/evidence within 48h)

Formula:
- `SCD = missing_fresh_items / total_notable_active_items`

Target:
- Green <= 0.15
- Watch 0.16-0.30
- Red > 0.30

### Weekly evidence artifact
Publish a weekly baseline/checkpoint note at:
- `knowledge/evidence/YYYY-MM-DD__ops-2026-043-chat-continuity-sprint2-weekly-baseline.md`

Minimum contents:
- sample window
- HCS value + denominator
- SCD value + denominator
- key gaps detected
- corrective action for next week
