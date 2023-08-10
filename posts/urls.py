from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.models import User

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostListAPIView)
router.register(r'comments', views.CommentCreateAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.post_list_view, name='post_list'),

]
