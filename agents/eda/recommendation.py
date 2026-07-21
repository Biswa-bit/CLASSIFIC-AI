"""
==============================================================
CLASSIFIC-AI

EDA Recommendation Engine

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_recommendation import BaseRecommendation


class EDARecommendation(BaseRecommendation):
    """
    Recommendation Engine for EDA Agent.
    """

    def generate(self, eda_result):

        recommendations = []

        if "missing_data" in eda_result:

            recommendations.append(
                "Review missing values before modelling."
            )

        if "distribution_analysis" in eda_result:

            recommendations.append(
                "Inspect skewed variables."
            )

        if "data_quality" in eda_result:

            recommendations.append(
                "Review data quality issues."
            )

        recommendations.append(
            "EDA completed successfully."
        )

        return recommendations
    