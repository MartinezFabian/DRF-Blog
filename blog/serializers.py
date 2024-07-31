from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "excerpt",
            "content",
            "slug",
            "published",
            "updated_at",
            "status",
            "category",
            "author",
        )

        read_only_fields = ("published", "updated_at", "slug", "author")
