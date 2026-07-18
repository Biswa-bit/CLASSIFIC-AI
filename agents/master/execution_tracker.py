"""
==============================================================
CLASSIFIC-AI

Execution Tracker

Purpose
-------
Tracks execution details of every AI Agent.

Author : Biswadip Choudhury
==============================================================
"""

from datetime import datetime


class ExecutionTracker:

    def __init__(self):

        self.logs = []

    def start(self, agent_name):

        return {
            "Agent": agent_name,
            "Start Time": datetime.now(),
            "End Time": None,
            "Execution Time (sec)": None,
            "Status": "Running",
            "Error": None
        }

    def end(self, record):

        end_time = datetime.now()

        record["End Time"] = end_time

        record["Execution Time (sec)"] = round(
            (end_time - record["Start Time"]).total_seconds(),
            3
        )

        record["Status"] = "Completed"

        self.logs.append(record)

    def fail(self, record, error):

        end_time = datetime.now()

        record["End Time"] = end_time

        record["Execution Time (sec)"] = round(
            (end_time - record["Start Time"]).total_seconds(),
            3
        )

        record["Status"] = "Failed"

        record["Error"] = str(error)

        self.logs.append(record)

    def summary(self):

        return self.logs
    