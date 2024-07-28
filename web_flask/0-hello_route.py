#!/usr/bin/python3

""" A Flask application that returns Hello HBNB! """

from flask import Flask

# Creates a flask instance
app = Flask(__name__)


# route tell Flask the URL that triggers our function.
@app.route('/', strict_slashes=False)
def hello():
    """ Returns message to user browser. Default's HTML """
    return "Hello HBNB!"


# run if script is executed directlly
if __name__ == "__main__":
    """ Listen on 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port=5000)
