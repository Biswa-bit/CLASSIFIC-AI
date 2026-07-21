"""
=============================================================
CLASSIFIC-AI

EDA Missing Data Module

Author : Biswadip Choudhury
Version : 1.0.0
=============================================================
"""

import pandas as pd


class MissingData:
    """
    Missing Data Analysis Module
    """

    def execute(self, df: pd.DataFrame):

        missing_counts = df.isnull().sum()

        missing_percentage = (
            df.isnull().mean() * 100
        ).round(2)

        result = {

            "total_missing": int(missing_counts.sum()),

            "columns_with_missing": list(
                missing_counts[missing_counts > 0].index
            ),

            "missing_counts": missing_counts.to_dict(),

            "missing_percentage": missing_percentage.to_dict(),

            "complete_columns": list(
                missing_counts[missing_counts == 0].index
            )

        }

        return result
    