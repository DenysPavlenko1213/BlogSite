from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    full_text = models.TextField()
    date = models.DateField(null=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_text = models.TextField()
    date = models.DateField(null=True)
