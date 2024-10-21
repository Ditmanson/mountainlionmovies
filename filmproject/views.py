from datetime import date
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db import models
from django.db.models import Case, Count, F, Q, Sum, Value, When
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.views.generic import ListView
from .forms import ViewerRegistrationForm
from .models import Collection, Company, Country, Film, Genre, Keyword, Language, Person, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Ratings, LT_Viewer_Seen, LT_Viewer_Watchlist, FriendRequest
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib import messages
from django.http import JsonResponse
from .serializers import (
    FilmSerializer, ViewerSerializer, LT_Viewer_SeenSerializer, LT_Viewer_WatchlistSerializer,
    FriendRequestSerializer, LT_Films_CastSerializer, LT_Films_CompaniesSerializer, LT_Films_CountriesSerializer,
    LT_Films_CrewSerializer, LT_Films_GenresSerializer, LT_Films_KeywordsSerializer, LT_Films_LanguagesSerializer
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib import messages
from django.http import JsonResponse
from .serializers import (
    FilmSerializer, ViewerSerializer, LT_Viewer_SeenSerializer, LT_Viewer_WatchlistSerializer,
    FriendRequestSerializer, LT_Films_CastSerializer, LT_Films_CompaniesSerializer, LT_Films_CountriesSerializer,
    LT_Films_CrewSerializer, LT_Films_GenresSerializer, LT_Films_KeywordsSerializer, LT_Films_LanguagesSerializer
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import random

class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'filmproject/film_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context['is_seen'] = viewer.has_seen_film(film)
            context['is_in_watchlist'] = viewer.is_in_watchlist(film)
        else:
            context['is_seen'] = False
            context['is_in_watchlist'] = False
        context['film'] = film
        return context
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")
        film = self.get_object()
        viewer = request.user.viewer
        action = request.POST.get('action')
        # Handle the Mark as Seen / Remove from Seen actions
        if action == 'mark_as_seen':
            seen_entry, created = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == 'remove_from_seen':
            seen_entry = LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).first()
            if seen_entry:
                seen_entry.seen_film = False
                seen_entry.save()
        # Handle the Add to Watchlist / Remove from Watchlist actions
        elif action == 'add_to_watchlist':
            watchlist_entry, created = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == 'remove_from_watchlist':
            watchlist_entry = LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).first()
            if watchlist_entry:
                watchlist_entry.watchlist = False
                watchlist_entry.save()
        # Redirect back to the film detail page
        return redirect('film-detail', pk=film.id)

class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'film_list'
    paginate_by = 20
    def post(self, request, *args, **kwargs):
        # If the user is not authenticated, they cannot perform post actions like marking as seen or adding to watchlist
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")
        film_id = request.POST.get('film_id')
        action = request.POST.get('action')
        page_number = request.POST.get('page', 1)  # Default to page 1 if not provided
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer
        # Handle the Mark as Seen / Remove from Seen actions
        if action == 'mark_as_seen':
            seen_entry, created = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == 'remove_from_seen':
            seen_entry = LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).first()
            if seen_entry:
                seen_entry.seen_film = False
                seen_entry.save()
        # Handle the Add to Watchlist / Remove from Watchlist actions
        elif action == 'add_to_watchlist':
            watchlist_entry, created = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == 'remove_from_watchlist':
            watchlist_entry = LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).first()
            if watchlist_entry:
                watchlist_entry.watchlist = False
                watchlist_entry.save()
        # Redirect back to the same page
        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            seen_films = Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True)
            watchlist_films = Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True)
            context['seen_films'] = seen_films
            context['watchlist_films'] = watchlist_films
        else:
            context['seen_films'] = []
            context['watchlist_films'] = []
        return context
    
class ViewerDetailView(generic.DetailView):
    model = Viewer

    def get(self, request, *args, **kwargs):
        viewer = self.get_object()
        return redirect('profile_viewer', viewer_id=viewer.id)

class ViewerListView(generic.ListView):
    model = Viewer

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'filmproject/account_activation_invalid.html')
    
   




@login_required
def add_to_watchlist(request, pk):  # Assuming pk is passed in the URL
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer  # Assuming Viewer is tied to the logged-in user
    if request.method == 'POST':
        # Check if this viewer has already added this film to their watchlist
        watchlist_entry, created = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
        # Mark it as added to the watchlist
        watchlist_entry.watchlist = True
        watchlist_entry.save()
        return redirect('film-detail', pk=pk)
    return redirect('film-detail', pk=pk)

