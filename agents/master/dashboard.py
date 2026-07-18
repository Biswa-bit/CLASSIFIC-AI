"""
==============================================================
CLASSIFIC-AI

Enterprise Execution Dashboard

Displays execution summary of the complete pipeline.

Author : Biswadip Choudhury
Version : 2.0.0
==============================================================
"""

from datetime import datetime
import platform
from core.base_dashboard import BaseDashboard


class ExecutionDashboard(BaseDashboard):

    """
    Enterprise Dashboard
    """

    def pipeline_information(
        self,
        run_id,
        execution_time,
        pipeline_status,
    ):

        print()

        print("Pipeline Information")

        print("-" * 90)

        print(f"Run ID               : {run_id}")

        print(
            f"Execution Date       : "
            f"{datetime.now().strftime('%d-%b-%Y %H:%M:%S')}"
        )

        print(f"Execution Time       : {execution_time:.3f} sec")

        print(f"Pipeline Status      : {pipeline_status}")

        print("Environment          : Development")

        print(f"Python Version       : {platform.python_version()}")

        print("CLASSIFIC-AI Version : 1.0.0")

    def dataset_information(
        self,
        dataset_name,
        rows,
        columns,
        dataset_size,
    ):

        print()

        print("=" * 90)

        print()

        print("Dataset Information")

        print("-" * 90)

        print(f"Dataset Name         : {dataset_name}")

        print(f"Rows                 : {rows}")

        print(f"Columns              : {columns}")

        print(f"Dataset Size         : {dataset_size} MB")

    def execution_timeline(
        self,
        execution_logs,
    ):

        print()

        print("=" * 90)

        print()

        print("Pipeline Execution")

        print("-" * 90)

        print(
            "{:<30} {:<15} {:>12}".format(
                "Agent",
                "Status",
                "Time(s)"
            )
        )

        print("-" * 90)

        total_time = 0

        for log in execution_logs:

            total_time += log["Execution Time (sec)"]

            print(
                "{:<30} {:<15} {:>12.3f}".format(
                    log["Agent"],
                    log["Status"],
                    log["Execution Time (sec)"]
                )
            )

        print("-" * 90)

        print(f"Total Execution Time : {total_time:.3f} sec")

    #################################################################
    # MAIN DASHBOARD
    #################################################################

    def show(
        self,
        execution_logs,
        dataset_name,
        rows,
        columns,
        dataset_size,
    ):

        total_time = sum(
            log["Execution Time (sec)"]
            for log in execution_logs
        )

        run_id = (
            "RUN_" +
            datetime.now().strftime("%Y%m%d_%H%M%S")
        )

        self.header("CLASSIFIC-AI ENTERPRISE EXECUTION DASHBOARD")

        self.pipeline_information(
            run_id=run_id,
            execution_time=total_time,
            pipeline_status="SUCCESS",
        )

        self.dataset_information(
            dataset_name,
            rows,
            columns,
            dataset_size,
        )

        self.execution_timeline(
            execution_logs,
        )

        self.footer()
