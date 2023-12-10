from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *



class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Animal
        fields = "__all__"


