from flask import render_template, request

import logging

from capybara_clicker import create_app

logger = logging.getLogger(__name__)

app = create_app()


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


if __name__ == "__main__":
    app.run(debug=True)
