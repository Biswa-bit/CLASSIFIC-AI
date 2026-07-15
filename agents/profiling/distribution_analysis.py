"""
==============================================================
CLASSIFIC-AI
Distribution Analysis Module
--------------------------------------------------------------
Purpose:
    Performs statistical distribution analysis for every
    numeric feature in the dataset.

Checks:
    • Mean
    • Median
    • Standard Deviation
    • Variance
    • Skewness
    • Kurtosis
    • Distribution Type
    • Distribution Health
    • AI Recommendation

Author : Biswadip Choudhury
Version: 1.0.0
==============================================================
"""

import pandas as pd


class DistributionAnalysis:

    def analyze(self, df: pd.DataFrame):

        distribution_information = []

        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            series = df[column].dropna()

            if len(series) == 0:
                continue

            # --------------------------------------------------
            # Basic Statistics
            # --------------------------------------------------

            count = series.count()

            mean = round(series.mean(), 4)

            median = round(series.median(), 4)

            std = round(series.std(), 4)

            variance = round(series.var(), 4)

            minimum = round(series.min(), 4)

            maximum = round(series.max(), 4)

            value_range = round(maximum - minimum, 4)

            skewness = round(series.skew(), 4)

            kurtosis = round(series.kurt(), 4)

            # --------------------------------------------------
            # Distribution Type
            # --------------------------------------------------

            if abs(skewness) < 0.5:

                distribution_type = "Approximately Normal"

            elif skewness >= 0.5:

                distribution_type = "Right Skewed"

            else:

                distribution_type = "Left Skewed"

            # --------------------------------------------------
            # Distribution Shape
            # --------------------------------------------------

            if abs(kurtosis) < 3:

                distribution_shape = "Light Tail"

            elif abs(kurtosis) == 3:

                distribution_shape = "Normal Tail"

            else:

                distribution_shape = "Heavy Tail"

            # --------------------------------------------------
            # Distribution Health
            # --------------------------------------------------

            if abs(skewness) < 0.5 and abs(kurtosis) < 3:

                distribution_health = "Excellent"

            elif abs(skewness) < 1:

                distribution_health = "Good"

            elif abs(skewness) < 2:

                distribution_health = "Needs Review"

            else:

                distribution_health = "Poor"

            # --------------------------------------------------
            # AI Recommendation
            # --------------------------------------------------

            if abs(skewness) < 0.5:

                recommendation = "Distribution looks healthy. No transformation required."

            elif abs(skewness) < 1:

                recommendation = "Moderately skewed. Scaling is recommended."

            else:

                recommendation = "Highly skewed. Consider Log Transformation."

            # --------------------------------------------------
            # Scaling Recommendation
            # --------------------------------------------------

            if std > 1:

                scaling = "Recommended"

            else:

                scaling = "Not Required"

            # --------------------------------------------------
            # Log Transformation Recommendation
            # --------------------------------------------------

            if skewness > 1:

                log_transformation = "Recommended"

            else:

                log_transformation = "Not Required"

            # --------------------------------------------------
            # Store Results
            # --------------------------------------------------

            ##################################################
            # Store Results
            ##################################################

            distribution_information.append({

                "column_name": column,

                "count": count,

                "mean": mean,

                "median": median,

                "minimum": minimum,

                "maximum": maximum,

                "range": value_range,

                "std": std,

                "variance": variance,

                "skewness": skewness,

                "kurtosis": kurtosis,

                "distribution_type": distribution_type,

                "distribution_shape": distribution_shape,

                "distribution_health": distribution_health,

                "scaling": scaling,

                "log_transformation": log_transformation,

                "recommendation": recommendation

            })

        ##################################################
        # Print Distribution Analysis
        ##################################################

        print()
        print("=" * 70)
        print("DISTRIBUTION ANALYSIS")
        print("=" * 70)

        for item in distribution_information:

            print("-" * 60)

            print(f"Column                 : {item['column_name']}")
            print(f"Count                  : {item['count']}")
            print(f"Mean                   : {item['mean']}")
            print(f"Median                 : {item['median']}")
            print(f"Minimum                : {item['minimum']}")
            print(f"Maximum                : {item['maximum']}")
            print(f"Range                  : {item['range']}")
            print(f"Std                    : {item['std']}")
            print(f"Variance               : {item['variance']}")
            print(f"Skewness               : {item['skewness']}")
            print(f"Kurtosis               : {item['kurtosis']}")
            print(f"Distribution Type      : {item['distribution_type']}")
            print(f"Distribution Shape     : {item['distribution_shape']}")
            print(f"Distribution Health    : {item['distribution_health']}")
            print(f"Scaling                : {item['scaling']}")
            print(f"Log Transformation     : {item['log_transformation']}")
            print(f"Recommendation         : {item['recommendation']}")

        print("-" * 60)
        print("DISTRIBUTION ANALYSIS COMPLETED")
        print("=" * 70)
        
        # --------------------------------------------------
        # Return Result
        # --------------------------------------------------

        return {

            "module": "Distribution Analysis",

            "status": "Completed",

            "distribution": distribution_information

        }
    