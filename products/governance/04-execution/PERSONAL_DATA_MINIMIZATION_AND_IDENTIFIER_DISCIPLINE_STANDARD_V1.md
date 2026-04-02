# Personal Data Minimization and Identifier Discipline Standard v1

Status: Draft active standard
Owner: Governance Product (`A-008`)
Date: 2026-04-02
Related capability: `products/governance/06-architecture/CAPABILITIES.md` (`A-008.C6`)

## Purpose
Define a default governance rule for how Lyra OS and downstream workspaces should reference people, organizations, and other stakeholders in durable operating artifacts.

The intent is to reduce unnecessary spread of personal data, improve privacy/compliance posture, and create more portable operating artifacts without making execution harder.

## Core rule
Use the **least identifying reference that still preserves operational clarity**.

Default to:
- company name
- account name
- project name
- role title
- stakeholder/contact ID
- case/work item ID

Use a personal name only when the identity of the specific person is materially necessary.

## Why this standard exists
Names and other direct identifiers are personal data when they identify or can identify a person.

That does not make all use of names forbidden. It does mean durable operating artifacts should avoid embedding personal data where a less identifying reference would work just as well.

This standard supports:
- privacy and data minimization
- cleaner repo/workspace structure
- more reusable artifacts
- lower accidental replication of personal data across comments, filenames, paths, and notes

## Scope
This standard applies to durable/internal operating artifacts in Lyra OS and to downstream workspaces that adopt it through their local authority surfaces.

Included examples:
- folder and file naming
- canonical operational docs
- governance/process artifacts
- issue/PR comments and review notes where durable trace is created
- task/decision/error artifact names and references
- workspace-local operating-package artifacts

This standard does not by itself govern external legal/contractual documents, CRM records, or cases where the named individual is the operative entity and identity is materially required.

## Default naming and reference rules
### 1. Paths and filenames
Prefer:
- company / workspace / project / account / case / stakeholder-ID based naming

Avoid by default:
- personal names in folder names
- personal names in filenames
- full names embedded in durable canonical artifact paths

### 2. Document content
Prefer:
- company or role references when they are sufficient
- internal stakeholder/contact IDs if the exact person does not need to be named repeatedly

Allowed when necessary:
- naming an individual approver, signer, contact owner, or participant when identity materially matters

### 3. Comments and review threads
Prefer:
- role/company-based references in routine GitHub or repo review discussion

Use personal names only when:
- the exact person is operationally relevant
- ambiguity cannot otherwise be resolved cleanly
- the discussion is specifically about that person as a responsible actor/contact

### 4. Mapping pattern
Where recurring person references are needed, prefer:
- a controlled local identifier such as `STK-###`, `CONTACT-###`, or equivalent
- a restricted mapping surface where the name-to-ID relationship is maintained if needed

Do not spread the name itself into every downstream artifact when a stable internal reference is sufficient.

## Decision test
Before using a personal name in a durable artifact, ask:
1. Is the exact person materially necessary here?
2. Would role/company/ID preserve enough clarity?
3. Will this artifact replicate widely or live a long time?
4. Is this the best place for personal data to persist?

If role/company/ID is sufficient, prefer that.

## Exceptions
Using personal names is acceptable when the exact person is materially required, including for example:
- legal/contractual sign-off or named approval
- participant lists where identity matters
- contact records
- relationship-management notes
- cases where the person rather than the organization is the relevant actor
- evidence or audit trails that would be weakened by removing the individual identity

## Workspace adoption rule
A downstream workspace should not be assumed to adopt this standard automatically just because it exists in Lyra OS.

Adoption should be made explicit through the local workspace operating package, typically by updating:
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- local `AGENTS.md`
- any local policy/security/contribution guidance where relevant

## Enforcement posture
This standard is intentionally staged.

### Phase 1
- forward-looking adoption for new artifacts
- selective cleanup of the most replicated/high-visibility surfaces
- review-based enforcement

### Phase 2
- bounded validation/linting for selected path/file/comment patterns where false positives can be controlled
- exception logging where needed

### Phase 3
- stronger automation only where the rule is stable enough and operational value clearly exceeds maintenance cost

## Initial cleanup priority
Prioritize cleanup in this order:
1. public or externally visible surfaces
2. highly replicated durable paths/filenames
3. canonical governance/operating artifacts
4. lower-value historical material later

## Evidence of use
Evidence that this standard is active may include:
- workspace adoption notes
- changed naming conventions in new artifacts
- review comments applying the rule
- future validator or audit outputs

## Review trigger
Upgrade this standard when:
- the first downstream workspace adoption is complete
- the first bounded validator/review loop exists
- exception handling needs become clearer from live use
