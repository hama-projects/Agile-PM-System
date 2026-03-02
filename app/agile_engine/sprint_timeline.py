import pandas as pd
import matplotlib.pyplot as plt

def run():
    df = pd.read_csv("data/backlog.csv")

    sprint_data = df.groupby(["sprint", "status"]).size().unstack(fill_value=0)

    sprint_data.plot(kind="bar")
    plt.title("Sprint Timeline Progress")
    plt.xlabel("Sprint")
    plt.ylabel("Tasks Count")
    plt.tight_layout()

    plt.savefig("app/static/sprint_timeline.png")
    print("Sprint timeline chart generated.")