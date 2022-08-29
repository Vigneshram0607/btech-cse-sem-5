from django import forms
from constructionapp.models import Member,Properties

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['fname','lname','email','passwd','age','landproperty']

class PropertyForm(forms.ModelForm):
    class Meta:
        model=Properties
        fields=['city','address','landsq','price']

