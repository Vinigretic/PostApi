"""
API Post App Admin Configuration.

This module defines the configuration for the Django admin interface
"""
from django.contrib import admin

from api.posts.models.posts import Posts


class PostAdmin(admin.ModelAdmin):
    """Administrative interface configuration for the Post model."""

    list_display = ['id', 'created', 'title']
    list_filter = ['created']
    search_fields = ['title']


admin.site.register(Posts, PostAdmin)
