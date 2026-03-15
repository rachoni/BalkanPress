from django.contrib import admin

from .models import NewsletterSubscriber


# Register your models here.
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "created_at",
    )
    search_fields = ("email",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
