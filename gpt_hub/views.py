from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from django.http import JsonResponse
from rest_framework import exceptions as rest_exceptions, response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions
from user import serializers, models
import traceback

# Create your views here.

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def document_create(request):
    if request.method == "POST":
        try:
            user_id  = request.user.id
            file = request.FILES['file']
            topic = request.POST['topic']
            time = request.POST['time']
            doc_type = request.POST['type']
            new_document = models.Document(
                user_id=user_id, 
                document_type=doc_type,
                date=time,
                topic=topic
            )
            new_document.save()
            return response.Response(({"message": True}))
        except Exception as e:
            print(traceback.format_exc())
            return response.Response(({'message': False}))

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def chat_doc(request):
    if request.method == "POST":
        
        return response.Response(({"message": "success"}))