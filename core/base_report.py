"""
==============================================================
CLASSIFIC-AI

Base Report

Parent class for all reports.
==============================================================
"""


class BaseReport:
    """
    Parent class for all reports.
    """

    def title(self, title):

        print("=" * 90)
        print(title.center(90))
        print("=" * 90)

    def section(self, title):

        print()
        print(title)
        print("-" * 90)
        