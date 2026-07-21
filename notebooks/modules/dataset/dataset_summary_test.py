"""
==============================================================
CLASSIFIC-AI

Dataset Summary Module Test

Purpose
-------
Tests the Dataset Summary independently.

Author : Biswadip Choudhury
Version : 1.0.0
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

##########################################################
# Dataset
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Load Dataset
##########################################################

df = load_data(DATASET)

##########################################################
# Dataset Summary
##########################################################

summary = {

    "Rows": len(df),

    "Columns": len(df.columns),

    "Numeric Columns":
        len(df.select_dtypes(include="number").columns),

    "Categorical Columns":
        len(df.select_dtypes(include=["object","category"]).columns),

    "Datetime Columns":
        len(df.select_dtypes(include=["datetime64"]).columns),

    "Duplicate Rows":
        int(df.duplicated().sum()),

    "Dataset Size (MB)":
        round(df.memory_usage(deep=True).sum()/1024/1024,2)

}

##########################################################
# Output
##########################################################

print()

print("="*80)

print("DATASET SUMMARY MODULE")

print("="*80)

print()

for key,value in summary.items():

    print(f"{key:<25}: {value}")

print()

print("="*80)

print("DATASET SUMMARY TEST COMPLETED")

print("="*80)
