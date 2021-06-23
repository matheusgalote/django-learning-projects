from django.db import models

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    # image = models.FilePathField(path="/img")