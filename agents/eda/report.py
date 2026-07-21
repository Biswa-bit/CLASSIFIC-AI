"""
==============================================================
CLASSIFIC-AI

EDA Executive Report

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_report import BaseReport


class EDAReport(BaseReport):
    """
    Executive Report for EDA Agent.
    """

    def generate(self, eda_result):

        report = {}

        report["Dataset Overview"] = eda_result.get(
            "dataset_overview",
            {}
        )

        report["Data Quality"] = eda_result.get(
            "data_quality",
            {}
        )

        report["Missing Data"] = eda_result.get(
            "missing_data",
            {}
        )

        report["Distribution Analysis"] = eda_result.get(
            "distribution_analysis",
            {}
        )

        return report
    