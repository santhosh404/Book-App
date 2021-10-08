from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    email = models.CharField(max_length=50)
    Book = models.CharField(max_length=100)
    Description = models.TextField()

