from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(default="", blank=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.CharField(max_length=256) 

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
