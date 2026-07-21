"""
==============================================================
CLASSIFIC-AI

Dataset Loader Module Test

Purpose
-------
Tests the Dataset Loader independently.

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
# Dataset Path
##########################################################

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

##########################################################
# Execute Loader
##########################################################

df = load_data(DATASET)

##########################################################
# Output
##########################################################

print()

print("=" * 80)
print("DATASET LOADER MODULE")
print("=" * 80)

print()

print("Dataset Loaded Successfully")

print()

print(df.head())

print()

print("Shape :", df.shape)

print()

print("Columns :", len(df.columns))

print()

print("Memory Usage (MB) :",
      round(df.memory_usage(deep=True).sum()/1024/1024,2))

print()

print("=" * 80)
print("DATASET LOADER TEST COMPLETED")
print("=" * 80)
