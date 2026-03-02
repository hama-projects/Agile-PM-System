import pandas as pd
import numpy as np

def run():
    sprint = pd.read_csv("data/sprint_data.csv")

    completion_rate = 1 - (sprint["remaining_points"].iloc[-1] /
                           sprint["remaining_points"].max())

    velocity = sprint["remaining_points"].diff().abs().mean()

    success_probability = (completion_rate * 0.6) + (velocity * 0.02)

    success_probability = max(0, min(success_probability, 1))

    print("\n=== AI Sprint Success Prediction ===")
    print("Sprint Success Probability:", round(success_probability * 100, 2), "%")