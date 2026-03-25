from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from BalkanPress.common.forms import BootStrapModelForm, ReadOnlyModelForm
from BalkanPress.common.validators import validate_confirmation

UserModel = get_user_model()


class ProfileBaseForm(BootStrapModelForm):
    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "display_name",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "is_author",
        )
        labels = {
            "display_name": "Display name",
            "is_author": "Author profile",
        }
        help_texts = {
            "display_name": "Optional name shown publicly.",
            "is_author": "Mark if you want to publish articles",
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "display_name",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "display_name": forms.TextInput(attrs={"placeholder": "Display name"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )


class LogoutForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="I want to log out.",
    )


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ReadOnlyModelForm):
    confirmation = forms.BooleanField(
        required=True,
        label="I understand this action cannot be undone.",
    )

    readonly_exclude = ["confirmation"]

    class Meta(ProfileBaseForm.Meta):
        pass

    def clean_confirmation(self):
        return validate_confirmation(self.cleaned_data.get("confirmation"))
