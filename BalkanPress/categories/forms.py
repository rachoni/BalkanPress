from django import forms
from .models import Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CategoryCreateForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Create Category', css_class='btn btn-primary'
            )
        )

class CategoryEditForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Update Category', css_class='btn btn-success'
            )
        )

class CategoryDeleteForm(CategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit(
                'submit', 'Delete Category', css_class='btn btn-danger'
            )
        )