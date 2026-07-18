from pathlib import Path

from agents.dataset_agent import DatasetAgent
from agents.preprocessing_agent import PreprocessingAgent
from agents.profiling_agent import ProfilingAgent

# --------------------------------------------------
# Dataset
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

# --------------------------------------------------
# Dataset Agent
# --------------------------------------------------

print("\n" + "=" * 80)
print("RUNNING DATASET AGENT")
print("=" * 80)

dataset_agent = DatasetAgent()

df = dataset_agent.execute(DATASET)

# --------------------------------------------------
# Preprocessing Agent
# --------------------------------------------------

print("\n" + "=" * 80)
print("RUNNING PREPROCESSING AGENT")
print("=" * 80)

preprocessing_agent = PreprocessingAgent()

preprocessing_results = preprocessing_agent.execute(df)

clean_df = preprocessing_results["dataframe"]

# --------------------------------------------------
# Profiling Agent
# --------------------------------------------------

print("\n" + "=" * 80)
print("RUNNING PROFILING AGENT")
print("=" * 80)

profiling_agent = ProfilingAgent()

profiling_results = profiling_agent.execute(clean_df)

print("\n")
print("=" * 80)
print("PIPELINE EXECUTED SUCCESSFULLY")
print("=" * 80)

print("\nReturned Objects")

print(profiling_results.keys())
