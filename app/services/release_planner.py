import pandas as pd

DATA_PATH = "data/sprint_data.csv"


def plan_release():
    df = pd.read_csv(DATA_PATH)

    done_tasks = df[df["status"] == "Done"]

    print("\n=== Release Plan ===")
    print("Tasks ready for release:\n")
    print(done_tasks[["task_id", "title", "assignee"]])


def run():
    print("\nPlanning Release...")
    plan_release()