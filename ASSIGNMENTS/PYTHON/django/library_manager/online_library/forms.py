from django import forms
from .models import *


class AddReaderForm(forms.ModelForm):
    class Meta:
        model = ReaderModel
        fields = ["RName", "RNumber", "Gender", "City", "ContactNumber", "Subscription"]
        widgets = {
            'Gender': forms.RadioSelect(choices=GENDER_CHOICES)
        }