"""
Main entry point for Flask calculator
"""
import os
import time
from flask import Flask

APP = Flask(__name__)
APP.secret_key = 'd\xb6^\xc3vI\xf1\xb1\xea`\xba\xa3\xbd}l\x08\xb4g\xa5\xcc\x85\x0b\xa2\xdf'


@APP.route('/')
def index():
    """ Default route """
    return str(int(time.time()))


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6738))
    APP.run(host="0.0.0.0", port=PORT)


    #2YGLGEQE4POJG
