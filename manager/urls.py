from django.urls import path
from manager.views import hello, MyPage, Addlike

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('hello/<str:name>/', hello),
    path('hello/', hello),
    path('add_like/<int:id>/', Addlike.as_view(), name='add_like'),
    path('', MyPage.as_view(), name='the-main-page'),
    
]