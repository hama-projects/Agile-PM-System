import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "agile_project_secret"
    DEBUG = True

    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    BACKLOG_FILE = os.path.join(DATA_FOLDER, "backlog.csv")
    SPRINT_FILE = os.path.join(DATA_FOLDER, "sprint_data.csv")
    RISK_FILE = os.path.join(DATA_FOLDER, "risks.csv")
    BUDGET_FILE = os.path.join(DATA_FOLDER, "budget.csv")