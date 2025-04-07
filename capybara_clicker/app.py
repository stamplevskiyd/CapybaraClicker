from flask import render_template

import logging

from capybara_clicker import create_app

logger = logging.getLogger(__name__)

app = create_app()

@app.route("/")
def index():
    """Main index page"""
    logger.info(app.url_map)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
