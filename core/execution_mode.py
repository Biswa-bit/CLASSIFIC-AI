"""
==========================================================
CLASSIFIC-AI

Execution Mode

Defines how CLASSIFIC-AI executes
agents and modules.

Author : Biswadip Choudhury
==========================================================
"""

from enum import Enum


class ExecutionMode(Enum):

    AUTOMATIC = "Automatic"

    HUMAN_IN_LOOP = "Human-in-the-Loop"

    MANUAL = "Manual"
    