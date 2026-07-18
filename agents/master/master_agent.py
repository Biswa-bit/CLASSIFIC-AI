"""
==============================================================
CLASSIFIC-AI

Master Orchestrator Agent

Purpose
-------
Coordinates all AI Agents in the correct order.

Current Pipeline
----------------

Dataset Agent
      ↓
Preprocessing Agent
      ↓
Profiling Agent

Future Pipeline
---------------

Dataset
↓
Preprocessing
↓
Profiling
↓
EDA
↓
Feature Engineering
↓
Model Training
↓
Evaluation
↓
Deployment

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""

from core.base_agent import BaseAgent
from agents.master.execution_tracker import ExecutionTracker
from agents.master.dashboard import ExecutionDashboard

from agents.dataset.dataset_agent import DatasetAgent
from agents.preprocessing.preprocessing_agent import PreprocessingAgent
from agents.profiling.profiling_agent import ProfilingAgent


class MasterAgent(BaseAgent):
    """
    Master Orchestrator

    Responsible for coordinating all AI agents.
    """

    def __init__(self):

        super().__init__("Master Orchestrator")

        self.dataset_agent = DatasetAgent()

        self.preprocessing_agent = PreprocessingAgent()

        self.profiling_agent = ProfilingAgent()
        self.tracker = ExecutionTracker()

    def execute(self, dataset_path):

        print()
        print("=" * 80)
        print("MASTER ORCHESTRATOR STARTED")
        print("=" * 80)

        ####################################################
        # Dataset Agent
        ####################################################

        record = self.tracker.start("Dataset Agent")
        try:
            dataframe = self.dataset_agent.execute(dataset_path)

            self.tracker.end(record)

        except Exception as e: 
            self.tracker.fail(record, e)
            raise
   
        ####################################################
        # Preprocessing Agent
        ####################################################

        record = self.tracker.start("Preprocessing Agent")
        try:
                preprocessing_result = self.preprocessing_agent.execute(dataframe)

                clean_dataframe = preprocessing_result["dataframe"]

                self.tracker.end(record)

        except Exception as e:
                self.tracker.fail(record, e)
                raise    


        ####################################################
        # Profiling Agent
        ####################################################

        record = self.tracker.start("Profiling Agent")
        try:
             profiling_result = self.profiling_agent.execute(clean_dataframe)

             self.tracker.end(record)
        except Exception as e:
             self.tracker.fail(record, e)
             raise     

        ####################################################
        # Final Result
        ####################################################

        result = {

            "status": "Completed",

            "dataset": dataframe,

            "clean_dataframe": clean_dataframe,

            "preprocessing": preprocessing_result,

            "profiling": profiling_result

        }

        print()
        print("=" * 80)
        print("MASTER ORCHESTRATOR COMPLETED")
        print("=" * 80)
        print()

        ####################################################
        # Enterprise Execution Dashboard
        ####################################################

       ####################################################
        # Enterprise Execution Dashboard
        ####################################################

        dashboard = ExecutionDashboard()

        dataset_size = round(
            clean_dataframe.memory_usage(deep=True).sum()
            / 1024
            / 1024,
            2,
        )

        dashboard.show(

            execution_logs=self.tracker.summary(),

            dataset_name=dataset_path.name,

            rows=clean_dataframe.shape[0],

            columns=clean_dataframe.shape[1],

            dataset_size=dataset_size,

        )

        return result
    

        