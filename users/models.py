from django.db import models

# Create your models here.
class userregister(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)