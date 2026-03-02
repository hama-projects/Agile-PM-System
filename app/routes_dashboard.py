from flask import Blueprint, render_template
import pandas as pd

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def dashboard_home():
    backlog = pd.read_csv("data/backlog.csv")
    sprint = pd.read_csv("data/sprint_data.csv")
    risks = pd.read_csv("data/risks.csv")
    budget = pd.read_csv("data/budget.csv")

    total_tasks = len(backlog)
    completed_tasks = len(backlog[backlog["status"] == "Done"])
    active_sprint = sprint["sprint"].iloc[-1]

    high_risks = len(risks[risks["severity"] == "High"])

    total_budget = budget["allocated"].sum()
    spent_budget = budget["spent"].sum()

    return render_template(
        "dashboard.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        active_sprint=active_sprint,
        high_risks=high_risks,
        total_budget=total_budget,
        spent_budget=spent_budget
    )