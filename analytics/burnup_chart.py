import pandas as pd
import matplotlib.pyplot as plt

def run():
    df = pd.read_csv("data/sprint_data.csv")

    if "completed_points" not in df.columns:
        df["completed_points"] = df["remaining_points"].max() - df["remaining_points"]

    plt.figure()
    plt.plot(df["day"], df["completed_points"])
    plt.title("Release Burnup Chart")
    plt.xlabel("Day")
    plt.ylabel("Completed Story Points")

    plt.savefig("app/static/burnup_chart.png")

    print("Burnup chart generated.")