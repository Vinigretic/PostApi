"""
API Post App Configuration.

This module defines the configuration for api Post.

"""
from django.apps import AppConfig


class PostConfig(AppConfig):
    """Configuration class for api Post."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.posts'
