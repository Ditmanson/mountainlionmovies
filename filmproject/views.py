import json
import numpy as np
import random
from datetime import date, timedelta
from decimal import Decimal
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db import IntegrityError, models
from django.db.models import Case, Count, F, Q, Sum, When
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.timezone import now
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .forms import ViewerRegistrationForm, ProfileUpdateForm
from .models import FeedEntry, Film, FriendRequest, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Cosine_Similarity, LT_Viewer_Ratings, LT_Viewer_Recommendations, LT_Viewer_Seen, LT_Viewer_Watchlist, Person, Viewer
from .serializers import FilmSerializer, FriendRequestSerializer, LT_Films_CastSerializer, LT_Films_CompaniesSerializer, LT_Films_CountriesSerializer, LT_Films_CrewSerializer, LT_Films_GenresSerializer, LT_Films_KeywordsSerializer, LT_Films_LanguagesSerializer, LT_Viewer_RatingsSerializer, LT_Viewer_SeenSerializer, LT_Viewer_WatchlistSerializer, PersonSerializer, ViewerSerializer
from .tokens import account_activation_token


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "filmproject/film_detail.html"
    def get_viewer(self):
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
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()
                messages.success(request, "Film marked as seen!")
            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(seen_film=False)
                messages.success(request, "Film removed from seen list.")
            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
                watchlist_entry.watchlist = True
                watchlist_entry.save()
                messages.success(request, "Film added to watchlist!")
            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(watchlist=False)
                messages.success(request, "Film removed from watchlist.")
        except ValueError:
            messages.error(request, "Invalid input for rating.")
            return redirect("film-detail", pk=film.id)
        return redirect("film-detail", pk=film.id)

class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    context_object_name = "film_list"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True)
            context["watchlist_films"] = Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True)
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context
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
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(seen_film=False)
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(watchlist=False)
        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

@method_decorator([csrf_exempt, login_required], name='dispatch')
class IndexView(View):
    template_name = "filmproject/index.html"
    def get(self, request, *args, **kwargs):
        """Handles GET requests to render the page with context data."""
        viewer = request.user.viewer
        today = now().date()
        six_months_ago = today - timedelta(days=6 * 30)
        context = {
            "recommendations": LT_Viewer_Recommendations.objects.filter(viewer=viewer).order_by("-recommendation_score"),
            "seen_films": Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True).annotate(viewer_rating=models.F("lt_viewer_seen__viewer_rating")).order_by("-lt_viewer_seen__viewer_rating", "-mlm_rating"),
            "watchlist": Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True).order_by("-mlm_rating", "-vote_average"),
            "new_releases": Film.objects.filter(release_date__lte=today, release_date__gte=six_months_ago).order_by("-release_date", "-mlm_rating", "-vote_average"),
            "coming_soon": Film.objects.filter(release_date__gt=today).order_by("release_date", "-mlm_rating", "-vote_average"),
            "popular_movies": Film.objects.order_by("-mlm_rating", "-vote_average"),
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        """Handles POST requests for adding/removing movies."""
        viewer = request.user.viewer
        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        if not film_id or not action:
            return redirect("index")
        film = get_object_or_404(Film, id=film_id)
        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
            seen_entry.seen_film = True
            seen_entry.save()
            messages.success(request, f"'{film.title}' marked as seen.")
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(seen_film=False)
            messages.success(request, f"'{film.title}' removed from seen list.")
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
            watchlist_entry.watchlist = True
            watchlist_entry.save()
            messages.success(request, f"'{film.title}' added to watchlist.")
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(watchlist=False)
            messages.success(request, f"'{film.title}' removed from watchlist.")
        return redirect("index")

class LT_Films_CastViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Cast.objects.all()
    serializer_class = LT_Films_CastSerializer

class LT_Films_CompaniesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Companies.objects.all()
    serializer_class = LT_Films_CompaniesSerializer

class LT_Films_CountriesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Countries.objects.all()
    serializer_class = LT_Films_CountriesSerializer

class LT_Films_CrewViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Crew.objects.all()
    serializer_class = LT_Films_CrewSerializer

class LT_Films_GenresViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Genres.objects.all()
    serializer_class = LT_Films_GenresSerializer

class LT_Films_KeywordsViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Keywords.objects.all()
    serializer_class = LT_Films_KeywordsSerializer

