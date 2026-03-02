import pandas as pd
import numpy as np

def run():
    sprint = pd.read_csv("data/sprint_data.csv")

    velocity = sprint["remaining_points"].diff().abs().mean()

    forecast = sprint["remaining_points"].iloc[-1] - velocity

    print("\n=== Velocity Forecast ===")
    print("Average Velocity:", round(velocity, 2))
    print("Forecast Remaining Work:", round(max(forecast, 0), 2))