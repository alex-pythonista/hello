from django.contrib import admin
from django.urls import path

from .views import HelloAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', HelloAPI.as_view()),
]
