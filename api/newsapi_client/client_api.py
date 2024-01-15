"""Module for api.newsapi_client.views.

This module contains Django Rest Framework views for handling article newsapi_client and post creation.
"""

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchView(APIView):
    """View for searching articles based on a keyword using an external API."""

    def get_articles(self, keyword: str) -> Response:
        """Fetch articles from an external API based on a given keyword."""
        headers = {
            'X-Api-Key': '2f1efe9b61be499683c5a5f0436dd8c1',
            # I know that all the keys need to be hidden, I leave it if need to launch the app
        }
        url = 'https://newsapi.org/v2/everything'
        try:
            response = requests.get(url, params={'q': keyword}, headers=headers, timeout=30)
            response.raise_for_status()
        except Exception as err:
            return Response({'error': f'Error: {err}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(response.json(), status=response.status_code)
