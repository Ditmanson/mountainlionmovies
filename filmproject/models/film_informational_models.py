from django.db import models
from django.urls import reverse


class Collection(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Company(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    company = models.CharField(max_length=200)
    def __str__(self):
        return self.company

class Country(models.Model):
    code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.country

class Film(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)
    belongs_to_collection = models.BooleanField(default=False)
    budget = models.IntegerField(null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    imdb_id = models.CharField(max_length=20, blank=True, null=True)
    original_title = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000, blank=True, null=True)
    popularity = models.DecimalField(decimal_places=6, max_digits=20)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    revenue = models.BigIntegerField(null=True)
    runtime = models.IntegerField(null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    tagline = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    tmdb_id = models.IntegerField(unique=True, null=True)
    vote_average = models.DecimalField(decimal_places=3, max_digits=6, null=True, blank=True)
    vote_count = models.IntegerField(null=True)
    mlm_rating = models.DecimalField(decimal_places=6, max_digits=20, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("film-detail", args=[str(self.id)])

class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    genre = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.genre

class Keyword(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    keyword = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.keyword

class Language(models.Model):
    code = models.CharField(null=True, unique=True, max_length=4)
    language = models.CharField(null=True, max_length=200)
    def __str__(self):
        return self.language

class Person(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    tmdb_id = models.IntegerField(unique=True)
    known_for_department = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    popularity = models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)
    profile_path = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("person-detail", args=[str(self.id)])
