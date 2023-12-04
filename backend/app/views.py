from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Utilities
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

import typing as t

from .models import *
from .serializer import *

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]

test = [
    {
        "Welcome": "Portfolio v1",
        "Owner": "CoderMoongun",
        "Api Version 1.0": "/docs or /redoc",
    }
]

@api_view(["GET"])
def index(request: HttpRequest) -> Response:
    return Response(test, status=status.HTTP_200_OK)

@api_view(["GET"])
def blog_main_response_get(request: HttpRequest) -> Response:
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def category_blog_response_get(request: HttpRequest) -> Response:
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer(queryset, many=True)

    return Response(serializer_class.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def blog_special_theme_get(request: HttpRequest, slug: str) -> Response:
    blog_special_theme = Blog.objects.filter(slug=slug).first()
    serializers = BlogSerializer(blog_special_theme)

    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def article_main_response_get(request: HttpRequest) -> Response:
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def category_article_response_get(request: HttpRequest) -> Response:
    category_articles = CategoryArticle.objects.all()
    serializers = CategoryArticleSerializer(category_articles, many=True)

    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def article_special_theme_get(request: HttpRequest, slug: str) -> Response:
    article_special_theme = Article.objects.filter(slug=slug).first()
    serializers = ArticleSerializer(article_special_theme)

    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def contact_form_post(request: HttpRequest) -> Response:
    contact_form = ContactFormSerializer(data=request.data)

    if contact_form.is_valid():
        contact_form.save()
        return Response(contact_form.data, status=status.HTTP_200_OK)

    else:
        return Response(
            {"message": "Invalid data", "error": contact_form.errors}, status=status.HTTP_400_BAD_REQUEST
        )