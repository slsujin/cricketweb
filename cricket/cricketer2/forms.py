from django import forms
from .models import cric

class cricform(forms.ModelForm):
    class Meta:
        model=cric
        fields=['name','about','age','img']

