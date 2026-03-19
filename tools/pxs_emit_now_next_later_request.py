#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PXS_NNL = ROOT / "pxs/docs/now-next-later.md"
REQUEST_DIR = ROOT / "control/runtime/pxs-tm-requests"
RESPONSE_DIR = ROOT / "control/runtime/pxs-tm-responses"
PROCESSOR = ROOT / "tools/pxs_tm_contract_processor.py"


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _read_first_next_item(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_next = False
    for line in lines:
        if line.strip() == "## Next":
            in_next = True
            continue
        if in_next and line.startswith("## "):
            break
        if in_next and line.strip().startswith("- "):
            return line.strip()[2:].strip()
    raise RuntimeError("No Next bullet found in pxs/docs/now-next-later.md")


def _request_id(title: str) -> str:
    digest = hashlib.sha1(title.encode("utf-8")).hexdigest()[:10]
    return f"pxs-nnl-next-{digest}"


def build_request(*, title: str) -> dict:
    now = _iso_now()
    request_id = _request_id(title)
    return {
        "artifactType": "pxs_tm_request_envelope",
        "schemaVersion": "1.0.0",
        "request_id": request_id,
        "consumer_workspace": "pxs",
        "request_type": "intake",
        "canonical_contract_ref": "products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md",
        "payload_schema_ref": "schemas/tde_intake_packet/v1.0.0.schema.json",
        "payload_schema_version": "1.0.0",
        "payload_inline": {
            "artifactType": "tde_intake_packet",
            "schemaVersion": "1.0.0",
            "intake_id": request_id,
            "intake_class": "work",
            "source_system": "pxs",
            "source_type": "document",
            "source_reference": "pxs/docs/now-next-later.md#next",
            "submitted_at": now,
            "submitted_by": "Vega",
            "title": title,
            "summary": f"Emit the current first pxs Next priority into the bounded PXS -> Task Management contract path: {title}",
            "body": f"Produced automatically from pxs/docs/now-next-later.md#next. Current first Next item: {title}",
            "priority_hint": "high",
            "workspace_scope": "pxs",
            "product_scope": None,
            "related_entities": [
                {
                    "entity_type": "artifact",
                    "entity_ref": "pxs/docs/now-next-later.md",
                    "relationship": "source_priority_surface"
                }
            ],
            "evidence_links": [],
            "proposed_action": "form_bounded_execution_item",
            "requested_action": f"Turn '{title}' into one bounded execution-ready item with explicit scope and next action.",
            "success_signal": "A bounded execution item or equivalent Task Management target exists and can be reviewed by another operator."
        },
        "submitted_by": "Vega",
        "submitted_at": now,
        "source_reference": "pxs/docs/now-next-later.md#next",
        "note": "Automatically emitted from the first Next bullet in pxs/docs/now-next-later.md"
    }


def write_request(request: dict, output_dir: Path = REQUEST_DIR) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{request['request_id']}.json"
    out.write_text(json.dumps(request, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def run_processor(request_path: Path, response_dir: Path = RESPONSE_DIR) -> Path:
    response_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "python3",
            str(PROCESSOR),
            str(request_path),
            "--search-root",
            str(response_dir),
            "--write-governed",
            "--output-dir",
            str(response_dir),
        ],
        cwd=str(ROOT),
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip())


def emit_and_process() -> tuple[Path, Path]:
    title = _read_first_next_item(PXS_NNL)
    request = build_request(title=title)
    request_path = write_request(request)
    response_path = run_processor(request_path)
    return request_path, response_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit the first pxs Next item into the PXS -> Task Management contract path.")
    parser.add_argument("--emit-only", action="store_true", help="Only write the governed request artifact")
    args = parser.parse_args()

    title = _read_first_next_item(PXS_NNL)
    request = build_request(title=title)
    request_path = write_request(request)
    if args.emit_only:
        print(str(request_path))
        return
    response_path = run_processor(request_path)
    print(json.dumps({"request": str(request_path), "response": str(response_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
