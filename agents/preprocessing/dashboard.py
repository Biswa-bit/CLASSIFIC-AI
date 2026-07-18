"""
==============================================================
CLASSIFIC-AI

Preprocessing Dashboard

Displays preprocessing summary.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_dashboard import BaseDashboard


class PreprocessingDashboard(BaseDashboard):

    """
    Dashboard for Preprocessing Agent.
    """

    def show(self, preprocessing_result):

        self.header("PREPROCESSING AGENT DASHBOARD")

        self.section("Preprocessing Summary")

        for key, value in preprocessing_result.items():

            print(f"{key} : {value}")

        self.footer()
        