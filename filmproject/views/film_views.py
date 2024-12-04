from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from ..models import Film, LT_Viewer_Recommendations, LT_Viewer_Seen, LT_Viewer_Watchlist, Viewer


from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "filmproject/film_detail.html"

    def get_viewer(self):
        """Helper to get or create the Viewer object."""
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            return viewer
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        viewer = self.get_viewer()

        if viewer:
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer = self.get_viewer()
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()
                messages.success(request, "Film marked as seen!")

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )
                messages.success(request, "Film removed from seen list.")

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()
                messages.success(request, "Film added to watchlist!")

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)
                messages.success(request, "Film removed from watchlist.")

        except ValueError:
            messages.error(request, "Invalid input for rating.")
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)



class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    context_object_name = "film_list"
    paginate_by = 20

    def get_queryset(self):
        return Film.objects.all().order_by("-mlm_rating")

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context


@login_required
def add_to_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
            viewer=viewer, film=film
        )
        watchlist_entry.watchlist = True
        watchlist_entry.save()
    return redirect("film-detail", pk=pk)


def index(request):
    recommendations = []
    if request.user.is_authenticated:
        recommendations = LT_Viewer_Recommendations.objects.filter(
            viewer=request.user.viewer
        ).order_by('-recommendation_score')
    return render(request, "filmproject/index.html", {"recommendations": recommendations})


@login_required
def mark_as_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer

    if request.method == "POST":
        seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
            viewer=viewer, film=film
        )
        seen_entry.seen_film = True
        seen_entry.viewer_rating = seen_entry.viewer_rating or 0.5
        seen_entry.save()

    return redirect("film-detail", pk=pk)


@login_required
def remove_from_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
            seen_film=False
        )
    return redirect("film-detail", pk=pk)


@login_required
def remove_from_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(
            watchlist=False
        )
    return redirect("film-detail", pk=pk)


def search_movies(request):
    return render(request, "filmproject/search_movies.html")
