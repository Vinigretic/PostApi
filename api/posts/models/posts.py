"""
API Post App Configuration.

This module defines the configuration for api Post

"""
from django.db import models


class Posts(models.Model):
    """Model for presenting posts."""

    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='')
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        """Metadata options for the Post model."""

        ordering = ['created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
