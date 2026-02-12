from django.db import models
from django.utils.text import slugify
from BalkanPress.common.models import TimeStampModel
from BalkanPress.categories.models import Category
from BalkanPress.settings import MEDIA_ROOT
from BalkanPress.tags.models import Tag

# Create your models here.
class Article(TimeStampModel):
    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        editable=False
    )

    featured_image = models.ImageField(
        upload_to= MEDIA_ROOT,
        blank=True,
        null=True,
        help_text='Upload a featured image for the article'
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

    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        category_name = self.categories.first().name if self.categories.exists() else 'uncategorized'
        self.slug = slugify(f'{self.categories.name}/{self.title}-{str(self.pk)}')
        super().save(*args, **kwargs)