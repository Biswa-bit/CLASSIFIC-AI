"""
==============================================================
CLASSIFIC-AI

Dataset Readiness Module Test

Purpose
-------
Tests the Dataset Readiness independently.

Author : Biswadip Choudhury
Version : 2.0.0
==============================================================
"""

from pathlib import Path
import sys

##########################################################
# Project Root
##########################################################

PROJECT_ROOT = Path(__file__).resolve().parents[3]

sys.path.insert(0, str(PROJECT_ROOT))

##########################################################
# Imports
##########################################################

from utils.file_handler import load_data
from agents.dataset.readiness import DatasetReadiness

##########################################################
# Dataset
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Load Dataset
##########################################################

df = load_data(DATASET)

##########################################################
# Summary
##########################################################

summary = {

    "Rows": len(df),

    "Columns": len(df.columns),

    "Duplicate Rows": int(df.duplicated().sum())

}

##########################################################
# Readiness
##########################################################

readiness = DatasetReadiness()

readiness_output = readiness.build(summary)

print(readiness_output)

##########################################################
# Output
##########################################################

print()

print("=" * 70)
print("READINESS MODULE")
print("=" * 70)

print()

print()

print("=" * 80)
print("READINESS MODULE")
print("=" * 80)

print()

for key, value in readiness_output.items():

    print(f"{key:<25}: {value}")

print()

print("=" * 80)
print("READINESS TEST COMPLETED")
print("=" * 80)

print()

print("Checks")

for item in readiness_output["checks"]:

    print(f"✓ {item}")

print()

print("Next Step")

print(readiness_output["next_step"])

print()

print("=" * 70)
print("READINESS TEST COMPLETED")
print("=" * 70)
