#!/usr/bin/env python3
""" Python script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)

@app.route("/")
def greetings():
    return <p>Hello HBNB</>

if __name__ = "__main__":
    app.run(debug=True, port=0.0.0.0)
