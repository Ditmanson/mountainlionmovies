import random
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import LT_Viewer_Ratings, LT_Viewer_Seen, Film
from ..serializers import FilmSerializer, LTViewerRatingsSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comparison_movies(request):
    viewer = request.user.viewer
    seen_movies = LT_Viewer_Ratings.objects.filter(viewer=viewer).values_list('film_a', 'film_b')
    unique_movie_ids = {movie for pair in seen_movies for movie in pair}
    if len(unique_movie_ids) < 2:
        return Response({'error': 'Not enough movies in seen list'}, status=400)
    movie1, movie2 = random.sample(list(unique_movie_ids), 2)
    movie1 = Film.objects.get(id = movie1)
    movie2 = Film.objects.get(id  =movie2)
    serializer1 = FilmSerializer(movie1)
    serializer2 = FilmSerializer(movie2)
    return Response({'movie1': serializer1.data, 'movie2': serializer2.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_movie_selection(request):
    data = request.data
    selected_movie_id = data.get('selected_movie')
    movie1_id = data.get('movie1_id')
    movie2_id = data.get('movie2_id')
    if selected_movie_id not in [str(movie1_id), str(movie2_id), "can't_decide"]:
        return Response({'error': 'Invalid selection'}, status=400)
    viewer = request.user.viewer
    movie1 = Film.objects.get(id=movie1_id)
    movie2 = Film.objects.get(id=movie2_id)
    a_points = b_points = 0
    if selected_movie_id == str(movie1.id):
        a_points = 1
    elif selected_movie_id == str(movie2.id):
        b_points = 1
    elif selected_movie_id == "can't_decide":
        a_points = b_points = 0.5
    rating, created = LT_Viewer_Ratings.objects.update_or_create(
        viewer=viewer,
        film_a=movie1,
        film_b=movie2,
        defaults={'a_points': a_points, 'b_points': b_points, 'date': date.today()}
    )
    return Response({'success': True, 'rating': LTViewerRatingsSerializer(rating).data})


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
        return redirect('compare_movies')
    return render(request, 'filmproject/compare_movies.html', {'movie1': movie1, 'movie2': movie2})
