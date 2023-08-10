from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    #제목
    title = models.CharField(max_length=50, blank=True)
    #본문
    content = models.TextField()
    #생성 시간
    created_at = models.DateTimeField(auto_now_add=True)
    #이미지
    image = models.ImageField(blank=True, null=True)
    #댓글 리스트


class Comment(models.Model):

    #댓글 내용
    #content = models.CharField(max_length=100)
    #비밀번호
    password = models.CharField(max_length=15)
    #password2 = models.CharField(max_length=15)
    #아이디
    #users = models.CharField(max_length=50,blank=True)
    #myidentity = models.CharField(max_length=15)
    def __str__(self):
        return self.content
    
