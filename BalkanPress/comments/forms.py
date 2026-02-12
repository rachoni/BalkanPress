from django import forms
from .models import Comment

class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'body']

class CommentCreateForm(CommentBaseForm):
    class Meta(CommentBaseForm.Meta):
        widgets = {
            'author_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your comment...',
                    'rows': 4
                }
            ),
        }
        labels = {
            'author_name': 'Name:',
            'body': 'Comment:',
        }