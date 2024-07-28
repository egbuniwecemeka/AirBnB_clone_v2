#!/usr/bin/python3

# Imported Flask class
from flask import Flask

# created an instance of Flask class
app = Flask(__name__)


# route tell Flask the URL that triggers our function.
@app.route('/', strict_slashes=False)
def hello():
    # Returns message to user browser. Default's HTML
    return "Hello HBNB!"


# run if script is executed directlly
if __name__ == "__main__":
    app.run(port=5000)
