from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse



class Index(View):

    def get(self, request):
        context = {
            'test': "latest_question_list",
            }
        return render(request, 'home.html', context)

    def post(self, request):
        pass


class Topics(View):

    def get(self, request):
        context = {
            'test': "latest_question_list",
            }
        return render(request, 'addTopic.html', context)

    def post(self, request):
        pass


class Questions(View):

    def get(self, request):
        context = {
            'test': "latest_question_list",
            }
        return render(request, 'addQuestions.html', context)

    def post(self, request):
        pass
