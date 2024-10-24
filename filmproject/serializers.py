from rest_framework import serializers
from .models import (
    Film, Viewer, LT_Viewer_Seen, LT_Viewer_Watchlist, FriendRequest, 
    LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, 
    LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages
)

# Film Serializer
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__' 

# Viewer Serializer
class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['id', 'name', 'email', 'profile_picture']

class LT_Viewer_SeenSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)  # Nested Film serializer to show film details
    
    class Meta:
        model = LT_Viewer_Seen
        fields = ['id', 'film', 'seen_film']  # Exclude 'viewer' from the fields

class LT_Viewer_WatchlistSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)  # Nested Film serializer to show film details
    
    class Meta:
        model = LT_Viewer_Watchlist
        fields = ['id', 'film', 'watchlist']  # Exclude 'viewer' from the fields

# FriendRequest Serializer
class FriendRequestSerializer(serializers.ModelSerializer):
    sender = ViewerSerializer(read_only=True)
    receiver = ViewerSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'sender', 'receiver', 'status', 'created_at']

# LT_Films_Cast Serializer
class LT_Films_CastSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = LT_Films_Cast
        fields = ['id', 'film', 'person', 'character', 'credit_id', 'order']

# LT_Films_Companies Serializer
class LT_Films_CompaniesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = LT_Films_Companies
        fields = ['id', 'film', 'company']

# LT_Films_Countries Serializer
class LT_Films_CountriesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = LT_Films_Countries
        fields = ['id', 'film', 'country']

# LT_Films_Crew Serializer
class LT_Films_CrewSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)

    class Meta:
        model = LT_Films_Crew
        fields = ['id', 'film', 'person', 'credit_id', 'department', 'job']

# LT_Films_Genres Serializer
class LT_Films_GenresSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = LT_Films_Genres
        fields = ['id', 'film', 'genre']

# LT_Films_Keywords Serializer
class LT_Films_KeywordsSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = LT_Films_Keywords
        fields = ['id', 'film', 'keyword']

# LT_Films_Languages Serializer
class LT_Films_LanguagesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)

    class Meta:
        model = LT_Films_Languages
        fields = ['id', 'film', 'language']

# Bulk create films function
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def bulk_create_films(request):
    if isinstance(request.data, list):  # Check if the data is a list
        serializer = FilmSerializer(data=request.data, many=True)
        if serializer.is_valid():
            films = serializer.save()
            return Response(FilmSerializer(films, many=True).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Expected a list of films."}, status=status.HTTP_400_BAD_REQUEST)
