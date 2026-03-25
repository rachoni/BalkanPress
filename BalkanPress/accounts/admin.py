from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser

    list_display = (
        "username",
        "email",
        "display_name",
        "is_author",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "is_author",
        "is_staff",
        "is_active",
        "groups",
    )

    search_fields = (
        "username",
        "email",
        "display_name",
        "first_name",
        "last_name",
    )

    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "display_name",
                    "bio",
                    "avatar",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_author",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "display_name",
                    "is_author",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
