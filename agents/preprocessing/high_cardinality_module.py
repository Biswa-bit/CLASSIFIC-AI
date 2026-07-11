"""
==============================================================
CLASSIFIC-AI
High Cardinality Detection Module

Author : Biswadip Choudhury
Version : 1.0.0

Purpose
-------
Detect categorical columns having a large number of unique values.

Current Version (v1.0.0)
------------------------
- Detect high-cardinality categorical columns
- Count unique values
- Calculate uniqueness percentage
- Recommend suitable encoding
- Human approval support

Future Enhancements
-------------------
Version 1.1
- Frequency Threshold
- Rare Category Detection
- Category Distribution Analysis

Version 2.0
-----------
- Automatic Encoding Recommendation
- Target Encoding Recommendation
- Embedding Recommendation
- RAG Integration

==============================================================
"""

import pandas as pd

class HighCardinalityModule:

    def analyze(self, df: pd.DataFrame):

        ############################################################
        # Initialize Variables
        ############################################################

        high_cardinality_recommendation = {}

        recommendation = ""

        approval = False

        total_high_cardinality = 0

        ############################################################
        # Detect High Cardinality Columns
        ############################################################

        for column in df.columns:

            if df[column].dtype == "object":

                unique_values = df[column].nunique()

                total_rows = len(df)

                uniqueness_percentage = round(
                    (unique_values / total_rows) * 100,
                    2
                )

                if uniqueness_percentage > 50:

                    status = "High Cardinality"

                    recommended_action = (
                        "Frequency Encoding / Target Encoding / Embeddings"
                    )

                    reason = (
                        "Large number of unique categories detected."
                    )

                    human_approval = True

                    total_high_cardinality += 1

                else:

                    status = "Normal Cardinality"

                    recommended_action = "One-Hot Encoding"

                    reason = (
                        "Number of unique categories is within acceptable range."
                    )

                    human_approval = False

                high_cardinality_recommendation[column] = {

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

            "High Cardinality Columns": total_high_cardinality

        }

        ############################################################
        # Recommendation
        ############################################################

        if total_high_cardinality > 0:

            recommendation = (

                "Review high-cardinality columns before encoding. "

                "Consider Frequency Encoding, Target Encoding or Embeddings."

            )

            approval = True

        else:

            recommendation = (

                "No high-cardinality columns detected."

            )

            approval = False

            ############################################################
        # Result
        ############################################################

        result = {

            "summary": summary,

            "high_cardinality_recommendation": high_cardinality_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    
    

