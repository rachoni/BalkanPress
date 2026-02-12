from django.db import models
from BalkanPress.common.models import TimeStampModel
from BalkanPress.articles.models import Article

# Create your models here.
class Comment(TimeStampModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author_name = models.CharField(
        max_length=100
    )

    body = models.TextField()

    is_approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author_name} on {self.article.title}'

    def approve(self):
        self.is_approved = True
        self.save(update_fields=['is_approved'])