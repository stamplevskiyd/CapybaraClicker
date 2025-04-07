from flask import Blueprint, render_template

from capybara_clicker.extensions import db
from capybara_clicker.models.clicker import ClickCounter

main_bp = Blueprint("index", __name__, template_folder="templates")


@main_bp.route("/capybara")
def index():
    """Main index page"""
    counter_exists = db.session.query(ClickCounter).exists()
    return render_template("index.html")
