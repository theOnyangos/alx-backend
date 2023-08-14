#!/usr/bin/env python3
"""i18n compliant flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=True)
def index() -> str:
    """main route"""
    return render_template('0-index.html')
