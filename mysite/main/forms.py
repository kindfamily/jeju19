from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ('name', 'lat', 'lng', 'mainphoto', 'subphoto', 'content', 'locate', 'phone', 'insta',)