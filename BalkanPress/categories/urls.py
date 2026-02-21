from django.urls import include, path

from .views import (
    CategoryArticleListView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryEditView,
    CategoryListView,
)

app_name = "categories"

category_patterns = [
    path("", CategoryArticleListView.as_view(), name="category-articles"),
    path("edit/", CategoryEditView.as_view(), name="edit"),
    path("delete/", CategoryDeleteView.as_view(), name="delete"),
]

urlpatterns = [
    path("", CategoryListView.as_view(), name="list"),
    path("create/", CategoryCreateView.as_view(), name="create"),
    path("<slug:slug>/", include(category_patterns)),
]
