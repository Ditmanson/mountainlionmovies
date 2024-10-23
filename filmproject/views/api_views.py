from ..models import  (
    Film, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, 
    LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Seen, 
    LT_Viewer_Watchlist, FriendRequest
)
from ..serializers import (
    FilmSerializer, ViewerSerializer, LT_Viewer_SeenSerializer, LT_Viewer_WatchlistSerializer,
    FriendRequestSerializer, LT_Films_CastSerializer, LT_Films_CompaniesSerializer, LT_Films_CountriesSerializer,
    LT_Films_CrewSerializer, LT_Films_GenresSerializer, LT_Films_KeywordsSerializer, LT_Films_LanguagesSerializer
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


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