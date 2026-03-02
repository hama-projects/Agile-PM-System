import pandas as pd

DATA_PATH = "data/sprint_data.csv"


def calculate_remaining_work():
    df = pd.read_csv(DATA_PATH)

    if "story_points" not in df.columns or "status" not in df.columns:
        print("Invalid sprint data format.")
        return

    total_points = df["story_points"].sum()
    completed_points = df[df["status"] == "Done"]["story_points"].sum()

    remaining = total_points - completed_points

    print("\n=== Burndown Calculation ===")
    print("Total Story Points:", total_points)
    print("Completed Story Points:", completed_points)
    print("Remaining Work:", remaining)

    return remaining


def run():
    print("\nRunning Burndown Engine...")
    calculate_remaining_work()