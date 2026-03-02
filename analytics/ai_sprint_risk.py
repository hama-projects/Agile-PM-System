import pandas as pd
import numpy as np

def run():
    sprint = pd.read_csv("data/sprint_data.csv")

    risk_score = np.random.uniform(0.2, 0.9)

    print("\n=== AI Sprint Risk Prediction ===")
    print("Predicted Sprint Risk:", round(risk_score, 2))

    if risk_score > 0.7:
        print("High risk: Sprint delay likely")
    elif risk_score > 0.4:
        print("Moderate risk detected")
    else:
        print("Low sprint risk")