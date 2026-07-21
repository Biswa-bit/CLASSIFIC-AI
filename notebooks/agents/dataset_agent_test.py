"""
==============================================================
CLASSIFIC-AI

Dataset Agent Unit Test

Purpose
-------
Tests the Dataset Agent independently.

Author : Biswadip Choudhury
Version : 2.0.0
==============================================================
"""

from pathlib import Path
import sys

##########################################################
# Project Root
##########################################################

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(PROJECT_ROOT))

##########################################################
# Imports
##########################################################

from agents.dataset.dataset_agent import DatasetAgent

##########################################################
# Dataset Path
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Execute Dataset Agent
##########################################################

agent = DatasetAgent()

result = agent.execute(DATASET)

##########################################################
# Agent Information
##########################################################

print()

print("=" * 80)
print("CLASSIFIC-AI DATASET AGENT")
print("=" * 80)

print()

print(f"Agent Name : {result.agent_name}")
print(f"Status     : {result.status}")

##########################################################
# Dataset Preview
##########################################################

print()

print("=" * 80)
print("DATASET PREVIEW")
print("=" * 80)

print(result.dataframe.head())

##########################################################
# Summary
##########################################################

print()

print("=" * 80)
print("DATASET SUMMARY")
print("=" * 80)

for key, value in result.summary.items():

    print(f"{key:<30}: {value}")

##########################################################
# Dashboard
##########################################################

print()

print("=" * 80)
print("DATASET DASHBOARD")
print("=" * 80)

print()

print(result.dashboard["title"])

print()

for metric, value in result.dashboard["metrics"].items():

    print(f"{metric:<30}: {value}")

##########################################################
# Executive Report
##########################################################

print()

print("=" * 80)
print("EXECUTIVE REPORT")
print("=" * 80)

print()

print(result.report["title"])

print()

print("Status")

print(result.report["status"])

print()

print("Overview")

for line in result.report["overview"]:

    print(f"• {line}")

print()

print("Overall Assessment")

print(result.report["overall_assessment"])

print()

print("Human Approval Required")

print(result.report["human_approval_required"])

##########################################################
# Recommendation
##########################################################

print()

print("=" * 80)
print("RECOMMENDATIONS")
print("=" * 80)

print()

print(result.recommendations["title"])

print()

for item in result.recommendations["recommendations"]:

    print(f"✓ {item}")

print()

print("Next Agent")

print(result.recommendations["next_agent"])

print()

print("Approval Required")

print(result.recommendations["approval_required"])

##########################################################
# Readiness
##########################################################

print()

print("=" * 80)
print("READINESS")
print("=" * 80)

print()

print("Score")

print(result.readiness["score"])

print()

print("Status")

print(result.readiness["status"])

print()

print("Checks")

for item in result.readiness["checks"]:

    print(item)

print()

print("Next Step")

print(result.readiness["next_step"])

##########################################################
# Approval Gate
##########################################################

print()

print("=" * 80)
print("APPROVAL GATE")
print("=" * 80)

print()

print("Status")

print(result.approval_status["status"])

print()

print("Human Approval Required")

print(result.approval_status["human_approval_required"])

print()

print("Message")

print(result.approval_status["message"])

##########################################################
# Test Completed
##########################################################

print()

print("=" * 80)
print("DATASET AGENT TEST COMPLETED SUCCESSFULLY")
print("=" * 80)


