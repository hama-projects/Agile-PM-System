import pandas as pd
import matplotlib.pyplot as plt

def run():
    df = pd.read_csv("data/sprint_data.csv")

    plt.figure()
    plt.plot(df["day"], df["remaining_points"])
    plt.title("Sprint Timeline")
    plt.xlabel("Day")
    plt.ylabel("Remaining Story Points")

    plt.savefig("app/static/sprint_timeline.png")

    print("Sprint timeline generated.")