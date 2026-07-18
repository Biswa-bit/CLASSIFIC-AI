"""
==============================================================
CLASSIFIC-AI

Workflow Manager

Controls execution order of AI agents.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""


class WorkflowManager:
    """
    Stores pipeline workflow.
    """

    def __init__(self):

        self.workflow = []

    ###########################################################
    # Add Agent
    ###########################################################

    def add(self, name, agent):

        self.workflow.append(
            {
                "name": name,
                "agent": agent
            }
        )

    ###########################################################
    # Return Workflow
    ###########################################################

    def get_workflow(self):

        return self.workflow

    ###########################################################
    # Clear Workflow
    ###########################################################

    def clear(self):

        self.workflow.clear()

    ###########################################################
    # Total Agents
    ###########################################################

    def size(self):

        return len(self.workflow)
    