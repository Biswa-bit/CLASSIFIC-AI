"""
=========================================================
CLASSIFIC-AI

Data Type Module

Purpose:
Analyzes data types of every feature.

Author : Biswadip Choudhury
Version : 1.0.0
=========================================================
"""

import pandas as pd


class DataTypeModule:

    def analyze(self, df: pd.DataFrame):

        datatype_summary = {}

        for column in df.columns:

            datatype_summary[column] = str(df[column].dtype)

        result = {

            "module": "Data Type Module",

            "status": "Completed",

            "summary": {

                "total_columns": len(df.columns)

            },

            "datatypes": datatype_summary,

            "recommendation":
                "Review detected data types before preprocessing.",

            "human_approval_required": False,

            "dataframe": df

        }

        return result
    