from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from ..models import  Film, LT_Viewer_Seen, LT_Viewer_Watchlist, Viewer


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'filmproject/film_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        
        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context['is_seen'] = viewer.has_seen_film(film)
            context['is_in_watchlist'] = viewer.is_in_watchlist(film)
        else:
            context['is_seen'] = False
            context['is_in_watchlist'] = False
        
        context['film'] = film
        context['mlm_rating'] = film.mlm_rating
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")
        
        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get('action')
        rating = request.POST.get('rating')
        
        try:
            # Handle the Mark as Seen / Remove from Seen actions
            if action == 'mark_as_seen':
                seen_entry, created = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
                seen_entry.seen_film = True
                if rating:  # Only update if a rating is provided
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()
            
            elif action == 'remove_from_seen':
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(seen_film=False)
            
            # Handle the Add to Watchlist / Remove from Watchlist actions
            elif action == 'add_to_watchlist':
                watchlist_entry, created = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
                watchlist_entry.watchlist = True
                watchlist_entry.save()
            
            elif action == 'remove_from_watchlist':
                LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(watchlist=False)
            
        except ValueError:
            # Handle invalid rating input, redirect or inform the user as needed
            return redirect('film-detail', pk=film.id)
        
        # Redirect back to the film detail page
        return redirect('film-detail', pk=film.id)



class FilmListView(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'film_list'
    paginate_by = 20
    def get_queryset(self):
        return Film.objects.all().order_by('-mlm_rating') # Sort films by mlm_rating in descending order
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
def mark_as_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer

    if request.method == 'POST':
        # Get or create the LT_Viewer_Seen entry
        seen_entry, created = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
        
        # Mark the film as seen
        seen_entry.seen_film = True

        # Update the viewer rating if desired, or remove this line if not needed
        seen_entry.viewer_rating = seen_entry.viewer_rating or 0.5  # Example rating

        # Save to trigger `save()` method, which updates `film.mlm_rating`
        seen_entry.save()

    return redirect('film-detail', pk=pk)


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

@login_required
def search_movies(request):
    return render( request, 'filmproject/search_movies.html')