from django.db import models
from django.conf import settings

# Create your models here.
class feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)