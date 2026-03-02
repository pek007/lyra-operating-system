# TASKS.md (Temporary Kanban)

Use this until a dedicated work tool is selected.

## Inbox
- [ ] SEC-AUTO-20260227-01 | Restrict Telegram group command senders via `groupAllowFrom` (or per-group `allowFrom`) to remove critical command-invocation exposure.
- [ ] SEC-AUTO-20260227-02 | Decide and enforce trust-boundary model for multi-user/group usage (separate gateways vs hardened shared runtime sandbox/tool scope).
- [ ] SEC-AUTO-20260227-03 | Confirm reverse-proxy posture for Control UI; if proxied, set `gateway.trustedProxies`, otherwise explicitly keep local-only.
- [ ] SEC-AUTO-20260228-01 | Resolve persistent `security.trust_model.multi_user_heuristic` warning: choose single-trust boundary or split to separate gateways/identities for group contexts.
- [ ] SEC-AUTO-20260228-02 | Resolve persistent `gateway.trusted_proxies_missing` warning: explicitly document local-only UI posture or configure `gateway.trustedProxies` for actual reverse proxy IPs.
- [ ] IMP-AUTO-20260227-02 | Add smoke tests for `tools/` parsers (task ID extraction + frontmatter parsing) to prevent silent automation regressions.
- [ ] IMP-AUTO-20260228-01 | Automate daily OpenClaw release-delta evidence snapshot (`openclaw --version/status/update status`) into `knowledge/evidence/` for auditable change tracking.

## Triage

## Active
- [ ] TDE-2026-004 | Milestone gate packet for JOB-OWN-001 presented for decision (`knowledge/distilled/2026-03-02__milestone-packet__tde-kernel-s1-s2-gate-for-job-own-001-v1.md`)

## Waiting

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
- [x] OPS-2026-027 | Establish product portfolio setup (registry, boundary template, repo naming standard, dependency rule)
- [x] OPS-2026-028 | Add OpenClaw release-delta tracking SOP and integrate into daily continuous-improvement sweep
- [x] OPS-2026-029 | Implement agent lifecycle SOP + internal job market model; supersede Chief Architect agent plan in favor of Chief Architect job
- [x] OPS-2026-030 | Implement Control Panel post-mortem process hardening (start gate, decision-first MVP, data/system ownership contracts, supplier WIP/evidence rules)
- [x] OPS-2026-031 | Implement system-level direction package (governance layer + runtime mapping) from ChatGPT 5.2 Pro analysis
- [x] OPS-2026-032 | Ingest Claude direction package, deploy compiled runtime charter into AGENTS.md, and align SOUL/USER with non-duplication rule
- [x] OPS-2026-033 | Establish strict OpenClaw config change-control + rollback SOP (preview/approval/apply/validate/rollback)
- [x] OPS-2026-034 | Refine Claude Code prompting system: outcome-oriented schema, explicit modes, stronger verification, and fresh-context recovery rule
- [x] IMP-AUTO-20260227-01 | Added lightweight markdown link-check script (`tools/markdown_link_check.py`) with cron-safe scope filters.
- [x] WO-2026-TDE-KERNEL-S1 | Implemented TDE kernel thin-slice scaffolding (T1–T7 acceptance runner + anti-stall heartbeat/cron hook contract + verification evidence).
- [x] TDE-2026-001 | Formal acceptance sign-off completed for WO-2026-TDE-KERNEL-S1 (JOB-PROD-001 + JOB-ARC-001, owner acknowledged 2026-03-02).
- [x] TDE-2026-002 | Defined S2 WO and planning packet (`WO-2026-TDE-KERNEL-S2.md`, `knowledge/distilled/2026-03-02__packet__tde-kernel-s2-planning-v1.md`).
- [x] TDE-2026-003 | Executed kernel-slice S2 planning packet (progress-state model, anti-stall integration, deterministic routing verification tests).
- [x] TDE-2026-005 | Executed WO-2026-TDE-KERNEL-S2 (heartbeat anti-stall + progress-state classification + routing checks) with S2 evidence artifact.
