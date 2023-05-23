from django.urls import path, include

from .views import PostAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view()),
]