from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils import timezone

class BlogSerializer(ModelSerializer):

    category = serializers.StringRelatedField()
    label = serializers.StringRelatedField(many=True)
    class Meta:
        model = Blog
        fields = "__all__"

class CategorySerializer(ModelSerializer):

    class Meta:
        model = CategoryBlog
        fields = "__all__"


class ArticleSerializer(ModelSerializer):

    category = serializers.StringRelatedField()
    label = serializers.StringRelatedField(many=True)
    createAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", default_timezone=timezone.get_current_timezone())
    class Meta:
        model = Article
        fields = "__all__"

