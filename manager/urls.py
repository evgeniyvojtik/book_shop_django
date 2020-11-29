from django.urls import path

from manager.views import hello

urlpatterns = [
    path('hello/<str:name>/', hello)
]