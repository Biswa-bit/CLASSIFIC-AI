"""
==============================================================
CLASSIFIC-AI

Pipeline Controller

Responsible for executing the complete AI pipeline.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from agents.master.workflow_manager import WorkflowManager
from agents.master.state_manager import StateManager


class PipelineController:
    """
    Executes all AI agents in sequence.
    """

    def __init__(self):

        self.workflow = WorkflowManager()

        self.state = StateManager()

    ###########################################################
    # Register Agent
    ###########################################################

    def add_agent(self, name, agent):

        self.workflow.add(name, agent)

    ###########################################################
    # Execute Pipeline
    ###########################################################

    def execute(self, *args, **kwargs):

        results = {}

        for step in self.workflow.get_workflow():

            name = step["name"]

            agent = step["agent"]

            result = agent.execute(*args, **kwargs)

            results[name] = result

            self.state.set(name, result)

        return results

    ###########################################################
    # Pipeline State
    ###########################################################

    def get_state(self):

        return self.state.get_state()

    ###########################################################
    # Reset
    ###########################################################

    def clear(self):

        self.workflow.clear()

        self.state.clear()
        