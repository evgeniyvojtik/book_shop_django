from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from manager.models import Book


def hello(request, name = 'Filipp', digit = None):
    if digit is not None:
        response = {'name': 'Bogdna', 'addr':'Minsk'}
    return HttpResponse(f'Hello {name}')

class MyPage(View):
    def get(self, request):
        context = {'books': Book.objects.all()}
        return render(request, 'index.html', context)