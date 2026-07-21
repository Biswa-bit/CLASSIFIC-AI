"""
==========================================================
CLASSIFIC-AI

Agent Output

Every agent returns this object.

==========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class AgentOutput:

    agent_name: str

    status: str

    dataframe: Any

    summary: dict

    dashboard: Any

    report: Any

    recommendations: Any

    readiness: Any

    approval_status: Any
