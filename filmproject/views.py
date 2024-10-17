from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView
from .forms import ViewerRegistrationForm
from .models import Collection, Company, Country, Film, Genre, Keyword, Language, Person, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Ratings, LT_Viewer_Seen, LT_Viewer_Watchlist
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .tokens import account_activation_token

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
        return context

@method_decorator(login_required, name='dispatch')
class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'film_list'
    paginate_by = 20

    def post(self, request, *args, **kwargs):
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
        return redirect(f"{reverse_lazy('film-list')}?page={page_number}")
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
    template_name = 'filmproject/viewer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        user = self.request.user
        try:
            # Try to access the viewer associated with the logged-in user
            viewer = user.viewer
        except Viewer.DoesNotExist:
            # If no Viewer exists, create one for the user
            viewer = Viewer.objects.create(user=user, name=user.username, email=user.email)
    
        # Get the films in the viewer's watchlist
        watchlist = Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True)
    
        # Get the films the viewer has marked as seen
        seen_films = Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True)
    
        # Add the lists and the viewer to the context
        context['watchlist'] = watchlist
        context['seen_films'] = seen_films
        context['viewer'] = viewer
    
        return context



class ViewerListView(generic.ListView):
    model = Viewer

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
def profile(request):
    user = request.user
    try:
        viewer = user.viewer  # Try to get the related Viewer object
    except Viewer.DoesNotExist:
        # Check if a Viewer with this email already exists
        if Viewer.objects.filter(email=user.email).exists():
            viewer = Viewer.objects.get(email=user.email)
        else:
            try:
                # Create a new Viewer object if it doesn't exist and email is unique
                viewer = Viewer.objects.create(user=user, name=user.username, email=user.email)
            except IntegrityError:
                # Handle IntegrityError in case there's still a conflict
                return render(request, 'filmproject/profile_error.html', {'error': 'Email conflict, unable to create viewer.'})
    
    return render(request, 'filmproject/profile.html', {'viewer': viewer})


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

def viewer_list(request):
    viewers = Viewer.objects.all()
    return render(request, 'filmproject/viewer_list.html', {'viewer_list': viewers})