import json
from urllib import request as http
from urllib.parse import urlencode

from flask import current_app
from flask import request
from wtforms import ValidationError

RECAPTCHA_VERIFY_SERVER_DEFAULT = "https://www.google.com/recaptcha/api/siteverify"
RECAPTCHA_ERROR_CODES = {
    "missing-input-secret": "The secret parameter is missing.",
    "invalid-input-secret": "The secret parameter is invalid or malformed.",
    "missing-input-response": "The response parameter is missing.",
    "invalid-input-response": "The response parameter is invalid or malformed.",
}


__all__ = ["Recaptcha"]


class Recaptcha:
    """Validates a ReCaptcha."""

    def __init__(self, message=None):
        if message is None:
            message = RECAPTCHA_ERROR_CODES["missing-input-response"]
        self.message = message

    def __call__(self, form, field):
        if current_app.testing:
            return True

        if request.is_json:
            response = request.json.get("g-recaptcha-response", "")
        else:
            response = request.form.get("g-recaptcha-response", "")
        remote_ip = request.remote_addr

        if not response:
            raise ValidationError(field.gettext(self.message))

        if not self._validate_recaptcha(response, remote_ip):
            field.recaptcha_error = "incorrect-captcha-sol"
            raise ValidationError(field.gettext(self.message))

    def _validate_recaptcha(self, response, remote_addr):
        """Performs the actual validation."""
        pass
