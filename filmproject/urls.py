from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('popular_movies', views.popular_movies, name='popular_movies'),
path('search_movies', views.search_movies, name='search_movies'),
]
