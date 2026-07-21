"""
==============================================================
CLASSIFIC-AI

Profiling Agent Unit Test

Purpose
-------
Tests the complete Profiling Agent independently.

Pipeline

Dataset Agent
      ↓
Preprocessing Agent
      ↓
Profiling Agent

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

from agents.dataset.dataset_agent import DatasetAgent
from agents.preprocessing.preprocessing_agent import PreprocessingAgent
from agents.profiling.profiling_agent import ProfilingAgent


def main():

    ##########################################################
    # Dataset Path
    ##########################################################

    DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

    ##########################################################
    # Dataset Agent
    ##########################################################

    dataset_agent = DatasetAgent()

    dataframe = dataset_agent.execute(DATASET)

    ##########################################################
    # Preprocessing Agent
    ##########################################################

    preprocessing_agent = PreprocessingAgent()

    preprocessing_result = preprocessing_agent.execute(dataframe)

    clean_df = preprocessing_result["dataframe"]

    ##########################################################
    # Profiling Agent
    ##########################################################

    profiling_agent = ProfilingAgent()

    profiling_result = profiling_agent.execute(clean_df)

    ##########################################################
    # Validation
    ##########################################################

    assert isinstance(profiling_result, dict)

    print()

    print("✓ Dictionary validation passed.")

    ##########################################################
    # Output
    ##########################################################

    print()

    print("=" * 70)

    print("PROFILING AGENT RESULT")

    print("=" * 70)

    for key, value in profiling_result.items():

        print(f"{key:<35}: {type(value).__name__}")

    print()

    print("=" * 70)

    print("FULL PROFILING RESULT")

    print("=" * 70)

    print(profiling_result)


if __name__ == "__main__":

    main()

