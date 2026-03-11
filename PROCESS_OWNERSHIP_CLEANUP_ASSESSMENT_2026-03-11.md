# Process Ownership Cleanup Assessment — 2026-03-11

Status: Initial cleanup lens
Owner: Lyra
Basis:
- `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md`
- current shared artifacts in workspace root and `governance/`

## Purpose
Classify current shared artifacts into:
1. valid shared coordination mechanisms
2. valid templates/frameworks
3. likely candidates for narrowing, migration, or retirement

This is not a full refactor plan.
It is a hygiene pass to prevent drift into a parallel central process layer.

## Summary judgment
Current state is acceptable but mixed.

There are already several central artifacts that are clearly legitimate shared coordination mechanisms. There are also a number of older or broader artifacts that may now be too central, too vague, or duplicative relative to product-owned process logic.

The main action is not urgent deletion. It is controlled narrowing and clearer categorization.

## A. Clearly valid shared coordination artifacts
These appear well-justified under the new rule.

### 1. `PRODUCT_REVIEW_PROTOCOL_V1.md`
Assessment: **Keep central**
Why:
- coordinates product reviews across the portfolio
- does not define how one product internally runs
- acts as a shared review contract

### 2. `DELIVERY_MODES_DECISION_FRAMEWORK_V1.md`
Assessment: **Keep central**
Why:
- coordinates mode choice across products
- shapes cross-product packaging decisions
- not owned by any one product

### 3. `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md`
Assessment: **Keep central**
Why:
- architectural meta-rule
- governs ownership boundaries across the whole portfolio

### 4. `PRODUCT_MODEL_STANDARD_V1.md`
Assessment: **Keep central**
Why:
- defines shared product-model contract
- not a product-local operating process

### 5. `PRODUCT_MODEL_MATURITY_V1.md` / `PRODUCT_MODEL_VALIDATION_V1.md`
Assessment: **Keep central**
Why:
- portfolio-wide assessment tools
- governance/quality mechanisms rather than product-local processes

### 6. `PRODUCT_PORTFOLIO_REGISTRY.md` / `PRODUCT_PORTFOLIO_MAP_V1.md`
Assessment: **Keep central**
Why:
- explicit portfolio coordination and boundary mapping

## B. Clearly valid templates / scaffolding artifacts
These are central, but acceptable because they are templates rather than competing sources of process truth.

### 1. `PRODUCT_MODEL_TEMPLATE_PACK_V1.md`
Assessment: **Keep central as template**

### 2. `PRODUCT_REVIEW_TEMPLATE_V1.md`
Assessment: **Keep central as template**

### 3. `DELIVERY_MODES_DECISION_TEMPLATE_V1.md`
Assessment: **Keep central as template**

### 4. `PRODUCT_BOUNDARY_TEMPLATE.md`
Assessment: **Keep central as template**

### 5. `PRODUCT_MANAGEMENT_ARTIFACT_TEMPLATE.md`
Assessment: **Keep central, but likely aging**
Why:
- probably still useful as historical template/scaffold
- should not compete with the newer Product Model standard

## C. Central artifacts that look acceptable but should stay narrow
These are probably valid, but need discipline so they do not become pseudo-operating-manuals.

### 1. `TDE_PRODUCTION_READINESS_GATE_V1.md`
Assessment: **Keep central, narrow**
Why:
- acts as a cross-product/shared readiness gate for Task Management capability activation
- should remain a gate artifact, not expand into a full operating manual

### 2. `INTRA_LYRA_HANDOFF_PROTOCOL_V1.md`
Assessment: **Keep central if scoped to cross-lane / cross-product coordination**
Risk:
- could drift into defining product-local execution habits if not kept narrow

### 3. `PRODUCT_CRON_MODEL_V1.md`
Assessment: **Keep only if it remains a coordination/selection model**
Risk:
- if it starts defining how products internally run recurring work, that likely belongs inside product models

## D. Likely candidates for narrowing, migration, or retirement review
These are the main drift suspects.

### 1. `PROCESS_OWNERSHIP_MODEL_V1.md`
Assessment: **Review urgently for overlap with the new rule**
Why:
- title suggests broad central process modeling
- may now be redundant, superseded, or too expansive relative to the new ownership rule

### 2. `PROCESS_REGISTRY.md`
Assessment: **Review urgently**
Why:
- central registry of processes is high-risk for duplication
- likely only valid if it indexes cross-product coordination mechanisms rather than all processes

### 3. `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md`
Assessment: **Likely too central unless narrowed sharply**
Why:
- "way of working" for products may now belong mostly inside product-owned operating models
- may still be useful only as a narrow cross-product convention layer

### 4. `PRODUCT_RUNTIME_EMBODIMENT_FRAMEWORK_V1.md`
Assessment: **Review for category fit**
Why:
- may be legitimate architecture guidance
- but risks becoming central process/operating guidance if too broad

### 5. `PRODUCT_RUNTIME_EMBODIMENT_MAP_V1.md`
Assessment: **Review for category fit**
Why:
- may be acceptable as a mapping/index artifact
- needs confirmation that it is not duplicating product-owned implementation logic

### 6. `PRODUCT_SESSION_BOOTSTRAP_PACK_V1.md`
Assessment: **Review for ownership fit**
Why:
- may be valid shared coordination for session bootstrapping
- may also duplicate product-local onboarding/operation if too broad

## E. Governance-side artifacts needing category hygiene
Several `governance/` artifacts are probably fine, but should be classified more explicitly as one of:
- policy
- decision record
- coordination mechanism
- evidence / plan / incident artifact

Priority candidates for classification hygiene:
- `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`
- `governance/TDE_PRODUCT_OWNER_WEEKLY_REVIEW_TEMPLATE_V1.md`
- `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md`
- `governance/LYRA_TDE_CONTINUOUS_IMPROVEMENT_SOP_V1.md`
- `governance/SKILLS_DISTRIBUTION_LEARNINGS_FOR_PRODUCT_OWNERS_V1.md`

These may be legitimate, but the naming and location suggest some could now be better understood as product-owned, coordination, or historical artifacts rather than open-ended governance instructions.

## Immediate next actions recommended
1. Review `PROCESS_OWNERSHIP_MODEL_V1.md` and `PROCESS_REGISTRY.md` first.
2. Review `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md` next.
3. Create a simple classification rubric for central artifacts:
   - standard
   - template
   - coordination mechanism
   - governance/policy
   - historical/reference
4. For any artifact that tries to define how a single product operates, migrate or point it back into the owning product model.

## Overall conclusion
The central layer is not out of control, but there are clear candidates that could become a parallel process layer if left unreviewed.

The right response is not mass deletion.
It is:
- classify
- narrow
- migrate where needed
- keep central artifacts focused on standards, templates, and coordination
