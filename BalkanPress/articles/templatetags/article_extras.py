import math

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import strip_tags

register = template.Library()


@register.filter
@stringfilter
def word_count(value):
    if not value:
        return 0

    text = strip_tags(value)
    return len(text.split())


@register.filter
@stringfilter
def reading_time(value, wpm=200):
    if not value:
        return 1

    text = strip_tags(value)
    words = len(text.split())
    minutes = math.ceil(words / wpm)

    return max(minutes, 1)


@register.filter
@stringfilter
def preview(value, length=150):
    if not value:
        return ""

    text = strip_tags(value).strip()

    if len(text) <= length:
        return text

    truncated = text[:length].rsplit(" ", 1)[0]
    return f"{truncated}..."
