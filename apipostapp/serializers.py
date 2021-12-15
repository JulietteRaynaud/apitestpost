from rest_framework import serializers
from apipostapp.models import Post

class postSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('postId', 'postTitle', 'postContent')