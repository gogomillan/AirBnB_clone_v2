#!/usr/bin/python3
"""
Python script that starts a Flask web application:
- /: display Hello HBNB!
- /hbnb: display HBNB
- c/<text>: display C  followed by the value of the text variable (underscore _
  symbols are replaced with a space)
- /python/(<text>): display Python , followed by the value of the text variable
  (replace underscore _ symbols with a space ). The default value of text is is
  cool
- /number/<n>: display n is a number only if n is an integer
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Function associated to the '/' path
    """
    return "Hello HBNB!"


@app.route('/hbnb/')
def hbnb():
    """
    Function associated to the '/hbnb' path
    """
    return "HBNB"


@app.route('/c/<text>/')
def cplus(text):
    """
    Function associated to the '/c/<text>' path
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>/')
def pplus(text):
    """
    Function associated to the '/python/<text>' path
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>/')
def number(n):
    """
    Function associated to the '/number/<n>' path
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
