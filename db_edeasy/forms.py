from django import forms
from questions_db.models import Topic, McqQuestion


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class McqQuestionForm(forms.ModelForm):
    class Meta:
        model = McqQuestion
        fields = "__all__"
