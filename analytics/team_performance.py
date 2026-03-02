import pandas as pd

DATA_PATH = "data/sprint_data.csv"


def analyze_team_performance():
    df = pd.read_csv(DATA_PATH)

    if "assignee" not in df.columns:
        print("No team assignment data found.")
        return

    performance = df.groupby("assignee")["status"].value_counts().unstack(fill_value=0)

    print("\n=== Team Performance ===")
    print(performance)

    if "Done" in performance.columns:
        performance["completed_tasks"] = performance["Done"]
    else:
        performance["completed_tasks"] = 0

    top_member = performance["completed_tasks"].idxmax()
    print("\nTop Performer:", top_member)


def run():
    print("\nAnalyzing Team Performance...")
    analyze_team_performance()