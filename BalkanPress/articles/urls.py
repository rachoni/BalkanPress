from django.urls import path, include
from .views import (
    ArticleDetailView,
    ArticleCreateView,
    ArticleEditView,
    ArticleDeleteView
)

app_name = 'articles'

article_patterns = [
    path('', ArticleDetailView.as_view(), name='detail'),
    path('edit/', ArticleEditView.as_view(), name='edit'),
    path('delete/', ArticleDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('<slug:slug>/', include(article_patterns)),
]