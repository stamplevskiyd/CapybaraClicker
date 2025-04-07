"""Simple script to run the Flask app via `poetry run python -m app.main` if needed."""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    # This allows you to run `python app/main.py` directly for local dev
    app.run(debug=True)
