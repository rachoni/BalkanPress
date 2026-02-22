from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from BalkanPress.common.forms import BootStrapModelForm, ReadOnlyModelForm

from .models import Category


class CategoryBaseForm(BootStrapModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class CategoryCreateForm(CategoryBaseForm):
    pass


class CategoryEditForm(CategoryBaseForm):
    pass


class CategoryDeleteForm(ReadOnlyModelForm):
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
        model = Category
        fields = [
            "name",
        ]

    def clean_confirmation(self):
        if not self.cleaned_data.get("confirmation"):
            raise ValidationError("You must confirm that this action cannot be undone.")
        return True
