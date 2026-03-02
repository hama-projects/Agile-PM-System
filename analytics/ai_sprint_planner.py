import pandas as pd

MAX_SPRINT_POINTS = 20

def run():
    print("\n=== AI Sprint Planner ===")

    backlog = pd.read_csv("data/backlog.csv")

    backlog = backlog[backlog["status"] != "Done"]

    backlog = backlog.sort_values(
        by=["priority", "story_points"],
        ascending=[True, False]
    )

    sprint_plan = []
    total_points = 0

    for _, task in backlog.iterrows():
        points = int(task["story_points"])

        if total_points + points <= MAX_SPRINT_POINTS:
            sprint_plan.append(task)
            total_points += points

    print("\nSelected Tasks for Next Sprint:\n")

    for task in sprint_plan:
        print(
            f"{task['title']} | "
            f"Assignee: {task['assignee']} | "
            f"Points: {task['story_points']} | "
            f"Priority: {task['priority']}"
        )

    print("\nSprint Capacity Used:", total_points, "/", MAX_SPRINT_POINTS)