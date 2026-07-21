"""
==========================================================
CLASSIFIC-AI

Execution Context

Shared information passed
between agents.

==========================================================
"""

from dataclasses import dataclass

from core.governance import Governance


@dataclass
class ExecutionContext:

    dataset_name: str

    target_column: str

    governance: Governance

    pipeline_name: str = ""

    execution_id: str = ""
    