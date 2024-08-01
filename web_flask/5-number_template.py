#!/usr/bin/python3

""" A flask application that returns HTML response """

from flask import Flask, render_template

# Creates the flass instance
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Returns HTML response from URL """
    string = "Hello HBNB!"
    return f"{string}"


# Routes to a URL of a method.(Meaniful URL / Better user experience)
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HTML response from URL """
    string = "HBNB"
    return f"{string}"


# Routes to a URL of a method and uses variable as keyword argument
@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """ Returns HTML response from URL """
    return f"{text.replace('_', ' ')}"


# Routes to a URL of a method and uses a variable as keyword argument
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text):
    """ Returns HTML response from URL """
    return f"Python {text.replace('_', ' ')}"


# Routes to a URL that triggers the function
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Returns HTML response from URL """
    if n:
        return f'{n} is a number'


# Routes to a template that triggers the function
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Returns HTML response from Jinja template """
    if n:
        return render_template('5-number_template', n=n)


# Runs if script is executed as main program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
