#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"
VALID_STATUS = {
    "proposed",
    "accepted",
    "clarification-needed",
    "deferred",
    "rejected",
    "closed",
}


def extract_field(text: str, prefix: str) -> str | None:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return None


def main() -> int:
    results = []
    for inbox in sorted(PRODUCTS.glob("*/08-inbox")):
        product = inbox.parent.name
        for path in sorted(inbox.glob("REQ-*.md")):
            text = path.read_text(encoding="utf-8")
            status = extract_field(text, "Status:") or "unknown"
            request_id = extract_field(text, "Request ID:") or path.stem
            from_product = extract_field(text, "From product:")
            to_product = extract_field(text, "To product:")
            urgency = extract_field(text, "Urgency:")
            title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.name)
            open_item = status != "closed"
            results.append({
                "product": product,
                "path": str(path.relative_to(ROOT)),
                "request_id": request_id,
                "title": title,
                "status": status,
                "status_valid": status in VALID_STATUS,
                "from_product": from_product,
                "to_product": to_product,
                "urgency": urgency,
                "open": open_item,
            })

    open_items = [r for r in results if r["open"]]
    payload = {
        "generated_from": str(ROOT),
        "total_requests": len(results),
        "open_requests": len(open_items),
        "requests": results,
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
