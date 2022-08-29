from django.db import models

# Create your models here.
class Member(models.Model):
    objects = None
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    passwd=models.CharField(max_length=20)
    age=models.IntegerField()
    landproperty=models.CharField(max_length=15)



    def __str__(self):
        return self.fname+"  "+self.lname


class Properties(models.Model):

    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    landsq=models.IntegerField(max_length=20)
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.city + "   " +str(self.landsq) + "  " + self.price