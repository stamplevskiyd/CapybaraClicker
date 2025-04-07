from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from capybara_clicker.extensions import db
from capybara_clicker.models.clicker import ClickCounter
from capybara_clicker.models.user import User

capy_bp = Blueprint(
    "index", __name__, template_folder="templates", static_folder="static"
)


@capy_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Main index page"""
    username = current_user.get_id()
    counter: ClickCounter = (
        db.session.query(ClickCounter)
        .join(User, ClickCounter.user_id == User.id)
        .filter(ClickCounter.user.username == username)
    )
    if request.method == "POST":
        counter.count += 1
        db.session.add(counter)
        db.session.commit()

    # In any scenario return click count
    return render_template(
        "index.html", username=username, clicks=counter.count, image_path="capy_1.jpg"
    )
