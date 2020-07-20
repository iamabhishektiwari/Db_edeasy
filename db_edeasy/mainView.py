from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse



class Index(View):
    
    def get(self, request):
        context = {
            'test': "latest_question_list",
            }
        return render(request, 'index.html', context)

    def post(self, request):
        pass
