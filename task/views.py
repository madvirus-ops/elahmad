from django.shortcuts import render 
from rest_framework import generics
from . Serializers import SlackModelSerializer
from .models import SlackModel

class IndexView(generics.CreateAPIView):
    serializer_class = SlackModelSerializer

class ListView(generics.ListAPIView):
    queryset = SlackModel.objects.all()
    serializer_class = SlackModelSerializer 
