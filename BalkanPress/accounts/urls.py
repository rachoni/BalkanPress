from django.urls import path, include

from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    ProfileEditView,
    ProfileDeleteView,
    UserListView,
    AdminUserDeleteView,
)

app_name = "accounts"

profile_patterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("edit/", ProfileEditView.as_view(), name="profile-edit"),
    path("delete/", ProfileDeleteView.as_view(), name="profile-delete"),
]

user_admin_patterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("<int:pk>/delete/", AdminUserDeleteView.as_view(), name="user-delete"),
]

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", include(profile_patterns)),
    path("users/", include(user_admin_patterns)),
]