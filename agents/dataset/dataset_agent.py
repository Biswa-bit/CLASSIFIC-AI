"""
==========================================================
CLASSIFIC-AI Dataset Agent
==========================================================

Description
-----------
The Dataset Agent is the first AI agent executed in the
CLASSIFIC-AI pipeline.

It is responsible for loading, validating, and providing
dataset metadata to downstream AI agents.

Responsibilities
----------------
1. Load dataset
2. Validate dataset
3. Store dataframe
4. Provide dataset information
5. Provide metadata
6. Return dataframe to downstream agents

Author : Biswadip Choudhury
Project : CLASSIFIC-AI
==========================================================
"""

import pandas as pd

from core.base_agent import BaseAgent
from core.agent_output import AgentOutput

from utils.file_handler import load_data
from utils.validator import validate_dataframe

from agents.dataset.dashboard import DatasetDashboard
from agents.dataset.report import DatasetReport
from agents.dataset.recommendation import DatasetRecommendation
from agents.dataset.readiness import DatasetReadiness
from agents.dataset.approval import DatasetApproval


class DatasetAgent(BaseAgent):
    """
    CLASSIFIC-AI Dataset Agent

    This is the first agent executed by the Master
    Orchestrator.

    Every downstream agent receives the dataframe
    from this agent instead of loading the dataset again.
    """

    def __init__(self):

        super().__init__("Dataset Agent")

        self.df = None

    ####################################################
    # Agent Components
    ####################################################

        self.dashboard = DatasetDashboard()

        self.report = DatasetReport()

        self.recommendation = DatasetRecommendation()

        self.readiness = DatasetReadiness()

        self.approval = DatasetApproval()

    # -----------------------------------------------------
    # Main Execution
    # -----------------------------------------------------

    def execute(self, file_path):
        """
        Loads and validates the dataset.

        Parameters
        ----------
        file_path : str | Path

        Returns
        -------
        pandas.DataFrame
        """

        self.df = load_data(file_path)

        validate_dataframe(self.df)

        ####################################################
        # Dataset Summary
        ####################################################

        summary = self.dataset_info()

        dashboard = self.dashboard.build(summary)

        report = self.report.build(summary)

        recommendation = self.recommendation.build(summary)

        readiness = self.readiness.build(summary)

        approval = self.approval.build(readiness)


        ####################################################
        # Return Standardized Agent Output
        ####################################################

        return AgentOutput(

            agent_name=self.name,

            status="Completed",

            dataframe=self.df,

            summary=summary,

            dashboard=dashboard,

            report=report,

            recommendations=recommendation,

            readiness=readiness,

            approval_status=approval,

        )

    # -----------------------------------------------------
    # Dataset Access
    # -----------------------------------------------------

    def get_dataframe(self):
        """
        Returns loaded dataframe.
        """
        return self.df

    # -----------------------------------------------------
    # Dataset Information
    # -----------------------------------------------------

    def get_shape(self):
        """
        Returns dataset shape.
        """
        return self.df.shape

    def get_rows(self):
        """
        Returns number of rows.
        """
        return self.df.shape[0]

    def get_columns_count(self):
        """
        Returns number of columns.
        """
        return self.df.shape[1]

    def get_columns(self):
        """
        Returns all column names.
        """
        return self.df.columns.tolist()

    def get_column_types(self):
        """
        Returns dataframe dtypes.
        """
        return self.df.dtypes

    # -----------------------------------------------------
    # Column Categories
    # -----------------------------------------------------

    def get_numeric_columns(self):
        """
        Returns numeric columns.
        """
        return self.df.select_dtypes(include=["number"]).columns.tolist()

    def get_categorical_columns(self):
        """
        Returns categorical columns.
        """
        return self.df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    def get_datetime_columns(self):
        """
        Returns datetime columns.
        """
        return self.df.select_dtypes(
            include=["datetime64"]
        ).columns.tolist()

    # -----------------------------------------------------
    # Data Quality
    # -----------------------------------------------------

    def get_missing_summary(self):
        """
        Returns missing value summary.
        """
        return self.df.isnull().sum()

    def get_duplicate_count(self):
        """
        Returns duplicate row count.
        """
        return self.df.duplicated().sum()

    # -----------------------------------------------------
    # Dataset Memory
    # -----------------------------------------------------

    def get_memory_usage(self):
        """
        Returns memory usage in bytes.
        """
        return self.df.memory_usage(deep=True).sum()

    def get_dataset_size(self):
        """
        Returns dataset size in MB.
        """
        return round(
            self.get_memory_usage() / 1024 / 1024,
            2
        )

    # -----------------------------------------------------
    # Machine Learning Helpers
    # -----------------------------------------------------

    def get_target_column(self, target_column):
        """
        Returns target column.
        """
        return self.df[target_column]

    def get_feature_columns(self, target_column):
        """
        Returns feature dataframe.
        """
        return self.df.drop(columns=[target_column])

    # -----------------------------------------------------
    # Dataset Summary
    # -----------------------------------------------------

    def dataset_info(self):
        """
        Returns dataset summary.
        """

        return {
    "Rows": int(self.get_rows()),
    "Columns": int(self.get_columns_count()),
    "Numeric Columns": int(len(self.get_numeric_columns())),
    "Categorical Columns": int(len(self.get_categorical_columns())),
    "Datetime Columns": int(len(self.get_datetime_columns())),
    "Duplicate Rows": int(self.get_duplicate_count()),
    "Dataset Size (MB)": float(self.get_dataset_size())
    }
    
    
