# PRODUCT_RUNTIME_EMBODIMENT_MAP_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Apply `PRODUCT_RUNTIME_EMBODIMENT_FRAMEWORK_V1.md` to the first three products:
- Control Panel (CP-001)
- Task Management (A-001)
- Governance (A-002)

## 1. Control Panel (CP-001)

### Human-led functions
- portfolio prioritization
- cross-product arbitration
- operating-model decisions
- major escalation and runtime-boundary decisions
- memory/process ownership decisions

### Skill candidates
- Control Panel handoff/coordination skill
- runtime-topology review skill
- memory-governance review skill
- product-onboarding/checklist skill

### Cron candidates
- low-noise coordination hygiene sweep
- periodic memory-governance review
- topology/watch-item review loop

### Plugin candidates (later)
- coordination event substrate / board generation capability
- shared internal orchestration capability if cron+skills prove insufficient

### Activation model
- direct by Peter / central session
- cross-product escalation
- heartbeat visibility
- selective cron review loops

### First implementation priority
- **Control Panel coordination skill**

Reason:
- repeated pattern already exists
- handoff protocol is now standardized
- this would lower friction for cross-lane orchestration immediately

## 2. Task Management (A-001)

### Human-led functions
- major product-shape decisions for TDE
- deployment/cutover judgments
- interface/consumer trade-off calls
- larger operating-model changes

### Skill candidates
- TDE/task-operator skill
- job-bundle setup/update skill
- task-lane intake/triage skill
- TDE operating-impact alignment skill

### Cron candidates
- anti-stall review
- queue hygiene / claim check
- TDE alignment review loop
- bounded task-state/watch review cadence

### Plugin candidates (later)
- deeper TDE-facing capability surface
- reusable task-center/service integration if the product outgrows document/skill patterns

### Activation model
- direct Task Management lane requests
- Control Panel handoffs
- cron-driven review loops
- TDE/runtime-driven bounded task work where appropriate

### First implementation priority
- **Task Management / TDE operator skill**

Reason:
- highest leverage product for repeated execution
- closest to an actual engine
- best fit for structured operating procedures with evidence output

## 3. Governance (A-002)

### Human-led functions
- policy decisions
- authority/risk judgments
- boundary exceptions
- major standards changes

### Skill candidates
- VERIFY-cycle skill
- governance drift review skill
- evidence packaging / closeout skill
- boundary exception review skill

### Cron candidates
- scheduled VERIFY cycle review
- recurring drift/risk check
- cadence reminder with bounded evidence output

### Plugin candidates (later)
- governance validation/enforcement helpers only if repeated runtime integration need emerges

### Activation model
- direct Governance lane requests
- Control Panel escalation/handoff
- scheduled review cadence via cron

### First implementation priority
- **Governance VERIFY-cycle skill**

Reason:
- highly repeatable pattern
- consistency matters
- evidence output is natural
- strong candidate for bounded automation without overreaching

## Portfolio-level recommendation

### First wave
1. Control Panel coordination skill
2. Task Management / TDE operator skill
3. Governance VERIFY-cycle skill

### Second wave
- product-specific cron design for these three products
- one bounded cron loop per product where the benefit is clear

### Third wave
- reassess whether any of the above still feel too awkward in doc/skill/cron form
- only then consider plugin-level embodiment

## Non-recommendations for now
- do not create multiple plugins immediately
- do not create many cron jobs before defining product-level output/noise rules
- do not convert strategic/product-owner judgment into automation prematurely

## Version
- v1.0
- Date: 2026-03-10
