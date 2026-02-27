# TASKS.md (Temporary Kanban)

Use this until a dedicated work tool is selected.

## Inbox
- [ ] SEC-AUTO-20260227-01 | Restrict Telegram group command senders via `groupAllowFrom` (or per-group `allowFrom`) to remove critical command-invocation exposure.
- [ ] SEC-AUTO-20260227-02 | Decide and enforce trust-boundary model for multi-user/group usage (separate gateways vs hardened shared runtime sandbox/tool scope).
- [ ] SEC-AUTO-20260227-03 | Confirm reverse-proxy posture for Control UI; if proxied, set `gateway.trustedProxies`, otherwise explicitly keep local-only.
- [ ] IMP-AUTO-20260227-01 | Add lightweight markdown link-check script + cron-safe scope filters to catch local doc drift before reviews.
- [ ] IMP-AUTO-20260227-02 | Add smoke tests for `tools/` parsers (task ID extraction + frontmatter parsing) to prevent silent automation regressions.

## Triage
- [ ] OPS-2026-024 | Sprint 3 kickoff decision: confirm read-first scope freeze (no task write-back in S3)
- [ ] OPS-2026-025 | Approve S3 workflow taxonomy v1 (domain, area, task_type governed values)

## Active
- [ ] OPS-2026-020 | Chief Architect: publish Sprint 3 architecture brief v1 + guardrails pack
- [ ] OPS-2026-021 | Claude Code supplier run: implement S3 Task Center + Skills Visibility from approved prompt
- [ ] OPS-2026-022 | Architecture QA gate: verify S3 against must constraints (taxonomy, DoW subset, redaction)

## Waiting
- [ ] OPS-2026-023 | Sprint 3 closeout pack (release notes + tag + vNext backlog update) after QA pass

## Done
- [x] Create MODEL_ROUTING_POLICY.md
- [x] Create WAYS_OF_WORKING_V1.md
- [x] Create ADR-001_SYSTEMS_OF_RECORD.md
- [x] Create SOP-001_INTAKE_TRIAGE.md
- [x] Create STD-001_DEFINITION_OF_DONE.md
- [x] Create DESIGN_PRINCIPLES.md
- [x] Create DECISION_PRINCIPLES.md
- [x] Set up concrete work tool (Trello) for Option C
- [x] Configure Trello API credentials (key/token/board id)
- [x] Run `tools/trello_sync.py` dry-run then apply
- [x] Add automated Trello sync cron (every 30 min)
- [x] Define task ID + task↔doc linking convention
- [x] Execute first restore test and record evidence (RST-2026-001)
- [x] Run first SEC-001 baseline review and log remediation tasks
- [x] OPS-2026-004 | Harden state-dir permissions (`chmod 700 /Users/lyra/.openclaw`)
- [x] Start 30-day Brave API usage/ROI baseline (`BRAVE_USAGE_BASELINE_2026-03.md`)
- [x] Schedule monthly subscription review cron
- [x] Implement multi-agent v1.1 execution semantics (`AGENT_EXECUTION_SEMANTICS.md`)
- [x] Define permission envelopes per agent (`AGENT_PERMISSION_ENVELOPES.md`)
- [x] Add champion-challenger model routing scorecard + monthly anti-thrash rule (`MODEL_ROUTING_SCORECARD.md`)
- [x] OPS-2026-005 | Clean ineffective denyCommands entries and re-audit
- [x] OPS-2026-007 | Define machine-readable registry schemas (agent/routing/evidence/change)
- [x] OPS-2026-008 | Implement evidence ingestion job (doctor/security -> knowledge evidence entries)
- [x] OPS-2026-009 | Build Control Tower MVP views spec (Now/Next/Watch/Change)
- [x] OPS-2026-010 | Wire evidence ingestion into daily hygiene flow
- [x] OPS-2026-012 | Schedule weekly OpenClaw release delta review
- [x] OPS-2026-013 | Enable embeddings-backed memory indexing (OpenAI embeddings active)
- [x] OPS-2026-016 | Implement autonomous security + continuous-improvement governance sweeps (cron + guardrails + docs)
- [x] OPS-2026-017 | Implement cadence governance policy (throughput-first planning + cadence floor guardrails)
- [x] OPS-2026-026 | Adopt AI-native operating policy v1 + WO/CA templates and wire into SOP/DoD/process registry
