from django.db import models
# from django library for specifically postgres
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()

class Tweets(models.Model):
    body = models.CharField(max_length=200)
    img = models.CharField(max_length=300)
    likes = models.IntegerField(blank=True)
    # unlimited users can reply to tweet with a max character length
    tags = ArrayField(models.CharField(max_length=200), blank=True)
