from django.db import models

# Create your models here.
class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=100)
    postContent = models.CharField(max_length=500)

