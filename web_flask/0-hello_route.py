#!/usr/bin/python3
"""
Python script that starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Function associated to the '/' path
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
