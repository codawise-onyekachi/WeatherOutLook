from django import forms

class LocationForm(forms.Form):
    city = forms.CharField(max_length=100, required=True, label="Enter City")
