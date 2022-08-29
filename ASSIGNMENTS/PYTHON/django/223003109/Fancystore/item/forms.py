from .models import *
from django import forms

# THIS IS FORMS FILE
class FancystoreForm(forms.ModelForm):
    class Meta:
        model = FancyStoreModel
        fields = '__all__' # to include all fields
