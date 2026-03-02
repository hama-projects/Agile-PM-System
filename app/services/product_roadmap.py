import pandas as pd

def run():
    backlog = pd.read_csv("data/backlog.csv")

    roadmap = backlog.groupby("sprint")["title"].apply(list)

    print("\n=== Product Roadmap ===")

    for sprint, tasks in roadmap.items():
        print(f"\n{sprint}")
        for t in tasks:
            print("-", t)