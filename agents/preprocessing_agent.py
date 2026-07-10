"""
=====================================================================

CLASSIFIC-AI

Preprocessing Agent

Author : Biswadip Choudhury
Version : 1.2.0

=====================================================================

Responsibilities

1. Duplicate Analysis
2. Missing Value Analysis
3. Data Type Detection
4. Outlier Detection (Future)
5. Encoding Recommendation (Future)
6. Scaling Recommendation (Future)
7. Date Detection (Future)
8. Text Detection (Future)
9. Boolean Detection (Future)
10. Constant Feature Detection (Future)
11. High Cardinality Detection (Future)
12. ID Detection (Future)
13. Recommendation Engine (Future)

=====================================================================
"""

import pandas as pd

from core.base_agent import BaseAgent
from agents.preprocessing.duplicate_module import DuplicateModule
from agents.preprocessing.missing_value_module import MissingValueModule
from agents.preprocessing.datatype_module import DataTypeModule
from agents.preprocessing.outlier_module import OutlierModule
from agents.preprocessing.encoding_module import EncodingModule
from agents.preprocessing.scaling_module import ScalingModule



class PreprocessingAgent(BaseAgent):
    """
    CLASSIFIC-AI Preprocessing Agent
    """

    def __init__(self):
        super().__init__("Preprocessing Agent")

    def execute(self, df: pd.DataFrame):

        print("\n" + "=" * 70)
        print("PREPROCESSING AGENT")
        print("=" * 70)

        ####################################################################
        # Duplicate Module
        ####################################################################

        duplicate_module = DuplicateModule()

        duplicate_result = duplicate_module.analyze(df)

        print("\n" + "=" * 70)
        print("DUPLICATE MODULE")
        print("=" * 70)

        print(
            f"Total Rows            : "
            f"{duplicate_result['summary']['total_rows']}"
        )

        print(
            f"Duplicate Rows        : "
            f"{duplicate_result['summary']['duplicate_rows']}"
        )

        print(
            f"Duplicate Percentage  : "
            f"{duplicate_result['summary']['duplicate_percentage']} %"
        )

        print("\nRecommendation")
        print("-" * 40)
        print(duplicate_result["recommendation"])

        print("\nHuman Approval Required")
        print("-" * 40)
        print(duplicate_result["human_approval_required"])

        ####################################################################
        # Missing Value Module
        ####################################################################

        missing_module = MissingValueModule()

        missing_result = missing_module.analyze(df)

        print("\n" + "=" * 70)
        print("MISSING VALUE MODULE")
        print("=" * 70)

        print(
            f"Total Rows              : "
            f"{missing_result['summary']['total_rows']}"
        )

        print(
            f"Total Columns           : "
            f"{missing_result['summary']['total_columns']}"
        )

        print(
            f"Total Missing Values    : "
            f"{missing_result['summary']['total_missing']}"
        )

        print(
            f"Columns With Missing    : "
            f"{missing_result['summary']['columns_with_missing']}"
        )

        print("\nColumns")
        print("-" * 40)

        if len(missing_result["missing_columns"]) == 0:

            print("No missing values detected.")

        else:

            for column, info in missing_result["missing_columns"].items():

                print(
                    f"{column} : "
                    f"{info['missing_count']} "
                    f"({info['missing_percentage']}%)"
                )

        print("\nRecommendation")
        print("-" * 40)
        print(missing_result["recommendation"])

        print("\nHuman Approval Required")
        print("-" * 40)
        print(missing_result["human_approval_required"])

        total_missing = missing_result["summary"]["total_missing"]

        ####################################################################
        # Data Type Module
        ####################################################################

        datatype_module = DataTypeModule()

        datatype_result = datatype_module.analyze(df)

        print("\n" + "=" * 70)
        print("DATA TYPE MODULE")
        print("=" * 70)

        print(
            f"Total Columns : "
            f"{datatype_result['summary']['total_columns']}"
        )

        print("\nDetected Data Types")
        print("-" * 40)

        for column, dtype in datatype_result["datatypes"].items():

            print(f"{column:<35} {dtype}")

        print("\nRecommendation")
        print("-" * 40)

        print(datatype_result["recommendation"])

        print("\nHuman Approval Required")
        print("-" * 40)

        print(datatype_result["human_approval_required"])

      ####################################################################
        # Outlier Module
        ####################################################################

        outlier_module = OutlierModule()

        outlier_result = outlier_module.analyze(df)

        print("\n" + "=" * 70)
        print("OUTLIER MODULE")
        print("=" * 70)

        print(
            f"Numeric Columns        : "
            f"{outlier_result['summary']['numeric_columns']}"
        )

        print(
            f"Columns With Outliers  : "
            f"{outlier_result['summary']['columns_with_outliers']}"
        )

        print(
            f"Total Outliers         : "
            f"{outlier_result['summary']['total_outliers']}"
        )

        print("\nOutlier Details")
        print("-" * 40)

        if len(outlier_result["outlier_columns"]) == 0:

            print("No outliers detected.")

        else:

            for column, info in outlier_result["outlier_columns"].items():

                print(
                    f"{column} : "
                    f"{info['outlier_count']} "
                    f"({info['outlier_percentage']}%)"
                )

        print("\nRecommendation")
        print("-" * 40)

        print(outlier_result["recommendation"])

        print("\nHuman Approval Required")
        print("-" * 40)

        print(outlier_result["human_approval_required"])

        ####################################################################
        # Encoding Module
        ####################################################################

        encoding_module = EncodingModule()

        encoding_result = encoding_module.analyze(df)

        print("\n" + "=" * 70)
        print("ENCODING MODULE")
        print("=" * 70)

        print(
            f"Categorical Columns    : "
            f"{encoding_result['summary']['categorical_columns']}"
        )

        print("\nEncoding Recommendation")
        print("-" * 40)

        if len(encoding_result["encoding_columns"]) == 0:

            print("No categorical columns detected.")

        else:

            for column, info in encoding_result["encoding_columns"].items():

                print(
                    f"{column} : "
                    f"{info['recommended_encoding']} "
                    f"({info['unique_values']} unique values)"
                )

        print("\nRecommendation")
        print("-" * 40)

        print(encoding_result["recommendation"])

        print("\nHuman Approval Required")
        print("-" * 40)

        print(encoding_result["human_approval_required"])

        ######################################################################
        # Scaling Module
        ######################################################################

        scaling_module = ScalingModule()

        scaling_result = scaling_module.analyze(df)

        print("\n" + "=" * 70)
        print("SCALING MODULE")
        print("=" * 70)

        print(
            f"Numeric Columns        : "
            f"{scaling_result['summary']['numeric_columns']}"
        )

        print("\nScaling Recommendation")
        print("-" * 40)

        for column, method in scaling_result["scaling_recommendation"].items():

            print(
                f"{column} : {method}"
            )

        print("\nRecommendation")
        print("-" * 40)

        print(
            scaling_result["recommendation"]
        )

        print("\nHuman Approval Required")
        print("-" * 40)

        if scaling_result["human_approval_required"]:
            print("✓ Human approval required before applying scaling.")
        else:
            print("✓ No human approval required.")

        ####################################################################
        # Future Modules
        ####################################################################

        print("\n" + "=" * 70)
        print("PREPROCESSING MODULE STATUS")
        print("=" * 70)

        print("[✓] Duplicate Module")
        print("[✓] Missing Value Module")
        print("[✓] Data Type Module")
        print("[✓] Outlier Detection Module")
        print("[✓] Encoding Module")
        print("[✓] Scaling Module")
        print("[ ] Date Module")
        print("[ ] Text Module")
        print("[ ] Boolean Module")
        print("[ ] Constant Feature Module")
        print("[ ] High Cardinality Module")
        print("[ ] ID Detection Module")
        print("[ ] Recommendation Engine v2")

        ####################################################################
        # Recommendation Engine (Version 1.0)
        ####################################################################

        print("\n" + "=" * 70)
        print("PREPROCESSING RECOMMENDATIONS")
        print("=" * 70)

        duplicate_count = duplicate_result["summary"]["duplicate_rows"]

        if duplicate_count > 0:

            print("✓ Duplicate rows detected.")
            print("  Recommendation : Review duplicate rows before removing.")
            print("  Human Approval : Required")

        else:

            print("✓ No duplicate rows detected.")

        if total_missing > 0:

            print("\n✓ Missing values detected.")
            print("  Recommendation : Handle missing values before modeling.")

        else:

            print("\n✓ No missing values detected.")

        print("\n✓ Review categorical columns for encoding.")

        print("✓ Review numeric columns for scaling.")

        print("✓ Review outliers.")

        print("✓ Review ID columns.")

        print("✓ Review date columns.")

        print("✓ Review constant columns.")

        ####################################################################
        # Future Human-in-the-Loop Decisions
        ####################################################################

        print("\n" + "=" * 70)
        print("HUMAN-IN-THE-LOOP CHECKPOINTS")
        print("=" * 70)

        print("[ ] Duplicate Removal Approval")
        print("[ ] Missing Value Strategy Approval")
        print("[ ] Encoding Approval")
        print("[ ] Scaling Approval")
        print("[ ] Outlier Handling Approval")
        print("[ ] Feature Engineering Approval")
        print("[ ] Feature Selection Approval")

        ####################################################################
        # Agent Status
        ####################################################################

        print("\n" + "=" * 70)
        print("PREPROCESSING AGENT STATUS")
        print("=" * 70)

        print("Status : Completed")

        print("Completed Modules :")
        print("  ✓ Duplicate Analysis")
        print("  ✓ Missing Value Analysis")
        print("  ✓ Data Type Analysis")
        print("  ✓ Outlier Detection")
        print("  ✓ Encoding Recommendation")
        print("  ✓ Scaling Recommendation")

        print("\nPending Modules :")
        print("  • Date Detection")
        print("  • Text Detection")
        print("  • Boolean Detection")
        print("  • Constant Feature Detection")
        print("  • High Cardinality Detection")
        print("  • ID Detection")
        print("  • Recommendation Engine v2")

        ####################################################################
        # Agent Completed
        ####################################################################

        print("\nPreprocessing Agent Completed Successfully.")

        ####################################################################
        # Return Results
        ####################################################################

        preprocessing_results = {

        "dataframe": df,

        "duplicate_result": duplicate_result,

        "missing_value_result": missing_result,

        "datatype_result": datatype_result,

        "outlier_result": outlier_result,

        "encoding_result": encoding_result,

        "scaling_result": scaling_result

    }
        ####################################################################
        # Return Results
        ####################################################################

        preprocessing_results = {

            "dataframe": df,

            "duplicate_result": duplicate_result,

            "missing_value_result": missing_result

        }

        return preprocessing_results
    
    
    