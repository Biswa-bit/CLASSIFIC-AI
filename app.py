"""
======================================================================
CLASSIFIC-AI

Main Application

AI-Powered Supervised Machine Learning Framework

Author : Biswadip Choudhury
======================================================================
"""

# ======================================================================
# IMPORT AGENTS
# ======================================================================

from agents.dataset_agent import DatasetAgent
from agents.preprocessing_agent import PreprocessingAgent


# ======================================================================
# DEVELOPMENT ROADMAP
# ======================================================================
#
# Completed
# ---------
# ✓ Dataset Agent
# ✓ Preprocessing Agent
#
# Upcoming Agents
# ---------------
# □ Data Profiling Agent
# □ Business Rules Agent
# □ EDA Agent
# □ Feature Engineering Agent
# □ Feature Selection Agent
# □ Data Splitting Agent
# □ Class Imbalance Agent
# □ Scaling Agent
# □ Model Recommendation Agent
# □ Hyperparameter Tuning Agent
# □ Ensemble Learning Agent
# □ Model Evaluation Agent
# □ Explainability Agent
# □ Report Generation Agent
# □ Deployment Agent
# □ Monitoring Agent
# □ Master Orchestrator Agent
#
# ======================================================================


def main():
    """
    Main entry point of CLASSIFIC-AI.
    """

    print("\n" + "=" * 70)
    print("                 CLASSIFIC-AI")
    print(" AI-Powered Supervised Machine Learning Framework")
    print("=" * 70)

    # ==================================================================
    # STEP 1 : DATASET AGENT
    # ==================================================================

    print("\n[STEP 1] Dataset Agent")

    dataset_agent = DatasetAgent()

    file_path = "datasets/Glassdor.xlsx"

    df = dataset_agent.execute(file_path)

    print("✓ Dataset Agent Completed")

    # ==================================================================
    # STEP 2 : PREPROCESSING AGENT
    # ==================================================================

    print("\n[STEP 2] Preprocessing Agent")

    preprocessing_agent = PreprocessingAgent()

    preprocessing_results = preprocessing_agent.execute(df)
    df = preprocessing_results["dataframe"]

    # ==================================================================
    # PIPELINE SUMMARY
    # ==================================================================

    print("\n" + "=" * 70)
    print("CLASSIFIC-AI PIPELINE")
    print("=" * 70)

    print("\nPipeline Status")
    print("-" * 30)

    print(f"Dataset Shape : {df.shape}")
    print(f"Rows          : {df.shape[0]}")
    print(f"Columns       : {df.shape[1]}")

    print("\nCompleted Agents")
    print("-" * 30)
    print("✓ Dataset Agent")
    print("✓ Preprocessing Agent")

    print("\nNext Agent")
    print("-" * 30)
    print("→ Data Profiling Agent")

    print("\n" + "=" * 70)
    print("CLASSIFIC-AI Pipeline Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()
    