import pandas as pd

def run():
    backlog = pd.read_csv("data/backlog.csv")
    sprint = pd.read_csv("data/sprint_data.csv")

    completion_rate = (backlog["status"] == "Done").mean()
    sprint_consistency = sprint["remaining_points"].diff().abs().mean()

    score = (completion_rate * 70) + (1 / (1 + sprint_consistency) * 30)

    print("\n=== Agile Maturity Score ===")
    print("Score:", round(score * 100, 2), "/ 100")

    if score > 0.7:
        print("Maturity Level: Advanced Agile Team")
    elif score > 0.4:
        print("Maturity Level: Developing Agile Team")
    else:
        print("Maturity Level: Early Agile Stage")