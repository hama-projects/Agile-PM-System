import pandas as pd

DATA_PATH = "data/sprint_data.csv"


def generate_sprint_report():
    df = pd.read_csv(DATA_PATH)

    total_tasks = len(df)
    completed_tasks = len(df[df["status"] == "Done"])
    in_progress = len(df[df["status"] == "In Progress"])
    pending = len(df[df["status"] == "To Do"])

    print("\n=== Sprint Report ===")
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("In Progress:", in_progress)
    print("Pending:", pending)

    completion_rate = (completed_tasks / total_tasks) * 100
    print("Completion Rate:", round(completion_rate, 2), "%")


def run():
    print("\nGenerating Sprint Report...")
    generate_sprint_report()