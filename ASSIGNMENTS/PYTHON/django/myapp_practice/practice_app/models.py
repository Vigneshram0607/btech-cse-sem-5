from django.db import models

# Create your models here.
class practice_app(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default="Type Your Summary!")

