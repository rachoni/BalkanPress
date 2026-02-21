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
    class Meta:
        model = Category
        fields = ["name"]
