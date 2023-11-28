from rest_framework.decorators import api_view
from rest_framework.response import Response

# Utilities
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

import typing as t

from .models import *
from .serializer import *

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]

test = [
    {
        "Welcome" : "Portfolio v1",
        "Owner"   : "CoderMoongun",
    }
    ]


@api_view(["GET"])
def index(request: HttpRequest) -> Response:
    return Response(test)

@api_view(["GET"])
def category_response_get(request: HttpRequest) -> Response:
    
    categories = CategoryBlog.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data, status=200)

@api_view(["GET"])
def blog_main_response_get(request: HttpRequest) -> Response:

    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data, status=200)
