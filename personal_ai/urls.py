from django.urls import path
from .views import gpt_chat_coding, gpt_chat_presentation

urlpatterns = [
    path('chat/coding', gpt_chat_coding),
    path('chat/presentation', gpt_chat_presentation)
]