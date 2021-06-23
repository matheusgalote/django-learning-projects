from django.db import models

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=70)
    grade = models.FloatField(max_length=10)
    genre = models.CharField(max_length=20)
    status = models.BooleanField() # se o status for True já terminou de ler, se false ainda lendo
    image = models.FilePathField(path="/img")