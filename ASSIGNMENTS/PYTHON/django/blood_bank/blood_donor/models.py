from django.db import models

# Create your models here.



# class BloodGroup(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'myapp_city'

GENDER_CHOICES = [
    ('Male','male'),
    ('Female','female'),
]
BLOOD_GROUP = [
    ('A+','A+') ,
    ('A−','A−'),
    ('B+','B+') ,
    ('B−','B−') ,
    ('AB+','AB+') ,
    ('AB−','AB−' ),
    ('O+','O+' ),
    ('O−','O−'),
]
class BloodDonor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10, default='A+', choices=BLOOD_GROUP)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male',max_length=10)
    city = models.CharField(max_length=15)
    phonenumber = models.IntegerField()
    class Meta:
        db_table = 'blooddonor'


