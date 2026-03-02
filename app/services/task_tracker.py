import pandas as pd

DATA_PATH = "data/backlog.csv"


def load_tasks():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame(columns=["task_id", "title", "status", "assignee", "story_points"])


def show_tasks():
    df = load_tasks()

    print("\n=== Task Backlog ===")
    print(df)


def add_task(title, assignee, story_points):
    df = load_tasks()

    task_id = len(df) + 1

    new_task = pd.DataFrame([[task_id, title, "To Do", assignee, story_points]],
                            columns=["task_id", "title", "status", "assignee", "story_points"])

    df = pd.concat([df, new_task], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    print("Task added to backlog.")


def run():
    show_tasks()