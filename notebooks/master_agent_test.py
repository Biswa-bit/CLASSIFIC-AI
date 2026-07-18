from pathlib import Path

from agents.master.master_agent import MasterAgent


BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = BASE_DIR / "datasets" / "CLASSIFIC_AI_EDA.xlsx"


master = MasterAgent()

result = master.execute(DATASET)


print()

print("=" * 80)

print("MASTER AGENT RETURNED")

print("=" * 80)

print(result.keys())
