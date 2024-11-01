from django import forms
from .models import Member

class LocationForm(forms.Form):
    city = forms.CharField(max_length=100, required=True, label="Enter City")

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone_number']
