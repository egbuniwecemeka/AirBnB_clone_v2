#!/usr/bin/python3

""" A Flask application that returns an Escaped HTML output """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>', strict_slashes=False)
def hello(name):
    """ Returns escaped HTML response. Injection attack protected """
    return f"Hello {escape(name)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
