from flask import Blueprint, render_template
import pandas as pd
from app.agile_engine.kanban_board import get_board

main = Blueprint("main", __name__)

@main.route("/kanban")
def kanban():
    board = get_board()
    return render_template("kanban.html", board=board)

@main.route("/sprints")
def sprints():
    sprint_data = pd.read_csv("data/sprint_data.csv")
    sprints = sprint_data["sprint"].unique()
    return render_template("sprints.html", sprints=sprints)

@main.route("/risks")
def risks():
    risks = pd.read_csv("data/risks.csv")
    return render_template("risks.html", risks=risks.to_dict("records"))