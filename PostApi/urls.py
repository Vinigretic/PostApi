"""
TestBlog URL Configuration.

This module defines the URL patterns for the TestBlog project.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.posts.urls', namespace='posts')),
]