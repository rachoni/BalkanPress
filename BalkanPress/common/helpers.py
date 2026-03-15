
def strip_value(value):
    if isinstance(value, str):
        return value.strip()

    return value


def normalize_email(value):
    if isinstance(value, str):
        return value.strip().lower()

    return value


def get_next_url(request, default="/"):
    if request is None:
        return default

    return request.POST.get("next") or request.META.get("HTTP_REFERER") or default
