import pandas as pd

def get_board():
    df = pd.read_csv("data/backlog.csv")

    todo = df[df["status"] == "To Do"]
    doing = df[df["status"] == "In Progress"]
    done = df[df["status"] == "Done"]

    return {
        "todo": todo.to_dict("records"),
        "doing": doing.to_dict("records"),
        "done": done.to_dict("records"),
    }