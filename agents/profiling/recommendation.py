"""
==============================================================
CLASSIFIC-AI

Profiling Recommendation Engine

Generates recommendations based on profiling results.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_recommendation import BaseRecommendation


class ProfilingRecommendation(BaseRecommendation):
    """
    Recommendation Engine for Profiling Agent.
    """

    def generate(self, profiling_result):

        recommendations = []

        ########################################################
        # Missing Values
        ########################################################

        if "missing_value_analysis" in profiling_result:

            recommendations.append(
                "Review columns containing missing values."
            )

        ########################################################
        # Duplicate Rows
        ########################################################

        if "duplicate_analysis" in profiling_result:

            recommendations.append(
                "Review duplicate rows before model training."
            )

        ########################################################
        # Correlation
        ########################################################

        if "correlation_analysis" in profiling_result:

            recommendations.append(
                "Inspect highly correlated variables."
            )

        ########################################################
        # Outliers
        ########################################################

        if "outlier_detection" in profiling_result:

            recommendations.append(
                "Investigate detected outliers."
            )

        ########################################################
        # Distribution
        ########################################################

        if "distribution_analysis" in profiling_result:

            recommendations.append(
                "Review skewed features and consider transformation."
            )

        ########################################################
        # Feature Quality
        ########################################################

        if "feature_quality" in profiling_result:

            recommendations.append(
                "Evaluate low-quality features for removal or improvement."
            )

        ########################################################
        # Dataset Health
        ########################################################

        recommendations.append(
            "Profiling completed successfully."
        )

        return recommendations
    