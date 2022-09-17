from django.contrib import admin # type: ignore
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'create_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoyAdmin)