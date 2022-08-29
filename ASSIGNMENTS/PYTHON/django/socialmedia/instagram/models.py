from django.db import models

# Create your models here.

"""
TO ORDER:
ordering = (colName) ->ASC
ordering = (-colName) ->DESC
"""


class Instagram(models.Model):
    name = models.CharField(max_length=20)
    regnum = models.CharField(max_length=20)

    class Meta:
        db_table = "instagram"


