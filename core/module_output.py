"""
==========================================================
CLASSIFIC-AI

Module Output

Every module returns this object.

==========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ModuleOutput:

    module_name: str

    status: str

    summary: dict

    dashboard: Any

    report: Any

    recommendations: Any
    