class LT_Films_LanguagesViewSet(viewsets.ModelViewSet):
    queryset = LT_Films_Languages.objects.all()
    serializer_class = LT_Films_LanguagesSerializer

class LT_Viewer_RatingsViewSet(ModelViewSet):
    queryset = LT_Viewer_Ratings.objects.all()
    serializer_class = LT_Viewer_RatingsSerializer
    def create(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5
        rating_data = {"viewer": viewer.id, "film_a": movie1_id, "film_b": movie2_id, "a_points": a_points, "b_points": b_points, "date": date.today()}
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LT_Viewer_SeenViewSet(viewsets.ModelViewSet):
    queryset = LT_Viewer_Seen.objects.all()
    serializer_class = LT_Viewer_SeenSerializer

class LT_Viewer_WatchlistViewSet(viewsets.ModelViewSet):
    queryset = LT_Viewer_Watchlist.objects.all()
    serializer_class = LT_Viewer_WatchlistSerializer

# class NotificationsViewSet(viewsets.ModelViewSet):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationsSerializer
#     permission_classes = [IsAuthenticated]
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
#     @action(detail=True, methods=["post"])
#     def mark_as_read(self, request, pk=None):
#         try:
#             notification = self.get_object()
#             notification.is_read = True
#             notification.save()
#             return Response({"status": "notification marked as read"}, status=status.HTTP_200_OK)
#         except Notification.DoesNotExist:
#             return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProfileView(LoginRequiredMixin, DetailView):
    model = Viewer
    template_name = "filmproject/profile.html"
    context_object_name = "viewer"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viewer = self.object
        seen_films = (Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True).annotate(user_rating=F('lt_viewer_seen__viewer_rating')).order_by('-lt_viewer_seen__viewer_rating'))
        watchlist = Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True)
        context["seen_films"] = seen_films
        context["watchlist"] = watchlist
        context.update(self.get_friend_requests(viewer))
        return context
    def create_viewer(self, user):
        if Viewer.objects.filter(email=user.email).exists():
            return Viewer.objects.get(email=user.email)
        try:
            return Viewer.objects.create(user=user, name=user.username, email=user.email)
        except IntegrityError:
            self.template_name = "filmproject/profile_error.html"
            return {"error": "Email conflict, unable to create viewer."}
    def get_film_ratings(self, viewer):
        seen_films = Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True)
        film_ratings = []
        for film in seen_films:
            a_points_sum = (LT_Viewer_Ratings.objects.filter(film_a=film, viewer=viewer).aggregate(total_a_points=Sum("a_points"))["total_a_points"] or 0)
            b_points_sum = (LT_Viewer_Ratings.objects.filter(film_b=film, viewer=viewer).aggregate(total_b_points=Sum(F("a_points") * -1 + 1))["total_b_points"] or 0)
            total_count = LT_Viewer_Ratings.objects.filter(Q(film_a=film) | Q(film_b=film), viewer=viewer).count()
            user_rating = ((a_points_sum + b_points_sum) / total_count if total_count > 0 else 0)
            film_ratings.append({"film": film, "user_rating": user_rating})
        film_ratings.sort(key=lambda x: x["user_rating"], reverse=True)
        return film_ratings
    def get_friend_requests(self, viewer):
        user_viewer = self.request.user.viewer
        is_friend = viewer.friends.filter(id=user_viewer.id).exists()
        friend_request_sent = False
        friend_request_received = False
        if user_viewer != viewer:
            friend_request_sent = FriendRequest.objects.filter(sender=user_viewer, receiver=viewer, status="pending").exists()
            friend_request_received = FriendRequest.objects.filter(sender=viewer, receiver=user_viewer, status="pending").exists()
        return {"is_friend": is_friend, "friend_request_sent": friend_request_sent, "friend_request_received": friend_request_received, "num_pending_requests": FriendRequest.objects.filter(receiver=user_viewer, status="pending").count()}
    def get_object(self, queryset=None):
        user = self.request.user
        viewer_id = self.kwargs.get("viewer_id")
        if viewer_id:
            return get_object_or_404(Viewer, id=viewer_id)
        try:
            return user.viewer
        except Viewer.DoesNotExist:
            return self.create_viewer(user)

class ViewerDetailView(generic.DetailView):
    model = Viewer
    def get(self, request, *args, **kwargs):
        viewer = self.get_object()
        return redirect("profile_viewer", viewer_id=viewer.id)

