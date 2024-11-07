from datetime import date
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from ..models import  Film, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Seen, LT_Viewer_Watchlist, FriendRequest, Person, LT_Viewer_Ratings
from ..serializers import FilmSerializer, LT_Viewer_RatingsSerializer, ViewerSerializer, LT_Viewer_SeenSerializer, LT_Viewer_WatchlistSerializer, FriendRequestSerializer, LT_Films_CastSerializer, LT_Films_CompaniesSerializer, LT_Films_CountriesSerializer, LT_Films_CrewSerializer, LT_Films_GenresSerializer, LT_Films_KeywordsSerializer, LT_Films_LanguagesSerializer, PersonSerializer

# DJANGO REST FRAMEWORK VIEWS

# Person ViewSet
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

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

# Viewer Ratings ViewSet
class LT_Viewer_RatingsViewSet(ModelViewSet):
    queryset = LT_Viewer_Ratings.objects.all()
    serializer_class = LT_Viewer_RatingsSerializer
    def create(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get('selected_movie')
        movie1_id = request.data.get('movie1_id')
        movie2_id = request.data.get('movie2_id')
        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5
        # Save the rating comparison
        rating_data = {
            'viewer': viewer.id,
            'film_a': movie1_id,
            'film_b': movie2_id,
            'a_points': a_points,
            'b_points': b_points,
            'date': date.today()
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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