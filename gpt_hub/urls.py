from django.urls import path
from .views import document_create, chat_doc
urlpatterns = [
    path('chat/create', document_create),
    path('chat/doc', chat_doc)
]