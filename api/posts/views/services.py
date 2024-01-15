"""
Service for API Post.

This module defines an additional API Post service.
"""
from typing import Dict

from rest_framework import status
from rest_framework.response import Response

from api.newsapi_client.client_api import SearchView
from api.posts.serializers.serializers import PostSerializer


class ArticleService:
    """Handler providing methods for API Post."""

    serializer_class = PostSerializer

    def get_articles_list(self, keyword: str) -> Response:
        """Fetch a list of articles from an external API based on a keyword."""
        search_view = SearchView()
        res_from_api = search_view.get_articles(keyword)
        if res_from_api.status_code == 200:
            list_articles = res_from_api.data.get('articles', [])
            if list_articles:
                return Response(list_articles)
            else:
                return Response({'message': 'No results were found for your request'})
        return res_from_api

    def choose_article(self, keyword: str, selected_url: str) -> Response:
        """Find the selected article from the list based on the URL."""
        articles = self.get_articles_list(keyword)
        if articles.status_code == 200 and isinstance(articles.data, list):
            article = None
            for a in articles.data:
                if a.get('url') == selected_url:
                    article = a
                    break
            if article is None:
                return Response({'message': 'The article with the specified URL was not found'})
            return self.create_post(article)
        return articles

    def create_post(self, article: Dict[str, any]) -> Response:
        """Create a post using the provided data."""
        post_data = {
            'title': article.get('title', ''),
            'body': article.get('content', '')
        }
        serializer = self.serializer_class(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post successfully created'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Error creating post'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
