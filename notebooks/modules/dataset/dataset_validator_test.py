"""
==============================================================
CLASSIFIC-AI

Dataset Validator Module Test

Purpose
-------
Tests the Dataset Validator independently.

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
from utils.validator import validate_dataframe

##########################################################
# Dataset
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Load Dataset
##########################################################

df = load_data(DATASET)

##########################################################
# Validate
##########################################################

validate_dataframe(df)

##########################################################
# Output
##########################################################

print()

print("=" * 80)
print("DATASET VALIDATOR MODULE")
print("=" * 80)

print()

print("Validation Passed Successfully")

print()

print("Rows      :", len(df))

print("Columns   :", len(df.columns))

print("Duplicate Rows :", df.duplicated().sum())

print()

print("=" * 80)
print("DATASET VALIDATOR TEST COMPLETED")
print("=" * 80)
