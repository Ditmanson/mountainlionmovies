from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ViewerRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'filmproject/profile.html')

def index(request):
    return render( request, 'filmproject/index.html')

def popular_movies(request):
    return render( request, 'filmproject/popular_movies.html')

def search_movies(request):
    return render( request, 'filmproject/search_movies.html')

def register(request):
    if request.method == 'POST':
        form = ViewerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('index')  # Redirect to the home page after registration
    else:
        form = ViewerRegistrationForm()
    return render(request, 'filmproject/register.html', {'form': form})
