from django import forms
from .models import *

class add_reader(forms.ModelForm):
    class Meta:
        model = reader
        fields = ["RName","RNumber","Gender","City","ContactNumber","Subscription"]
        widgets={
            'Gender':forms.RadioSelect(choices=GENDER_CHOICES)
        }