from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import TopicForm, McqQuestionForm
from questions_db.models import Topic, McqQuestion
from django.shortcuts import redirect


class Index(View):

    def get(self, request):
        context = {
            'test': "latest_question_list",
            }
        return render(request, 'home.html', context)

    def post(self, request):
        pass


class Topics(View):
    form = TopicForm()

    def get(self, request):
        topics = Topic.objects.all()
        context = {
            "form": self.form,
            "topics": topics,
            }
        return render(request, 'addTopic.html', context)

    def post(self, request):
        submitedForm = TopicForm(request.POST)
        if submitedForm.is_valid():
            submitedForm.save()
            return redirect('Topics')
        else:
            return redirect('Topics')




class Questions(View):

    def get(self, request):
        form = McqQuestionForm()
        questions = McqQuestion.objects.all()
        context = {
            'form': form,
            'questions':questions,
            }
        return render(request, 'addQuestions.html', context)

    def post(self, request):
        form = McqQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Questions')
        else:
            return redirect('Questions')
