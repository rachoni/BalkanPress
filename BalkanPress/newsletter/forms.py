from django import forms

from BalkanPress.common.helpers import normalize_email

from .models import NewsletterSubscriber


class NewsletterSubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email",
                    "aria-label": "Email address",
                }
            )
        }
        labels = {
            "email": "",
        }
        error_messages = {
            "email": {
                "required": "Please enter an email address.",
                "invalid": "Please enter a valid email address.",
                "unique": "This email is already subscribed.",
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return normalize_email(email)
