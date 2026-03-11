# Delivery-as-Code Design v1

Status: Draft
Owner: Lyra
Date: 2026-03-11

## 1. Definition
Delivery-as-Code is the executable control layer that moves a unit of work from intent to accepted outcome using machine-readable state, policy-governed transitions, mandatory evidence, and auditable approvals.

It is broader than CI/CD.
It covers software delivery, operational/process delivery, research-backed change work, and any other work that should be executed end to end with professional traceability.

## 2. Why this exists
Lyra OS is moving from document-led process to executable operating systems.
That makes delivery a prime candidate for codification because autonomous execution only becomes trustworthy when:
- stages are explicit
- gates are enforced
- evidence is attached at each stage
- deviations are visible
- approvals are captured formally
- human-readable documentation is rendered from operational truth

## 3. Strategic role in Lyra OS
Delivery-as-Code should become the standard operating layer between:
- product intent
- work execution
- verification
- release/handoff
- post-delivery learning

It should be used by TDE as both:
1. a product capability to manage work autonomously
2. a proving ground for autonomous end-to-end delivery itself

Design principle:
**Use TDE to build Delivery-as-Code, then use Delivery-as-Code to govern TDE and other products.**

## 4. Scope
### In scope
- delivery object model
- lifecycle/state machine
- policy and approval rules
- evidence requirements
- release/handoff packet generation
- exception/deviation handling
- audit trail design
- rendered professional outputs generated from canonical state

### Out of scope in v1
- full generalized workflow engine for every product type
- sophisticated event bus or direct-dispatch chains by default
- replacing all existing docs immediately
- fully automated external release authority for high-risk changes

## 5. Core principles
1. **Operational truth first**
   Canonical state, policy, and evidence are primary. Narrative documents are rendered outputs or curated summaries.

2. **Outcome over process theater**
   Every required step must improve quality, safety, clarity, or auditability.

3. **Fail closed on unclear authority**
   If approval, risk class, or policy state is ambiguous, progression stops.

4. **Evidence before advancement**
   A stage is not complete because someone says so. It is complete when required evidence exists and validates.

5. **Human judgment stays at high-consequence boundaries**
   The system should automate preparation, checking, and packet assembly; humans should decide irreversible or material-risk boundaries.

6. **Render, don’t manually retype**
   Release notes, decision memos, readiness packets, and audit packs should be generated from canonical delivery state whenever possible.

7. **One delivery model, many work types**
   Software, process, policy, and operational improvements should share one governing shape, with type-specific evidence packs where needed.

## 6. Delivery unit
The core object should be a **Delivery Unit (DU)**.

A Delivery Unit is the smallest governed package of work that should move through a full delivery lifecycle and leave an auditable trail.

Examples:
- a software feature/change
- a process redesign
- a policy-pack update
- a schema-pack change
- an ops-pack rollout
- a TDE capability slice

### Minimum fields for a Delivery Unit
- `delivery_unit_id`
- `title`
- `product_id`
- `work_type` (`software|process|policy|schema|ops|research-backed-change|other`)
- `objective_id` or strategic linkage
- `owner`
- `delivery_mode`
- `risk_class`
- `verification_class`
- `current_state`
- `approval_profile`
- `scope_statement`
- `non_goals`
- `acceptance_criteria[]`
- `dependencies[]`
- `required_evidence[]`
- `exceptions[]`
- `decision_log[]`
- `artifact_refs[]`
- `rendered_outputs[]`

## 7. State model
Recommended v1 lifecycle:
- `proposed`
- `qualified`
- `planned`
- `in_execution`
- `in_verification`
- `release_recommended`
- `awaiting_approval`
- `approved`
- `released` or `handed_off`
- `verified_in_use`
- `closed`
- `blocked`
- `retired`

