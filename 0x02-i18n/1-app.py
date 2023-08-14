#!/usr/bin/env python3
"""i18n compliant flask application"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Configure languages
class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

@app.route('/')
def index() -> str:
    """main route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
