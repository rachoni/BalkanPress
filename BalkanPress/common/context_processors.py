from django.db.models import Count, Q

from BalkanPress.articles.models import Article
from BalkanPress.categories.models import Category
from BalkanPress.comments.models import Comment
from BalkanPress.tags.models import Tag


def sidebar_data(request):
    published_articles_qs = Article.objects.filter(is_published=True)

    quick_stats = {
        "published_articles_count": published_articles_qs.count(),
        "categories_count": Category.objects.count(),
        "tags_count": Tag.objects.count(),
        "approved_comments_count": Comment.objects.filter(is_approved=True).count(),
    }

    trending_categories = (
        Category.objects.annotate(
            published_articles_count=Count(
                "articles",
                filter=Q(articles__is_published=True),
                distinct=True,
            )
        )
        .filter(published_articles_count__gt=0)
        .order_by("-published_articles_count", "name")[:5]
    )

    trending_tags = (
        Tag.objects.annotate(
            published_articles_count=Count(
                "articles",
                filter=Q(articles__is_published=True),
                distinct=True,
            )
        )
        .filter(published_articles_count__gt=0)
        .order_by("-published_articles_count", "name")[:5]
    )

    latest_comments = (
        Comment.objects.filter(is_approved=True, article__is_published=True)
        .select_related("article")
        .order_by("-created_at")[:5]
    )

    return {
        "quick_stats": quick_stats,
        "trending_categories": trending_categories,
        "trending_tags": trending_tags,
        "latest_comments": latest_comments,
    }
