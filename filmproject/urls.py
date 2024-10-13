from django.urls import path
from .views import FilmListView, FilmDetailView, ViewerListView, ViewerDetailView, index, popular_movies, search_movies

urlpatterns = [
    path('', index, name='index'),
    path('films/', FilmListView.as_view(), name='films'),
    path('films/<int:pk>', FilmDetailView.as_view(), name='film-detail'),
    path('popular_movies', popular_movies, name='popular_movies'),
    path('search_movies', search_movies, name='search_movies'),
    path('viewers/', ViewerListView.as_view(), name='viewers'),
    path('viewers/<int:pk>', ViewerDetailView.as_view(), name='viewer-detail'),
]