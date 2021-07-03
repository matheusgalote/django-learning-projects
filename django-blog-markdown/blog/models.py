from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    cover_img = models.ImageField(upload_to='imgs/covers/')