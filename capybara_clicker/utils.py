from flask import Flask
from capybara_clicker.extensions import db, migrate, login_manager


def create_app() -> Flask:
    """Application-factory pattern"""
    # Prepare app and db
    app = Flask(__name__)
    app.config.from_object("capybara_clicker.config")
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from capybara_clicker.routes.capybaras import capy_bp

    app.register_blueprint(capy_bp)

    return app
