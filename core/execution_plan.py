"""
==========================================================
CLASSIFIC-AI

Execution Plan

Created by Streamlit or Copilot.

Executed by the Master Agent.

==========================================================
"""

from dataclasses import dataclass

from core.execution_context import ExecutionContext


@dataclass
class ExecutionPlan:

    context: ExecutionContext

    selected_agents: list

    selected_modules: dict
    