#!/usr/bin/env python3
'''adding a babel configration'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Babel config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    '''function to be invoked for each request'''
    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    '''index page'''
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
