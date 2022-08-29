from django.db import models

class ConferenceDetails(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    deadline = models.DateField()
    ind = models.CharField(max_length=50)
    frn = models.CharField(max_length=50)

    def __str__(self):
        return self.title