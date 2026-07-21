"""
=============================================================
CLASSIFIC-AI

EDA Distribution Analysis Module

Author : Biswadip Choudhury
Version : 1.0.0
=============================================================
"""

import pandas as pd


class DistributionAnalysis:
    """
    Distribution Analysis Module
    """

    def execute(self, df: pd.DataFrame):

        numeric_df = df.select_dtypes(include="number")

        result = {}

        for column in numeric_df.columns:

            result[column] = {

                "mean": numeric_df[column].mean(),

                "median": numeric_df[column].median(),

                "std": numeric_df[column].std(),

                "min": numeric_df[column].min(),

                "max": numeric_df[column].max(),

                "skewness": numeric_df[column].skew(),

                "kurtosis": numeric_df[column].kurt()

            }

        return result
    