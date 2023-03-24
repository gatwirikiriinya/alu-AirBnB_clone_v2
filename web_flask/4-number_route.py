#!/usr/bin/python3
""" working with default routes
    python is cool"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ home """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """  hbnb end point """
    return "HBNB"


@app.route("/c/<text>")
def info_c(text):
    """ taking argument for displaying c """
    takeout = text.replace("_", " ")
    return "C {}".format(takeout)


@app.route('/python/')
@app.route('/python/<text>')
def pythonR(text='is cool'):
    """ python is cool """
    takeout = text.replace("_", " ")
    return "Python {}".format(takeout)


@app.route('/number/<int:n>')
def number(n):
    """ work for numbers only """
    return "{} is a number".format(n)


if __name__ == '__main__':
    # """ starts """
    app.run(host="0.0.0.0", port=5000, debug=True)
