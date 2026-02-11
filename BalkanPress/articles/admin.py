from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'summary', 'content']
    list_filter = ['is_published', 'created_at', 'updated_at', 'categories']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories', 'tags']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    ordering = ['-created_at']
    list_per_page = 25
    date_hierarchy = 'created_at'