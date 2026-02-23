# ADR-001: Systems of Record for Work and Knowledge

- **Status:** Proposed (ready for decision)
- **Date:** 2026-02-23
- **Owner:** Peter (A), Lyra (R)

## Context
We need one canonical system for:
1. **Work management** (tasks, intake, prioritization, status, due dates)
2. **Knowledge management** (policies, runbooks, templates, decisions)

Design constraints:
- Low overhead, high reliability
- Strong clarity and traceability
- Suitable for a one-person firm operating at professional-firm quality
- Works well with OpenClaw workflows and incremental improvement

## Decision Criteria
1. Setup friction (lower is better)
2. Ongoing maintenance load
3. Searchability and structure
4. Version history / auditability
5. Collaboration readiness (future contractors)
6. Cost

---

## Options Considered

## Option A — GitHub (private repo) for both work + knowledge
Use GitHub Issues/Projects for work; Markdown docs in repo for knowledge.

### Pros
- Excellent version control and audit trail
- Strong fit for automation and structured workflows
- Easy PR-style review when team grows
- Knowledge and work linked in one ecosystem

### Cons
- Slightly higher setup and usage friction for non-technical workflows
- Issue/project UX can feel heavier for service-style request intake

### Cost
- Low to moderate (depends on plan)

### Best fit when
- We want maximal traceability and future automation around code/process assets

---

## Option B — Notion for both work + knowledge
Use Notion tasks/projects + doc wiki in one workspace.

### Pros
- Very low friction and flexible structure
- Fast to adopt; strong for narrative + databases
- Good UX for planning and documentation in one place

### Cons
- Versioning/audit less rigorous than git-based approach
- Can drift into inconsistent structures without discipline
- API/automation workflows are possible but can be more brittle

### Cost
- Typically low to moderate depending on tier

### Best fit when
- Speed and usability are top priorities, with moderate governance needs

---

## Option C — Hybrid (Recommended): Work in a lightweight task tool, Knowledge in Git repo
Suggested implementation:
- **Work system:** linear task board (kanban-style) in a simple task manager
- **Knowledge system:** this workspace Git repo (`.md` files, versioned)

### Pros
- Best balance: easy daily operations + strong documentation governance
- Knowledge base remains portable, auditable, and automation-friendly
- Work board remains fast and low-friction
- Scales to contractors: tasks in tool, controlled docs in repo

### Cons
- Two systems to maintain (requires clear linking discipline)
- Need simple linking convention between tasks and docs

### Cost
- Low to moderate depending on task tool

### Best fit when
- We want pragmatic execution now without sacrificing long-term control

---

## Recommendation
**Adopt Option C (Hybrid) for v1.**

### Why this
- Minimizes operational friction day-to-day
- Preserves enterprise-grade knowledge control (versioned docs)
- Matches our current setup and incremental strategy
- De-risks future scaling and compliance posture

## Operating Rules (if Option C is approved)
1. Every significant task gets a task ID in work system.
2. Every decision/policy/runbook lives in Git knowledge repo.
3. Task cards link to canonical docs; docs can reference task IDs.
4. “Done” requires doc updates when process/decision changed.

## Initial Tooling Suggestion (v1)
- **Knowledge:** current workspace Git repo (already active)
- **Work:** start with a simple kanban tool you already use or can adopt quickly
- If undecided this week, use a temporary `TASKS.md` kanban in repo for 7 days, then migrate.

## Decision Required
Please choose one:
- Approve Option A
- Approve Option B
- Approve Option C (recommended)
