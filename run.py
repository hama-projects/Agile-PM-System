from app import create_app
from analytics.ai_sprint_planner import run as ai_sprint_planner

app = create_app()

if __name__ == "__main__":
    print("Starting Agile Project Management System...\n")

    ai_sprint_planner()

    app.run(debug=True)