from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Collection, Company, Country, Film, Genre, Keyword, Language, Person, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Seen_Films, LT_Viewer_Ratings

def index(request):
    return render( request, 'filmproject/index.html')

class FilmDetailView(generic.DetailView):
    model = Film

class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'film_list'
    paginate_by = 30

def popular_movies(request):
    return render( request, 'filmproject/popular_movies.html')

def search_movies(request):
    return render( request, 'filmproject/search_movies.html')

class ViewerDetailView(generic.DetailView):
    model = Viewer

class ViewerListView(generic.ListView):
    model = Viewer