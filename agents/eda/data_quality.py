"""
=============================================================
CLASSIFIC-AI

EDA Data Quality Module

Author : Biswadip Choudhury
Version : 1.0.0
=============================================================
"""

import pandas as pd


class DataQuality:
    """
    Data Quality Module
    """

    def execute(self, df: pd.DataFrame):

        result = {

            "duplicate_rows": int(df.duplicated().sum()),

            "duplicate_percentage": round(
                (df.duplicated().sum() / len(df)) * 100,
                2
            ),

            "missing_values": df.isnull().sum().to_dict(),

            "missing_percentage": (
                df.isnull().mean() * 100
            ).round(2).to_dict(),

            "data_types": df.dtypes.astype(str).to_dict()

        }

        return result
    