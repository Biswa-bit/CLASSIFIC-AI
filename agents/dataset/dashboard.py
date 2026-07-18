from core.base_dashboard import BaseDashboard


class DatasetDashboard(BaseDashboard):

    def show(
        self,
        dataset_name,
        rows,
        columns,
        dataset_size,
    ):

        self.header("DATASET AGENT DASHBOARD")

        self.section("Dataset Information")

        print(f"Dataset Name : {dataset_name}")
        print(f"Rows         : {rows}")
        print(f"Columns      : {columns}")
        print(f"Size         : {dataset_size} MB")

        self.footer()
        