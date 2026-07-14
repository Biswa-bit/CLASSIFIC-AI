"""
==============================================================
CLASSIFIC-AI

Column Intelligence Module

Purpose
-------
Analyzes every feature individually and generates
column-level intelligence for downstream AI agents.

Responsibilities
----------------
• Detect data type
• Count missing values
• Calculate missing percentage
• Count unique values
• Detect cardinality
• Detect constant columns
• Detect identifier columns
• Detect text columns
• Generate preprocessing recommendation

Author : Biswadip Choudhury
Version : 1.1.0
==============================================================
"""

import pandas as pd


class ColumnIntelligence:

    def analyze(self, df: pd.DataFrame):

        ###############################################################
        # Start
        ###############################################################

        print()
        print("=" * 70)
        print("COLUMN INTELLIGENCE")
        print("=" * 70)

        column_information = []

        ###############################################################
        # Analyze Every Column
        ###############################################################

        for column in df.columns:

            series = df[column]

            ###########################################################
            # Data Type
            ###########################################################

            if pd.api.types.is_numeric_dtype(series):
                column_type = "Numeric"

            elif pd.api.types.is_datetime64_any_dtype(series):
                column_type = "Datetime"

            elif pd.api.types.is_bool_dtype(series):
                column_type = "Boolean"

            else:
                column_type = "Categorical"

            ###########################################################
            # Missing Values
            ###########################################################

            missing_values = series.isna().sum()

            missing_percent = round(
                (missing_values / len(df)) * 100,
                2
            )

            ###########################################################
            # Unique Values
            ###########################################################

            unique_values = series.nunique(dropna=True)

            ###########################################################
            # Cardinality
            ###########################################################

            cardinality_ratio = unique_values / len(df)

            if cardinality_ratio > 0.50:
                cardinality = "Very High"

            elif cardinality_ratio > 0.20:
                cardinality = "High"

            elif cardinality_ratio > 0.05:
                cardinality = "Medium"

            else:
                cardinality = "Low"

            ###########################################################
            # Constant Column
            ###########################################################

            constant_column = unique_values == 1

            ###########################################################
            # Identifier Column
            ###########################################################

            identifier_column = unique_values == len(df)

            ###########################################################
            # Text Column
            ###########################################################

            text_column = False

            if column_type == "Categorical":

                average_length = (
                    series.astype(str)
                    .str.len()
                    .mean()
                )

                if average_length > 50:
                    text_column = True

            ###########################################################
            # Recommendation
            ###########################################################

            if constant_column:

                recommendation = "Remove Constant Column"

            elif identifier_column:

                recommendation = "Remove Identifier"

            elif text_column:

                recommendation = "TF-IDF / Embeddings"

            elif cardinality in ["High", "Very High"]:

                recommendation = "Frequency / Target Encoding"

            elif column_type == "Numeric":

                recommendation = "Scaling"

            else:

                recommendation = "One-Hot Encoding"

            ###########################################################
            # Print Summary
            ###########################################################

            print("-" * 70)
            print(f"Column            : {column}")
            print(f"Type              : {column_type}")
            print(f"Missing Values    : {missing_values}")
            print(f"Missing %         : {missing_percent}")
            print(f"Unique Values     : {unique_values}")
            print(f"Cardinality       : {cardinality}")
            print(f"Constant Column   : {constant_column}")
            print(f"Identifier Column : {identifier_column}")
            print(f"Text Column       : {text_column}")
            print(f"Recommendation    : {recommendation}")

            ###########################################################
            # Store Results
            ###########################################################

            column_information.append({

                "column_name": column,

                "data_type": column_type,

                "missing_values": missing_values,

                "missing_percent": missing_percent,

                "unique_values": unique_values,

                "cardinality": cardinality,

                "constant_column": constant_column,

                "identifier_column": identifier_column,

                "text_column": text_column,

                "recommendation": recommendation

            })

        ###############################################################
        # Return Results
        ###############################################################

        return {

            "module": "Column Intelligence",

            "status": "Completed",

            "columns": column_information

        }
       