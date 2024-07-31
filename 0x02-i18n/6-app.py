#!/usr/bin/env python3
'''adding a babel configration'''
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''Babel config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    '''function to be invoked for each request'''
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    elif g.user:
        return g.user.get("locale")
    elif request:
        return request.accept_languages.best_match(
            app.config["LANGUAGES"]
        )
    else:
        return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    '''function to get the current user'''
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request():
    '''runnes before every request is processed'''
    g.user = get_user()


@app.route("/")
def index():
    '''index page'''
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
