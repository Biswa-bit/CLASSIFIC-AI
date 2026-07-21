"""
=============================================================
CLASSIFIC-AI

EDA Dataset Overview Module

Author : Biswadip Choudhury
Version : 1.0.0
=============================================================
"""

import pandas as pd


class DatasetOverview:
    """
    Dataset Overview Module
    """

    def execute(self, df: pd.DataFrame):

        result = {
            "rows": len(df),
            "columns": len(df.columns),
            "shape": df.shape,
            "memory_usage_mb": round(
                df.memory_usage(deep=True).sum() / (1024 ** 2), 2
            ),
            "column_names": list(df.columns)
        }

        return result
    