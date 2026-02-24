# AGENT_PERMISSION_ENVELOPES.md

## Purpose
Define least-privilege boundaries by agent role.

| Agent Role | Read Scope | Write Scope | Tool Scope | Requires Approval |
|---|---|---|---|---|
| Control Tower (Main) | All OS + strategy docs | All docs | Full orchestration tools | High-risk external actions |
| Ops/Control | Registries, metrics, tasks, runbooks | TASKS/registries/metrics | shell(read/check), cron review, status checks | Destructive commands, external sends |
| Security & Audit | Security docs, logs, configs, incidents | SEC/IR/GOV docs, risk register | security audit, doctor, status/log tools | Credential rotations (unless incident), policy-breaking changes |
| Improvement/R&D | All process docs, benchmark inputs | proposals, improvement docs, backlog items | web_search/web_fetch, analysis tools | Direct production config changes |
| Build Agent | code/scripts/tool docs | tools, scripts, build docs | shell/git/dev tooling | External deployment, public release, secret handling changes |
| Research Agent | source corpus, research inputs | research packs | web tools, fetch, synthesis | Client-facing publishing |
| Content Delivery Agent | research packs, style guides | draft deliverables | drafting/editing | Final send/publication |

## General Guardrails
- No agent stores secrets in docs.
- No external message send without explicit intent unless pre-approved workflow says so.
- All high-risk actions must be logged.

## Version
- v1.0
- Date: 2026-02-24
