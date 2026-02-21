from django.db import models
from django.utils.text import slugify

from BalkanPress.categories.models import Category
from BalkanPress.common.models import TimeStampModel
from BalkanPress.tags.models import Tag


# Create your models here.
class Article(TimeStampModel):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, editable=False)

    featured_image = models.ImageField(
        upload_to=".",
        blank=True,
        null=True,
        help_text="Upload a featured image for the article",
    )

    summary = models.TextField()

    content = models.TextField()

    categories = models.ManyToManyField(Category, related_name="articles")

    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        self.slug = slugify(f"{self.title}-{self.pk}")
        super().save(*args, **kwargs)
