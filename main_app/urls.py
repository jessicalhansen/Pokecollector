from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='pokemon_index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon_detail'),

    # path('pokemon/<int:pokemon_id>/delete/', views.delete_pokemon, name='delete_pokemon'),
    # path('pokemon/<int:pokemon_id>/edit/', views.edit_pokemon, name='edit_pokemon'),
    # path('pokemon/<int:pokemon_id>/add_battle/', views.add_battle, name='add_battle'),
]