@login_required
def compare_movies(request):
    viewer = request.user.viewer
    seen_movies = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list('film', flat=True)
    if seen_movies.count() < 2:
        return render(request, 'filmproject/compare_movies.html', {'message': "You need to mark at least two movies as seen to start comparing."})
    # Randomly select two movies
    movie1, movie2 = random.sample(list(Film.objects.filter(id__in=seen_movies)), 2)
    # Ensure movie1 has the lower ID
    if movie1.id > movie2.id:
        movie1, movie2 = movie2, movie1
    if request.method == 'POST':
        selected_movie_id = request.POST.get('selected_movie')
        # Assign `a_points` based on the user's choice
        if selected_movie_id == str(movie1.id):
            a_points = 1
        elif selected_movie_id == "can't_decide":
            a_points = 0.5
        elif selected_movie_id == str(movie2.id):
            a_points = 0
        else:
            # Handle unexpected cases where the selected_movie_id is not one of the given choices
            return redirect('compare_movies')
        # Update or create the LT_Viewer_Ratings entry for this comparison
        rating, created = LT_Viewer_Ratings.objects.update_or_create(
            viewer=viewer,
            film_a=movie1,
            film_b=movie2,
            defaults={'a_points': a_points, 'date': date.today()}
        )
        # Update ratings for both films
        update_viewer_rating(viewer, movie1)
        update_viewer_rating(viewer, movie2)
        return redirect('compare_movies')
    return render(request, 'filmproject/compare_movies.html', {'movie1': movie1, 'movie2': movie2})

def index(request):
    return render( request, 'filmproject/index.html')

@login_required
def mark_as_seen(request, pk):  # Changed film_id to pk
    film = get_object_or_404(Film, id=pk)  # Use pk instead of film_id
    viewer = request.user.viewer  # Assuming Viewer is tied to the logged-in user
    if request.method == 'POST':
        # Check if this viewer has already marked this film as seen
        seen_entry, created = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
        # Mark it as seen
        seen_entry.seen_film = True
        seen_entry.save()
        return redirect('film-detail', pk=pk)
    return redirect('film-detail', pk=pk)

def popular_movies(request):
    return render( request, 'filmproject/popular_movies.html')


