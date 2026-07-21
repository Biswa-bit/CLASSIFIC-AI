"""
==========================================================
CLASSIFIC-AI

Base Module

Purpose
-------
Every module inside every agent inherits from this class.

Examples
--------
Dataset Overview Module
Missing Value Module
Distribution Module
Correlation Module
Scaling Module

Every module has the same interface.

Author : Biswadip Choudhury
==========================================================
"""

from abc import ABC, abstractmethod


class BaseModule(ABC):

    def __init__(self, module_name):

        self.module_name = module_name

    @abstractmethod
    def execute(self, dataframe):
        """
        Executes the module.
        """
        pass

    def dashboard(self):
        """
        Returns dashboard information.
        """
        return None

    def report(self):
        """
        Returns executive report.
        """
        return None

    def recommendation(self):
        """
        Returns recommendations.
        """
        return None
    