from django.db import models

# Create your models here.
# This is model file

class FancyStoreModel(models.Model):
    item_id = models.IntegerField(unique=True) # item id
    item_name = models.CharField(max_length=30) # item name
    stock = models.IntegerField(default=25) # item stock
    price = models.IntegerField() # item price

    class Meta:
        db_table = 'facystore' # table name
        ordering = ('item_id',) # to print in ascending order

    def __str__(self):
        return self.item_name #STRING REPRESENTATION






