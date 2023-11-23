from flask import Flask
from config import Config
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config.from_object(Config())

    # Create a Google Calendar API service
    credentials = service_account.Credentials.from_service_account_file(
        app.config['GOOGLE_CREDENTIALS_PATH'],
        scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )
    calendar_service = build('calendar', 'v3', credentials=credentials)
    app.config["CALENDAR_SERVICE"] = calendar_service

    # Blueprints
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
