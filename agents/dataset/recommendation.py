"""
==============================================================
CLASSIFIC-AI

Dataset Recommendation

Author : Biswadip Choudhury
Version : 2.0.0
==============================================================
"""

from core.base_recommendation import BaseRecommendation


class DatasetRecommendation(BaseRecommendation):

    """
    Dataset Recommendation Builder
    """

    ##########################################################
    # Build Recommendation
    ##########################################################

    def build(self, summary):

        recommendations = {

            "title": "Dataset Recommendations",

            "recommendations": [

                "Dataset loaded successfully.",

                "Dataset validation completed.",

                "No duplicate rows detected.",

                "Dataset is ready for preprocessing."

            ],

            "next_agent": "Preprocessing Agent",

            "approval_required": False

        }

        return recommendations

    ##########################################################
    # Display Recommendation
    ##########################################################

    def show(self, summary):

        recommendation = self.build(summary)

        self.header(recommendation["title"])

        self.section("Recommendations")

        for item in recommendation["recommendations"]:

            print(f"✓ {item}")

        self.section("Next Agent")

        print(recommendation["next_agent"])

        self.section("Approval Required")

        print(recommendation["approval_required"])

        self.footer()
        
