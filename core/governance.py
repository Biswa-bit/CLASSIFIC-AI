"""
==========================================================
CLASSIFIC-AI

Governance

Stores governance configuration
for pipeline execution.

==========================================================
"""

from dataclasses import dataclass

from core.execution_mode import ExecutionMode


@dataclass
class Governance:

    execution_mode: ExecutionMode

    approval_required: bool = False

    user_name: str = ""

    comments: str = ""
    