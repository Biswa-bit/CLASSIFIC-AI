"""
=====================================================================

CLASSIFIC-AI

Preprocessing Agent

Author : Biswadip Choudhury
Version : 1.0

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
13. Preprocessing Recommendation Engine (Future)

=====================================================================
"""

import pandas as pd

from core.base_agent import BaseAgent


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

        ###############################################################
        # Duplicate Analysis
        ###############################################################

        print("\n[1] Duplicate Analysis")
        print("-" * 40)

        duplicate_count = df.duplicated().sum()

        print(f"Duplicate Rows : {duplicate_count}")

        if duplicate_count > 0:

            print("\nRecommendation")
            print("----------------")

            print("Review duplicate rows before removing them.")
            print("Keeping duplicate rows for now.")

        else:

            print("No duplicate rows found.")

        ###############################################################
        # Missing Value Analysis
        ###############################################################

        print("\n[2] Missing Value Analysis")
        print("-" * 40)

        missing_values = df.isnull().sum()

        print(missing_values)

        ###############################################################
        # Data Type Analysis
        ###############################################################

        print("\n[3] Column Data Types")
        print("-" * 40)

        print(df.dtypes)

        ###############################################################
        # Future Modules
        ###############################################################

        print("\n[4] Outlier Detection")
        print("Status : Pending")

        print("\n[5] Encoding Recommendation")
        print("Status : Pending")

        print("\n[6] Feature Scaling Recommendation")
        print("Status : Pending")

        print("\n[7] Date Detection")
        print("Status : Pending")

        print("\n[8] Text Detection")
        print("Status : Pending")

        print("\n[9] Boolean Detection")
        print("Status : Pending")

        print("\n[10] Constant Feature Detection")
        print("Status : Pending")

        print("\n[11] High Cardinality Detection")
        print("Status : Pending")

        print("\n[12] ID Detection")
        print("Status : Pending")

        ###############################################################
        # Recommendation Engine
        ###############################################################

        print("\n" + "=" * 70)
        print("PREPROCESSING RECOMMENDATIONS")
        print("=" * 70)

        if duplicate_count > 0:

            print("✓ Review duplicate rows.")

        if missing_values.sum() > 0:

            print("✓ Missing values detected.")
            print("  Recommendation : Handle missing values before modeling.")

        else:

            print("✓ No missing values detected.")

        print("✓ Review categorical columns for encoding.")

        print("✓ Review numeric columns for scaling.")

        print("✓ Review outliers.")

        print("✓ Review ID columns.")

        print("✓ Review date columns.")

        print("✓ Review constant columns.")

        ###############################################################
        # Return Dataset
        ###############################################################

        print("\nPreprocessing Agent Completed.")

        return df
    