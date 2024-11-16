
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from datetime import date
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.viewsets import ModelViewSet

from ..models import (
    Film,
    Viewer,
    LT_Films_Cast,
    LT_Films_Companies,
    LT_Films_Countries,
    LT_Films_Crew,
    LT_Films_Genres,
    LT_Films_Keywords,
    LT_Films_Languages,
    LT_Viewer_Seen,
    LT_Viewer_Watchlist,
    FriendRequest,
    Person,
    LT_Viewer_Ratings,
    Notification,
)
from ..serializers import (
    NotificationsSerializer,
    FilmSerializer,
    LT_Viewer_RatingsSerializer,
    ViewerSerializer,
    LT_Viewer_SeenSerializer,
    LT_Viewer_WatchlistSerializer,
    FriendRequestSerializer,
    LT_Films_CastSerializer,
    LT_Films_CompaniesSerializer,
    LT_Films_CountriesSerializer,
    LT_Films_CrewSerializer,
    LT_Films_GenresSerializer,
    LT_Films_KeywordsSerializer,
    LT_Films_LanguagesSerializer,
    PersonSerializer,
)


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

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_orig(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_1(self, request, *args, **kwargs):
        viewer = None
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_2(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("XXselected_movieXX")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_3(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = None
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_4(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("XXmovie1_idXX")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_5(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = None
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_6(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("XXmovie2_idXX")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_7(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = None

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_8(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie != movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_9(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 2, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_10(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 1
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_11(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = None
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_12(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie != movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_13(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 1, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_14(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 2
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_15(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = None
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_16(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 1.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_17(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 1.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_18(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = None

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_19(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "XXviewerXX": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_20(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "XXfilm_aXX": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_21(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "XXfilm_bXX": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_22(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "XXa_pointsXX": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_23(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "XXb_pointsXX": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_24(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "XXdateXX": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_25(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = None
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_26(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=None)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_27(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = None
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_28(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=False)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_29(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_30(self, request, *args, **kwargs):
        viewer = request.user.viewer
        selected_movie = request.data.get("selected_movie")
        movie1_id = request.data.get("movie1_id")
        movie2_id = request.data.get("movie2_id")

        # Set points based on selection
        if selected_movie == movie1_id:
            a_points, b_points = 1, 0
        elif selected_movie == movie2_id:
            a_points, b_points = 0, 1
        else:
            a_points, b_points = 0.5, 0.5

        # Save the rating comparison
        rating_data = {
            "viewer": viewer.id,
            "film_a": movie1_id,
            "film_b": movie2_id,
            "a_points": a_points,
            "b_points": b_points,
            "date": date.today(),
        }
        serializer = self.get_serializer(data=rating_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,)

    xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_mutants = {
    'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_1': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_1, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_2': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_2, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_3': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_3, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_4': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_4, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_5': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_5, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_6': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_6, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_7': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_7, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_8': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_8, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_9': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_9, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_10': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_10, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_11': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_11, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_12': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_12, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_13': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_13, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_14': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_14, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_15': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_15, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_16': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_16, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_17': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_17, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_18': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_18, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_19': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_19, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_20': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_20, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_21': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_21, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_22': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_22, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_23': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_23, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_24': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_24, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_25': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_25, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_26': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_26, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_27': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_27, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_28': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_28, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_29': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_29, 
        'xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_30': xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_30
    }

    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_mutants"), *args, **kwargs)
        return result 

    create.__signature__ = _mutmut_signature(xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_orig)
    xǁLT_Viewer_RatingsViewSetǁcreate__mutmut_orig.__name__ = 'xǁLT_Viewer_RatingsViewSetǁcreate'




# Watchlist view for the current user
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_watchlist(request):
    viewer = request.user.viewer
    watchlist = LT_Viewer_Watchlist.objects.filter(
        viewer=viewer, watchlist=True
    )
    serializer = LT_Viewer_WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)


# Seen films view for the current user
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_seen_films(request):
    viewer = request.user.viewer
    seen_films = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True)
    serializer = LT_Viewer_SeenSerializer(seen_films, many=True)
    return Response(serializer.data)


# Notifications ViewSet
class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAuthenticated]

    def xǁNotificationsViewSetǁget_queryset__mutmut_orig(self):
        return self.queryset.filter(user=self.request.user)

    xǁNotificationsViewSetǁget_queryset__mutmut_mutants = {

    }

    def get_queryset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNotificationsViewSetǁget_queryset__mutmut_orig"), object.__getattribute__(self, "xǁNotificationsViewSetǁget_queryset__mutmut_mutants"), *args, **kwargs)
        return result 

    get_queryset.__signature__ = _mutmut_signature(xǁNotificationsViewSetǁget_queryset__mutmut_orig)
    xǁNotificationsViewSetǁget_queryset__mutmut_orig.__name__ = 'xǁNotificationsViewSetǁget_queryset'



    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None):
        try:
            notification = self.get_object()
            notification.is_read = True
            notification.save()
            return Response(
                {"status": "notification marked as read"},
                status=status.HTTP_200_OK,
            )
        except Notification.DoesNotExist:
            return Response(
                {"error": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
