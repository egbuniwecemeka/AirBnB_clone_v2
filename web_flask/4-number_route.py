#!/usr/bin/python3

""" A flask application that returns HTML response """

from flask import Flask

# Creates the flass instance
app = Flask(__name__)


# Routes to a root URL
@app.route('/', strict_slashes=False)
def home():
    """ Returns HTML content """
    string = "Hello HBNB!"
    return f"{string}"


# Routes to a URL of a method.(Meaniful URL / Better user experience)
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HTML content """
    string = "HBNB"
    return f"{string}"


# Routes to a URL of a method and uses variable as keyword argument
@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """ Returns HTML but replace _ with indent """
    return f"{text.replace('_', ' ')}"


# Routes to a URL of a method and uses a variable as keyword argument
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text):
    """ Returns HTML content but replace _ with indent"""
    return f"Python {text.replace('_', ' ')}"


# Route to /number method of a URL
@app.route('/number/<integer:n>', strict_slashes=False)
def number(n):
    """ Returns HTML content if n is an integer"""
    if n:
        return f"{n} is a number"


# Runs if script is executed as main program
if __name__ == "__main__":
    """ Host and Port identities """
    app.run(host='0.0.0.0', port=5000, debug=True)
