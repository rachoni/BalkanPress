from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from .forms import (LoginForm, LogoutForm, ProfileDeleteForm, ProfileEditForm,
                    RegisterForm)

# Create your views here.
UserModel = get_user_model()


class BaseProfileMixin(LoginRequiredMixin):
    model = UserModel

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")


class LoginView(DjangoLoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm


class LogoutView(LoginRequiredMixin, FormView):
    form_class = LogoutForm
    template_name = "accounts/logout.html"
    success_url = reverse_lazy("articles:list")

    def form_valid(self, form):
        auth_logout(self.request)
        return super().form_valid(form)


class ProfileView(BaseProfileMixin, DetailView):
    template_name = "accounts/profile.html"
    context_object_name = "profile"


class ProfileEditView(BaseProfileMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = "accounts/profile-edit.html"
    success_url = reverse_lazy("accounts:profile")


class ProfileDeleteView(BaseProfileMixin, UpdateView):
    form_class = ProfileDeleteForm
    template_name = "accounts/profile-delete.html"
    success_url = reverse_lazy("articles:list")

    def form_valid(self, form):
        user = self.get_object()
        auth_logout(self.request)
        user.delete()
        return redirect(self.get_success_url())


# Admin-only list of users
class UserListView(UserPassesTestMixin, ListView):
    model = UserModel
    template_name = "accounts/user-list.html"
    context_object_name = "users"
    paginate_by = 20
    ordering = ("id",)

    def test_func(self):
        return self.request.user.is_staff


# Admin-only delete any user
class AdminUserDeleteView(UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = "accounts/user-delete.html"
    success_url = reverse_lazy("accounts:user-list")

    def test_func(self):
        return self.request.user.is_staff
