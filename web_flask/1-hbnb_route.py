<<<<<<< HEAD
from flask import Flask
''' Script thst runs an app with flask'''

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the / route '''
    return "Hello, HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    ''' Function called through the /hbnb route '''
    return "HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
#!/usr/bin/python3
""" starts a Flask web application
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
>>>>>>> cf1fc677ef1197ef3f1d764ad5bfd068db10d086
