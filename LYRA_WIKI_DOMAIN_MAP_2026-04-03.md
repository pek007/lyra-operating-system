# Lyra Wiki Domain Map

Date: 2026-04-03
Owner: Lyra
Status: Draft domain map

## Purpose
Define the first top-level domain structure for the Lyra wiki as the human-facing compiled-wiki representation of Lyra-level knowledge.

This map is for the **Lyra wiki**, not the PXS wiki.
The Lyra wiki should focus on cross-context capability, architecture, controls, patterns, and system knowledge used by Lyra across workspaces.

---

## Core design rule
The Lyra wiki should represent:
- reusable Lyra-level knowledge
- cross-workspace patterns
- capability and architecture understanding
- control and governance concepts
- tool and runtime patterns

It should not become:
- a dump of every dated note
- a duplicate of operational state surfaces
- a merged business wiki for PXS domain knowledge

---

## Proposed top-level domains

### 1. Capabilities
Purpose:
- represent Lyra’s reusable capabilities as concepts, models, patterns, and implementation status

Examples:
- Knowledge Compilation
- Control Panel coordination
- Governance verification
- Task/decision support
- Security posture and hardening capabilities
- Reporting/synthesis capabilities

Why this domain matters:
This is likely the most important top-level domain because Lyra is fundamentally a capability-bearing system.

---

### 2. Architecture
Purpose:
- represent Lyra’s system architecture, runtime model, interfaces, boundaries, components, and design patterns

Examples:
- runtime architecture
- agent/session model
- tool model
- memory architecture
- workspace model
- trust boundaries
- cross-product architecture concepts

Why this domain matters:
A great deal of Lyra knowledge is architectural rather than merely topical.

---

### 3. Controls & Security
Purpose:
- represent reusable control patterns, security concepts, threat models, hardening approaches, and evidence-backed posture knowledge

Examples:
- prompt injection defense
- trust-boundary patterns
- least privilege for agents
- sandboxing models
- approval-gating patterns
- traceability standards
- runtime risk concepts

Why this domain matters:
Security and control knowledge is cross-cutting and should be reusable rather than rediscovered each time.

---

### 4. Operating Patterns
Purpose:
- represent the repeatable ways Lyra operates, coordinates, reviews, synthesizes, escalates, and improves work

Examples:
- nightly review patterns
- handoff patterns
- heartbeat patterns
- error-management loops
- portfolio review patterns
- capability rollout patterns
- evidence-to-capability translation pattern

Why this domain matters:
Many of Lyra’s most valuable assets are not facts but good operating patterns.

---

### 5. Tools & Agents
Purpose:
- represent knowledge about tools, agent patterns, tool-use strategy, runtime constraints, and external-system interaction patterns

Examples:
- browser-use patterns
- tool-selection heuristics
- workflow vs agent patterns
- runtime/tool blast-radius patterns
- tool safety implications
- agent role patterns

Why this domain matters:
Lyra’s performance depends heavily on tool and agent behavior.

---

### 6. Governance & Authority
Purpose:
- represent authority models, decision-rights patterns, governance concepts, review triggers, and escalation logic

Examples:
- authority boundaries
- governance layers
- residual-risk decision logic
- product vs capability ownership patterns
- cross-context authority distinctions

Why this domain matters:
Lyra operates in a high-judgment environment where governance clarity matters.

---

### 7. Research & Intelligence Methods
Purpose:
- represent reusable research methods, synthesis methods, evidence-handling methods, and intelligence-building patterns used by Lyra across contexts

Examples:
- source evaluation patterns
- compiled wiki method
- linting/health-check patterns
- comparative research methods
- evidence translation patterns

Why this domain matters:
This is where Lyra’s meta-level research methodology belongs.

---

## Optional later domains
These may emerge later if needed, but should not be created too early:

### A. Entities
For specific tools, vendors, models, standards, protocols, or named systems that deserve their own pages.

### B. Glossary / vocabulary
For standardization of recurring Lyra terms where ambiguity becomes costly.

### C. History / evolution
For major architecture/capability evolution timelines if that becomes useful.

---

## Domain relationships

### Capabilities ↔ Architecture
Capabilities describe what Lyra can do; Architecture describes how that is realized.

### Controls & Security ↔ Tools & Agents
Security patterns often constrain or shape tool/agent usage.

### Operating Patterns ↔ Governance & Authority
Operating patterns describe how work is done; governance describes what authority applies when doing it.

### Research & Intelligence Methods ↔ all other domains
Research and intelligence methods are cross-cutting and help update every other domain.

---

## What should likely become the first wiki pages

### In Capabilities
- Knowledge Compilation
- Prompt Injection Defense
- Control Panel Coordination

### In Architecture
- Runtime Model
- Trust Boundary Model
- Memory Architecture

### In Controls & Security
- Prompt Injection
- Least Privilege for Agents
- Minimum Traceability for High-Risk Actions

### In Operating Patterns
- Nightly Learn/Replan Pattern
- Error-to-Capability Translation Pattern
- Bounded Workflow vs Agent Pattern

### In Tools & Agents
- Browser Use Pattern
- Workflow vs Agent
- Tool Blast Radius

### In Governance & Authority
- Capability vs Product Ownership
- Governance Escalation Pattern
- Operational Truth vs Compiled Knowledge Boundary

### In Research & Intelligence Methods
- Knowledge Compilation Method
- Compiled Wiki Method
- Lint/Health Check Method

---

## Bottom line
The Lyra wiki should be organized around reusable Lyra-level knowledge domains, not around business domains or transient execution artifacts.

The most important initial top-level domains are:
1. Capabilities
2. Architecture
3. Controls & Security
4. Operating Patterns
5. Tools & Agents
6. Governance & Authority
7. Research & Intelligence Methods

This is enough structure to start making the wiki legible without overdesigning it too early.
