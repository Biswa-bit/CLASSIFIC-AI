"""
=====================================================================

CLASSIFIC-AI

Encoding Recommendation Module

Author : Biswadip Choudhury
Version : 1.4.0

=====================================================================

Responsibilities

1. Detect Categorical Columns
2. Count Unique Values
3. Recommend Encoding Strategy
4. Human Approval Required

=====================================================================
"""

import pandas as pd


class EncodingModule:
    """
    CLASSIFIC-AI Encoding Recommendation Module
    """

    def analyze(self, df: pd.DataFrame):

        encoding_columns = {}

        recommendation = (
            "Apply recommended encoding before model training."
        )

        approval = True

        categorical_columns = df.select_dtypes(
            include=["object", "category"]
        ).columns

        ####################################################################
        # Analyze Each Categorical Column
        ####################################################################

        for column in categorical_columns:

            unique_values = df[column].nunique()

            if unique_values == 2:

                encoding_method = "Label Encoding"

            elif unique_values <= 10:

                encoding_method = "One-Hot Encoding"

            elif unique_values <= 30:

                encoding_method = (
                    "Ordinal / Frequency Encoding"
                )

            else:

                encoding_method = (
                    "High Cardinality (Review Required)"
                )

            encoding_columns[column] = {

                "unique_values": unique_values,

                "recommended_encoding": encoding_method

            }

        ####################################################################
        # Summary
        ####################################################################

        summary = {

            "categorical_columns": len(categorical_columns)

        }

        ####################################################################
        # Result
        ####################################################################

        result = {

            "summary": summary,

            "encoding_columns": encoding_columns,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    