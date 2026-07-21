"""
==============================================================
CLASSIFIC-AI

EDA Dashboard

Displays EDA execution summary.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_dashboard import BaseDashboard


class EDADashboard(BaseDashboard):
    """
    Dashboard for EDA Agent.
    """

    def show(self, eda_result):

        self.header("CLASSIFIC-AI EDA DASHBOARD")

        ########################################################
        # Dataset Overview
        ########################################################

        if "dataset_overview" in eda_result:

            self.section("Dataset Overview")

            overview = eda_result["dataset_overview"]

            if isinstance(overview, dict):

                for key, value in overview.items():

                    print(f"{key:<35}: {value}")

        ########################################################
        # Data Quality
        ########################################################

        if "data_quality" in eda_result:

            self.section("Data Quality")

            print("Completed")

        ########################################################
        # Missing Data
        ########################################################

        if "missing_data" in eda_result:

            self.section("Missing Data")

            print("Completed")

        ########################################################
        # Distribution Analysis
        ########################################################

        if "distribution_analysis" in eda_result:

            self.section("Distribution Analysis")

            print("Completed")

        self.footer()
        