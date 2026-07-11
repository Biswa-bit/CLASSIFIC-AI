"""
====================================================================

CLASSIFIC-AI

Constant Feature Module

Purpose:
Detects constant features and recommends appropriate
actions before machine learning.

Responsibilities:
- Detect constant columns
- Recommend feature removal
- Support Human-in-the-Loop approval
- Explain feature importance

Current Version (v1.0.0):
- Detect constant columns
- Recommend constant feature review

Future Enhancements
-------------------

Version 1.1
- Near-constant detection
- Variance Threshold
- Low-information feature detection

Version 2.0
- Knowledge Retrieval Agent Integration
- Local RAG Agent Integration
- Automatic feature removal recommendation

Author : Biswadip Choudhury
Version : 1.0.0

====================================================================
"""

import pandas as pd


class ConstantFeatureModule:

    def analyze(self, df: pd.DataFrame):

        ###############################################################
        # Initialize Variables
        ###############################################################

        constant_recommendation = {}

        recommendation = ""

        approval = False

        total_constant_columns = 0

        ###############################################################
        # Constant Feature Detection
        ###############################################################

        for column in df.columns:

            unique_values = df[column].nunique(dropna=False)

            if unique_values == 1:

                status = "Constant"

                recommended_action = "Remove Feature"

                reason = (
                    "Column contains only one unique value."
                )

                human_approval = True

                total_constant_columns += 1

                approval = True

            else:

                status = "Not Constant"

                recommended_action = "No Action"

                reason = (
                    "Column contains multiple unique values."
                )

                human_approval = False

            constant_recommendation[column] = {

                "status": status,

                "recommended_action": recommended_action,

                "reason": reason,

                "human_approval": human_approval

            }

            ###############################################################
        # Recommendation
        ###############################################################

        if total_constant_columns > 0:

            recommendation = (

                "Remove constant features before modelling. "
                "Constant features provide no predictive value."

            )

        else:

            recommendation = (

                "No constant features detected."

            )

            ###############################################################
        # Summary
        ###############################################################

        summary = {

            "Constant Columns": total_constant_columns

        }

        ###############################################################
        # Result
        ###############################################################

        result = {

            "summary": summary,

            "constant_recommendation": constant_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    

