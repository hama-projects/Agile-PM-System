import pandas as pd

def run():
    backlog = pd.read_csv("data/backlog.csv")

    completed = backlog[backlog["status"] == "Done"]
    in_progress = backlog[backlog["status"] == "In Progress"]

    productivity_score = (
        len(completed) * 5
        + len(in_progress) * 2
    )

    print("\n=== Team Productivity Score ===")
    print("Productivity Score:", productivity_score)

    team = backlog.groupby("assignee")["story_points"].sum()

    print("\nTeam Contribution:")
    print(team)