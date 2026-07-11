"""
==============================================================
CLASSIFIC-AI

Boolean Module

Purpose:
Detects boolean features and recommends appropriate
conversions for machine learning.

Responsibilities:
- Detect boolean columns
- Recommend conversions
- Validate binary variables
- Support Human-in-the-Loop approval
- Explain conversion strategy

Current Version (v1.0.0):
- Detect boolean columns
- Recommend boolean review

Future Enhancements
-------------------

Version 1.1
- Binary conversion
- Yes/No conversion
- True/False conversion
- Custom boolean mapping

Version 2.0
- Knowledge Retrieval Agent integration
- Local RAG Agent integration
==============================================================
"""

import pandas as pd


class BooleanModule:

    def analyze(self, df: pd.DataFrame):

        ############################################################
        # Initialize
        ############################################################

        boolean_recommendation = {}

        recommendation = ""

        approval = False

        total_boolean_columns = 0

        ############################################################
        # Loop Through Columns
        ############################################################

        for column in df.columns:

            status = "Not Boolean"

            recommended_action = "No Action"

            reason = "Column is not boolean."

            human_approval = False

            series = df[column].dropna()

            unique_values = set(series.astype(str).str.lower().unique())

            ############################################################
            # Native Boolean
            ############################################################

            if df[column].dtype == bool:

                status = "Boolean"

                recommended_action = "Keep Boolean"

                reason = "Native boolean datatype detected."

                total_boolean_columns += 1

            ############################################################
            # True / False
            ############################################################

            elif unique_values <= {"true", "false"}:

                status = "Boolean"

                recommended_action = "Convert to Boolean"

                reason = "True/False values detected."

                total_boolean_columns += 1

            ############################################################
            # Yes / No
            ############################################################

            elif unique_values <= {"yes", "no"}:

                status = "Boolean"

                recommended_action = "Convert to Boolean"

                reason = "Yes/No values detected."

                total_boolean_columns += 1

            ############################################################
            # Y / N
            ############################################################

            elif unique_values <= {"y", "n"}:

                status = "Boolean"

                recommended_action = "Convert to Boolean"

                reason = "Y/N values detected."

                total_boolean_columns += 1

            ############################################################
            # 0 / 1
            ############################################################

            elif unique_values <= {"0", "1"}:

                status = "Boolean"

                recommended_action = "No Action"

                reason = "Binary numeric values detected."

                total_boolean_columns += 1

            ############################################################
            # Binary Category
            ############################################################

            elif len(unique_values) == 2:

                status = "Possible Boolean"

                recommended_action = "Review"

                reason = "Binary categorical feature detected."

                human_approval = True

                approval = True

                total_boolean_columns += 1

            ############################################################
            # Store Recommendation
            ############################################################

            boolean_recommendation[column] = {

                "status": status,

                "recommended_action": recommended_action,

                "reason": reason,

                "human_approval": human_approval

            }

        ############################################################
        # Summary
        ############################################################

        summary = {

            "Boolean Columns": total_boolean_columns

        }

        ############################################################
        # Recommendation
        ############################################################

        if total_boolean_columns == 0:

            recommendation = (

                "No boolean columns detected."

            )

            approval = False

        else:

            recommendation = (

                f"{total_boolean_columns} boolean column(s) detected. "

                "Convert Yes/No, Y/N and True/False where appropriate. "

                "Review custom binary categories before modelling."

            )

        ############################################################
        # Result
        ############################################################

        result = {

            "summary": summary,

            "boolean_recommendation": boolean_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    