@login_required
def profile(request, viewer_id=None):
    user = request.user
    try:
        # Get the viewer based on the ID passed or the current user
        if viewer_id:
            viewer = get_object_or_404(Viewer, id=viewer_id)
        else:
            viewer = user.viewer
    except Viewer.DoesNotExist:
        # Handle the case where the viewer doesn't exist yet
        if Viewer.objects.filter(email=user.email).exists():
            viewer = Viewer.objects.get(email=user.email)
        else:
            try:
                viewer = Viewer.objects.create(user=user, name=user.username, email=user.email)
            except IntegrityError:
                return render(request, 'filmproject/profile_error.html', {'error': 'Email conflict, unable to create viewer.'})

    # Friend request logic
    friend_request = None
    received_friend_request = None
    if request.user.viewer != viewer:
        # Outgoing friend request
        friend_request = FriendRequest.objects.filter(sender=request.user.viewer, receiver=viewer).first()
        # Incoming friend request
        received_friend_request = FriendRequest.objects.filter(sender=viewer, receiver=request.user.viewer, status='pending').first()

    # Get the user's watchlist and seen films
    watchlist = LT_Viewer_Watchlist.objects.filter(viewer=viewer, watchlist=True)
    seen_films = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True)

      # Calculate the dynamic rating for each film
    film_ratings = []
    for film in seen_films:
        # Get total points for the film as film_a
        a_points_sum = LT_Viewer_Ratings.objects.filter(film_a=film, viewer=viewer).aggregate(
             total_a_points=Sum('a_points')
         )['total_a_points'] or 0
         # Get total points for the film as film_b
        b_points_sum = LT_Viewer_Ratings.objects.filter(film_b=film, viewer=viewer).aggregate(
                total_b_points=Sum(F('a_points') * -1 + 1)
        )['total_b_points'] or 0
            # Count total comparisons involving this film
        total_count = LT_Viewer_Ratings.objects.filter(
                models.Q(film_a=film) | models.Q(film_b=film), viewer=viewer
            ).count()
            # Calculate the user rating dynamically
        user_rating = (a_points_sum + b_points_sum) / total_count if total_count > 0 else 0
            # Add to film ratings list
        film_ratings.append({
                'film': film,
                'user_rating': user_rating
            })
        # Sort the films by rating in descending order
        film_ratings.sort(key=lambda x: x['user_rating'], reverse=True)
        # Add to context

    # Notification bell logic: Count the number of pending friend requests for this user
    num_pending_requests = FriendRequest.objects.filter(receiver=user.viewer, status='pending').count()

    # Context for the template
    context = {
        'viewer': viewer,
        'friend_request': friend_request,  # Outgoing friend request
        'received_friend_request': received_friend_request,  # Incoming friend request
        'watchlist': watchlist,
        'seen_films': seen_films,
        'num_pending_requests': num_pending_requests,  # For the notification bell
    }

    return render(request, 'filmproject/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = ViewerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email verification
            user.save()

            # Create the Viewer object linked to the user
            Viewer.objects.create(user=user, name=user.username, email=user.email)

            # Send activation email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('filmproject/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'mountainlionmovies@gmail.com', [to_email])  

            return render(request, 'filmproject/registration_confirm.html')
    else:
        form = ViewerRegistrationForm()
    return render(request, 'filmproject/register.html', {'form': form})

@login_required
def remove_from_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == 'POST':
        seen_entry = get_object_or_404(LT_Viewer_Seen, viewer=viewer, film=film)
        seen_entry.seen_film = False
        seen_entry.save()
        return redirect('film-detail', pk=pk)
    return redirect('film-detail', pk=pk)

@login_required
def remove_from_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == 'POST':
        watchlist_entry = get_object_or_404(LT_Viewer_Watchlist, viewer=viewer, film=film)
        watchlist_entry.watchlist = False
        watchlist_entry.save()
        return redirect('film-detail', pk=pk)
    return redirect('film-detail', pk=pk)

def search_movies(request):
    return render( request, 'filmproject/search_movies.html')

def update_viewer_rating(viewer, film):
    # Sum a_points where the film is in film_a
    film_a_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_a=film).aggregate(
        total_a_points=Sum('a_points', default=0),
        count_a=Count('id')
    )
    total_a_points = film_a_data['total_a_points'] or 0
    count_a = film_a_data['count_a'] or 0

    # Sum (1 - a_points) where the film is in film_b
    film_b_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_b=film).aggregate(
        total_b_points=Sum(Case(
            When(a_points=1, then=0),
            When(a_points=0, then=1),
            When(a_points=0.5, then=0.5),
            default=0,
            output_field=models.DecimalField()
        )),
        count_b=Count('id')
    )
    total_b_points = film_b_data['total_b_points'] or 0
    count_b = film_b_data['count_b'] or 0

    # Calculate total points and total comparisons
    total_points = total_a_points + total_b_points
    total_comparisons = count_a + count_b

    # Calculate and update viewer_rating
    if total_comparisons > 0:
        viewer_rating = total_points / total_comparisons
    else:
        viewer_rating = None  # or set to 0 if you prefer

    # Update the LT_Viewer_Seen entry with the new viewer_rating
    LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(viewer_rating=viewer_rating)

def viewer_list(request):
    viewers = Viewer.objects.all()
    return render(request, 'filmproject/viewer_list.html', {'viewer_list': viewers})


@login_required
def send_friend_request(request, viewer_id):
    """Send a friend request to another viewer."""
    receiver = get_object_or_404(Viewer, id=viewer_id)
    
    # Check if a pending friend request already exists
    if FriendRequest.objects.filter(sender=request.user.viewer, receiver=receiver, status='pending').exists():
        messages.info(request, 'Friend request already sent.')
    else:
        # Create a new friend request
        FriendRequest.objects.create(sender=request.user.viewer, receiver=receiver)
        messages.success(request, f'Friend request sent to {receiver.name}.')
    
    # Redirect to the receiver's profile after sending the friend request
    return redirect('profile_viewer', viewer_id=receiver.id)




