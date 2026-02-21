from django.urls import include, path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleEditView,
    ArticleListView,
    ArticleSearchView,
)

app_name = "articles"

article_patterns = [
    path("", ArticleDetailView.as_view(), name="detail"),
    path("edit/", ArticleEditView.as_view(), name="edit"),
    path("delete/", ArticleDeleteView.as_view(), name="delete"),
]

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("search/", ArticleSearchView.as_view(), name="search"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("<slug:slug>/", include(article_patterns)),
]
