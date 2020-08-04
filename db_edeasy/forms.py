from django import forms
from questions_db.models import Topic, McqQuestion, RelatedExam


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class McqQuestionForm(forms.ModelForm):
    class Meta:
        model = McqQuestion
        fields = "__all__"


class RelatedExamForm(forms.ModelForm):
    class Meta:
        model = RelatedExam
        fields = "__all__"
