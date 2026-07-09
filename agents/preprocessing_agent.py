"""
============================================================

CLASSIFIC-AI

Preprocessing Agent

Responsibilities

1. Analyze duplicate rows
2. Report duplicate rows
3. Analyze missing values
4. Detect column data types
5. Return DataFrame

Author : Biswadip Choudhury

============================================================
"""

import pandas as pd

from core.base_agent import BaseAgent


class PreprocessingAgent(BaseAgent):

    def __init__(self):
        super().__init__("Preprocessing Agent")

    def execute(self, df):
        """
        Execute Preprocessing Agent

        Parameters
        ----------
        df : pandas.DataFrame
            Input DataFrame

        Returns
        -------
        pandas.DataFrame
            Processed DataFrame
        """

        print("=" * 60)
        print("Running Preprocessing Agent")
        print("=" * 60)

        # --------------------------------------------------
        # Duplicate Analysis
        # --------------------------------------------------

        duplicate_count = df.duplicated().sum()

        print("\nDuplicate Analysis")
        print("------------------------------")
        print(f"Duplicate Rows : {duplicate_count}")

        if duplicate_count > 0:
            print("\nRecommendation:")
            print("Review duplicate rows before removing them.")
            print("Keeping duplicate rows for now.")
        else:
            print("\nNo duplicate rows found.")

        # --------------------------------------------------
        # Missing Value Analysis
        # --------------------------------------------------

        print("\nMissing Value Analysis")
        print("------------------------------")
        print(df.isnull().sum())

        # --------------------------------------------------
        # Column Data Types
        # --------------------------------------------------

        print("\nColumn Data Types")
        print("------------------------------")
        print(df.dtypes)

        # --------------------------------------------------
        # Return DataFrame
        # --------------------------------------------------

        return df
    