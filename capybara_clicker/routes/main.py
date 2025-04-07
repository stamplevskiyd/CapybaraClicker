from flask import Blueprint, render_template

main_bp = Blueprint("index", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    """Main index page"""
    return render_template("index.html")
