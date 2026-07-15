"""
==============================================================
CLASSIFIC-AI

Correlation Analysis Module

--------------------------------------------------------------
Purpose

    Measures relationships between numeric features.

Checks

    • Pearson Correlation
    • Strong Positive Correlation
    • Strong Negative Correlation
    • Moderate Correlation
    • Weak Correlation
    • Duplicate Feature Detection
    • Multicollinearity Detection
    • AI Recommendation

Author : Biswadip Choudhury
Version: 1.0.0
==============================================================
"""

import pandas as pd


class CorrelationAnalysis:

    def analyze(self, df: pd.DataFrame):

        correlation_information = []

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.shape[1] < 2:

            return {

                "module": "Correlation Analysis",

                "status": "Skipped",

                "reason": "Less than two numeric columns."

            }

        correlation_matrix = numeric_df.corr(numeric_only=True)

        columns = correlation_matrix.columns

        ####################################################
        # Compare every feature pair
        ####################################################

        for i in range(len(columns)):

            for j in range(i + 1, len(columns)):

                feature_1 = columns[i]

                feature_2 = columns[j]

                correlation = round(
                    correlation_matrix.iloc[i, j],
                    4
                )

                ################################################
                # Relationship Strength
                ################################################

                abs_corr = abs(correlation)

                if abs_corr >= 0.90:

                    strength = "Very Strong"

                elif abs_corr >= 0.70:

                    strength = "Strong"

                elif abs_corr >= 0.50:

                    strength = "Moderate"

                elif abs_corr >= 0.30:

                    strength = "Weak"

                else:

                    strength = "Very Weak"

                ################################################
                # Correlation Direction
                ################################################

                if correlation > 0:

                    direction = "Positive"

                elif correlation < 0:

                    direction = "Negative"

                else:

                    direction = "No Correlation"

                ################################################
                # AI Recommendation
                ################################################

                if abs_corr >= 0.90:

                    recommendation = (
                        "Very high correlation detected. "
                        "Consider removing one feature to reduce multicollinearity."
                    )

                elif abs_corr >= 0.70:

                    recommendation = (
                        "Strong correlation detected. "
                        "Review feature importance before modeling."
                    )

                elif abs_corr >= 0.50:

                    recommendation = (
                        "Moderate correlation. "
                        "Generally acceptable."
                    )

                else:

                    recommendation = (
                        "No action required."
                    )

                ################################################
                # Store Results
                ################################################

                result = {

                    "feature_1": feature_1,

                    "feature_2": feature_2,

                    "correlation": correlation,

                    "strength": strength,

                    "direction": direction,

                    "recommendation": recommendation

                }

                correlation_information.append(result)

                ################################################
                # Print Correlation Report
                ################################################

                print()

                print("=" * 70)

                print("CORRELATION ANALYSIS")

                print("=" * 70)

                print("-" * 60)

                print(f"Feature 1            : {feature_1}")

                print(f"Feature 2            : {feature_2}")

                print(f"Correlation          : {correlation}")

                print(f"Strength             : {strength}")

                print(f"Direction            : {direction}")

                print(f"Recommendation       : {recommendation}")

                print("-" * 60)

                print("CORRELATION ANALYSIS COMPLETED")

                print("=" * 70)

        ###############################################################
        # Return Results
        ###############################################################

        return {

            "module": "Correlation Analysis",

            "status": "Completed",

            "correlation": correlation_information

        }
    
