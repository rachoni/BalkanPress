from django.db import models
from BalkanPress.common.models import AricleCommentBase
from BalkanPress.articles.models import Article

# Create your models here.
class Comment(AricleCommentBase):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author_name = models.CharField(
        max_length=100
    )

    body = models.TextField()

    def __str__(self):
        return f'Comment by {self.author_name}'