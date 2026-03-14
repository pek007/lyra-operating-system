# Interfaces

## Upstream interfaces
- governance and security evidence sources
- audit/evidence outputs
- incident signals
- deployment changes requiring security review
- security research intake

## Downstream interfaces
- security requirements and posture outputs to products and consuming environments
- risk decisions and remediation priorities
- posture summaries and enforcement recommendations

## High-value cross-product interfaces
### OS↔PXS boundary interface
- Security defines the required boundary/security expectations.
- Platform/Governance/runtime owners implement the actual enforcement path.
- Boundary-affecting changes should be treated as interface-process changes with explicit review and evidence.

### PXS consumption interface
- consuming environments should have reproducible security baseline references
- security-impacting promotions should use explicit verification and narrow pass criteria

### High-risk external action interface
- external write or mutation surfaces should carry structured auditability and approval semantics proportionate to risk

## Canonical boundary artifact
Use `06-architecture/BOUNDARY.md` as the canonical Security boundary definition.

## Key boundary rule
Security governs across products but should not silently take ownership of their domain decisions.
