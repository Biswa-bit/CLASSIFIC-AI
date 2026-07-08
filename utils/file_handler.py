"""
====================================================
CLASSIFIC-AI File Handler
====================================================
Handles loading and saving of datasets.
Supports CSV and Excel files.
====================================================
"""

import pandas as pd


def load_data(file_path):
    """
    Load CSV or Excel dataset automatically.
    """

    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)

    elif file_path.endswith((".xlsx", ".xls")):
        return pd.read_excel(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please upload CSV or Excel."
        )
    