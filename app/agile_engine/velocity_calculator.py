import pandas as pd

DATA_PATH = "data/sprint_data.csv"


def calculate_velocity():
    df = pd.read_csv(DATA_PATH)

    completed = df[df["status"] == "Done"]

    velocity = completed["story_points"].sum()

    print("\n=== Team Velocity ===")
    print("Total Completed Story Points:", velocity)

    return velocity


def run():
    calculate_velocity()