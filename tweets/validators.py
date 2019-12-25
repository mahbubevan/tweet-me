from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content == 'abc':
        raise ValidationError("Can not")

    return value
