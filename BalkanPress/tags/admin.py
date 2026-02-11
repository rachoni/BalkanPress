from django.contrib import admin
from .models import Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    readonly_fields = ['slug']