from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import viewsets
from .models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import render

from posts.serializers import CommentSerializer, PostListSerializer
from rest_framework.response import Response


class PostListAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class CommentCreateAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def post_list_view(request):
    return render(request, 'templates/post_list.html')
