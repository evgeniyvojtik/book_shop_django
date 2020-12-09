from django.urls import path
from manager.views import hello, MyPage, Addlike, AddCommentlike, DeleteLike, BookPage, AddRate2Book

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path('click_the_book/<int:id>/', BookPage.as_view(), name='click_the_book'),
    path('add_like/<int:id>/', Addlike.as_view(), name='add_like'),
    path('add_comment_like/<int:id>/', AddCommentlike.as_view(), name='add_comment_like'),
    path('delete_like/<int:id>/', DeleteLike.as_view(), name='delete_like'),
    path('add_rate_to_book/<int:id>/<str:rate>/', AddRate2Book.as_view(), name='add-rate'),
    path('', MyPage.as_view(), name='the-main-page'),
    
]