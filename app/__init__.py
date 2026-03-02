from flask import Flask
from app.routes import main
from app.routes_dashboard import dashboard

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(dashboard)

    return app