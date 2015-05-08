from django.db import models


class Post(models.Model):
    created = models.DateTimeField()


class Comment(models.Model):
    created = models.DateTimeField()
    post = models.ForeignKey(Post, related_name='comments')
