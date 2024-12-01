import json
import random
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Case, Count, F, Q, Sum, When
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ..models import Film, LT_Viewer_Ratings, LT_Viewer_Seen


@login_required
def compare_movies(request):
    viewer = request.user.viewer
    seen_movies = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film", flat=True)
    if seen_movies.count() < 2:
        return render(request, "filmproject/compare_movies.html", {"message": "You need to mark at least two movies as seen to start comparing."})
    least_rated_movie = (
        Film.objects.filter(id__in=seen_movies)
        .annotate(
            total_count=Count(
                'film_a__id',  # Count occurrences as film_a
                filter=Q(film_a__viewer=viewer)
            )
            + Count(
                'film_b__id',  # Count occurrences as film_b
                filter=Q(film_b__viewer=viewer)
            )
        )
        .order_by('total_count')  # Sort by total count
        .first()
    )
    if least_rated_movie:
        movie1 = least_rated_movie
    else:
        movie1 = random.choice(Film.objects.filter(id__in=seen_movies))
    
    compared_movies = set(
        LT_Viewer_Ratings.objects.filter(
            Q(film_a=movie1) | Q(film_b=movie1),
            viewer=viewer
        ).values_list('film_a', 'film_b').distinct()
    )
    compared_movies = {movie for pair in compared_movies for movie in pair}

    movie2_candidates = Film.objects.filter(id__in=seen_movies).exclude(id__in=compared_movies)
    if movie2_candidates.exists():
        movie2 = random.choice(movie2_candidates)
    else:
        # Fallback to a random movie if all have been compared
        movie2 = Film.objects.get(id=random.choice([id for id in seen_movies if id != movie1.id]))

    if movie1.id > movie2.id:
        movie1, movie2 = movie2, movie1

    # Check if the request is AJAX to send JSON response
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse(
            {
                "movie1": {
                    "id": movie1.id,
                    "title": movie1.title,
                    "poster_path": f"https://image.tmdb.org/t/p/w300/{movie1.poster_path}",
                    "overview": movie1.overview,
                },
                "movie2": {
                    "id": movie2.id,
                    "title": movie2.title,
                    "poster_path": f"https://image.tmdb.org/t/p/w300/{movie2.poster_path}",
                    "overview": movie2.overview,
                },
            }
        )
    return render(request, "filmproject/compare_movies.html", {"movie1": movie1, "movie2": movie2})


def submit_movie_selection(request):
    if request.method == "POST":
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)

            # Debugging output
            print("Received data (pre-conversion):", data)

            selected_movie_id = str(data.get("selected_movie"))
            movie1_id = str(data.get("movie1_id"))
            movie2_id = str(data.get("movie2_id"))

            # Debugging output
            print("Received data (after conversion to string):", data)

            # Ensure valid selection
            if selected_movie_id not in [movie1_id, movie2_id, "can't_decide"]:
                # Log if selection data is invalid
                print("Invalid selection data")
                return JsonResponse({"error": "Invalid selection"}, status=400)

            # Get the viewer from the request's user
            viewer = request.user.viewer
            movie1 = get_object_or_404(Film, id=movie1_id)
            movie2 = get_object_or_404(Film, id=movie2_id)

            # Determine points to assign based on selection
            if selected_movie_id == str(movie1_id):
                a_points = 1
                b_points = 0
            elif selected_movie_id == str(movie2_id):
                a_points = 0
                b_points = 1
            else:  # "can't decide"
                a_points = 0.5
                b_points = 0.5

            # Update or create the LT_Viewer_Ratings entry for this comparison
            rating, created = LT_Viewer_Ratings.objects.update_or_create(
                viewer=viewer,
                film_a=movie1,
                film_b=movie2,
                defaults={
                    "a_points": a_points,
                    "b_points": b_points,
                    "date": date.today(),
                },
            )

            # Confirm that the points were updated correctly
            print("Updated points:", rating.a_points, rating.b_points)

            update_viewer_rating(viewer, movie1)
            update_viewer_rating(viewer, movie2)

            return JsonResponse({"success": True})

        except Exception as e:
            print("Error in submit_movie_selection:", e)
            return JsonResponse(
                {"error": "Failed to submit selection"}, status=500
            )


def update_viewer_rating(viewer, film):
    # Sum a_points where the film is in film_a
    film_a_data = LT_Viewer_Ratings.objects.filter(
        viewer=viewer, film_a=film
    ).aggregate(total_a_points=Sum("a_points", default=0), count_a=Count("id"))
    total_a_points = film_a_data["total_a_points"] or 0
    count_a = film_a_data["count_a"] or 0

    film_b_data = LT_Viewer_Ratings.objects.filter(
        viewer=viewer, film_b=film
    ).aggregate(
        total_b_points=Sum(
            Case(
                When(a_points=1, then=0),
                When(a_points=0, then=1),
                When(a_points=0.5, then=0.5),
                default=0,
                output_field=models.DecimalField(),
            )
        ),
        count_b=Count("id"),
    )
    total_b_points = film_b_data["total_b_points"] or 0
    count_b = film_b_data["count_b"] or 0

    # Calculate total points and total comparisons
    total_points = total_a_points + total_b_points
    total_comparisons = count_a + count_b

    # Calculate and update viewer_rating
    viewer_rating = (
        total_points / total_comparisons if total_comparisons > 0 else 0.5
    )

    # Update the LT_Viewer_Seen entry with the new viewer_rating
    LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
        viewer_rating=viewer_rating
    )
