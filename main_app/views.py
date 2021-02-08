from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def pokemon_index(request):
    return render(request, 'pokemon/index.html')
