from django.urls import path, include
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryEditView,
    CategoryDeleteView
)

app_name = 'categories'

category_patterns = [
    path('edit/', CategoryEditView.as_view(), name='edit'),
    path('delete/', CategoryDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<slug:slug>/', include(category_patterns)),
]