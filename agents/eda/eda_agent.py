"""
==============================================================
CLASSIFIC-AI

EDA Agent

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

import pandas as pd

from core.base_agent import BaseAgent

from agents.eda.dashboard import EDADashboard
from agents.eda.report import EDAReport
from agents.eda.recommendation import EDARecommendation

from agents.eda.dataset_overview import DatasetOverview
from agents.eda.data_quality import DataQuality
from agents.eda.missing_data import MissingData
from agents.eda.distribution_analysis import DistributionAnalysis

class EDAAgent(BaseAgent):
    """
    CLASSIFIC-AI EDA Agent
    """

    def __init__(self):

        super().__init__("EDA Agent")

        ####################################################
        # Agent Components
        ####################################################

        self.dashboard = EDADashboard()
        self.report = EDAReport()
        self.recommendation = EDARecommendation()

        ####################################################
        # Core EDA Modules
        ####################################################

        self.dataset_overview = DatasetOverview()
        self.data_quality = DataQuality()
        self.missing_data = MissingData()
        self.distribution_analysis = DistributionAnalysis()

        ##############################################################
        # Dashboard
        ##############################################################

    def get_dashboard(self):

        return self.dashboard


        ##############################################################
        # Report
        ##############################################################

    def get_report(self):

        return self.report


        ##############################################################
        # Recommendation
        ##############################################################

    def get_recommendation(self):

        return self.recommendation
    
        ##############################################################
        # Execute
        ##############################################################

    def execute(self, df):

        print()
        print("#" * 70)
        print("#")
        print("#        EDA AGENT STARTED")
        print("#")
        print("#" * 70)
        print()

        ##############################################################
        # Dataset Overview
        ##############################################################

        dataset_overview_result = self.dataset_overview.execute(df)

        ##############################################################
        # Data Quality
        ##############################################################

        data_quality_result = self.data_quality.execute(df)

        ##############################################################
        # Missing Data
        ##############################################################

        missing_data_result = self.missing_data.execute(df)

        ##############################################################
        # Distribution Analysis
        ##############################################################

        distribution_result = self.distribution_analysis.execute(df)

        ##############################################################
        # Combine Results
        ##############################################################

        result = {

            "dataset_overview": dataset_overview_result,

            "data_quality": data_quality_result,

            "missing_data": missing_data_result,

            "distribution_analysis": distribution_result

        }

        ##############################################################
        # Executive Report
        ##############################################################

        report_result = self.report.generate(result)

        result["executive_report"] = report_result

        ##############################################################
        # Recommendations
        ##############################################################

        recommendation_result = self.recommendation.generate(result)

        result["recommendations"] = recommendation_result

        ##############################################################
        # Completion Message
        ##############################################################

        print()
        print("#" * 70)
        print("#")
        print("#        EDA AGENT COMPLETED")
        print("#")
        print("#" * 70)
        print()

        return result

    
        