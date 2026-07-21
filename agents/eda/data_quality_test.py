"""
==============================================================
CLASSIFIC-AI

Data Quality Unit Test

Author : Biswadip Choudhury
==============================================================
"""

from pathlib import Path

from agents.dataset.dataset_agent import DatasetAgent
from agents.preprocessing.preprocessing_agent import PreprocessingAgent
from agents.eda.data_quality import DataQuality


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
    # Data Quality Module
    ##########################################################

    module = DataQuality()

    result = module.execute(clean_df)

    ##########################################################
    # Validate Output Structure
    ##########################################################

    assert isinstance(result, dict)

    assert "duplicate_rows" in result
    assert "duplicate_percentage" in result
    assert "missing_values" in result
    assert "missing_percentage" in result
    assert "data_types" in result

    print()
    print("✓ Dictionary validation passed.")

    ##########################################################
    # Validate Returned Values
    ##########################################################

    assert isinstance(result["duplicate_rows"], int)

    assert isinstance(result["duplicate_percentage"], float)

    assert isinstance(result["missing_values"], dict)

    assert isinstance(result["missing_percentage"], dict)

    assert isinstance(result["data_types"], dict)

    print("✓ Value validation passed.")

    ##########################################################
    # Validate Business Logic
    ##########################################################

    # Duplicate Rows

    assert result["duplicate_rows"] == clean_df.duplicated().sum()

    # Duplicate Percentage

    expected_duplicate_percentage = round(

        (clean_df.duplicated().sum() / len(clean_df)) * 100,

        2

    )

    assert result["duplicate_percentage"] == expected_duplicate_percentage

    # Missing Values

    assert result["missing_values"] == clean_df.isnull().sum().to_dict()

    # Missing Percentage

    expected_missing_percentage = (

        clean_df.isnull().mean() * 100

    ).round(2).to_dict()

    assert result["missing_percentage"] == expected_missing_percentage

    # Data Types

    assert result["data_types"] == clean_df.dtypes.astype(str).to_dict()

    print()

    print("✓ Business Logic validation passed.")

    ##########################################################
    # Output
    ##########################################################

    print()

    print("=" * 70)

    print("DATA QUALITY RESULT")

    print("=" * 70)

    for key, value in result.items():

        print(f"{key:<25}: {value}")


if __name__ == "__main__":

    main()
