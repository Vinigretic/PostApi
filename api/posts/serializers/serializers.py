"""
API Post App Configuration.

This module defines the configuration for api Post.

"""
from typing import Any, Dict

from rest_framework import serializers

from api.posts.models.posts import Posts


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    class Meta:
        """Metadata options for the PostSerializer."""

        model = Posts

        fields = [
            'id',
            'created',
            'body',
            'title',
        ]
        read_only_fields = ['id']

    def create(self, validated_data: Dict[str, Any]) -> Posts:
        """Post creation method."""
        body = validated_data['body']
        title = validated_data['title']
        return Posts.objects.create(body=body, title=title)
