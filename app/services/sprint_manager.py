import pandas as pd
import datetime

DATA_PATH = "data/sprint_data.csv"


def show_sprint_overview():
    df = pd.read_csv(DATA_PATH)

    total_tasks = len(df)
    completed = len(df[df["status"] == "Done"])

    print("\n=== Sprint Overview ===")
    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed)


def start_new_sprint(name, duration_days=14):
    start = datetime.date.today()
    end = start + datetime.timedelta(days=duration_days)

    print("\nNew Sprint Created")
    print("Sprint Name:", name)
    print("Start:", start)
    print("End:", end)


def run():
    show_sprint_overview()