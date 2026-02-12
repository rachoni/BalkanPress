from django import forms
from .models import Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class TagBaseForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class TagCreateForm(TagBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Create Tag', css_class='btn btn-primary'
            )
        )

class TagEditForm(TagBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Update Tag', css_class='btn btn-success'
            )
        )

class TagDeleteForm(TagBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Delete Tag', css_class='btn btn-danger'
            )
        )