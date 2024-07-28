#!/usr/bin/python3

""" A flask application that returns  HTML content """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def salute():
    string = "Hello HBNB!"
    return f"{string}"


@app.route("/hbnb", strict_slashes=False)
def salute_type():
    string_type = "HBNB"
    return f"{salute_type}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
