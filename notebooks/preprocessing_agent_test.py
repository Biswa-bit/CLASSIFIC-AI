from pathlib import Path

from agents.dataset_agent import DatasetAgent
from agents.preprocessing_agent import PreprocessingAgent

# -------------------------------------------------------
# Dataset Location
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

# -------------------------------------------------------
# Run Dataset Agent
# -------------------------------------------------------

print("=" * 80)
print("RUNNING DATASET AGENT")
print("=" * 80)

dataset_agent = DatasetAgent()

df = dataset_agent.execute(DATASET)

# -------------------------------------------------------
# Run Preprocessing Agent
# -------------------------------------------------------

print("\n")
print("=" * 80)
print("RUNNING PREPROCESSING AGENT")
print("=" * 80)

preprocessing_agent = PreprocessingAgent()

results = preprocessing_agent.execute(df)

print("\n")
print("=" * 80)
print("PREPROCESSING PIPELINE COMPLETED")
print("=" * 80)

print()

print("Returned Objects")

print(results.keys())
