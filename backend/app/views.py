from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import *

test = [{"First": "Api", "Test": "Test", "Alimdar": "Full Stack", "Naber": "Moruk","calistim":"amk", "nasilsin": "iyiyim"}]


@api_view(["GET"])
def index(request):
    return Response(test)


@api_view(["GET"])
def deneme(request):
    return Response({"selam": "naber"})


def halil(request):
    return render("index.html")