@login_required
def accept_friend_request(request, request_id):
    """Accept a friend request."""
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    
    if friend_request.status == 'pending':
        friend_request.accept()  # Custom method to handle acceptance
        messages.success(request, f'You are now friends with {friend_request.sender.name}.')
        
        # Redirect to the sender's profile after accepting the friend request
        return redirect('profile_viewer', viewer_id=friend_request.sender.id)
    
    messages.error(request, 'Invalid request.')
    return redirect('profile', viewer_id=request.user.viewer.id)  # Redirect to the current user's profile



@login_required
def reject_friend_request(request, request_id):
    """Reject a friend request."""
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    
    # Ensure the request is pending before rejecting
    if friend_request.status == 'pending':
        friend_request.reject()  # Custom method to handle rejection
        messages.success(request, f'Friend request from {friend_request.sender.name} rejected.')
        return redirect('profile', viewer_id=friend_request.sender.id)
    
    messages.error(request, 'Invalid request.')
    return redirect('profile', viewer_id=request.user.viewer.id)


@login_required
def remove_friend(request, viewer_id):
    """Remove a friend from the user's friend list."""
    viewer_to_remove = get_object_or_404(Viewer, id=viewer_id)
    viewer = request.user.viewer  # Get the current user's viewer object
    
    # Remove the friend connection bidirectionally
    viewer.friends.remove(viewer_to_remove)
    viewer_to_remove.friends.remove(viewer)
    
    messages.success(request, f'{viewer_to_remove.name} has been removed from your friend list.')
    
    return redirect('profile', viewer_id=request.user.viewer.id)  # Redirect back to the user's profile


@login_required
def manage_friend_requests(request):
    """Display the user's friend requests (both sent and received)."""
    user_viewer = request.user.viewer
    
    # Retrieve received and sent friend requests
    received_friend_requests = FriendRequest.objects.filter(receiver=user_viewer, status='pending')
    sent_friend_requests = FriendRequest.objects.filter(sender=user_viewer)

    context = {
        'received_friend_requests': received_friend_requests,
        'sent_friend_requests': sent_friend_requests,
    }
    
    return render(request, 'filmproject/friend_requests.html', context)


def base_context_processor(request):
    if request.user.is_authenticated:
        num_pending_requests = FriendRequest.objects.filter(receiver=request.user.viewer, status='pending').count()
    else:
        num_pending_requests = 0
    return {'num_pending_requests': num_pending_requests}


# DJANGO REST FRAMEWORK VIEWS
# Film ViewSet
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# Viewer ViewSet
class ViewerViewSet(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer

# Watchlist ViewSet
class LT_Viewer_WatchlistViewSet(viewsets.ModelViewSet):
    queryset = LT_Viewer_Watchlist.objects.all()
    serializer_class = LT_Viewer_WatchlistSerializer

# Seen Films ViewSet
class LT_Viewer_SeenViewSet(viewsets.ModelViewSet):
    queryset = LT_Viewer_Seen.objects.all()
    serializer_class = LT_Viewer_SeenSerializer

# FriendRequest ViewSet
class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

# Cast ViewSet
class LT_Films_CastViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Cast.objects.all()
    serializer_class = LT_Films_CastSerializer

# Companies ViewSet
class LT_Films_CompaniesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Companies.objects.all()
    serializer_class = LT_Films_CompaniesSerializer

# Countries ViewSet
class LT_Films_CountriesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Countries.objects.all()
    serializer_class = LT_Films_CountriesSerializer

# Crew ViewSet
class LT_Films_CrewViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Crew.objects.all()
    serializer_class = LT_Films_CrewSerializer

# Genres ViewSet
class LT_Films_GenresViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Genres.objects.all()
    serializer_class = LT_Films_GenresSerializer

# Keywords ViewSet
class LT_Films_KeywordsViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Keywords.objects.all()
    serializer_class = LT_Films_KeywordsSerializer

# Languages ViewSet
class LT_Films_LanguagesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Languages.objects.all()
    serializer_class = LT_Films_LanguagesSerializer

# Watchlist view for the current user
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def user_watchlist(request):
    viewer = request.user.viewer
    watchlist = LT_Viewer_Watchlist.objects.filter(viewer=viewer, watchlist=True)
    serializer = LT_Viewer_WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)

# Seen films view for the current user
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def user_seen_films(request):
    viewer = request.user.viewer
    seen_films = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True)
    serializer = LT_Viewer_SeenSerializer(seen_films, many=True)
    return Response(serializer.data)