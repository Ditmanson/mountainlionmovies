from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render( request, 'filmproject/index.html')

def popular_movies(request):
    return render( request, 'filmproject/popular_movies.html')