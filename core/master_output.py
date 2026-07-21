"""
==========================================================
CLASSIFIC-AI

Master Output

Returned by the Master Agent.

==========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class MasterOutput:

    status: str

    execution_time: float

    pipeline_summary: dict

    agent_outputs: Any
    