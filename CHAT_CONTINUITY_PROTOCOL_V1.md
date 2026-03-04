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
- **Operational tasks:** `TASKS.md`
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
