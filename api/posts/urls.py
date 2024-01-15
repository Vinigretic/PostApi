"""
API Post App Configuration.

This module defines the configuration for api Post.

"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.posts.views.views import CreateArticleView, PostViewSet, SearchArticleView

post_router = SimpleRouter()
post_router.register(prefix='posts', viewset=PostViewSet, basename='posts')

app_name = 'posts'

urlpatterns = [
    path('', include(post_router.urls)),
    path('articles', SearchArticleView.as_view(), name='articles'),
    path('articles/create', CreateArticleView.as_view(), name='create_article'),
]
