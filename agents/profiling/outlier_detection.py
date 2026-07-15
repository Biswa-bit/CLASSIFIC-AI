"""
==============================================================
CLASSIFIC-AI

Outlier Detection Module

--------------------------------------------------------------
Purpose

    Detects potential outliers from numeric features
    using statistical methods.

Version 1.0 Methods

     ✓ IQR Method
    ✓ Z-Score Method
    ✓ Modified Z-Score Method

Future Enhancements

Version 1.1

    □ Isolation Forest
    □ Local Outlier Factor
    □ One-Class SVM

Version 2.0

    □ DBSCAN
    □ Ensemble Outlier Detection
    □ Outlier Confidence Score
    □ AI Outlier Explanation

Author : Biswadip Choudhury
Version : 1.0.0

==============================================================
"""

import pandas as pd


class OutlierDetection:

    def analyze(self, df: pd.DataFrame):

        outlier_information = []

        ###############################################################
        # Select Numeric Features
        ###############################################################

        numeric_columns = df.select_dtypes(include="number").columns

        ###############################################################
        # Analyze Every Numeric Feature
        ###############################################################

        for column in numeric_columns:

            series = df[column].dropna()

            if len(series) == 0:

                continue

            ###########################################################
            # Quartiles
            ###########################################################

            q1 = round(series.quantile(0.25), 4)

            q3 = round(series.quantile(0.75), 4)

            ###########################################################
            # Inter Quartile Range
            ###########################################################

            iqr = round(q3 - q1, 4)

            ###########################################################
            # Lower / Upper Bound
            ###########################################################

            lower_bound = round(q1 - (1.5 * iqr), 4)

            upper_bound = round(q3 + (1.5 * iqr), 4)

            ###########################################################
            # Mean and Standard Deviation
            ###########################################################

            mean = round(series.mean(), 4)

            std = round(series.std(), 4)

            ###########################################################
            # Median and Median Absolute Deviation (MAD)
            ###########################################################

            median = round(series.median(), 4)

            mad = round((series - median).abs().median(), 4)

            ###########################################################
            # Z-Score Threshold
            ###########################################################

            z_score_threshold = 3.0

            ###########################################################
            # Modified Z-Score Threshold
            ###########################################################

            modified_z_threshold = 3.5

            ###########################################################
            # IQR Outliers
            ###########################################################

            iqr_outliers = series[
                (series < lower_bound) |
                (series > upper_bound)
            ]

            iqr_count = len(iqr_outliers)

            ###########################################################
            # Z-Score Outliers
            ###########################################################

            if std != 0:

                z_scores = ((series - mean) / std).abs()

                z_outliers = series[z_scores > z_score_threshold]

                z_count = len(z_outliers)

            else:

                z_count = 0

            ###########################################################
            # Modified Z-Score Outliers
            ###########################################################

            if mad != 0:

                modified_z_scores = (
                    0.6745 * (series - median) / mad
                ).abs()

                modified_z_outliers = series[
                    modified_z_scores > modified_z_threshold
                ]

                modified_z_count = len(modified_z_outliers)

            else:

                modified_z_count = 0

            ###########################################################
            # Outlier Percentage
            ###########################################################

            total_records = len(series)

            iqr_percentage = round(
                (iqr_count / total_records) * 100,
                2
            )

            ###########################################################
            # Outlier Severity
            ###########################################################

            if iqr_percentage < 1:

                severity = "Low"

            elif iqr_percentage < 5:

                severity = "Moderate"

            else:

                severity = "High"

            ###########################################################
            # AI Recommendation
            ###########################################################

            if severity == "Low":

                recommendation = (
                    "No action required."
                )

            elif severity == "Moderate":

                recommendation = (
                    "Review outliers before model training."
                )

            else:

                recommendation = (
                    "Consider RobustScaler or Log Transformation."
                )

            ###########################################################
            # Consensus Score
            ###########################################################

            methods_flagged = 0

            if iqr_count > 0:

                methods_flagged += 1

            if z_count > 0:

                methods_flagged += 1

            if modified_z_count > 0:

                methods_flagged += 1

            ###########################################################
            # Confidence Level
            ###########################################################

            if methods_flagged == 3:

                confidence = "High"

            elif methods_flagged == 2:

                confidence = "Medium"

            elif methods_flagged == 1:

                confidence = "Low"

            else:

                confidence = "None"

            ###########################################################
            # Store Results
            ###########################################################

            outlier_information.append({

                "column_name": column,

                "minimum": round(series.min(), 4),

                "maximum": round(series.max(), 4),

                "q1": q1,

                "q3": q3,

                "iqr": iqr,

                "lower_bound": lower_bound,

                "upper_bound": upper_bound,

                "mean": mean,

                "std": std,

                "median": median,

                "mad": mad,

            ###################################################
            # Individual Detection Methods
            ###################################################

            "iqr_outliers": iqr_count,

            "zscore_outliers": z_count,

            "modified_z_outliers": modified_z_count,

            ###################################################
            # Consensus Engine
            ###################################################

            "methods_flagged": methods_flagged,

            "confidence": confidence,

            ###################################################
            # Final Assessment
            ###################################################

            "outlier_percentage": iqr_percentage,

            "severity": severity,

            "recommendation": recommendation

        })
            ###############################################################
        # Print Outlier Detection Report
        ###############################################################

        print()
        print("=" * 70)
        print("OUTLIER DETECTION")
        print("=" * 70)

        for item in outlier_information:

            print("-" * 60)

            print(f"Column                    : {item['column_name']}")

            print(f"Minimum Value             : {item['minimum']}")
            print(f"Maximum Value             : {item['maximum']}")

            print(f"Q1                        : {item['q1']}")
            print(f"Q3                        : {item['q3']}")
            print(f"IQR                       : {item['iqr']}")

            print(f"Lower Bound               : {item['lower_bound']}")
            print(f"Upper Bound               : {item['upper_bound']}")

            print(f"Mean                      : {item['mean']}")
            print(f"Standard Deviation        : {item['std']}")

            print(f"Median                    : {item['median']}")
            print(f"MAD                       : {item['mad']}")

            print()

            print("Detection Summary")
            print("-" * 30)

            print(f"IQR Outliers              : {item['iqr_outliers']}")
            print(f"Z-Score Outliers          : {item['zscore_outliers']}")
            print(f"Modified Z Outliers       : {item['modified_z_outliers']}")

            print()

            print("Consensus")
            print("-" * 30)

            print(f"Methods Flagged           : {item['methods_flagged']} / 3")
            print(f"Confidence                : {item['confidence']}")

            print()

            print("Assessment")
            print("-" * 30)

            print(f"Outlier Percentage        : {item['outlier_percentage']} %")
            print(f"Severity                  : {item['severity']}")
            print(f"Recommendation            : {item['recommendation']}")

        print("-" * 60)
        print("OUTLIER DETECTION COMPLETED")
        print("=" * 70)

        ###############################################################
        # Return Results
        ###############################################################

        return {

            "module": "Outlier Detection",

            "status": "Completed",

            "outliers": outlier_information

        }
    