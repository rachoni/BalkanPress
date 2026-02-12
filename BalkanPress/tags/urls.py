from django.urls import path, include
from .views import (
    TagListView,
    TagCreateView,
    TagEditView,
    TagDeleteView
)

app_name = 'tags'

tag_patterns = [
    path('edit/', TagEditView.as_view(), name='edit'),
    path('delete/', TagDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('', TagListView.as_view(), name='list'),
    path('create/', TagCreateView.as_view(), name='create'),
    path('<slug:slug>/', include(tag_patterns)),
]