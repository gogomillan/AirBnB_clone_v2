#!/usr/bin/python3
"""
Python script that starts a Flask web application:
- /: display Hello HBNB!
- /hbnb: display HBNB
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


if __name__ == "__main__":
    app.run()
