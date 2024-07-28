#!/usr/bin/python3

""" A flask application that returns HTML content """

from flask import Flask
from markupsafe import escape

# Creates flask instance
app = Flask(__name__)


# Route to a URL
@app.route('/', strict_slashes=False)
def home():
    """ Returns HTML content """
    string = "Hello HBNB!"
    return f"{string}"


# Route to a URL
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns HTML content """
    string = "HBNB"
    return f"{string}"


# Route to a URL
@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """ Returns formatted replaced output """
    return f"C {text.replace(_, ' ')}"


if __name__ == "__main__":
    """ Host and port parameter """
    app.run(host='0.0.0.0', port=5000, debug=True)
