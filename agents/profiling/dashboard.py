"""
==============================================================
CLASSIFIC-AI

Profiling Dashboard

Displays Data Profiling results.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_dashboard import BaseDashboard


class ProfilingDashboard(BaseDashboard):
    """
    Dashboard for the Profiling Agent.
    """

    def show(self, profiling_result):

        self.header("DATA PROFILING DASHBOARD")

        ########################################################
        # Dataset Overview
        ########################################################

        if "dataset_overview" in profiling_result:

            self.section("Dataset Overview")

            for key, value in profiling_result["dataset_overview"].items():
                print(f"{key:<35}: {value}")

        ########################################################
        # Statistics Summary
        ########################################################

        if "statistics_summary" in profiling_result:

            self.section("Statistics Summary")

            stats = profiling_result["statistics_summary"]

            if isinstance(stats, dict):

                for key, value in stats.items():
                    print(f"{key:<35}: {value}")

        ########################################################
        # Feature Quality
        ########################################################

        if "feature_quality" in profiling_result:

            self.section("Feature Quality")

            quality = profiling_result["feature_quality"]

            if isinstance(quality, dict):

                for key, value in quality.items():
                    print(f"{key:<35}: {value}")

        ########################################################
        # Correlation
        ########################################################

        if "correlation_analysis" in profiling_result:

            self.section("Correlation Analysis")

            print("Correlation analysis completed.")

        ########################################################
        # Outlier Detection
        ########################################################

        if "outlier_detection" in profiling_result:

            self.section("Outlier Detection")

            print("Outlier detection completed.")

        ########################################################

        self.footer()
        