from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('Male','male'),
    ('Female','female')
]
SUBSCRIPTION_CHOICES = [
    ('Month','Monthly'),
    ('Annual', 'Annually'),
]

CHARGE_CHOICES = [
    (100,'100'),
    (1000, '1000'),
]

class ReaderModel(models.Model):
    RName = models.CharField(max_length=30)
    RNumber = models.IntegerField(unique=True)
    Gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=10)
    City = models.CharField(max_length=40)
    ContactNumber = models.BigIntegerField()
    Subscription = models.CharField(choices=SUBSCRIPTION_CHOICES, default='Month', max_length=10)
    Charges = models.IntegerField(choices=CHARGE_CHOICES, default=100)

    class Meta:
        db_table = 'reader'
        ordering = ('-Charges',)

