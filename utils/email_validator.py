from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def email_validator(email):
    try:
        validate_email(email)
        return True

    except ValidationError:
        return False
