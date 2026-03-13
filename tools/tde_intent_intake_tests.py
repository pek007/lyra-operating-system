#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_intent_intake import detect_request_class, REQUEST_CLASS_TABLE
from tde_formation_creator import create_from_formation


def run_tests() -> None:
    assert detect_request_class('Create a basic GUI for TDE') == 'basic_tde_gui'
    assert detect_request_class('Build an internal tool for TDE operators') == 'internal_tool'
    assert detect_request_class('Do runtime hardening for TDE') == 'runtime_hardening'
    assert detect_request_class('Research the best approach for staging') == 'research_request'
    assert detect_request_class('Review the TDE runtime promotion process') == 'review_audit_request'
    assert detect_request_class('Plan a picnic') is None

    gui_formation = REQUEST_CLASS_TABLE['basic_tde_gui'](
        request_text='Create a basic GUI for TDE',
        source_ref='telegram:test:gui',
    )
    assert gui_formation['recommended_next_action'] == 'proceed_with_assumptions'

    internal_tool_formation = REQUEST_CLASS_TABLE['internal_tool'](
        request_text='Build an internal tool',
        source_ref='telegram:test:internal-tool',
    )
    assert internal_tool_formation['recommended_next_action'] == 'ask_clarifying_questions'
    assert len(internal_tool_formation['required_clarifications']) == 3

    scoped_internal_tool = REQUEST_CLASS_TABLE['internal_tool'](
        request_text='Build an internal tool for TDE operators dashboard',
        source_ref='telegram:test:internal-tool-scoped',
    )
    assert scoped_internal_tool['recommended_next_action'] == 'proceed_with_assumptions'

    for request_class, fn in REQUEST_CLASS_TABLE.items():
        sample_text = 'test request for ' + request_class
        if request_class == 'internal_tool':
            sample_text = 'Build an internal tool for TDE operators dashboard'
        formation = fn(request_text=sample_text, source_ref=f'telegram:test:{request_class}')
        assert formation['artifactType'] == 'tde_intent_formation_record'
        assert formation['proposed_workflow_family'] == 'implementation_verification_readiness'

    formation = gui_formation
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        formation_path = root / 'formation.json'
        formation_path.write_text(json.dumps(formation, indent=2), encoding='utf-8')
        result = create_from_formation(
            formation_path=formation_path,
            db_path=root / 'tde_state.sqlite',
            objectives_path=root / 'tde_objectives.json',
            tasks_projection_path=root / 'TASKS_from_db.md',
        )
        assert result['formation_id'] == formation['formation_id']
        assert len(result['created_tasks']) == 2

    print('[PASS] TDE intent intake tests passed')


if __name__ == '__main__':
    run_tests()