class ViewerListView(LoginRequiredMixin, ListView):
    model = Viewer
    template_name = "filmproject/viewer_list.html"
    context_object_name = "viewer_list"
    def get_friend_requests(self, viewer):
        user_viewer = self.request.user.viewer
        is_friend = viewer.friends.filter(id=user_viewer.id).exists()
        friend_request_sent = FriendRequest.objects.filter(sender=user_viewer, receiver=viewer, status="pending").exists()
        friend_request_received = FriendRequest.objects.filter(sender=viewer, receiver=user_viewer, status="pending").exists()
        print(f"Viewer: {viewer.id} | is_friend: {is_friend} | friend_request_sent: {friend_request_sent} | friend_request_received: {friend_request_received}")
        return {"is_friend": is_friend, "friend_request_sent": friend_request_sent, "friend_request_received": friend_request_received}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_viewer = self.request.user.viewer
        similarity_scores = {}
        similarities = LT_Viewer_Cosine_Similarity.objects.filter(Q(viewer_1=user_viewer) | Q(viewer_2=user_viewer))
        for sim in similarities:
            if sim.viewer_1 == user_viewer:
                similarity_scores[sim.viewer_2.id] = Decimal(sim.cosine_similarity)
            else:
                similarity_scores[sim.viewer_1.id] = Decimal(sim.cosine_similarity)
        context["similarity_scores"] = similarity_scores
        viewer_list = list(Viewer.objects.exclude(id=user_viewer.id))
        viewer_list.sort(key=lambda viewer: similarity_scores.get(viewer.id, 0), reverse=True)
        context["viewer_list"] = viewer_list
        context["received_friend_requests"] = FriendRequest.objects.filter(receiver=user_viewer, status="pending")
        context["sent_friend_requests"] = FriendRequest.objects.filter(sender=user_viewer, status="pending")
        context["num_pending_requests"] = context["received_friend_requests"].count()
        friendship_status = {viewer.id: self.get_friend_requests(viewer) for viewer in Viewer.objects.exclude(id=user_viewer.id)}
        context["friendship_status"] = friendship_status
        return context
    def get_queryset(self):
        return Viewer.objects.all()

