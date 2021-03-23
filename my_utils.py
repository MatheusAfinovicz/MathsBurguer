from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def check_for_special_chars(word):
    if word is '':
        return False
    for char in word:
        if not char.isdigit() and not char.isalpha():
            return False
    return True


def email_validator(email):
    try:
        validate_email(email)
        return True

    except ValidationError:
        return False
