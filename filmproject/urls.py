from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import FilmListView, FilmDetailView, ViewerListView, ViewerDetailView, index, popular_movies, search_movies

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('films/', FilmListView.as_view(), name='film-list'),
    path('films/<int:pk>', FilmDetailView.as_view(), name='film-detail'),
    path('films/<int:pk>/add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('films/<int:pk>/mark_as_seen/', views.mark_as_seen, name='mark_as_seen'),
    path('films/<int:pk>/remove_from_seen/', views.remove_from_seen, name='remove_from_seen'),
    path('films/<int:pk>/remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('login/', auth_views.LoginView.as_view(template_name='filmproject/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='filmproject/logout.html'), name='logout'),
    path('popular_movies', popular_movies, name='popular_movies'),
    path('register/', views.register, name='register'),
    path('search_movies', search_movies, name='search_movies'),
    path('viewers/', ViewerListView.as_view(), name='viewers'),
    path('viewers/<int:pk>', ViewerDetailView.as_view(), name='viewer-detail'),
]