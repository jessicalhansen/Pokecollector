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
    return render(request, 'pokemon/detail.html', { 'pokemon': pokemon, 'battle_form': battle_form })
