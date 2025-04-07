# from flask import Response
# import logging
#
# from .bp import api
#
# from ..app import db
# from ..models import ClickCounter
#
# logger = logging.getLogger(__name__)
#
# @api.route("/", methods=["GET"])
# def get_counter() -> Response:
#     """Get count from api"""
#     counter: ClickCounter | None = db.session.query(ClickCounter).one_or_none()
#     if not counter:


