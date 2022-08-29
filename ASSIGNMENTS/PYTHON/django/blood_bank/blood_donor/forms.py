from .models import *
from django import forms

# gender = forms.CharField(label='gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))


class BloodDonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = '__all__'
        widgets={
            'gender':forms.RadioSelect(choices=GENDER_CHOICES),
        }
