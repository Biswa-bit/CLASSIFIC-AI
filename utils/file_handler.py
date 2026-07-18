"""
==========================================================
CLASSIFIC-AI File Handler
==========================================================

Description
-----------
Handles loading and saving of datasets.

Supported Formats
-----------------
1. CSV
2. Excel (.xlsx, .xls)
3. JSON
4. Parquet

Supports both:
- pathlib.Path
- String file paths

Author : Biswadip Choudhury
Project : CLASSIFIC-AI
==========================================================
"""

from pathlib import Path

import pandas as pd


def load_data(file_path):
    """
    Loads a dataset automatically based on file extension.

    Parameters
    ----------
    file_path : str | pathlib.Path

    Returns
    -------
    pandas.DataFrame
    """

    # Convert Path object to string if necessary
    file_path = Path(file_path)

    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(file_path)

    elif suffix in [".xlsx", ".xls"]:
        return pd.read_excel(file_path)

    elif suffix == ".json":
        return pd.read_json(file_path)

    elif suffix == ".parquet":
        return pd.read_parquet(file_path)

    else:
        raise ValueError(
            f"Unsupported file format: {suffix}\n"
            "Supported formats are:\n"
            "- CSV\n"
            "- Excel (.xlsx, .xls)\n"
            "- JSON\n"
            "- Parquet"
        )


def save_data(df, file_path):
    """
    Saves dataframe automatically based on file extension.

    Parameters
    ----------
    df : pandas.DataFrame
    file_path : str | pathlib.Path
    """

    file_path = Path(file_path)

    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        df.to_csv(file_path, index=False)

    elif suffix in [".xlsx", ".xls"]:
        df.to_excel(file_path, index=False)

    elif suffix == ".json":
        df.to_json(file_path, orient="records")

    elif suffix == ".parquet":
        df.to_parquet(file_path, index=False)

    else:
        raise ValueError(
            f"Unsupported file format: {suffix}"
        )
    
    