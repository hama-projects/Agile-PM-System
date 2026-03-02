import pandas as pd
import numpy as np

def run():
    df = pd.read_csv("data/backlog.csv")

    df["risk_score"] = np.random.uniform(0.1, 0.95, size=len(df))

    risky_tasks = df[df["risk_score"] > 0.7]

    print("\n=== AI Sprint Risk Prediction ===")

    if risky_tasks.empty:
        print("No major sprint risks detected.")
    else:
        for _, row in risky_tasks.iterrows():
            print(f"Risky Task: {row['title']} | Score: {round(row['risk_score'],2)}")