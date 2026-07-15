"""
==============================================================
CLASSIFIC-AI

Data Profiling Agent

Purpose
-------
Generates a comprehensive statistical profile of the dataset.

Responsibilities
----------------
• Dataset Overview
• Column Intelligence
• Statistical Summary
• Distribution Analysis
• Correlation Analysis
• Outlier Detection
• Feature Quality Assessment
• AI Recommendations
• Executive Profiling Report

Completed Modules
-----------------
✓ Dataset Overview
✓ Column Intelligence
✓ Statistics Summary
✓ Feature Quality
✓ Distribution Analysis

In Development
--------------
□ Correlation Analysis
□ Outlier Detection
□ Recommendation Engine
□ Executive Profiling Report

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

import pandas as pd

from core.base_agent import BaseAgent
from agents.profiling.dataset_overview import DatasetOverview
from agents.profiling.column_intelligence import ColumnIntelligence
from agents.profiling.statistics_summary import StatisticsSummary
from agents.profiling.feature_quality import FeatureQuality
from agents.profiling.distribution_analysis import DistributionAnalysis
from agents.profiling.correlation_analysis import CorrelationAnalysis
from agents.profiling.outlier_detection import OutlierDetection
from agents.profiling.profiling_recommendation import ProfilingRecommendation
from agents.profiling.profiling_report import ProfilingReport

class ProfilingAgent(BaseAgent):

    def __init__(self):

        super().__init__("Data Profiling Agent")

    def execute(self, df: pd.DataFrame):

        print()
        print("#" * 70)
        print("#")
        print("#        DATA PROFILING AGENT STARTED")
        print("#")
        print("#" * 70)
        print()

        ###############################################################
        # Dataset Overview Module
        ###############################################################

        overview_module = DatasetOverview()

        overview_result = overview_module.analyze(df)

        ###############################################################
        # Column Intelligence Module
        ###############################################################

        column_module = ColumnIntelligence()

        column_result = column_module.analyze(df)


        ###############################################################
        # Statistics Summary Module
        ###############################################################

        statistics_module = StatisticsSummary()

        statistics_result = statistics_module.analyze(df)

        ###############################################################
        # Feature Quality Module
        ###############################################################

        feature_module = FeatureQuality()

        feature_result = feature_module.analyze(df)


        ###############################################################
        # Distribution Analysis Module
        ###############################################################

        distribution_module = DistributionAnalysis()

        distribution_result = distribution_module.analyze(df)


        ###############################################################
        # Correlation Analysis Module
        ###############################################################

        correlation_module = CorrelationAnalysis()

        correlation_result = correlation_module.analyze(df)


        ###############################################################
        # Outlier Detection Module
        ###############################################################

        outlier_module = OutlierDetection()

        outlier_result = outlier_module.analyze(df)

        ###############################################################
        # Profiling Recommendation Module
        ###############################################################

        recommendation_module = ProfilingRecommendation()

        recommendation_result = recommendation_module.analyze(

            df,

            overview_result,

            column_result,

            statistics_result,

            feature_result,

            distribution_result,

            correlation_result,

            outlier_result

        )

        ###############################################################
        # Return Results
        ###############################################################

        result = {

            "module": "Data Profiling Agent",

            "status": "Completed",

            ###########################################################
            # Original Dataset
            ###########################################################

            "dataset": {

            "raw": df

            },

            ###########################################################
            # Profiling Modules
            ###########################################################

            "dataset_overview": overview_result,

            "column_intelligence": column_result,

            "statistics_summary": statistics_result,

            "feature_quality": feature_result,

            "distribution_analysis": distribution_result,

            "correlation_analysis": correlation_result,

            "outlier_detection": outlier_result,

            "profiling_recommendation": recommendation_result

        }

        ###############################################################
        # Executive Profiling Report
        ###############################################################

        report_module = ProfilingReport()

        report_result = report_module.generate(result)

        ###############################################################
        # Store Executive Report
        ###############################################################

        result["executive_report"] = report_result

        ###############################################################
        # Completion Message
        ###############################################################

        print()
        print("#" * 70)
        print("#")
        print("#        DATA PROFILING AGENT COMPLETED")
        print("#")
        print("#" * 70)

        return result

        
    

      

    

       
    
    
    
