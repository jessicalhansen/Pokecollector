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

    def __str__(self):
        return self.name
    

OUTCOMES = (
    ('L', 'Loss'),
    ('W', 'Win')
)
class Battle(models.Model):
    date = models.DateField()
    outcome = models.CharField(
        max_length=1,
        choices=OUTCOMES,
        default=OUTCOMES[0][0]
    ),
    opponent = models.CharField(max_length=100)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.get_OUTCOME_display()} on {self.date}'
    



# def fetch_pokemon():
#     name = input('Which Pokemon do you want? ')
#     print("Fetching " + name)
#     poke=pokemon(name)
#     print(f"{poke.name} is #{poke.id} in the Pokedex, and weighs {poke.weight} lbs.")

# fetch_pokemon()
