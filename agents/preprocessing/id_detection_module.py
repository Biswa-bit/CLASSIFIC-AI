"""
==============================================================
CLASSIFIC-AI
ID Detection Module

Author : Biswadip Choudhury
Version : 1.0.0

Purpose
-------
Detect identifier (ID) columns that should not be used as
predictive features.

Current Version (v1.0.0)
------------------------
- Detect ID columns
- Detect unique identifiers
- Recommend exclusion from ML models
- Human approval support

Future Enhancements
-------------------
Version 1.1
- Composite Key Detection
- UUID Detection
- Hash Key Detection

Version 2.0
-----------
- Foreign Key Detection
- Relationship Mapping
- Automatic Feature Exclusion
- RAG Integration

==============================================================
"""

import pandas as pd
class IDDetectionModule:

    def analyze(self, df: pd.DataFrame):
        ############################################################
        # Initialize Variables
        ############################################################

        id_recommendation = {}

        recommendation = ""

        approval = False

        total_id_columns = 0

        ############################################################
        # Detect ID Columns
        ############################################################

        for column in df.columns:

            unique_values = df[column].nunique(dropna=False)

            uniqueness_percentage = round(
                (unique_values / len(df)) * 100,
                2
            )

            column_name = column.lower()

            is_id_name = (
                column_name == "id"
                or column_name.endswith("_id")
                or column_name.startswith("id_")
            )

            is_unique = unique_values == len(df)

            if is_id_name or is_unique:

                total_id_columns += 1

                status = "ID Column"

                recommended_action = (
                    "Exclude from model features"
                )

                reason = (
                    "Column appears to be an identifier."
                )

                human_approval = True

            else:

                status = "Not ID"

                recommended_action = "No Action"

                reason = (
                    "Column is not an identifier."
                )

                human_approval = False

            id_recommendation[column] = {

                "status": status,

                "unique_values": unique_values,

                "uniqueness_percentage": uniqueness_percentage,

                "recommended_action": recommended_action,

                "reason": reason,

                "human_approval": human_approval

            }

        ############################################################
        # Summary
        ############################################################

        summary = {

            "ID Columns": total_id_columns

        }
        
        ############################################################
        # Recommendation
        ############################################################

        if total_id_columns > 0:

            recommendation = (

                "One or more ID columns detected. "
                "These columns should usually be excluded from "
                "machine learning models because they do not contain "
                "predictive information."

            )

            approval = True

        else:

            recommendation = (

                "No ID columns detected."

            )

            approval = False

        ############################################################
        # Result
        ############################################################

        result = {

            "summary": summary,

            "id_recommendation": id_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    