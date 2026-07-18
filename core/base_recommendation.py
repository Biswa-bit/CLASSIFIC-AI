"""
==============================================================
CLASSIFIC-AI

Base Recommendation

Parent class for all recommendation engines.
==============================================================
"""


class BaseRecommendation:
    """
    Parent class for all recommendation engines.
    """

    def __init__(self):

        self.recommendations = []

    def add(self, message):

        self.recommendations.append(message)

    def get(self):

        return self.recommendations

    def clear(self):

        self.recommendations.clear()
        