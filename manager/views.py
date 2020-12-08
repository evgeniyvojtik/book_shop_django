from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from manager.models import Book, LikeBookUser, Comment, LikeCommentUser


def hello(request, name = 'Filipp', digit = None):
    if digit is not None:
        response = {'name': 'Bogdan', 'addr':'Minsk'}
    return HttpResponse(f'Hello {name}')


class MyPage(View):
    def get(self, request):
        context = {}
        context['books'] = Book.objects.prefetch_related("authors", "comments").\
                                                annotate(count=Count("likes1"))
        context["commenter"] = Comment.objects.prefetch_related('like_comment')
        return render(request, 'index.html', context)


class Addlike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
                LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect('the-main-page')


class AddCommentlike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
                LikeCommentUser.objects.create(user=request.user, comment_id=id)
        return redirect('the-main-page')


class DeleteLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            Comment.objects.get(id=id).delete()
        return redirect('the-main-page')

class OpenBook(View):
    def get(self, request,id):
        context = {}
        context['books'] = Book.objects.get(id=id)

        return render(request, 'book.html', context)

