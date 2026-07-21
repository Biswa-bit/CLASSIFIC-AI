"""
==============================================================
CLASSIFIC-AI

Dataset Recommendation Module Test

Purpose
-------
Tests the Dataset Recommendation independently.

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
from agents.dataset.recommendation import DatasetRecommendation

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
# Recommendation
##########################################################

recommendation = DatasetRecommendation()

recommendation_output = recommendation.build(summary)

##########################################################
# Output
##########################################################

print()

print("=" * 70)
print("RECOMMENDATION MODULE")
print("=" * 70)

print()

print(recommendation_output["title"])

print()

print("Recommendations")

for item in recommendation_output["recommendations"]:

    print(f"• {item}")

print()

print("Next Agent")

print(recommendation_output["next_agent"])

print()

print("=" * 70)
print("RECOMMENDATION TEST COMPLETED")
print("=" * 70)
