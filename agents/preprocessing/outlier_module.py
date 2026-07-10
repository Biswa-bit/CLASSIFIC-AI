"""
=========================================================
CLASSIFIC-AI

Outlier Detection Module

Purpose
-------
Detects potential outliers in numerical columns.

Current Version
---------------
Version 1.0
- Detect numeric columns
- Detect outliers using IQR
- Count outliers
- Calculate percentage
- Human approval recommendation

Future Versions
---------------
Version 1.1
- Z-Score detection
- Modified Z-Score
- Winsorization recommendation

Version 2.0
- Isolation Forest
- Local Outlier Factor
- DBSCAN
- Business-rule outlier detection
- AI recommendation engine

Author : Biswadip Choudhury
Version : 1.0.0
=========================================================
"""

import pandas as pd


class OutlierModule:

    def analyze(self, df: pd.DataFrame):

        total_rows = len(df)

        numeric_columns = df.select_dtypes(
            include=["int64", "float64"]
        ).columns

        outlier_columns = {}

        total_outliers = 0

        for column in numeric_columns:

            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers = df[
                (df[column] < lower) |
                (df[column] > upper)
            ]

            count = len(outliers)

            if count > 0:

                outlier_columns[column] = {

                    "outlier_count": int(count),

                    "outlier_percentage": round(
                        (count / total_rows) * 100,
                        2
                    )

                }

                total_outliers += count

        if total_outliers == 0:

            recommendation = (
                "No significant outliers detected."
            )

            approval = False

        else:

            recommendation = (
                "Review detected outliers before removing or treating them."
            )

            approval = True

        result = {

            "module": "Outlier Module",

            "status": "Completed",

            "summary": {

                "total_rows": total_rows,

                "numeric_columns": len(numeric_columns),

                "columns_with_outliers": len(outlier_columns),

                "total_outliers": total_outliers

            },

            "outlier_columns": outlier_columns,

            "recommendation": recommendation,

            "human_approval_required": approval,

            "dataframe": df

        }

        return result
    