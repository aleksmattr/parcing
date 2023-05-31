from django.urls import path
from . import views

urlpatterns = [
    path('chatgpt', views.chatgpt, name='chatgpt')
]