class ViewerViewSet(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    if friend_request.status == "pending":
        friend_request.accept()
        messages.success(request, f"You are now friends with {friend_request.sender.name}.")
        return redirect("profile_viewer", viewer_id=friend_request.sender.id)
    messages.error(request, "Invalid request.")
    return redirect("profile", viewer_id=request.user.viewer.id)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("index")
    return render(request, "filmproject/account_activation_invalid.html", {"uidb64": urlsafe_base64_encode(force_bytes(user.pk))})

@login_required
def add_to_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(viewer=viewer, film=film)
        watchlist_entry.watchlist = True
        watchlist_entry.save()
    return redirect("film-detail", pk=pk)

def base_context_processor(request):
    if request.user.is_authenticated:
        num_pending_requests = FriendRequest.objects.filter(receiver=request.user.viewer, status="pending").count()
    else:
        num_pending_requests = 0
    return {"num_pending_requests": num_pending_requests}

def calculate_cosine_similarity():
    viewers = list(Viewer.objects.all())
    for i, viewer_1 in enumerate(viewers):
        for j, viewer_2 in enumerate(viewers):
            if i >= j:
                continue
            ratings_1 = dict(LT_Viewer_Seen.objects.filter(viewer=viewer_1, seen_film=True).values_list("film_id", "viewer_rating"))
            ratings_2 = dict(LT_Viewer_Seen.objects.filter(viewer=viewer_2, seen_film=True).values_list("film_id", "viewer_rating"))
            common_films = set(ratings_1.keys()) & set(ratings_2.keys())
            if common_films:
                vector_1 = np.array([ratings_1[film] for film in common_films])
                vector_2 = np.array([ratings_2[film] for film in common_films])
                norm_1 = np.linalg.norm(vector_1)
                norm_2 = np.linalg.norm(vector_2)
                similarity_score = (np.dot(vector_1, vector_2) / (norm_1 * norm_2) if norm_1 and norm_2 else 0.0)
            else:
                similarity_score = 0.0
            LT_Viewer_Cosine_Similarity.objects.update_or_create(viewer_1 = viewer_1, viewer_2 = viewer_2, defaults = {"cosine_similarity": similarity_score})
            print(f"Updated similarity for {viewer_1.name} and {viewer_2.name}: {similarity_score}")

def calculate_mlm_ratings():
    maximum_rating = Decimal("1.0")
    for film in Film.objects.all():
        viewer_ratings_sum = (LT_Viewer_Seen.objects.filter(film = film, viewer_rating__isnull = False, seen_film = True).aggregate(total=Sum("viewer_rating"))["total"] or Decimal("0"))
        watchlist_count = LT_Viewer_Watchlist.objects.filter(film = film, watchlist = True).count()
        film.mlm_rating = viewer_ratings_sum + (Decimal("0.5") * watchlist_count)
        if maximum_rating < film.mlm_rating:
            maximum_rating = film.mlm_rating
        film.save()
    for film in Film.objects.all():
        film.mlm_rating = film.mlm_rating / maximum_rating # Normalize the mlm_rating by dividing by the movie with the maximum rating
        film.save()

# @login_required
# @require_POST
# def comment_entry(request, entry_id):
#     entry = get_object_or_404(FeedEntry, id=entry_id)
#     data = json.loads(request.body)
#     comment = Comment.objects.create(feed_entry=entry, user=request.user, content=data["content"])
#     if entry.user != request.user:
#         Notification.objects.create(user=entry.user, feed_entry=entry, notification_type="comment")
#     return JsonResponse({"success": True, "user": comment.user.username, "content": comment.content,})

@login_required
def compare_movies(request):
    viewer = request.user.viewer
    seen_movies = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film", flat=True)
    if seen_movies.count() < 2:
        return render(request, "filmproject/compare_movies.html", {"message": "You need to mark at least two movies as seen to start comparing."})
    least_rated_movie = (Film.objects.filter(id__in=seen_movies).annotate(total_count=Count('film_a__id', filter=Q(film_a__viewer=viewer)) + Count('film_b__id', filter=Q(film_b__viewer=viewer))).order_by('total_count').first())
    if least_rated_movie:
        movie1 = least_rated_movie
    else:
        movie1 = random.choice(Film.objects.filter(id__in=seen_movies))
    compared_movies = set(LT_Viewer_Ratings.objects.filter(Q(film_a=movie1) | Q(film_b=movie1), viewer=viewer).values_list('film_a', 'film_b').distinct())
    compared_movies = {movie for pair in compared_movies for movie in pair}
    movie2_candidates = Film.objects.filter(id__in=seen_movies).exclude(id__in=compared_movies)
    if movie2_candidates.exists():
        movie2 = random.choice(movie2_candidates)
    else:
        movie2 = Film.objects.get(id=random.choice([id for id in seen_movies if id != movie1.id]))
    if movie1.id > movie2.id:
        movie1, movie2 = movie2, movie1
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse(
            {"movie1": {"id": movie1.id, "title": movie1.title, "poster_path": f"https://image.tmdb.org/t/p/w300/{movie1.poster_path}", "overview": movie1.overview,}, "movie2": {"id": movie2.id, "title": movie2.title, "poster_path": f"https://image.tmdb.org/t/p/w300/{movie2.poster_path}", "overview": movie2.overview}})
    return render(request, "filmproject/compare_movies.html", {"movie1": movie1, "movie2": movie2})

def database_cleanup():
    print("Database cleanup placeholder.")

def delete_invalid_viewer_ratings():
    all_viewers = Viewer.objects.all()
    for viewer in all_viewers:
        seen_films = list(LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film_id", flat=True))
        if not seen_films:
            continue
        all_ratings = LT_Viewer_Ratings.objects.filter(viewer=viewer)
        invalid_ratings = [rating.id for rating in all_ratings if rating.film_a_id not in seen_films or rating.film_b_id not in seen_films]
        if invalid_ratings:
            deleted_count = LT_Viewer_Ratings.objects.filter(id__in=invalid_ratings).delete()[0]

def feed_entries(request):
    page = request.GET.get("page", 1)
    user = request.user
    try:
        friends_viewers = user.viewer.friends.all()
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = ([])  # No friends attribute; proceed with an empty friends list
    if friends_users:
        entries = FeedEntry.objects.filter(user__in=[user, *friends_users]).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)
    data = [{"id": entry.id, "user": entry.user.username, "action": entry.action, "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "likes": entry.likes.count(), "comments": [{"user": c.user.username, "content": c.content} for c in entry.comments.all()], "movie": {"title": entry.movie.title, "tmdb_id": entry.movie.tmdb_id, "poster_path": entry.movie.poster_path,}}for entry in page_obj]
    return JsonResponse(data, safe=False)

def feed_entry_detail(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)
    data = {"id": entry.id, "user": entry.user.username, "action": entry.action, "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "likes": entry.likes.count(), "comments": [{"user": c.user.username, "content": c.content} for c in entry.comments.all()], "movie": {"title": entry.movie.title, "tmdb_id": entry.movie.tmdb_id, "poster_path": entry.movie.poster_path,}}
    return render(request, "filmproject/feed_entry_detail.html", {"entry": data})

def feed_page(request):
    return render(request, "filmproject/social_feed.html")

def film_list_api(request):
    films = Film.objects.all().order_by("-mlm_rating")
    paginator = Paginator(films, 20)  # Adjust items per page
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    film_data = [{"id": film.id, "title": film.title, "poster_path": film.poster_path, "mlm_rating": float(film.mlm_rating)} for film in page_obj]
    return JsonResponse({"films": film_data, "has_next": page_obj.has_next()})



# @login_required
# @require_POST
# def like_entry(request, entry_id):
#     entry = get_object_or_404(FeedEntry, id=entry_id)
#     Like.objects.get_or_create(feed_entry=entry, user=request.user)
#     likes_count = entry.likes.count()
#     if entry.user != request.user:
#         Notification.objects.create(user=entry.user, feed_entry=entry, notification_type="like")
#     return JsonResponse({"success": True, "likes": likes_count})

def load_recommendations(request):
    viewer = request.user.viewer
    recommendations = LT_Viewer_Recommendations.objects.filter(viewer=viewer).order_by('-recommendation_score')
    paginator = Paginator(recommendations, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    results = [{
        "id": rec.film.id,
        "title": rec.film.title,
        "poster_path": rec.film.poster_path,
        "get_absolute_url": rec.film.get_absolute_url(),
        "description": rec.film.overview
    } for rec in page_obj]
    return JsonResponse({"results": results})

def load_watchlist(request):
    viewer = request.user.viewer if request.user.is_authenticated else None
    watchlist = LT_Viewer_Watchlist.objects.filter(viewer=viewer).order_by('-film__mlm_rating') if viewer else []
    page_number = request.GET.get('page', 1)
    paginator = Paginator(watchlist, 10)  # 10 items per page
    page_obj = paginator.get_page(page_number)
    return render(request, 'filmproject/snippets/watchlist_snippet.html', {'watchlist': page_obj})

def load_new_movies(request):
    new_movies = Film.objects.order_by('-release_date')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(new_movies, 10)  # 10 items per page
    page_obj = paginator.get_page(page_number)
    return render(request, 'filmproject/snippets/new_movies_snippet.html', {'new_movies': page_obj})

def load_popular_movies(request):
    popular_movies = Film.objects.order_by('-mlm_rating')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(popular_movies, 10)  # 10 items per page
    page_obj = paginator.get_page(page_number)
    return render(request, 'filmproject/snippets/popular_movies_snippet.html', {'popular_movies': page_obj})

@staff_member_required
def manual_calculate_cosine_similarity(request):
    if request.method == "POST":
        try:
            calculate_cosine_similarity()
            messages.success(request, "Cosine similarity recalculated successfully.")
        except Exception as e:
            messages.error(request, f"Error recalculating cosine similarity: {e}")
    return redirect('staff_dashboard')

@staff_member_required
def manual_database_cleanup(request):
    if request.method == "POST":
        try:
            database_cleanup()
            messages.success(request, "Database cleanup completed successfully.")
        except Exception as e:
            messages.error(request, f"Error during database cleanup: {e}")
    return redirect('staff_dashboard')

@staff_member_required
def manual_recalculate_recommendations(request):
    if request.method == "POST":
        try:
            LT_Viewer_Recommendations.objects.all().delete()
            viewers = Viewer.objects.all()
            for viewer in viewers:
                seen_movies = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film", flat=True)
                similar_viewers = LT_Viewer_Cosine_Similarity.objects.filter(Q(viewer_1=viewer) | Q(viewer_2=viewer)).exclude(cosine_similarity__isnull=True).order_by('-cosine_similarity')
                film_scores = {}
                for sim in similar_viewers:
                    other_viewer = sim.viewer_2 if sim.viewer_1 == viewer else sim.viewer_1
                    other_seen_movies = LT_Viewer_Seen.objects.filter(viewer=other_viewer, seen_film=True).exclude(film__in=seen_movies)
                    for movie_entry in other_seen_movies:
                        film = movie_entry.film
                        viewer_rating = movie_entry.viewer_rating or 0.5
                        film_scores[film] = film_scores.get(film, 0) + float(sim.cosine_similarity) * float(viewer_rating)
                for film, score in sorted(film_scores.items(), key=lambda x: -x[1])[:10]:
                    LT_Viewer_Recommendations.objects.create(viewer=viewer, film=film, recommendation_score=round(score, 1))
            messages.success(request, "Movie recommendations have been recalculated successfully.")
        except Exception as e:
            messages.error(request, f"Error recalculating recommendations: {e}")
        return redirect('staff_dashboard')

@staff_member_required
def manual_update_film_ratings(request):
    try:
        update_film_ratings()
        return JsonResponse({"success": True, "message": "Film ratings updated successfully."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})

@staff_member_required
def manual_update_film_ratings(request):
    if request.method == "POST":
        try:
            update_film_ratings()
            messages.success(request, "Film ratings updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating film ratings: {e}")
    return redirect('staff_dashboard')

@login_required
def mark_as_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(viewer=viewer, film=film)
        seen_entry.seen_film = True
        seen_entry.viewer_rating = seen_entry.viewer_rating or 0.5
        seen_entry.save()
    return redirect("film-detail", pk=pk)

def register(request):
    if request.method == "POST":
        form = ViewerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your account."
            message = render_to_string("filmproject/account_activation_email.html", {"user": user, "domain": current_site.domain, "uidb64": urlsafe_base64_encode(force_bytes(user.pk)), "token": account_activation_token.make_token(user)})
            to_email = form.cleaned_data.get("email")
            send_mail(mail_subject, message, "mountainlionmovies@gmail.com", [to_email])
            return render(request, "filmproject/registration_confirm.html", {"uidb64": urlsafe_base64_encode(force_bytes(user.pk))})
    else:
        form = ViewerRegistrationForm()
    return render(request, "filmproject/register.html", {"form": form})

@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    if friend_request.status == "pending":
        friend_request.reject()
        messages.success(request, f"Friend request from {friend_request.sender.name} rejected.")
        return redirect("profile", viewer_id=friend_request.sender.id)
    messages.error(request, "Invalid request.")
    return redirect("profile", viewer_id=request.user.viewer.id)

@login_required
def remove_friend(request, viewer_id):
    viewer_to_remove = get_object_or_404(Viewer, id=viewer_id)
    viewer = request.user.viewer
    viewer.friends.remove(viewer_to_remove)
    viewer_to_remove.friends.remove(viewer)
    messages.success(request, f"{viewer_to_remove.name} has been removed from your friend list.")
    return redirect("profile")

@login_required
def remove_from_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(seen_film=False)
    return redirect("film-detail", pk=pk)

@login_required
def remove_from_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(watchlist=False)
    return redirect("film-detail", pk=pk)

def render_invalid_activation_page(request):
    return render(request, "filmproject/account_activation_invalid.html")

def resend_activation_email(request, uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        if not user.is_active:
            current_site = get_current_site(request)
            mail_subject = "Activate your account."
            message = render_to_string("filmproject/account_activation_email.html", {"user": user, "domain": current_site.domain, "uidb64": uidb64, "token": account_activation_token.make_token(user)})
            to_email = user.email
            send_mail(mail_subject, message, "mountainlionmovies@gmail.com", [to_email])
            return render(request, "filmproject/registration_confirm.html", {"resend_success": True, "uidb64": uidb64})
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    return render(request, "filmproject/registration_confirm.html", {"resend_success": False, "uidb64": uidb64})

def search_movies(request):
    return render(request, "filmproject/search_movies.html")

def search_results(request):
    q = request.GET
    search_query = request.GET.get("q")
    search_filter = request.GET.get("filter")
    movie_results = None
    viewer_results = None
    if search_query:
        if search_filter == "movie":
            movie_results = Film.objects.filter(title__icontains=search_query).order_by("title")
        elif search_filter == "viewer":
            viewer_results = Viewer.objects.filter(name__icontains=search_query).order_by("name")
        else:
            movie_results = Film.objects.filter(title__icontains=search_query).order_by("title")
            viewer_results = Viewer.objects.filter(name__icontains=search_query).order_by("name")
    print("QUERY:", search_query, "\n")
    print("Q:", q, "\n")
    print("MOVIE RESULTS:", movie_results, "\n")
    print("VIEWER RESULTS:", viewer_results, "\n")
    return render(request, "filmproject/search_results.html", {"query": search_query, "filter": search_filter, "movie_results": movie_results, "viewer_results": viewer_results})

@login_required
def send_friend_request(request, viewer_id):
    receiver = get_object_or_404(Viewer, id=viewer_id)
    if FriendRequest.objects.filter(sender=request.user.viewer, receiver=receiver, status="pending").exists():
        messages.info(request, "Friend request already sent.")
    else:
        FriendRequest.objects.create(sender=request.user.viewer, receiver=receiver)
        messages.success(request, f"Friend request sent to {receiver.name}.")
    return redirect("profile_viewer", viewer_id=receiver.id)

@staff_member_required
def staff_dashboard(request):
    return render(request, 'filmproject/staff_dashboard.html')

def submit_movie_selection(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            selected_movie_id = str(data.get("selected_movie"))
            movie1_id = str(data.get("movie1_id"))
            movie2_id = str(data.get("movie2_id"))
            if selected_movie_id not in [movie1_id, movie2_id, "can't_decide"]:
                return JsonResponse({"error": "Invalid selection"}, status=400)
            viewer = request.user.viewer
            movie1 = get_object_or_404(Film, id=movie1_id)
            movie2 = get_object_or_404(Film, id=movie2_id)
            if selected_movie_id == str(movie1_id):
                a_points = 1
                b_points = 0
            elif selected_movie_id == str(movie2_id):
                a_points = 0
                b_points = 1
            else:
                a_points = 0.5
                b_points = 0.5
            rating, created = LT_Viewer_Ratings.objects.update_or_create(viewer=viewer, film_a=movie1, film_b=movie2, defaults={"a_points": a_points, "b_points": b_points, "date": date.today()})
            update_viewer_rating(viewer, movie1)
            update_viewer_rating(viewer, movie2)
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"error": "Failed to submit selection"}, status=500)
        
def update_film_ratings():
    print("Starting film ratings update...")
    delete_invalid_viewer_ratings()
    calculate_cosine_similarity()
    calculate_mlm_ratings()
    print("Film ratings update completed.")

@login_required
def update_profile(request, pk):
    viewer = get_object_or_404(Viewer, id=pk)
    if request.user != viewer.user:
        return render(request, "filmproject/permission_denied.html", {"message": "You are not allowed to update this profile."})
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=viewer)
        if form.is_valid():
            user = form.save(commit=False)
            print("\nREQUEST POST:", request.POST, "\n")
            print("\nREQUEST FILES", request.FILES, "\n")
            print("\nUSER FORM", user, "\n")
            user.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=viewer)
    return render(request, "filmproject/profile_update.html", {"form": form, "pk": pk})

def update_viewer_rating(viewer, film):
    film_a_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_a=film).aggregate(total_a_points=Sum("a_points", default=0), count_a=Count("id"))
    total_a_points = film_a_data["total_a_points"] or 0
    count_a = film_a_data["count_a"] or 0
    film_b_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_b=film).aggregate(total_b_points=Sum(Case(When(a_points=1, then=0), When(a_points=0, then=1), When(a_points=0.5, then=0.5), default=0, output_field=models.DecimalField())), count_b=Count("id"))
    total_b_points = film_b_data["total_b_points"] or 0
    count_b = film_b_data["count_b"] or 0
    total_points = total_a_points + total_b_points
    total_comparisons = count_a + count_b
    viewer_rating = (total_points / total_comparisons if total_comparisons > 0 else 0.5)
    LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(viewer_rating=viewer_rating)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_seen_films(request):
    viewer = request.user.viewer
    seen_films = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True)
    serializer = LT_Viewer_SeenSerializer(seen_films, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_watchlist(request):
    viewer = request.user.viewer
    watchlist = LT_Viewer_Watchlist.objects.filter(viewer=viewer, watchlist=True)
    serializer = LT_Viewer_WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)