"""
==============================================================
CLASSIFIC-AI

Dataset Executive Report

Purpose
-------
Builds and displays the Executive Report for the
Dataset Agent.

This report is intended for business users,
management, Streamlit, PDF export,
PowerPoint export, RAG Agent and Copilot.

Author : Biswadip Choudhury
Version : 2.0.0
==============================================================
"""

from core.base_report import BaseReport


class DatasetReport(BaseReport):

    """
    Dataset Executive Report
    """

    ##########################################################
    # Build Report
    ##########################################################

    def build(self, summary):

        """
        Build standardized executive report.

        Parameters
        ----------
        summary : dict

        Returns
        -------
        dict
        """

        report = {

            "title": "Dataset Executive Report",

            "status": "Completed",

            "overview": [

                "Dataset loaded successfully.",

                f"Dataset contains {summary['Rows']} rows.",

                f"Dataset contains {summary['Columns']} columns.",

                "Dataset validation completed.",

                "Dataset is ready for preprocessing."

            ],

            "overall_assessment": "Ready",

            "human_approval_required": False

        }

        return report

    ##########################################################
    # Display Report
    ##########################################################

    def show(self, summary):

        report = self.build(summary)

        self.header(report["title"])

        self.section("Status")

        print(report["status"])

        self.section("Overview")

        for line in report["overview"]:

            print(f"• {line}")

        self.section("Overall Assessment")

        print(report["overall_assessment"])

        self.section("Human Approval Required")

        print(report["human_approval_required"])

        self.footer()
        