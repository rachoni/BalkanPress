from django.core.exceptions import ValidationError


def validate_min_length(value, min_length, message=None, code="min_length"):
    if value is None:
        return value

    if len(value) < min_length:
        raise ValidationError(
            message or f"Ensure this value has at least {min_length} characters.",
            code=code,
        )

    return value


def validate_confirmation(
    confirmed,
    message="You must confirm that this action cannot be undone.",
    code="confirmation_required",
):
    if not confirmed:
        raise ValidationError(message, code=code)

    return True
