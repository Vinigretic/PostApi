"""
API Post App Configuration.

This module defines the configuration for api Post.

"""
from django.db.models import QuerySet
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.posts.models.posts import Posts
from api.posts.serializers.serializers import PostSerializer
from api.posts.views.services import ArticleService


class PostViewSet(viewsets.ModelViewSet):
    """Handler for the Post model."""

    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = PostSerializer

    def get_queryset(self) -> QuerySet[Posts]:
        """Different queryset for different actions."""
        if self.action == 'list':
            return Posts.objects.all()
        if self.action in {'retrieve', 'partial_update', 'destroy'}:
            return Posts.objects.filter(pk=self.kwargs['pk'])


class SearchArticleView(APIView):
    """Handler for searching articles based on a keyword using an external API."""
    def post(self, request) -> Response:
        """Get a keyword to newsapi_client for articles with help of post method."""
        article_service = ArticleService()
        keyword = request.data.get('keyword', '')
        if not keyword:
            return Response({'error': 'Keyword not specified'}, status=status.HTTP_400_BAD_REQUEST)
        return article_service.get_articles_list(keyword)


class CreateArticleView(APIView):
    """Handler to create a post based on the selected article URL and keyword."""
    def post(self, request) -> Response:
        """Get a keyword and selected_url to newsapi_client for articles with help of post method."""
        article_service = ArticleService()
        selected_url = request.data.get('selected_url', '')
        keyword = request.data.get('keyword', '')

        if not selected_url or not keyword:
            return Response({'error': 'Article URL or keyword not specified'}, status=status.HTTP_400_BAD_REQUEST)

        return article_service.choose_article(keyword, selected_url)
