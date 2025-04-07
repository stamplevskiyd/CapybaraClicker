from flask import Flask
from flask_migrate import Migrate
from capybara_clicker.extensions import db

migrate = Migrate()

def create_app() -> Flask:
     """Application-factory pattern"""
     app = Flask(__name__)
     db.init_app(app)
     migrate.init_app(app, db)
     return app