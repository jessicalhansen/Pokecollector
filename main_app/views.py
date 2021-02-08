from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About PokeCollector!</h1>')


def pokemon_index(request):
    return HttpResponse('<h1>See All Pokemon!</h1>')
