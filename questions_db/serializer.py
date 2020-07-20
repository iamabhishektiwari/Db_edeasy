from rest_framework import serializers

from .models import Topic, Level




class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'



class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
