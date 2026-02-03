from django.db import models
from django.utils.text import slugify
from BalkanPress.common.models import AricleCommentBase
from BalkanPress.categories.models import Category
from BalkanPress.tags.models import Tag

# Create your models here.
class Article(AricleCommentBase):
    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    summary = models.TextField()

    content = models.TextField()

    categories = models.ManyToManyField(
        Category,
        related_name='articles'
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='srticles',
        blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slugg:
            self.slug = slugify(f'{Category__name}/{self.title}/')