from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Film, FriendRequest, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Ratings, LT_Viewer_Seen, LT_Viewer_Watchlist, Person, Viewer


class FilmSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Film
        fields = ["id", "adult", "backdrop_path", "belongs_to_collection", "budget", "homepage", "imdb_id", "original_title", "overview", "popularity", "poster_path", "release_date", "revenue", "runtime", "status", "tagline", "title", "tmdb_id", "vote_average", "vote_count"]
        extra_kwargs = {"id": {"required": False}}

class LT_Films_CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = LT_Films_Cast
        fields = ["id", "film", "person", "cast_id", "character", "credit_id", "order"]

class LT_Films_CompaniesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = LT_Films_Companies
        fields = ["id", "film", "company"]

class LT_Films_CountriesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = LT_Films_Countries
        fields = ["id", "film", "country"]

class LT_Films_CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LT_Films_Crew
        fields = ["id", "film", "person", "credit_id", "department", "job"]

class LT_Films_GenresSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = LT_Films_Genres
        fields = ["id", "film", "genre"]

class LT_Films_KeywordsSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = LT_Films_Keywords
        fields = ["id", "film", "keyword"]

class LT_Films_LanguagesSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    class Meta:
        model = LT_Films_Languages
        fields = ["id", "film", "language"]

class LT_Viewer_RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LT_Viewer_Ratings
        fields = ["viewer", "film_a", "film_b", "date", "a_points", "b_points"]

class LT_Viewer_SeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = LT_Viewer_Seen
        fields = ["id", "film", "seen_film", "viewer", "viewer_rating"]
        extra_kwargs = {"id": {"required": False}}

class LT_Viewer_WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = LT_Viewer_Watchlist
        fields = ["id", "film", "watchlist", "viewer"]
        extra_kwargs = {"id": {"required": False}}

# class NotificationsSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#     class Meta:
#         model = Notification
#         fields = ["id", "user", "feed_entry", "notification_type", "is_read", "timestamp"]

class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Person
        fields = ["id", "gender", "tmdb_id", "known_for_department", "name", "popularity", "profile_path"]
        extra_kwargs = {"id": {"required": False}}

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ["id", "name", "email", "profile_picture"]

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = ViewerSerializer(read_only=True)
    receiver = ViewerSerializer(read_only=True)
    class Meta:
        model = FriendRequest
        fields = ["id", "sender", "receiver", "status", "created_at"]

@api_view(["POST"])
def bulk_create_films(request):
    if isinstance(request.data, list):
        serializer = FilmSerializer(data=request.data, many=True)
        if serializer.is_valid():
            films = serializer.save()
            return Response(FilmSerializer(films, many=True).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Expected a list of films."}, status=status.HTTP_400_BAD_REQUEST)
