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

    signal_req = json.loads((examples / "PXS_TM_REQUEST_ENVELOPE_INTAKE_WORK_V1.json").read_text(encoding="utf-8"))
    signal_req["request_id"] = "pxs-tm-req-signal-test"
    signal_req["payload_inline"]["intake_id"] = "pxs-intake-signal-test"
    signal_req["payload_inline"]["intake_class"] = "signal"
    signal_req["payload_inline"]["signal_types"] = ["status"]
    signal_req["payload_inline"].pop("requested_action", None)
    with tempfile.TemporaryDirectory() as td:
        signal_path = Path(td) / "signal-request.json"
        _write(signal_path, signal_req)
        signal = process_request(request_path=signal_path, search_root=ROOT / "control/runtime/empty-duplicates")
        assert signal["status"] == "recorded_no_action"

    pending = process_request(
        request_path=examples / "PXS_TM_REQUEST_ENVELOPE_ASSIGNMENT_ACCEPTANCE_V1.json",
        search_root=ROOT / "control/runtime/empty-duplicates",
    )
    assert pending["status"] == "accepted_pending_binding"

    no_runner_req = json.loads((examples / "PXS_TM_REQUEST_ENVELOPE_ASSIGNMENT_ACCEPTANCE_V1.json").read_text(encoding="utf-8"))
    no_runner_req["request_id"] = "pxs-tm-req-no-runner"
    no_runner_req["payload_inline"]["assignment_id"] = "pxs-assign-no-runner"
    no_runner_req["payload_inline"]["runner_binding_required"] = False
    no_runner_req["payload_inline"]["decision_policy_ref"] = "products/task-management/06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md"
    no_runner_req["payload_inline"]["objective_id"] = None
    with tempfile.TemporaryDirectory() as td:
        no_runner_path = Path(td) / "no-runner-request.json"
        _write(no_runner_path, no_runner_req)
        no_runner = process_request(request_path=no_runner_path, search_root=ROOT / "control/runtime/empty-duplicates")
        assert no_runner["status"] == "accepted_no_runner"

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
