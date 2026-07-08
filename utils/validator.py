"""
====================================================
CLASSIFIC-AI Dataset Validator
====================================================
Checks whether the uploaded dataset is valid.
====================================================
"""

import pandas as pd


def validate_dataframe(df):
    """
    Validate uploaded dataframe.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input is not a pandas DataFrame.")

    if df.empty:
        raise ValueError("Uploaded dataset is empty.")

    return True
