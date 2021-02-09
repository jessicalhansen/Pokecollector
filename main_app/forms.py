from django import forms
from .models import Battle, Pokemon

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['date', 'result', 'opponent']
