from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from BalkanPress.common.forms import BootStrapModelForm, ReadOnlyModelForm

from .models import Tag


class TagBaseForm(BootStrapModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TagCreateForm(TagBaseForm):
    pass


class TagEditForm(TagBaseForm):
    pass


class TagDeleteForm(ReadOnlyModelForm):
    confirmation = forms.BooleanField(
        required=True,
        label=mark_safe(
            '<strong class="text-danger">'
            "I understand that this action cannot be undone."
            "</strong>"
        ),
        help_text="Check this box to confirm deletion.",
    )

    readonly_exclude = ["confirmation"]

    class Meta:
        model = Tag
        fields = [
            "name",
        ]

    def clean_confirmation(self):
        if not self.cleaned_data.get("confirmation"):
            raise ValidationError("You must confirm that this action cannot be undone.")
        return True
