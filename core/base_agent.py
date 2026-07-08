"""
==========================================================
CLASSIFIC-AI Base Agent
==========================================================

Every AI Agent in the framework will inherit from this class.

Examples

EDA Agent

Feature Engineering Agent

Model Training Agent

Hyperparameter Agent

Evaluation Agent

Deployment Agent

Report Agent

==========================================================
"""

from abc import ABC, abstractmethod


class BaseAgent(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        """
        Every AI agent must implement execute().
        """
        pass

    def info(self):
        """
        Display agent information.
        """
        print(f"Running Agent: {self.name}")