#!/usr/bin/env python3
"""
Flask-Babel is an extension to Flask that adds
"""

from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """Route that returns a template"""
    return render_template('3-index.html')
