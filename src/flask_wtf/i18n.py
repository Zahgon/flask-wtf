from babel import support
from flask import current_app
from flask import request
from flask_babel import get_locale
from wtforms.i18n import messages_path

__all__ = ("Translations", "translations")


def _get_translations():
    """Returns the correct gettext translations.
    Copy from flask-babel with some modifications.
    """
    pass


class Translations:



translations = Translations()
