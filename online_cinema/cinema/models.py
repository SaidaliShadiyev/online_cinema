from django.db import models
from django.shortcuts import reverse

class Film(models.Model):
      title = models.CharField(max_length=100)
      desc = models.TextField(max_length=500)
      img = models.CharField(max_length=500)
      year = models.IntegerField()
      slug = models.SlugField(unique=True)
      genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

      def __str__(self):
            return self.title
      
      def get_link(self):
            return reverse('film_detail_url', kwargs = {'slug':self.slug})

class Genre(models.Model):
      title = models.CharField(max_length=100)
      slug = models.SlugField(unique=True)

      def __str__(self):
            return self.title
      
      def get_link(self):
            return reverse('genre_detail_url', kwargs = {'slug':self.slug})
