from pathlib import Path

from agents.dataset_agent import DatasetAgent

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

agent = DatasetAgent()

df = agent.execute(DATASET)

print("=" * 60)
print("CLASSIFIC-AI Dataset Loaded Successfully")
print("=" * 60)

print(df.head())

print()

print("Shape:", agent.get_shape())

print()

print("Columns:")

print(agent.get_columns())

print()

print("Dataset Summary:")

print(agent.dataset_info())

