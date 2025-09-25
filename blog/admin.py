from django.contrib import admin

from about.models import About
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on',)
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)