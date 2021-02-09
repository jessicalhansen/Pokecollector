from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pokemon
from .forms import BattleForm

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    battle_form = BattleForm()

    context = {
        'pokemon': pokemon,
        'battle_form': battle_form,
    }
    return render(request, 'pokemon/detail.html', context)

def delete_pokemon(request, pokemon_id):
    if request.method == 'POST':
        Pokemon.objects.get(id=pokemon_id).delete()
    return redirect('pokemon_index')


def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)

    if request.method == 'GET':
        pokemon_form = PokemonForm(id=pokemon_id)
        context = {'form': pokemon_form}
        return render(request, 'pokemon/edit.html', context)
    else:
        pokemon_form = PokemonForm(instance=pokemon)
        if pokemon_form.is_valid():
            pokemon_form.save()
        return redirect('pokemon_detail', pokemon_id=pokemon_id)


def add_battle(request, pokemon_id):
    form = BattleForm(request.POST)

    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.pokemon_id = pokemon_id
        new_battle.save()
    return redirect('pokemon_detail', pokemon_id=pokemon_id)
