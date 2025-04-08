from flask import Flask, request, render_template

import logging

from capybara_clicker.extensions import db, migrate, login_manager

from capybara_clicker.models.user import User

logger = logging.getLogger(__name__)


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """Check if user exists"""
    user: User | None = (
        db.session.query(User).filter(User.username == user_id).one_or_none()
    )
    return user


def create_app() -> Flask:
    """Application-factory pattern"""
    # Prepare app and db
    app = Flask(__name__)
    app.config.from_object("capybara_clicker.config")
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    # Register blueprints
    from capybara_clicker.routes.capybaras import capy_bp
    from capybara_clicker.routes.users import login_bp
    from capybara_clicker.routes.api import api

    app.register_blueprint(capy_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(api)

    return app


app: Flask = create_app()


@app.route("/error")
def error_custom():
    """
    A generic error route that takes a status_code and a message from the query string.
    Example usage:
        return redirect(
            url_for('error_custom', status_code=422, message='Unprocessable Entity')
        )
    """
    status_code = request.args.get("status_code", default=400, type=int)
    message = request.args.get("message", default="Bad Request")

    return render_template(
        "error.html", status_code=status_code, message=message
    ), status_code
