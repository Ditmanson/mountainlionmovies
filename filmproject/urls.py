from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import FilmListView, FilmDetailView, ViewerListView, ViewerDetailView, index, popular_movies, search_movies
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *


# Create a router and register all the viewsets
router = DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'viewers', ViewerViewSet)
router.register(r'watchlist', LT_Viewer_WatchlistViewSet)
router.register(r'seen_films', LT_Viewer_SeenViewSet)
router.register(r'friend_requests', FriendRequestViewSet)
router.register(r'film_cast', LT_Films_CastViewSet)
router.register(r'film_companies', LT_Films_CompaniesViewSet)
router.register(r'film_countries', LT_Films_CountriesViewSet)
router.register(r'film_crew', LT_Films_CrewViewSet)
router.register(r'film_genres', LT_Films_GenresViewSet)
router.register(r'film_keywords', LT_Films_KeywordsViewSet)
router.register(r'film_languages', LT_Films_LanguagesViewSet)

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Profile pages
    path('accounts/profile/', views.profile, name='profile'),  # For current user profile
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('compare/', views.compare_movies, name='compare_movies'),
    path('profile/<int:viewer_id>/', views.profile, name='profile_viewer'),  # For other users' profiles

    # Film-related URLs
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),
    path('films/<int:pk>/add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('films/<int:pk>/mark_as_seen/', views.mark_as_seen, name='mark_as_seen'),
    path('films/<int:pk>/remove_from_seen/', views.remove_from_seen, name='remove_from_seen'),
    path('films/<int:pk>/remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='filmproject/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='filmproject/logout.html'), name='logout'),
    path('popular_movies', popular_movies, name='popular_movies'),
    path('register/', views.register, name='register'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='filmproject/password_reset.html'), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='filmproject/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='filmproject/password_reset_complete.html'), name='password_reset_complete'),

    path('search_movies', search_movies, name='search_movies'),
    path('viewers/', ViewerListView.as_view(), name='viewers'),
    path('viewers/<int:pk>', ViewerDetailView.as_view(), name='viewer-detail'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]