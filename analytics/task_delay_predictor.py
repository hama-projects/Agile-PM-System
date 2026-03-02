import pandas as pd
import numpy as np

def run():
    df = pd.read_csv("data/backlog.csv")

    df["delay_risk"] = np.random.uniform(0.1, 0.9, size=len(df))

    high_risk = df[df["delay_risk"] > 0.7]

    print("\n=== AI Task Delay Prediction ===")

    if high_risk.empty:
        print("No high risk tasks detected.")
    else:
        for _, row in high_risk.iterrows():
            print(f"Task: {row['title']} -> Risk: {round(row['delay_risk'],2)}")