"""
==============================================================
CLASSIFIC-AI

Dataset Overview Unit Test

Author : Biswadip Choudhury
==============================================================
"""

from pathlib import Path

from agents.dataset.dataset_agent import DatasetAgent
from agents.preprocessing.preprocessing_agent import PreprocessingAgent
from agents.eda.dataset_overview import DatasetOverview


def main():

    ##########################################################
    # Load Dataset
    ##########################################################

    dataset_path = Path("datasets/CLASSIFIC_AI_EDA.xlsx")

    dataset_agent = DatasetAgent()

    dataframe = dataset_agent.execute(dataset_path)

    ##########################################################
    # Preprocessing
    ##########################################################

    preprocessing = PreprocessingAgent()

    preprocessing_result = preprocessing.execute(dataframe)

    clean_df = preprocessing_result["dataframe"]

    ##########################################################
    # Dataset Overview
    ##########################################################

    module = DatasetOverview()

    result = module.execute(clean_df)

    ##########################################################
    # Validate Output
    ##########################################################

    assert isinstance(result, dict)

    assert "rows" in result
    assert "columns" in result
    assert "shape" in result
    assert "memory_usage_mb" in result
    assert "column_names" in result
    ##########################################################
    # Validate Returned Values
    ##########################################################

    assert result["rows"] == len(clean_df)

    assert result["columns"] == len(clean_df.columns)

    assert result["shape"] == clean_df.shape

    assert isinstance(result["memory_usage_mb"], float)

    assert len(result["column_names"]) == len(clean_df.columns)

    print("✓ Value validation passed.")

    print()
    print("✓ Dictionary validation passed.")

    ##########################################################
    # Output
    ##########################################################

    print()

    print("=" * 70)

    print("DATASET OVERVIEW RESULT")

    print("=" * 70)

    for key, value in result.items():

        print(f"{key:<20}: {value}")


if __name__ == "__main__":

    main()
