from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def hello(request, name = 'Filipp', digit = None):
    if digit is not None:
        response = {'name': 'Bogdna', 'addr':'Minsk'}
    return HttpResponse(f'Hello {name}')

class MyPage(View):
    def get(self, request):
        context = {'name':'Zhenya', 'addr':'Minsk'}
        context['arr'] = ['Igor', 'Abdul', 'Shahar', 'Ibragom', 'Oded']
        return render(request, 'index.html', context)