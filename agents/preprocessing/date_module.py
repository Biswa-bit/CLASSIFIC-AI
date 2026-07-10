"""
======================================================================
CLASSIFIC-AI

Date Detection Module

Author : Biswadip Choudhury
Version : 1.0.0

======================================================================

Description
-----------
This module detects date columns within the dataset and provides
recommendations for handling them before model training.

Current Version (v1.0.0)

Features
--------
- Detect datetime columns
- Detect date-like string columns
- Recommend datetime conversion
- Human approval support

Future Enhancements
-------------------
Version 1.1
- Year extraction
- Month extraction
- Quarter extraction
- Weekday extraction
- Fiscal calendar support

Version 2.0
- RAG integration
- Time-series recommendations
- Holiday detection
- Seasonality detection

======================================================================
"""

import pandas as pd


class DateModule:

    """
    CLASSIFIC-AI Date Detection Module
    """

    def analyze(self, df: pd.DataFrame):

        ###############################################################
        # Initialize Variables
        ###############################################################

        date_recommendation = {}

        recommendation = ""

        approval = False

        numeric_dates = 0

        ###############################################################
        # Loop Through Columns
        ###############################################################

        for column in df.columns:

            status = "Not a Date"

            recommended_action = "No Action"

            reason = "Column is not recognized as a date."

            human_approval = False

            ###########################################################
            # Already Datetime
            ###########################################################

            if pd.api.types.is_datetime64_any_dtype(df[column]):

                status = "Date Detected"

                recommended_action = "Already Datetime"

                reason = "Column already uses datetime datatype."

            ###########################################################
            # Try Parsing Object Columns
            ###########################################################

            elif df[column].dtype == "object":

                try:

                    converted = pd.to_datetime(
                        df[column],
                        errors="coerce"
                    )

                    success_rate = converted.notna().mean()

                    if success_rate >= 0.80:

                        status = "Date Detected"

                        recommended_action = "Convert to Datetime"

                        reason = (
                            f"{success_rate:.0%} values look like dates."
                        )

                        human_approval = True

                except Exception:

                    pass

            ###########################################################
            # Count Date Columns
            ###########################################################

            if status == "Date Detected":

                numeric_dates += 1

            ###########################################################
            # Store Result
            ###########################################################

            date_recommendation[column] = {

                "status": status,

                "recommended_action": recommended_action,

                "reason": reason,

                "human_approval": human_approval

            }

            ###########################################################
        # Summary
        ###########################################################

        summary = {

            "date_columns": numeric_dates

        }

        ###########################################################
        # Recommendation
        ###########################################################

        if numeric_dates == 0:

            recommendation = (

                "No date columns detected."

            )

            approval = False

        else:

            recommendation = (

                f"{numeric_dates} date column(s) detected. "

                "Review before feature engineering."

            )

            approval = True

        ###########################################################
        # Result
        ###########################################################

        result = {

            "summary": summary,

            "date_recommendation": date_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    