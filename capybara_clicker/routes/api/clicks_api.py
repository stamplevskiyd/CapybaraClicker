from . import api
from flask import jsonify
from flask_login import current_user

from capybara_clicker.capy_feed.utils import get_capy
from capybara_clicker.extensions import db
from capybara_clicker.models.clicker import ClickCounter
from capybara_clicker.models.user import User


@api.route("/click", methods=["POST"])
def click():
    """Click api method"""
    username = current_user.get_id()
    counter: ClickCounter = (
        db.session.query(ClickCounter)
        .join(User, ClickCounter.user_id == User.id)
        .filter(User.username == username)
        .first()
    )
    counter.count += 1
    db.session.add(counter)
    db.session.commit()
    description, path = get_capy(counter.count)
    return jsonify({"clicks": counter.count, "image_path": "/clicker_capys/" + path})


@api.route("/reset", methods=["POST"])
def reset():
    """Reset api method"""
    username = current_user.get_id()
    counter: ClickCounter = (
        db.session.query(ClickCounter)
        .join(User, ClickCounter.user_id == User.id)
        .filter(User.username == username)
        .first()
    )
    counter.count = 0
    db.session.add(counter)
    db.session.commit()
    description, path = get_capy(counter.count)
    return jsonify({"clicks": counter.count, "image_path": "/clicker_capys/" + path})
