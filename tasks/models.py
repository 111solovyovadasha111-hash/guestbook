from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    author = models.CharField("имя автора", max_length=100)
    text = models.TextField("")

