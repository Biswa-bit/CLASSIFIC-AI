"""
Dataset Overview Module

This module computes the overall statistics of the dataset.
"""

import pandas as pd


class DatasetOverview:

    def analyze(self, df: pd.DataFrame):

        total_rows = len(df)

        total_columns = len(df.columns)

        memory_usage = df.memory_usage(deep=True).sum()

        memory_usage_mb = round(
            memory_usage / (1024 * 1024),
            2
        )

        numeric_columns = len(
            df.select_dtypes(include=["number"]).columns
        )

        categorical_columns = len(
            df.select_dtypes(include=["object", "category"]).columns
        )

        boolean_columns = len(
            df.select_dtypes(include=["bool"]).columns
        )

        datetime_columns = len(
            df.select_dtypes(include=["datetime"]).columns
        )

        print()
        print("=" * 70)
        print("DATASET OVERVIEW")
        print("=" * 70)

        print(f"Rows                 : {total_rows}")
        print(f"Columns              : {total_columns}")
        print(f"Memory Usage (MB)    : {memory_usage_mb}")
        print(f"Numeric Columns      : {numeric_columns}")
        print(f"Categorical Columns  : {categorical_columns}")
        print(f"Boolean Columns      : {boolean_columns}")
        print(f"Datetime Columns     : {datetime_columns}")

        return {

            "total_rows": total_rows,

            "total_columns": total_columns,

            "memory_usage_mb": memory_usage_mb,

            "numeric_columns": numeric_columns,

            "categorical_columns": categorical_columns,

            "boolean_columns": boolean_columns,

            "datetime_columns": datetime_columns

        }
    