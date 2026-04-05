from rest_framework import permissions, viewsets

from BalkanPress.articles.models import Article
from BalkanPress.categories.models import Category
from BalkanPress.tags.models import Tag

from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer, CategorySerializer, TagSerializer


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = (
        Article.objects.select_related("author")
        .prefetch_related("categories", "tags")
        .order_by("-created_at")
    )
    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.order_by("name")
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
