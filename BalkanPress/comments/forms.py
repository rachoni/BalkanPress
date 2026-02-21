from django import forms
from django.core.exceptions import ValidationError

from .models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "body"]
        widgets = {
            "author_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g., John Doe"}
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your comment here...",
                    "rows": 4,
                }
            ),
        }
        error_messages = {
            "author_name": {
                "required": "Please enter your name.",
            },
            "body": {
                "required": "Comment cannot be empty.",
            },
        }
        labels = {
            "author_name": "Your Name:",
            "body": "Comment:",
        }
        help_texts = {
            "author_name": "Enter your full name or display name.",
            "body": "Share your thougts about this article.",
        }

    def clean_author_name(self):
        author_name = self.cleaned_data.get("author_name")
        return author_name.strip()

    def clean_body(self):
        body = self.cleaned_data.get("body")
        stripped_body = body.strip()

        if len(body.strip()) < 5:
            raise ValidationError(
                "Comment must be at least 5 characters long.", code="comment_too_short"
            )
        return stripped_body


class CommentCreateForm(CommentBaseForm):
    pass
