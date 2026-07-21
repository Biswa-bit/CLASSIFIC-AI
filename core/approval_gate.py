"""
==========================================================
CLASSIFIC-AI

Approval Gate

Used for Human-in-the-Loop mode.

==========================================================
"""

from dataclasses import dataclass


@dataclass
class ApprovalGate:

    stage: str

    approved: bool = False

    comments: str = ""
    