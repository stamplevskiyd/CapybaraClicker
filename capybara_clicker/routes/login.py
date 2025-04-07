from flask import Blueprint, Response, request, redirect, url_for, render_template
from flask_login import login_user

from capybara_clicker.extensions import login_manager, db
from capybara_clicker.models.clicker import ClickCounter
from capybara_clicker.models.user import User
from werkzeug.security import generate_password_hash

login_bp = Blueprint("login", __name__, template_folder="templates")


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """Check if user exists"""
    user: User | None = (
        db.session.query(User).filter_by(User.username == user_id).one_or_none()
    )
    return user


@login_bp.route("/register", methods=["GET", "POST"])
def register_user() -> Response | str:
    """Register user view"""
    if request.method == "POST":
        username: str = request.form.get("username", "")
        password: str = request.form.get("password", "")

        # Validate user
        if not username or not password:
            return redirect(
                url_for(
                    "error_custom",
                    status_code=400,
                    message="Invalid username or password",
                )
            )
        if db.session.query(User).filter_by(username=username).exists():
            return redirect(
                url_for("error_custom", status_code=400, message="User exists")
            )

        # Create user
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        # Create counter
        counter = ClickCounter(user=user)
        db.session.add(counter)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login user"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        user: User | None = db.session.query(User).filter_by(username=username).first()
        if not user:
            return redirect(
                url_for("error_custom", status_code=404, message="User not found")
            )

        if generate_password_hash(password) == user.password:
            login_user(user)
        else:
            return redirect(
                url_for("error_custom", status_code=403, message="Invalid password")
            )

    return render_template("login.html")
