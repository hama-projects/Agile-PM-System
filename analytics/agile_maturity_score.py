import pandas as pd

def run():
    sprint = pd.read_csv("data/sprint_data.csv")
    backlog = pd.read_csv("data/backlog.csv")
    risks = pd.read_csv("data/risks.csv")

    completed_ratio = (backlog["status"] == "Done").mean()
    velocity_stability = sprint["remaining_points"].std()
    risk_penalty = len(risks[risks["severity"] == "High"])

    score = (completed_ratio * 60) + (40 - velocity_stability * 5) - (risk_penalty * 3)

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    print("\n=== Agile Maturity Score ===")
    print("Agile Team Score:", round(score, 2), "/ 100")