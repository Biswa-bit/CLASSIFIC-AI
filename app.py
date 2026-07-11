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

    # ==============================================================
    # STEP 1 : DATASET AGENT
    # ==============================================================

    print("\n[STEP 1] Dataset Agent")

    dataset_agent = DatasetAgent()

    file_path = "datasets/Glassdor.xlsx"

    df = dataset_agent.execute(file_path)

    print("✓ Dataset Agent Completed")

    # ==============================================================
    # STEP 2 : PREPROCESSING AGENT
    # ==============================================================

    print("\n[STEP 2] Preprocessing Agent")

    preprocessing_agent = PreprocessingAgent()

    preprocessing_results = preprocessing_agent.execute(df)

    # Updated dataframe
    df = preprocessing_results["dataframe"]

    # Recommendation Engine Result
    recommendation = preprocessing_results["recommendation_result"]

    # ==============================================================
    # PIPELINE SUMMARY
    # ==============================================================

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

    # ==============================================================
    # AI PREPROCESSING REPORT
    # ==============================================================

    print("\n" + "=" * 70)
    print("AI PREPROCESSING REPORT")
    print("=" * 70)

    # -------------------------
    # Summary
    # -------------------------

    print("\nSummary")
    print("-" * 30)

    summary = recommendation["summary"]

    print("Dataset Health Score :", summary["Dataset Health Score"])
    print("Readiness Status     :", summary["Readiness Status"])
    print("Issues Detected      :", summary["Issues Detected"])
    print("Recommendations      :", summary["Recommendations"])
    print("Human Approval       :", summary["Human Approval"])

    # -------------------------
    # Issues
    # -------------------------

    print("\nIssues Detected")
    print("-" * 30)

    if recommendation["issues_detected"]:

        for issue in recommendation["issues_detected"]:
            print(f"• {issue}")

    else:

        print("No issues detected.")

    # -------------------------
    # Recommendations
    # -------------------------

    print("\nRecommendations")
    print("-" * 30)

    if recommendation["recommendations"]:

        for rec in recommendation["recommendations"]:
            print(f"• {rec}")

    else:

        print("No recommendations.")

    # -------------------------
    # Preprocessing Steps
    # -------------------------

    print("\nSuggested Preprocessing Steps")
    print("-" * 30)

    if recommendation["preprocessing_steps"]:

        for step in recommendation["preprocessing_steps"]:
            print(f"• {step}")

    else:

        print("No preprocessing required.")

    # -------------------------
    # Readiness
    # -------------------------

    print("\nReadiness Status")
    print("-" * 30)

    print(recommendation["readiness_status"])

    # -------------------------
    # Human Approval
    # -------------------------

    print("\nHuman Approval Required")
    print("-" * 30)

    print(recommendation["human_approval_required"])

    # ==============================================================
    # END
    # ==============================================================

    print("\n" + "=" * 70)
    print("CLASSIFIC-AI Pipeline Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()
    