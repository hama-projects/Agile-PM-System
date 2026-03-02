import sys
import os

sys.path.append(os.path.abspath("."))

from analytics.task_delay_predictor import run as delay
from analytics.product_metrics import run as metrics
from analytics.burnup_chart import run as burnup
from analytics.agile_health_score import run as health
from analytics.sprint_success_prediction import run as success
from analytics.team_productivity_ai import run as productivity
from analytics.sprint_timeline import run as timeline
from analytics.velocity_forecast import run as velocity
from analytics.product_roadmap import run as roadmap

def run():
    delay()
    metrics()
    burnup()
    health()
    success()
    productivity()
    timeline()
    velocity()
    roadmap()

if __name__ == "__main__":
    run()