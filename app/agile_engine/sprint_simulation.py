import pandas as pd
import random
import time

DATA_PATH = "data/sprint_data.csv"


def simulate_sprint():
    df = pd.read_csv(DATA_PATH)

    print("\n=== Sprint Simulation Started ===\n")

    for i in range(len(df)):
        if df.loc[i, "status"] != "Done":
            df.loc[i, "status"] = random.choice(["In Progress", "Done"])

        print(f"Task {df.loc[i, 'task_id']} → {df.loc[i, 'status']}")
        time.sleep(0.5)

    df.to_csv(DATA_PATH, index=False)

    print("\nSprint simulation completed and data updated.")


def run():
    simulate_sprint()