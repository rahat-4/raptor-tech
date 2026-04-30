from rest_framework import generics, permissions, serializers

from blog.models import Blog
from common.serializers import CommonUserSerializer


class BlogSerializer(serializers.ModelSerializer):
    author = CommonUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ("alias",'slug', 'title', 'content', 'author', "tag", 'created_at', 'updated_at', 'image', 'image_caption')
        read_only_fields = ('author', 'created_at', 'updated_at')

