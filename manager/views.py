from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from manager.models import Book, LikeBookUser


def hello(request, name = 'Filipp', digit = None):
    if digit is not None:
        response = {'name': 'Bogdna', 'addr':'Minsk'}
    return HttpResponse(f'Hello {name}')

class MyPage(View):
    def get(self, request):
        context = {}
        context['books'] =  Book.objects.prefetch_related("authors","comments").\
                                                annotate(count=Count("likes1"))
        return render(request, 'index.html', context)

class Addlike(View):
    def get(selfself, request, id):
        if request.user.is_authenticated:
                LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect('the-main-page')