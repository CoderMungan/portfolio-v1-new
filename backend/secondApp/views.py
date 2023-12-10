from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response

# ModelViewSet Import
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Modeli Çek
from .models import *

# Serializer Çek
from .serializers import *
# Create your views here.

# Model Geniş Model
class HayvanOlustur(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


# Retrive olduğundan dolayı tekli veriyi güncelleme
class HayvanSadeceGuncelle(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=Animal.objects.all()
    serializer_class = AnimalSerializer


# Retrive olduğundan dolayı tekli veriyi gösterme
class HayvanSadeceGet(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


# Retrive olduğundan dolayı tekli veriyi silme
class HayvanSinglePost(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)


        data = {'message': 'İt silindi'}
        
        return Response(data, status=status.HTTP_201_CREATED)
    

# Filtreleme işlemleri
class HayvanFiltre(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        return Animal.objects.filter(yas__lte = 50)