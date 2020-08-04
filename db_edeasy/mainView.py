from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import TopicForm, McqQuestionForm, RelatedExamForm
from questions_db.models import Topic, McqQuestion, RelatedExam
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
    ExamForm = RelatedExamForm()

    def get(self, request):
        topics = Topic.objects.all()
        examRelated = RelatedExam.objects.all()
        context = {
            "form": self.form,
            "topics": topics,
            "examRelated":examRelated,
            "ExamForm":self.ExamForm,
            }
        return render(request, 'addTopic.html', context)

    def post(self, request):
        submitedForm = TopicForm(request.POST)
        if submitedForm.is_valid():
            submitedForm.save()
            return redirect('Topics')
        else:
            return redirect('Topics')


class ExamRel(View):

    ExamForm = RelatedExamForm()

    def get(self, request):

        examRelated = RelatedExam.objects.all()
        context = {


            "examRelated":examRelated,
            "ExamForm":self.ExamForm,
            }
        return render(request, 'addExamRelated.html', context)

    def post(self, request):
        submitedForm = RelatedExamForm(request.POST)
        if submitedForm.is_valid():
            submitedForm.save()
            return redirect('ExamRel')
        else:
            return redirect('ExamRel')


class Questions(View):

    def get(self, request):
        form = McqQuestionForm()
        questions = McqQuestion.objects.all()
        count = len(questions)
        context = {
            'form': form,
            'questions':questions,
            'count':count,
            }
        return render(request, 'addQuestions.html', context)

    def post(self, request):
        form = McqQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Questions')
        else:
            return redirect('Questions')
