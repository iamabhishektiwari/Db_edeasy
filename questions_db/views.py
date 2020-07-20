from django.shortcuts import render
from rest_framework import viewsets

from .models import Topic, Level
from .serializer import TopicSerializer, LevelSerializer
# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
