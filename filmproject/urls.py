from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import FilmListView, FilmDetailView, ViewerListView, ViewerDetailView, index, popular_movies, search_movies

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import FilmListView, FilmDetailView, ViewerListView

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Profile pages
    path('accounts/profile/', views.profile, name='profile'),  # For current user profile
    path('profile/<int:viewer_id>/', views.profile, name='profile_viewer'),  # For other users' profiles

    # Film-related URLs
    path('films/', FilmListView.as_view(), name='film-list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),
    path('films/<int:pk>/add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('films/<int:pk>/mark_as_seen/', views.mark_as_seen, name='mark_as_seen'),
    path('films/<int:pk>/remove_from_seen/', views.remove_from_seen, name='remove_from_seen'),
    path('films/<int:pk>/remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='filmproject/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='filmproject/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='filmproject/password_reset.html'), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='filmproject/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='filmproject/password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='filmproject/password_reset_complete.html'), name='password_reset_complete'),

    # Movie search and popular movies
    path('search_movies/', views.search_movies, name='search_movies'),
    path('popular_movies/', views.popular_movies, name='popular_movies'),

    # Viewer list
    path('viewers/', ViewerListView.as_view(), name='viewers'),

    # Email activation
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # Friend request URLs
    path('accounts/friend_requests/', views.manage_friend_requests, name='friend_requests'),
    path('send_friend_request/<int:viewer_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('remove_friend/<int:viewer_id>/', views.remove_friend, name='remove_friend'),
]

