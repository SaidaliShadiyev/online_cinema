from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('genre/', views.genre, name='genre'),
      path('all_films/', views.all_films, name='all_films'),
      path('/<slug:slug>', views.film_detail, name='film_detail'),
]