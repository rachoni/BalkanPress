
"""
URL configuration for BalkanPress project.

The `urlpatterns` list routes URLs to views.
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from BalkanPress.common.views import AboutView


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path(
        "categories/",
        include(
            ("BalkanPress.categories.urls", "categories"),
            namespace="categories",
        ),
    ),
    path(
        "tags/",
        include(("BalkanPress.tags.urls", "tags"), namespace="tags"),
    ),
    path("about/", AboutView.as_view(), name="about"),
    path(
        "newsletter/",
        include(
            ("BalkanPress.newsletter.urls", "newsletter"),
            namespace="newsletter",
        ),
    ),
    path(
        "accounts/",
        include(
            ("BalkanPress.accounts.urls", "accounts"),
            namespace="accounts",
        ),
    ),
    path(
        "api/",
        include(("BalkanPress.api.urls", "api"), namespace="api"),
    ),
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "",
        include(("BalkanPress.articles.urls", "articles"), namespace="articles"),
    ),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )


handler404 = "BalkanPress.common.views.custom_404"
handler500 = "BalkanPress.common.views.custom_500"
