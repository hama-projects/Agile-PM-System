import pandas as pd

def run():
    backlog = pd.read_csv("data/backlog.csv")
    budget = pd.read_csv("data/budget.csv")

    completion = (backlog["status"] == "Done").mean() * 100

    total_allocated = budget["allocated"].sum()
    total_spent = budget["spent"].sum()

    print("\n=== Product Metrics ===")
    print("Completion Rate:", round(completion, 2), "%")
    print("Budget Allocated:", total_allocated)
    print("Budget Spent:", total_spent)