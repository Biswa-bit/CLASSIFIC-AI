"""
======================================================================

CLASSIFIC-AI

Scaling Recommendation Module

Author : Biswadip Choudhury
Version : 1.5.0

======================================================================

Responsibilities

1. Detect Numeric Columns
2. Recommend Scaling Strategy
3. Detect Already Scaled Features
4. Human-in-the-Loop Recommendation

======================================================================
"""

import pandas as pd


class ScalingModule:

    def analyze(self, df: pd.DataFrame):

        ###############################################################
        # Numeric Columns
        ###############################################################

        numeric_columns = df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        ###############################################################
        # Store Recommendations
        ###############################################################

        scaling_recommendation = {}

        ###############################################################
        # Scaling Recommendation
        ###############################################################

        for column in numeric_columns:

            unique_values = df[column].nunique()

            ###########################################################
            # IQR Outlier Detection
            ###########################################################

            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers = (
                (df[column] < lower) |
                (df[column] > upper)
            ).sum()

            ###########################################################
            # Recommend Scaling Method
            ###########################################################

            if unique_values <= 2:

                method = "No Scaling"

            elif outliers > 0:

                method = "RobustScaler"

            elif (
                df[column].min() >= 0 and
                df[column].max() <= 1
            ):

                method = "Already Scaled"

            else:

                method = "StandardScaler"

            scaling_recommendation[column] = method

            ###############################################################
        # Recommendation
        ###############################################################

        recommendation = (
            "Apply the recommended scaler before model training."
        )

        ###############################################################
        # Human Approval
        ###############################################################

        approval = False

        if any(
            method == "RobustScaler"
            for method in scaling_recommendation.values()
        ):

            approval = True

            recommendation = (
                "Dataset contains outliers. "
                "Review scaling strategy before training."
            )

        ###############################################################
        # Return Results
        ###############################################################

        result = {

            "summary": {

                "numeric_columns": len(numeric_columns)

            },

            "scaling_recommendation": scaling_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    