from flask import Flask

from capybara_clicker.models.user import User
from capybara_clicker.extensions import db, migrate, login_manager


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

    app.register_blueprint(capy_bp)
    app.register_blueprint(login_bp)

    return app
