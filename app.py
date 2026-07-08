"""
==========================================================
CLASSIFIC-AI

Main Application

This is the starting point of the framework.

Author : Biswadip Choudhury
==========================================================
"""

from agents.dataset_agent import DatasetAgent


def main():
    """
    Main function of the application.
    """

    # Create Dataset Agent
    dataset_agent = DatasetAgent()

    # Path of dataset
    file_path = "datasets/Glassdor.xlsx"

    # Execute Dataset Agent
    df = dataset_agent.execute(file_path)

    # Display final message
    print("\nDataset successfully processed.")
    print(f"Final Shape : {df.shape}")


if __name__ == "__main__":
    main()