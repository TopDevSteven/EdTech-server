from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user')),
    path('gpt_hub/', include('personal_ai.urls')),
    path('personal_ai/', include('gpt_hub.urls')),
    path('lesson/', include('lessonapp.urls')),
]
