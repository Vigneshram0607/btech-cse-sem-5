from django.db import models
# Create your models here.

class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)

    class Meta:
        db_table = 'store'
        ordering = ("-country","-state",)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=25)
    brand = models.CharField(max_length=15)
    category = models.CharField(max_length=15)

    class Meta:
        db_table = 'product'
        ordering = ("-brand",)


class Sale(models.Model):
    date = models.DateField()
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    units_sold = models.IntegerField()

    class Meta:
        db_table = 'sale'
        ordering = ("-date","-store_id","-product_id")
