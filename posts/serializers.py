from rest_framework import serializers
from .models import Post, Comment

#댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields =['content','password','password2']
        fields =['password',]
    
#전체 목록
#class PostListSerializer(serializers.ModelSerializer):
#    image = serializers.ImageField(use_url=True)
#    comment = CommentSerializer(many=True, read_only=True)
    #myidentity = CommentSerializer(read_only=True)
#    class Meta:
#        model = Post
#        fields = ['title','content', 'image','comment','password2']




