from django.urls import path
from manager.views import hello, MyPage, Addlike, AddCommentlike, DeleteLike, OpenBook

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path('click_the_book/<int:id>/', OpenBook.as_view(), name='click_the_book'),
    path('add_like/<int:id>/', Addlike.as_view(), name='add_like'),
    path('add_comment_like/<int:id>/', AddCommentlike.as_view(), name='add_comment_like'),
    path('delete_like/<int:id>/', DeleteLike.as_view(), name='delete_like'),
    path('', MyPage.as_view(), name='the-main-page'),
    
]