from django.db import models
from pokebase import pokemon


# Create your models here.

class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).lower()

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    pokedex_id = models.IntegerField(blank=True)
    type = models.CharField(
        max_length=100,
        blank=True
        )
    color = models.CharField(
        max_length=50,
        blank=True
        )
    description = models.TextField(
        max_length=250,
        blank=True
    )



# def fetch_pokemon():
#     name = input('Which Pokemon do you want? ')
#     print("Fetching " + name)
#     poke=pokemon(name)
#     print(f"{poke.name} is #{poke.id} in the Pokedex, and weighs {poke.weight} lbs.")

# fetch_pokemon()
