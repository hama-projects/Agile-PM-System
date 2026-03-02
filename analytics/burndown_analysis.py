import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "data/sprint_data.csv"
OUTPUT_PATH = "app/static/burndown_chart.png"


def generate_burndown_chart():
    df = pd.read_csv(DATA_PATH)

    if "day" not in df.columns or "remaining_work" not in df.columns:
        print("Sprint data format incorrect.")
        return

    plt.figure()
    plt.plot(df["day"], df["remaining_work"], marker="o")
    plt.title("Sprint Burndown Chart")
    plt.xlabel("Sprint Day")
    plt.ylabel("Remaining Work")
    plt.grid(True)

    os.makedirs("app/static", exist_ok=True)
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("Burndown chart generated.")


def run():
    print("\nRunning Burndown Analysis...")
    generate_burndown_chart()