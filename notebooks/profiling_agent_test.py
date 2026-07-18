from pathlib import Path

from agents.dataset_agent import DatasetAgent
from agents.preprocessing_agent import PreprocessingAgent
from agents.profiling_agent import ProfilingAgent

# --------------------------------------------------
# Dataset Path
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

# --------------------------------------------------
# Dataset Agent
# --------------------------------------------------

dataset_agent = DatasetAgent()

df = dataset_agent.execute(DATASET)

# --------------------------------------------------
# Preprocessing Agent
# --------------------------------------------------

preprocessing_agent = PreprocessingAgent()

preprocessing_results = preprocessing_agent.execute(df)

# Clean dataframe

clean_df = preprocessing_results["dataframe"]

# --------------------------------------------------
# Profiling Agent
# --------------------------------------------------

profiling_agent = ProfilingAgent()

profile = profiling_agent.execute(clean_df)

print(profile)
