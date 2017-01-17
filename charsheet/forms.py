from django import forms
from .models import Character, Stats

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','race','char_class',]

class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['str','dex','con','int','wis','cha']
