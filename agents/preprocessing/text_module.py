"""
====================================================================
CLASSIFIC-AI

Enterprise AI-Driven Machine Learning Framework

Module:
Text Detection Module

Architecture Identifier:
CA-ARCH-V1.2

Current Version (v1.0.0)

Features
--------
- Detect text columns
- Detect categorical text
- Detect long free-form text
- Recommend preprocessing strategy
- Human approval recommendation

Future Enhancements
-------------------
Version 1.1
- Language Detection
- Text Length Analysis
- Token Statistics
- Stopword Detection

Version 2.0
- RAG Integration
- Embedding Recommendation
- LLM Prompt Recommendation
- Sentiment Detection
- Named Entity Recognition (NER)

Author : Biswadip Choudhury
Version : 1.0.0
====================================================================
"""

import pandas as pd


class TextModule:

    def analyze(self, df: pd.DataFrame):

        ##############################################################
        # Initialize Variables
        ##############################################################

        text_recommendation = {}

        recommendation = ""

        approval = False

        total_text_columns = 0

        ##############################################################
        # Loop Through Columns
        ##############################################################

        for column in df.columns:

            status = "Not Text"

            recommended_action = "No Action"

            reason = "Column is not a text feature."

            human_approval = False

            ##############################################################
            # Check Text Columns
            ##############################################################

            if df[column].dtype == "object":

                total_text_columns += 1

                unique_values = df[column].nunique()

                avg_length = (
                    df[column]
                    .astype(str)
                    .str.len()
                    .mean()
                )

                ##########################################################
                # Long Free-form Text
                ##########################################################

                if avg_length > 50:

                    status = "Long Text"

                    recommended_action = "TF-IDF / Embeddings"

                    reason = (
                        "Long free-form text detected."
                    )

                    human_approval = True

                ##########################################################
                # Medium Text
                ##########################################################

                elif avg_length > 20:

                    status = "Medium Text"

                    recommended_action = "Review"

                    reason = (
                        "Medium-length text detected."
                    )

                    human_approval = True

                ##########################################################
                # Short Categorical Text
                ##########################################################

                elif unique_values <= 20:

                    status = "Categorical Text"

                    recommended_action = "Encoding"

                    reason = (
                        "Suitable for categorical encoding."
                    )

                    human_approval = False

                ##########################################################
                # General Text
                ##########################################################

                else:

                    status = "Text"

                    recommended_action = "Review"

                    reason = (
                        "Text column requires review."
                    )

                    human_approval = True

                    ##############################################################
        # Store Recommendation
        ##############################################################

        text_recommendation[column] = {

            "status": status,

            "recommended_action": recommended_action,

            "reason": reason,

            "human_approval": human_approval

        }

        ##############################################################
        # Summary
        ##############################################################

        summary = {

            "text_columns": total_text_columns

        }

        ##############################################################
        # Recommendation
        ##############################################################

        if total_text_columns == 0:

            recommendation = (

                "No text columns detected."

            )

            approval = False

        else:

            recommendation = (

                f"{total_text_columns} text column(s) detected. "

                "Review before feature engineering."

            )

            approval = True

            ##############################################################
        # Result
        ##############################################################

        result = {

            "summary": summary,

            "text_recommendation": text_recommendation,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    