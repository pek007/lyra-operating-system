# Skill Portfolio Registry

Status: Active draft v1
Owner: Lyra
Date: 2026-03-19

## Purpose
Maintain explicit ownership, classification, lifecycle state, and review expectations for the current skill estate.

This registry is the governance surface for Skills.
It complements skill folder metadata and prevents loose, unowned skills.

## Category definitions
- **shared-platform** — shared tool/API/runtime/operator enablement
- **product-capability** — skill implementing or exposing a product-owned capability
- **transitional-local** — local exploratory skill not yet promoted or scheduled for retirement

## Portfolio summary
- Total scanned skills: 55
- Core shared skills: 53
- ACP extension skills: 1
- Workspace-local skills: 1

## Current local / governed skills

| Skill | Category | Owner | Product | Capability ID | Lifecycle | Readiness | Review date | Notes |
|---|---|---|---|---|---|---|---|---|
| control-panel-coordination | product-capability | Lyra via Control Panel | CP-001 | CP-001.C1 (proposed) | building | draft | 2026-03-26 | First local product-capability skill; normalize metadata and link to capability record |
| skill-governance | product-capability | Lyra via Governance | A-008 | A-008.C5 | building | draft | 2026-03-26 | Meta-skill for create/audit/test/improve/constrain/retire discipline across the skill portfolio |

## Skills requiring immediate cleanup

| Skill | Category | Owner | Product | Capability ID | Lifecycle | Readiness | Review date | Notes |
|---|---|---|---|---|---|---|---|---|
| canvas | shared-platform | OpenClaw platform | Platform/shared | n/a | active | usable | 2026-04-02 | Missing/weak description; trigger quality should be fixed upstream |

## Shared-platform portfolio groups
These groups are not yet fully row-modeled individually in v1, but are recognized as governed portfolio classes.

### Communication / knowledge / productivity
- 1password
- apple-notes
- apple-reminders
- bear-notes
- bluebubbles
- discord
- github
- gog
- himalaya
- imsg
- notion
- obsidian
- slack
- things-mac
- trello
- wacli
- xurl

### Device / media / environment
- camsnap
- eightctl
- gifgrep
- nano-banana-pro
- nano-pdf
- openai-image-gen
- openai-whisper
- openai-whisper-api
- openhue
- peekaboo
- sag
- sherpa-onnx-tts
- songsee
- sonoscli
- spotify-player
- video-frames
- voice-call
- weather

### Runtime / operator / platform tooling
- acp-router
- blogwatcher
- blucli
- clawhub
- coding-agent
- gemini
- gh-issues
- goplaces
- mcporter
- model-usage
- node-connect
- oracle
- ordercli
- session-logs
- skill-creator
- summarize
- tmux

## Current local / governed skills

| Skill | Category | Owner | Product | Capability ID | Lifecycle | Readiness | Review date | Notes |
|---|---|---|---|---|---|---|---|---|
| control-panel-coordination | product-capability | Lyra via Control Panel | CP-001 | CP-001.C1 (proposed) | building | draft | 2026-03-26 | First local product-capability skill; normalize metadata and link to capability record |
| skill-governance | product-capability | Lyra via Governance | A-008 | A-008.C5 | building | draft | 2026-03-26 | Meta-skill for create/audit/test/improve/constrain/retire discipline across the skill portfolio |
| governance-verify-cycle | product-capability | Lyra via Governance | A-008 | A-008.C6 | building | draft | 2026-03-26 | Bounded governance verification cycle with deterministic evidence/output expectations |

## Planned product-capability skills
These are the leading candidates for the next governed implementation wave.

| Skill | Category | Owner | Product | Capability ID | Lifecycle | Readiness | Review date | Notes |
|---|---|---|---|---|---|---|---|---|
| task-management-tde-operator | product-capability | Lyra via Task Management | A-007 | A-007.C1 (proposed) | proposed | draft | 2026-03-26 | Bounded TDE operator workflow with continuity discipline |
| delivery-verification | product-capability | Lyra via Delivery | A-006 | A-006.C1 (proposed) | proposed | draft | 2026-03-26 | Verification-heavy skill for evidence-backed delivery checks |
| security-health-audit | product-capability | Lyra via Security | A-004 | A-004.C1 (proposed) | proposed | draft | 2026-03-26 | Security/deployment posture verification skill |
| interfaces-contract-validate | product-capability | Lyra via Interfaces | A-009 | A-009.C1 (proposed) | proposed | draft | 2026-03-26 | Contract-pack / compatibility / packaging validation |

## Registry maintenance rules
- Every local skill must appear in this registry.
- Every product-capability skill must have an owning product and capability ID.
- Transitional-local skills must carry either a promotion path or a retirement trigger.
- Shared-platform skills may be grouped in early versions, but materially important ones should be row-modeled over time.
- Reviews should update lifecycle/readiness, not just notes.

## Next expansion path
Future versions should add row-level registry records for:
- all local/product capability skills
- constrained shared-platform skills
- high-importance shared skills with non-trivial maintenance burden

## Version
- v1.0
- Date: 2026-03-19
