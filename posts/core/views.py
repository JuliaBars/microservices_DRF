from rest_framework.response import Response
from rest_framework.views import APIView

import requests

from .models import Post
from .serializers import PostSerializer


class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return Response([self.format_post(post) for post in posts])

    def format_post(self, post):
        comments = requests.get(
            f'http://127.0.0.1:8001/api/posts/{post.id}/comments/'
        ).json()
        return {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments': comments,
        }

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


