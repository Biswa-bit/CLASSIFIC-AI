"""
==============================================================
CLASSIFIC-AI

Dataset Dashboard Module Test

Purpose
-------
Tests the Dataset Dashboard independently.

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

from agents.dataset.dashboard import DatasetDashboard

##########################################################
# Dataset
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Load Dataset
##########################################################

df = load_data(DATASET)

##########################################################
# Build Summary
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
# Dashboard
##########################################################

dashboard = DatasetDashboard()

dashboard_output = dashboard.build(summary)

##########################################################
# Output
##########################################################

print()

print("="*70)
print("DATASET DASHBOARD MODULE")
print("="*70)

print()

print(dashboard_output["title"])

print()

for key, value in dashboard_output["metrics"].items():

    print(f"{key:<25}: {value}")

print()

print("="*70)
print("DASHBOARD TEST COMPLETED")
print("="*70)