### State intent
- `proposed`: candidate exists but is not yet ready to plan
- `qualified`: objective, scope, and risk are clear enough to enter delivery
- `planned`: execution contract is ready
- `in_execution`: work is being performed
- `in_verification`: implementation complete enough for checks/review
- `release_recommended`: system assembled a release/handoff recommendation packet
- `awaiting_approval`: waiting on human/policy boundary
- `approved`: approved for release/handoff
- `released` / `handed_off`: transition executed
- `verified_in_use`: post-release/post-handoff confirmation captured
- `closed`: complete with learning captured
- `blocked`: progression halted by unmet dependency/gate
- `retired`: intentionally stopped

## 8. Standard lifecycle gates
### Gate 1: Qualification
Required:
- objective linkage
- named owner
- scope and non-goals
- initial risk class
- decision on delivery mode

### Gate 2: Planning
Required:
- execution packet/work order
- acceptance criteria
- verification plan
- dependency declaration
- approval profile
- evidence requirements

### Gate 3: Execution completion
Required:
- claimed work completed
- changed artifacts linked
- implementation notes captured
- deviations logged

### Gate 4: Verification
Required evidence according to work type, for example:
- software: tests, static checks, review notes, change summary
- process: pilot evidence, walkthrough, control impact note, operating instructions
- policy: rule diff, affected scope, conflict check, approval note
- ops: run proof, observability note, rollback/recovery note

### Gate 5: Release/Handoff recommendation
Required:
- assembled release/handoff packet
- known risks summary
- unresolved exceptions summary
- recommendation with rationale

### Gate 6: Approval
Required:
- explicit approver or policy-based autonomous approval rule
- decision timestamp
- decision rationale

### Gate 7: Post-delivery verification
Required:
- confirmation that the change works in use
- any incident/issues logged
- learning or miss captured

## 9. Policy layer
Delivery-as-Code needs a machine-readable policy layer controlling:
- who can move which state transitions
- which risk classes require human approval
- which evidence types are mandatory by work type and risk class
- which exceptions are allowed
- what blocks release/handoff automatically
- when autonomous chaining is allowed

### Policy examples
- high-risk software changes cannot auto-release
- process changes affecting governance require approval
- no DU can advance to `in_execution` without acceptance criteria and verification plan
- no DU can close while required post-delivery verification is missing

## 10. Evidence layer
Evidence should be treated as a first-class object, not just attached prose.

### EvidenceRecord fields
- `evidence_id`
- `delivery_unit_id`
- `evidence_type`
- `generated_at`
- `producer`
- `artifact_path` or payload reference
- `validation_status`
- `summary`
- `related_gate`

### Evidence categories
- design/spec evidence
- implementation evidence
- verification evidence
- risk evidence
- approval evidence
- release/handoff evidence
- post-delivery verification evidence
- retrospective/learning evidence

## 11. Decision and exception handling
Two supporting objects should sit beside the DU:

### DecisionRecord
Captures material delivery decisions.
Fields:
- `decision_id`
- `delivery_unit_id`
- `decision_type`
- `decision_owner`
- `options_considered`
- `decision`
- `rationale`
- `timestamp`
- `evidence_refs[]`

### ExceptionRecord
Captures deviations from the standard path.
Fields:
- `exception_id`
- `delivery_unit_id`
- `exception_type`
- `opened_at`
- `owner`
- `reason`
- `approved_by`
- `expiry_or_review_date`
- `status`
- `closure_note`

This is how the system avoids false professionalism. If the team deviates, the deviation is visible and governable.

## 12. Rendering layer
The operating system should render professional outputs from canonical delivery state.

### Standard rendered outputs
- delivery brief
- implementation packet
- verification packet
- release/handoff packet
- approval memo
- audit pack
- post-delivery review
- executive status summary

### Rendering rule
Rendered documents should be generated from DU state/evidence where possible, then optionally curated for audience polish.
That preserves professional presentation without making prose the primary source of truth.

## 13. Recommended filesystem / artifact shape
A pragmatic v1 directory structure:

