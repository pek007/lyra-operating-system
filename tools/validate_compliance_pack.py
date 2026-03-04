#!/usr/bin/env python3
"""Validate minimum compliance pack presence in repo root."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'GDPR_AI_ACT_COMPLIANCE_BASELINE_V1.md',
    'ROPA_LITE_V1.md',
    'VENDOR_DPA_REGISTER_V1.md',
    'AI_ACT_ROLE_CLASSIFICATION_MEMO_V1.md',
]

missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print('Compliance pack missing required files:')
    for m in missing:
        print(f'- {m}')
    raise SystemExit(1)
print('Compliance pack validation passed.')
