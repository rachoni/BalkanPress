from django.contrib.auth import get_user_model
from rest_framework import serializers

from BalkanPress.articles.models import Article
from BalkanPress.categories.models import Category
from BalkanPress.comments.models import Comment
from BalkanPress.newsletter.models import NewsletterSubscriber
from BalkanPress.tags.models import Tag

UserModel = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")
        read_only_fields = ("id", "slug")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "slug")
        read_only_fields = ("id", "slug")


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, required=False
    )

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "slug",
            "author",
            "featured_image",
            "summary",
            "content",
            "categories",
            "tags",
            "is_published",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "slug", "author", "created_at", "updated_at")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "article",
            "author_name",
            "body",
            "is_approved",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "is_approved", "created_at", "updated_at")


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ("id", "email", "is_active", "created_at")
        read_only_fields = ("id", "is_active", "created_at")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "email",
            "display_name",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "is_author",
            "is_staff",
            "is_active",
        )
        read_only_fields = ("id", "is_staff", "is_active")
