from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)