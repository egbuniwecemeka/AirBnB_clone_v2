<<<<<<< HEAD
from flask import Flask
''' Script thst runs an app with flask'''

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    ''' Function called through the \ route'''
    return "Hello, HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
#!/usr/bin/python3
""" Python script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greetings():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
>>>>>>> cf1fc677ef1197ef3f1d764ad5bfd068db10d086
