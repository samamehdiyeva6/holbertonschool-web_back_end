#!/usr/bin/env python3
from flask import Flask, render_template
from babel import Babel
"""Flask-Babel is an extension to Flask that adds support for internationalization (i18n)"""


app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
