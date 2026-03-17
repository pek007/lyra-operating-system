# Project Start Packet — Chat Continuity Execution Track (v1)

## 1) Product Goal (Why)
Ensure high-signal chat outcomes are reliably captured into durable workspace artifacts so context survives channel switches and context-window limits.

## 2) Top 3 Decision Use-Cases
1. Resume execution in any channel/thread with minimal re-briefing overhead.
2. Preserve decision rationale and commitments for auditability and execution quality.
3. Reduce risk of dropped actions caused by long-running threads or fragmented conversations.

## 3) Explicit Non-Goals
- Full transcript archiving of all conversations.
- Automated external publication/sharing of private chat content.
- Replacing existing memory tooling; this is a complementary operational layer.

## 4) Success Metrics
- Metric: High-signal exchanges captured to daily memory within same working day.
- Baseline: Ad hoc capture (inconsistent).
- Target: >=95% capture compliance.
- Time window: First 14 days.

- Metric: Cross-channel handoff summary availability when channel switches occur.
- Baseline: Not standardized.
- Target: 100% of channel switches include compact handoff block.
- Time window: First 14 days.

## 5) Kill Criteria
- Capture workflow creates noticeable drag (>10 minutes/day average) without measurable execution-quality benefit after 2 weeks.
- Material security/privacy risk identified from stored summaries that cannot be mitigated with process controls.

## 6) Boundary Summary
- System of record: Workspace docs (`memory/YYYY-MM-DD.md`, governance/process docs) plus canonical TDE state (`os/runtime/tde_state.sqlite`) with generated projection at `os/runtime/TASKS_from_db.md`. 
- Derived view scope: Compact handoff summaries and status blocks in chat.
- Out of scope: External CRM/PM integrations in v1.

## 7) First MVP (Decision-first)
- Artifact/report/job to ship first: `CHAT_CONTINUITY_PROTOCOL_V1.md` + daily capture discipline + weekly consolidation check.
- Cadence: Real-time capture during execution, daily sweep, weekly consolidation.
- Freshness requirement: Same-day for high-signal items.

## 8) Acceptance for Sprint 1
- Protocol is in force and referenced in task process.
- Daily memory entries include decision/action/owner style capture.
- At least one explicit handoff summary produced when channel/thread changes.
- Task board includes a dedicated continuity task with owner and verification step.

## Approval
- Approver: Peter Eklind
- Date: 2026-03-01
