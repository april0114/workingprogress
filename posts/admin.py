from django.contrib import admin
from .models import Post, Comment
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('password',) #'users')  # 'user_display' 추가


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at','image')