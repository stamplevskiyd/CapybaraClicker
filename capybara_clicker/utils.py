from flask import Flask
from flask_migrate import Migrate
from capybara_clicker.extensions import db

migrate = Migrate()


def create_app() -> Flask:
    """Application-factory pattern"""
    # Prepare app and db
    app = Flask(__name__)
    app.config.from_object("capybara_clicker.config")
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from capybara_clicker.routes.main import main_bp

    app.register_blueprint(main_bp)

    return app
