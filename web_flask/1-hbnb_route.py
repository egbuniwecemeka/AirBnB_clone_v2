#!/usr/bin/python3

""" A flask application that returns  HTML content """

from flask import Flask

app = Flask(__name__)

# Routing to a URL
@app.route('/', strict_slashes=False)
def home():
    """ Method returning HTML content """
    string = "Hello HBNB!"
    return f"{string}"

# Routing a function to a URL
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Method returning HTML content """
    string_type = "HBNB"
    return f"{salute_type}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
