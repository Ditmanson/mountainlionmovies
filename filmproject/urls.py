from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('popular_movies', views.popular_movies, name='popular_movies'),
path('search_movies', views.search_movies, name='search_movies'),
path('register/', views.register, name='register'),
# Note these need 'filmproject/ ' since it cant be defined elsewhere as an out of the box component
path('login/', auth_views.LoginView.as_view(template_name='filmproject/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='filmproject/logout.html'), name='logout'),
path('accounts/profile/', views.profile, name='profile'),
]
