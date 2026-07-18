"""
==============================================================
CLASSIFIC-AI

Base Dashboard

Parent class for all dashboards.

Every dashboard in CLASSIFIC-AI inherits from this class.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""


class BaseDashboard:
    """
    Parent dashboard for all AI Agents.
    """

    def header(self, title):

        print()
        print("=" * 90)
        print(title.center(90))
        print("=" * 90)

    def section(self, title):

        print()
        print("-" * 90)
        print(title)
        print("-" * 90)

    def footer(self):

        print("=" * 90)
        
