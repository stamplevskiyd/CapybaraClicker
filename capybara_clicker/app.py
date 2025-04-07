import os
from flask import Flask, render_template
from capybara_clicker.extensions import app




@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
