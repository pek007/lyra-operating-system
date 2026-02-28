# Internal Job Market Model v1

## Purpose
Manage responsibilities as **jobs** that can be assigned to the best execution surface over time. Jobs are not bound 1:1 to agents.

## Model
- One runtime can hold multiple jobs.
- One job can move between runtimes as needs change.
- Job requirements drive agent lifecycle decisions.

## Job Record Schema
- Job ID
- Job Name
- Domain (OS / PX / Shared)
- Mission and outcomes
- Decision rights
- Required execution profile:
  - quality/reasoning level
  - tools and side effects allowed
  - memory scope
  - trust boundary
  - latency/cost target
- Preferred runtime default
- Escalation triggers
- KPI/acceptance signals
- Current assignee (session/sub-agent/persistent agent/gateway)
- Review cadence

## Assignment Rules
1. Start with existing runtime + session split.
2. Use sub-agent for parallel or independent bounded runs.
3. Promote to persistent agent only for durable boundary differences.
4. Use separate gateway/host when trust boundary is materially different.

## Job Change Process
1. Propose change (new job / changed requirement / retired job)
2. Re-score execution profile
3. Re-assign runtime if needed
4. Update job record + dependencies + KPI target

## Initial Job Catalog

### JOB-SEC-001 — Head of Security
- Domain: OS/PX Shared
- Mission: security posture monitoring, risk detection, hardening proposals
- Execution profile: high tool discipline, high trust sensitivity, audit trail mandatory
- Preferred runtime: main agent + isolated sub-agent runs; persistent specialist only if boundary divergence becomes durable

### JOB-ENG-001 — Software Developer
- Domain: OS/PX Shared
- Mission: implement approved work orders with verification evidence
- Execution profile: code tools, tests, bounded execution contracts, high throughput
- Preferred runtime: supplier sub-agents and/or coding workbench

### JOB-AUD-001 — Auditor
- Domain: OS/PX Shared
- Mission: independent review of decisions/changes/controls
- Execution profile: read-heavy, critique-oriented, limited side effects
- Preferred runtime: separate session or sub-agent with independent prompt profile

### JOB-ARC-001 — Chief Architect (Job, not agent)
- Domain: OS/PX Shared
- Mission: architecture constraints, boundary governance, ADR quality, sign-off recommendations
- Execution profile: high reasoning, low direct side effects, strict evidence requirements
- Preferred runtime: main agent ownership + dedicated architecture review sessions/sub-agents

## Governance Cadence
- Weekly: open jobs and assignment health
- Monthly: profile fit review + consolidation opportunities
- Quarterly: job catalog refactoring and retirement

## Version
- v1.0
- Date: 2026-02-28
- Owner: Peter/Lyra
