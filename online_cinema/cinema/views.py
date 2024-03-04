from django.shortcuts import render
from django.http import HttpResponse
from .models import Film, Genre

def index(request):
      film = Film.objects.all()
      context = {
            'film': film
      }
      return render(request, 'cinema/index.html', context)

def genre(request):
      genre = Genre.objects.all()
      context = {
            'genre' : genre
      }
      return render(request, 'cinema/genre.html', context)

def all_films(request):
      films = Film.objects.all().order_by('?')
      context = {
            'films': films
      }
      return render(request, 'cinema/all_films.html', context)

def film_detail(request, slug):
      films_detail = Film.objects.get(slug__exact=slug)
      context = {
            'films_detail': films_detail
      }
      return render(request, 'cinema/film_detail.html', context)