from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