```text
products/<product>/delivery-units/<DU-ID>/
  DELIVERY_UNIT.yaml
  STATE.yaml
  WORK_ORDER.md
  DECISIONS.md
  EXCEPTIONS.md
  EVIDENCE/
    <timestamp>__<type>__<slug>.md
    <timestamp>__<type>__<slug>.json
  RENDERED/
    DELIVERY_BRIEF.md
    VERIFICATION_PACKET.md
    RELEASE_PACKET.md
    POST_DELIVERY_REVIEW.md
```

For TDE-managed execution, the same shape can also be represented canonically in DB/state with rendered filesystem projections.

## 14. Relationship to existing Lyra OS artifacts
This design should not replace current artifacts immediately.
It should absorb and reorganize them over time.

### Existing artifacts that map well
- Work Orders already approximate execution contracts
- TDE evidence artifacts already approximate first-class evidence
- production/readiness gates already approximate release recommendation controls
- delivery mode framework already helps choose the vehicle
- TDE chaining design already points toward controlled lifecycle progression

### Migration stance
Short term:
- keep current docs
- add Delivery Unit structure around them
- start rendering key packets from canonical delivery state

Medium term:
- make gate progression machine-checkable
- make evidence mandatory by policy
- reduce hand-written status/reporting

Long term:
- docs become views and curated summaries over delivery state

## 15. How this should work with TDE
### v1 integration model
TDE should manage Delivery Units using state-driven progression rather than fully freeform autonomous chains.

Recommended pattern:
1. create DU
2. qualify and plan DU
3. execute bounded tasks/work orders
4. collect evidence into canonical store
5. evaluate gate rules deterministically
6. render packet(s)
7. pause for approval where policy requires
8. execute release/handoff
9. verify in use
10. close with learning

This aligns with the current TDE preference for scheduled ticks, canonical state, fail-closed checks, and evidence artifacts.

## 16. Work-type profiles
Delivery-as-Code should support profiles instead of one-size-fits-all evidence.

### Software profile
Needs:
- implementation packet
- code diff linkage
- tests/checks
- review evidence
- release notes
- rollback note if relevant

### Process profile
Needs:
- process definition/change diff
- pilot or walkthrough evidence
- control/risk note
- adoption instructions
- review cadence definition

### Policy profile
Needs:
- policy diff
- impacted products/scope
- conflict check
- approval evidence
- effective date

### Ops profile
Needs:
- runtime boundary note
- observability evidence
- recovery/rollback path
- canary/proof case if relevant

## 17. Metrics
Core metrics should balance throughput, quality, and control.

### Throughput / flow
- lead time by work type
- cycle time by state
- WIP by lane/profile
- blocked age

### Quality / stability
- verification pass rate
- post-release issue rate
- change fail rate for software DUs
- exception rate

### Governance / auditability
- % of DUs with complete evidence packs
- % of transitions executed with policy validation
- approval latency
- % of rendered outputs generated from canonical state

### Learning
- % of closed DUs with post-delivery review
- retro-to-policy conversion rate
- miss recurrence rate

## 18. Decision recommendation
Adopt Delivery-as-Code as the standard design direction for the Delivery product and as a governing pattern for TDE-enabled autonomous execution.

## 19. Recommended next moves
### Immediate
1. approve the concept and definition
2. define the Delivery Unit schema v1
3. define state-transition policy v1
4. pilot one real TDE slice as a DU end to end

### Next
5. define rendered packet templates
6. attach evidence requirements by work-type/risk profile
7. wire deterministic gate checks into TDE tick flow
8. add post-delivery verification and closeout writeback

### Later
9. support limited successor activation/creation for approved workflow families
10. generalize from TDE pilot into cross-product delivery capability

## 20. What I would want researched further
I think we already have enough to proceed with a v1 design.
If you want stronger external grounding before codifying policy, the highest-value research gaps are:
- release governance patterns outside pure software CI/CD
- evidence and approval models for autonomous/agentic operations
- practical examples of machine-readable workflow + human-readable audit rendering
- exception-management patterns in high-trust professional services or regulated delivery

That said, I would not wait for more research to start the pilot.
The local body of work is already sufficient to begin.