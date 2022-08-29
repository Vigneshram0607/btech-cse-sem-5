from django.db import models
from django.db.models.base import Model
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
SUBS_CHOICES=(("month","Monthly"),("Annual","Annually"))
CHG_CHOICES=(
    (100,"100"),
    (1000,"1000")
)
# Create your models here.
class reader(models.Model):
    RName=models.CharField(max_length=30)
    RNumber=models.IntegerField(unique = True)
    Gender=models.CharField(choices=GENDER_CHOICES,default='M', max_length=128)
    City=models.CharField(max_length=40)
    ContactNumber=models.BigIntegerField()
    Subscription=models.CharField(choices=SUBS_CHOICES,default='month', max_length=128)
    Charges=models.IntegerField(choices=CHG_CHOICES,default=100)
    
    class Meta:
        ordering=('-Charges',)