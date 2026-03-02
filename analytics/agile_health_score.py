import pandas as pd

def run():
    sprint = pd.read_csv("data/sprint_data.csv")
    backlog = pd.read_csv("data/backlog.csv")
    risks = pd.read_csv("data/risks.csv")

    completed_ratio = (backlog["status"] == "Done").mean()

    velocity_variation = sprint["remaining_points"].std()

    high_risks = len(risks[risks["severity"] == "High"])

    score = 100
    score -= velocity_variation * 4
    score -= high_risks * 5
    score += completed_ratio * 20

    if score > 100:
        score = 100
    if score < 0:
        score = 0

    print("\n=== Agile Health Score ===")
    print("Team Health:", round(score, 2), "/ 100")