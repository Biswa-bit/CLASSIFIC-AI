"""
======================================================================
CLASSIFIC-AI

Statistics Summary Module

Purpose
-------
Performs descriptive statistical analysis on every numeric feature.

Responsibilities
----------------
• Count observations
• Count missing values
• Mean
• Median
• Mode
• Minimum
• Maximum
• Range
• Standard Deviation
• Variance
• Quartiles
• Inter Quartile Range
• Skewness
• Kurtosis
• AI Statistical Health Assessment

Author : Biswadip Choudhury
Version : 1.0.0
======================================================================
"""

import pandas as pd


class StatisticsSummary:

    def analyze(self, df: pd.DataFrame):

        ###############################################################
        # Start
        ###############################################################

        print()
        print("=" * 70)
        print("STATISTICS SUMMARY")
        print("=" * 70)

        statistics_information = []

        ###############################################################
        # Analyze Numeric Columns
        ###############################################################

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            series = df[column]

            ###########################################################
            # Basic Statistics
            ###########################################################

            count = series.count()

            missing = series.isnull().sum()

            mean = round(series.mean(), 4)

            median = round(series.median(), 4)

            if not series.mode().empty:
                mode = round(series.mode().iloc[0], 4)
            else:
                mode = None

            minimum = round(series.min(), 4)

            maximum = round(series.max(), 4)

            value_range = round(maximum - minimum, 4)

            ###########################################################
            # Spread
            ###########################################################

            std = round(series.std(), 4)

            variance = round(series.var(), 4)

            ###########################################################
            # Quartiles
            ###########################################################

            q1 = round(series.quantile(0.25), 4)

            q2 = median

            q3 = round(series.quantile(0.75), 4)

            iqr = round(q3 - q1, 4)

            ###########################################################
            # Shape
            ###########################################################

            skewness = round(series.skew(), 4)

            kurtosis = round(series.kurt(), 4)

            ###########################################################
            # AI Statistics Health Assessment
            ###########################################################

            statistics_health = "Healthy"

            recommendation = "No action required."

            if variance == 0:

                statistics_health = "Problematic"

                recommendation = (
                    "Constant feature detected. Remove column."
                )

            elif std < 0.001:

                statistics_health = "Needs Review"

                recommendation = (
                    "Near-zero variance feature."
                )

            elif abs(skewness) > 1:

                statistics_health = "Needs Review"

                recommendation = (
                    "Highly skewed. Consider log transformation."
                )

            elif abs(kurtosis) > 3:

                statistics_health = "Needs Review"

                recommendation = (
                    "Heavy tails detected."
                )

            else:

                statistics_health = "Healthy"

                recommendation = "No action required."
            ###########################################################
            # Console Report
            ###########################################################

            print("-" * 70)

            print(f"Column               : {column}")
            print(f"Count                : {count}")
            print(f"Missing Values       : {missing}")
            print(f"Mean                 : {mean}")
            print(f"Median               : {median}")
            print(f"Mode                 : {mode}")
            print(f"Minimum              : {minimum}")
            print(f"Maximum              : {maximum}")
            print(f"Range                : {value_range}")
            print(f"Standard Deviation   : {std}")
            print(f"Variance             : {variance}")
            print(f"Q1                   : {q1}")
            print(f"Q2 (Median)          : {q2}")
            print(f"Q3                   : {q3}")
            print(f"IQR                  : {iqr}")
            print(f"Skewness             : {skewness}")
            print(f"Kurtosis             : {kurtosis}")
            print(f"Statistics Health    : {statistics_health}")
            print(f"Recommendation       : {recommendation}")

            ###########################################################
            # Store Results
            ###########################################################

            statistics_information.append({

                "column_name": column,

                "count": count,

                "missing": missing,

                "mean": mean,

                "median": median,

                "mode": mode,

                "minimum": minimum,

                "maximum": maximum,

                "range": value_range,

                "std": std,

                "variance": variance,

                "q1": q1,

                "q2": q2,

                "q3": q3,

                "iqr": iqr,

                "skewness": skewness,

                "kurtosis": kurtosis,

                "statistics_health": statistics_health,

                "recommendation": recommendation

            })

        ###############################################################
        # Module Completed
        ###############################################################

        print()
        print("=" * 70)
        print("STATISTICS SUMMARY COMPLETED")
        print("=" * 70)

        ###############################################################
        # Return Results
        ###############################################################

        return {

            "module": "Statistics Summary",

            "status": "Completed",

            "total_numeric_columns": len(numeric_columns),

            "statistics": statistics_information

        }
        
