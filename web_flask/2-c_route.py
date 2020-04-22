#!/usr/bin/python3
"""
Python script that starts a Flask web application:
- /: display Hello HBNB!
- /hbnb: display HBNB
- c/<text>: display C  followed by the value of the text variable (underscore _
  symbols are replaced with a space)
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Function associated to the '/' path
    """
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """
    Function associated to the '/hbnb' path
    """
    return "HBNB"


@app.route('/c/<text>/', strict_slashes=False)
def cplus(text):
    """
    Function associated to the '/c/<text>' path
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
