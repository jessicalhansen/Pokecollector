from django import forms
from .models import Battle, Pokemon

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['date', 'result', 'opponent']

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'name',
            'pokedex_id',
            'type',
            'color',
            'description'
        ]
