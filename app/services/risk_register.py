import pandas as pd

DATA_PATH = "data/risks.csv"


def load_risks():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame(columns=["risk_id", "description", "severity", "mitigation"])


def show_risks():
    df = load_risks()

    print("\n=== Risk Register ===")
    print(df)


def add_risk(description, severity, mitigation):
    df = load_risks()

    risk_id = len(df) + 1
    new_risk = pd.DataFrame([[risk_id, description, severity, mitigation]],
                            columns=["risk_id", "description", "severity", "mitigation"])

    df = pd.concat([df, new_risk], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    print("Risk added.")


def run():
    show_risks()