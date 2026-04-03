# Build vs Integrate in PXS Tools

Status: draft wiki page
Date: 2026-04-03
Domain: Products & Tools

## Summary
Build vs Integrate in PXS Tools is the decision pattern for determining when PX Strategy should create its own tool/product capability and when it should instead rely on or integrate external tools.

## Why it matters
This is one of the central practical questions for PXS Tools. Without a disciplined build-vs-integrate lens, the BU risks either:
- building too much bespoke software without sufficient product logic, or
- underbuilding and losing strategic leverage where internal or future product value is real.

## Current understanding
The current direction suggests:
- repeated internal pain can indicate a product opportunity
- internal utility alone is not enough to justify broad custom-building
- architecture quality, maintenance burden, and productization potential matter
- some domains are better solved through integration rather than full ownership
- tool/product work should be informed by both market/tool landscape research and architecture best-practice research

## Practical rule of thumb
Bias toward integration when:
- the capability is commodity-like
- differentiation value is low
- maintenance cost would be disproportionate
- external tools already solve the problem well enough

Bias toward building when:
- the need is strategically central
- repeated internal use creates a strong product kernel
- current external tools do not fit well enough
- the resulting tool could become a meaningful internal advantage or future product asset

## Why this page matters in the wiki
This page should become one of the key reusable decision lenses in the PXS wiki because it links research, product strategy, tool decisions, and BU scope.

## Related pages
- [PXS Tools](./pxs-tools.md)
- [CRM Product Direction](./crm-product-direction.md)
- [Products & Tools](./README.md)
