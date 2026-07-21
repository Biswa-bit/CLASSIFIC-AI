"""
==============================================================

CLASSIFIC-AI

Dataset Approval Module Test

Purpose
-------
Tests the Dataset Approval independently.

==============================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]

sys.path.insert(0, str(PROJECT_ROOT))

from agents.dataset.approval import DatasetApproval

##########################################################
# Summary
##########################################################

readiness = {

    "score": 100,

    "status": "READY",

    "checks": [

        "✓ Dataset Loaded",

        "✓ Validation Passed",

        "✓ Metadata Generated"

    ],

    "next_step": "Proceed to Preprocessing Agent"

}

##########################################################
# Approval
##########################################################

approval = DatasetApproval()

approval_output = approval.build(readiness)

##########################################################
# Output
##########################################################

print()

print("=" * 80)

print("APPROVAL MODULE")

print("=" * 80)

print()

for key, value in approval_output.items():

    print(f"{key:<25}: {value}")

print()

print("=" * 80)

print("APPROVAL TEST COMPLETED")

print("=" * 80)
