from dataclasses import fields
from django import forms
from .models import Header

class HeaderForm(forms.ModelForm):
    #form for the header models's image field
    class Meta:
        model = Header
        fields = ('headerwords', 'headerpic')