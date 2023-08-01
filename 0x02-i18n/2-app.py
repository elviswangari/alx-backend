#!/usr/bin/env python3
'''
simple flask babel app
'''
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    get and return best match locale
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
