from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


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