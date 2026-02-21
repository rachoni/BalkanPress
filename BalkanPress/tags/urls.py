from django.urls import include, path

from .views import (
    TagArticleListView,
    TagCreateView,
    TagDeleteView,
    TagEditView,
    TagListView,
)

app_name = "tags"

tag_patterns = [
    path("", TagArticleListView.as_view(), name="tag-articles"),
    path("edit/", TagEditView.as_view(), name="edit"),
    path("delete/", TagDeleteView.as_view(), name="delete"),
]

urlpatterns = [
    path("", TagListView.as_view(), name="list"),
    path("create/", TagCreateView.as_view(), name="create"),
    path("<slug:slug>/", include(tag_patterns)),
]
