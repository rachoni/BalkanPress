from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AppUser(AbstractUser):
    # You can add extra fields here if needed
    display_name = models.CharField(max_length=150, blank=True)

    is_author = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.username
