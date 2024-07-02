#!/usr/bin/env python3
"""API Basic Flask app with Babel, locale selection, and user login simulation
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


class Config:
    """Define the Config class for Babel translation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """Retrieve a user from the mock database based on the 'login_as'
        URL parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id=int(user_id)
        return users.get(user_id)

    return None

@app.before_request
def before_request() -> None:
    """Set the user on Flask's global object 'g' before each request."""
    g.user = get_user()


def get_locale():
    """Determine the best match with our supported languages or use locale
        parameter from URL.
    """
    # Check if 'locale' parameter is present in the query string
    locale_param = request.args.get('locale')

    if locale_param:
        # If 'locale' is present and is a supported language, return it
        if locale_param in app.config['LANGUAGES']:
            return locale_param

    # Otherwise, return the best match based on the browser's accepted lang..
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Return the homepage index when the application startup"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
