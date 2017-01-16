from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','race','char_class',]
