#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from pxs_tm_contract_processor import process_request, write_processed_response

ROOT = Path(__file__).resolve().parents[1]


def _write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def run_tests() -> None:
    examples = ROOT / "products/task-management/07-decisions/examples"

    accepted = process_request(
        request_path=examples / "PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json",
        search_root=ROOT / "control/runtime/empty-duplicates",
    )
    assert accepted["status"] == "accepted"
    assert any(ref["ref"] == "pxs/docs/now-next-later.md#next" for ref in accepted["canonical_target_refs"])

    duplicate = process_request(
        request_path=examples / "PXS_TM_REQUEST_ENVELOPE_SEMI_REAL_VERTICAL_SLICE_V1.json",
        search_root=examples,
    )
    assert duplicate["status"] == "duplicate"

    with tempfile.TemporaryDirectory() as td:
        bad_path = Path(td) / "bad-request.json"
        bad = json.loads((examples / "PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json").read_text(encoding="utf-8"))
        del bad["source_reference"]
        _write(bad_path, bad)
        rejected = process_request(request_path=bad_path, search_root=ROOT / "control/runtime/empty-duplicates")
        assert rejected["status"] == "rejected_invalid_request"
        assert rejected["validation_errors"]

    with tempfile.TemporaryDirectory() as td:
        bad_payload_path = Path(td) / "bad-payload.json"
        req = json.loads((examples / "PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json").read_text(encoding="utf-8"))
        del req["payload_inline"]["title"]
        _write(bad_payload_path, req)
        rejected = process_request(request_path=bad_payload_path, search_root=ROOT / "control/runtime/empty-duplicates")
        assert rejected["status"] == "rejected_invalid_request"
        assert rejected["validation_errors"]

    with tempfile.TemporaryDirectory() as td:
        output_dir = Path(td) / "responses"
        out_path = write_processed_response(
            request_path=examples / "PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json",
            search_root=ROOT / "control/runtime/empty-duplicates",
            output_dir=output_dir,
        )
        assert out_path.exists()
        written = json.loads(out_path.read_text(encoding="utf-8"))
        assert written["artifactType"] == "pxs_tm_response_envelope"
        assert written["request_id"] == "pxs-tm-req-2026-03-19-001"

    print("[PASS] PXS Task Management contract processor tests passed")


if __name__ == "__main__":
    run_tests()
