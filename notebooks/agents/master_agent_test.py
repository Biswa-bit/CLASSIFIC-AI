
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(PROJECT_ROOT))

from agents.master.master_agent import MasterAgent

DATASET = PROJECT_ROOT / "datasets" / "CLASSIFIC_AI_EDA.xlsx"

master = MasterAgent()

result = master.execute(DATASET)

print()

print("=" * 80)
print("MASTER AGENT RETURNED")
print("=" * 80)

print(result.keys())

