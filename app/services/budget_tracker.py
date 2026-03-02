import pandas as pd

DATA_PATH = "data/budget.csv"


def load_budget():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame(columns=["category", "allocated", "spent"])


def show_budget_status():
    df = load_budget()

    if df.empty:
        print("No budget data available.")
        return

    df["remaining"] = df["allocated"] - df["spent"]

    print("\n=== Budget Status ===")
    print(df)


def add_expense(category, amount):
    df = load_budget()

    if category in df["category"].values:
        df.loc[df["category"] == category, "spent"] += amount
    else:
        new_row = pd.DataFrame([[category, amount, amount]],
                               columns=["category", "allocated", "spent"])
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(DATA_PATH, index=False)
    print("Expense recorded.")


def run():
    show_budget_status()