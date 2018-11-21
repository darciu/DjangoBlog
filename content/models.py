from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, default='unknown')

    def __str__(self):
        return "Comment " + str(self.pk)
