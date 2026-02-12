from django.contrib import admin
from django.utils.html import format_html
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_image_preview', 'slug', 'is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'summary', 'content']
    list_filter = ['is_published', 'created_at', 'updated_at', 'categories']
    filter_horizontal = ['categories', 'tags']
    readonly_fields = ['created_at', 'updated_at', 'featured_image_preview']
    ordering = ['-created_at']
    list_per_page = 25
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'featured_image', 'featured_image_preview')
        }),
        ('Content', {
            'fields': ('summary', 'content')
        }),
        ('Classifications', {
            'fields': ('categories', 'tags')
        }),
        ('Publication settings', {
            'fields': ('is_published', 'slug', 'created_at', 'updated_at')
        }),
    )

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px" />',
                obj.featured_image.url
            )
        return 'No image'
    featured_image_preview.short_description = 'Image Preview'