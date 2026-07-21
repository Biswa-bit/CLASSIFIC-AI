"""
==============================================================
CLASSIFIC-AI

Dataset Executive Report Module Test

Purpose
-------
Tests the Dataset Executive Report independently.

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

from agents.dataset.report import DatasetReport

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

    "Numeric Columns":
        len(df.select_dtypes(include="number").columns),

    "Categorical Columns":
        len(df.select_dtypes(include=["object", "category"]).columns),

    "Datetime Columns":
        len(df.select_dtypes(include="datetime").columns),

    "Duplicate Rows":
        int(df.duplicated().sum()),

    "Dataset Size (MB)":
        round(df.memory_usage(deep=True).sum()/1024/1024,2)

}

##########################################################
# Report
##########################################################

report = DatasetReport()

report_output = report.build(summary)

##########################################################
# Output
##########################################################

print()

print("=" * 70)
print("EXECUTIVE REPORT MODULE")
print("=" * 70)

print()

print(report_output["title"])

print()

print("Status")
print(report_output["status"])

print()

print("Overview")

for item in report_output["overview"]:

    print(f"• {item}")

print()

print("Overall Assessment")

print(report_output["overall_assessment"])

print()

print("Human Approval Required")

print(report_output["human_approval_required"])

print()

print("=" * 70)
print("EXECUTIVE REPORT TEST COMPLETED")
print("=" * 70)
