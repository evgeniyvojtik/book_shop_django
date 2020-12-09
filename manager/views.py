from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from manager.models import Book, LikeBookUser, Comment, LikeCommentUser


def hello(request, name = 'Filipp', digit = None):
    if digit is not None:
        response = {'name': 'Bogdan', 'addr':'Minsk'}
    return HttpResponse(f'Hello {name}')



# class MyPage(View):
#     def get(self, request):
#         context = {}
#         comment_query = Comment.objects.all().annotate(count_like=Count("users_like")).select_related('author')
#         comments = Prefetch('comments', comment_query)
#         context['books'] = Book.objects.prefetch_related("authors", comments). \
#                                          annotate(count_like = Count('users_like'))
#
#
#         return render(request, 'index.html', context)

class MyPage(View):
    def get(self, request):
        context = {}
        comment_query = Comment.objects.annotate(count_like=Count("users_like")).select_related('author')
        comments = Prefetch('comments', comment_query)
        books = Book.objects.prefetch_related('authors', comments)
        context['books'] = books
        context['rate'] = "3"
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


class BookPage(View):
    def get(self, request,id):
        book = Book.objects.get(id=id)


        return render(request, 'book.html', {"book": book})

class AddRate2Book(View):
    def get(self, request, id, rate):
        return redirect('the-main-page')
