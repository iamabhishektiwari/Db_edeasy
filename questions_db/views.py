from django.shortcuts import render
from rest_framework import viewsets

from .models import Topic, Level, McqQuestion, RelatedExam
from .serializer import TopicSerializer, LevelSerializer, McqQuestionSerializer, RelatedExamSerializer
# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class McqQuestionViewSet(viewsets.ModelViewSet):
    queryset = McqQuestion.objects.all()
    serializer_class = McqQuestionSerializer


class RelatedExamViewSet(viewsets.ModelViewSet):
    queryset = RelatedExam.objects.all()
    serializer_class = RelatedExamSerializer
