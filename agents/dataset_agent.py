"""
==========================================================
CLASSIFIC-AI Dataset Agent
==========================================================

This is the first AI Agent.

Responsibilities

1. Load uploaded dataset
2. Validate dataset
3. Display dataset information
4. Check missing values
5. Check duplicate rows
6. Return clean DataFrame

Author : Biswadip Choudhury
==========================================================
"""

import pandas as pd

from core.base_agent import BaseAgent
from utils.file_handler import load_data
from utils.validator import validate_dataframe


class DatasetAgent(BaseAgent):

    def __init__(self):
        super().__init__("Dataset Agent")

    def execute(self, file_path):
        """
        Execute Dataset Agent.
        """

        print("=" * 60)
        print("Running Dataset Agent")
        print("=" * 60)
        df = load_data(file_path)

        validate_dataframe(df)
        print(f"Shape : {df.shape}")
        print("\nDataset Information")
        df.info()
        print("\nMissing Values")
        print(df.isnull().sum())
        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        return df
    
    


