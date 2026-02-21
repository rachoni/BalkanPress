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
    class Meta:
        model = Tag
        fields = ["name"]
