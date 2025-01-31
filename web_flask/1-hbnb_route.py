#!/usr/bin/python3
# flask application starting
""" flask application starting """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    # """ home """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    # hbnb end point
    return "HBNB"


if __name__ == '__main__':
    # """ starts  """
    app.run(host="0.0.0.0", port=5000, debug=True)
