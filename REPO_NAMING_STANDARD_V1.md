# Repo Naming Standard v1.0

## Purpose
Keep portfolio structure clear and prevent accidental coupling between products.

## Naming Rules
- Product repositories: `product-<domain>-<name>`
  - Example: `product-os-control-panel`
- Platform/shared repositories: `platform-<name>`
  - Example: `platform-agent-sdk`
- Tooling/automation repositories: `tool-<name>`
  - Example: `tool-evidence-ingest`

## Domain Convention
- `os` = Lyra operating system/internal control capabilities
- `px` = PX business/client/commercial product line

## Branch Policy (minimum)
- `main` = releasable state
- short-lived feature branches linked to WO-ID

## Metadata Requirement
Each repo should contain:
- `PRODUCT.md` (or link to product boundary doc)
- reference to Product ID
- dependency policy summary

## Version
- v1.0
- Date: 2026-02-27
- Owner: Peter/Lyra
