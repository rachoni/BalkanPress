from django import forms
from .models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Row, Column, HTML
from crispy_forms.bootstrap import PrependedText

class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'categories', 'tags', 'is_published']

class ArticleCreateForm(ArticleBaseForm):
    class Meta(ArticleBaseForm.meta):
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Basic Information',
                'title',
                Row(
                    Column(
                        'summary',
                        css_class='form-group col-md-12 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Content',
                'content',

            ),
            Fieldset(
                'Classification',
                Row(
                    Column(
                        'categories',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    Column(
                        'tags',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Publication Settings',
                'is_published',
            ),
            Submit(
                'submit', 'Create Article', css_class='btn btn-primary mt-3'
            )
        )

class ArticleEditForm(ArticleBaseForm):
    class Meta(ArticleBaseForm.meta):
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Basic Information',
                'title',
                Row(
                    Column(
                        'summary',
                        css_class='form-group col-md-12 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Content',
                'content',

            ),
            Fieldset(
                'Classification',
                Row(
                    Column(
                        'categories',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    Column(
                        'tags',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Publication Settings',
                'is_published',
            ),
            Submit(
                'submit', 'Update Article', css_class='btn btn-success mt-3'
            )
        )

class ArticleDeleteForm(ArticleBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Article Information',
                'title',
                Row(
                    Column(
                        'summary',
                        css_class='form-group col-md-12 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Content',
                'content',

            ),
            Fieldset(
                'Classification',
                Row(
                    Column(
                        'categories',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    Column(
                        'tags',
                        css_class='form-group col-md-6 mb-0'
                    ),
                    css_class='form-row'
                ),
            ),
            Fieldset(
                'Publication Settings',
                'is_published',
            ),
            HTML(
                "<hr>"
            ),
            HTML(
                "<p class='text-danger'><strong>Warning:</strong>This action cannot be undone.</p>"
            ),
            Submit(
                'submit', 'Delete Article', css_class='btn btn-danger mt-3'
            )
        )