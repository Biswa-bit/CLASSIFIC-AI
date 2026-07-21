"""
==============================================================
CLASSIFIC-AI

Metadata Generator Module Test

Purpose
-------
Generates metadata for every column independently.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from pathlib import Path
import sys
import pandas as pd

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
# Generate Metadata
##########################################################

metadata = []

for column in df.columns:

    metadata.append({

        "Column": column,

        "Data Type": str(df[column].dtype),

        "Missing Values": int(df[column].isna().sum()),

        "Unique Values": int(df[column].nunique()),

        "Memory (KB)": round(df[column].memory_usage(deep=True) / 1024, 2)

    })

metadata_df = pd.DataFrame(metadata)

##########################################################
# Output
##########################################################

print()

print("=" * 80)
print("METADATA GENERATOR MODULE")
print("=" * 80)

print()

print(metadata_df.head(10))

print()

print("Total Columns :", len(metadata_df))

print()

print("=" * 80)
print("METADATA GENERATOR TEST COMPLETED")
print("=" * 80)
