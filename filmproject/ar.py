from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import (
    Film,
    Viewer,
)

# 1st test to make sure our testing environment is working


class SimpleTest(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)


# Next, let's check our URLs


class URLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username="yomama", password="385"
        )
        self.superuser.save()
        self.regularuser = User.objects.create_user(
            username="yodaddy", password="123"
        )
        self.regularuser.save()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_admin_authenticated(self):
        self.client.login(username="yomama", password="385")
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_admin_not_authenticated(self):
        self.client.login(username="yodaddy", password="123")
        response = self.client.get("/admin/")
        self.assertNotEqual(response.status_code, 200)

    # def test_popular_movies(self):
    #     response = self.client.get(reverse('popular_movies'))
    #     self.assertEqual(response.status_code, 200)

    def test_search_movies(self):
        response = self.client.get(reverse("search_movies"))
        self.assertEqual(response.status_code, 200)


# Model tests


class FilmModelTest(TestCase):
    def test_film_creation(self):
        film = Film.objects.create(
            adult=False,
            backdrop_path="https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            belongs_to_collection=False,
            budget=69420,
            homepage="https://www.google.com",
            imdb_id="1",
            original_title="Joker",
            overview=(
                "During the 1980s, a failed stand-up comedian is driven insane "
                "and turns to a life of crime and chaos in Gotham City while "
                "becoming an infamous psychopathic crime figure."
            ),
            popularity=9.99,
            poster_path="https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            release_date="2019-10-01",
            revenue=500000,
            runtime=120,
            status="Released",
            tagline="A test tagline",
            title="Joker",
            tmdb_id=475557,
            vote_average=8.152,
            vote_count=25372,
        )
        # Assertions for each field
        self.assertEqual(film.adult, False)
        self.assertEqual(
            film.backdrop_path,
            "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
        )
        self.assertEqual(film.belongs_to_collection, False)
        self.assertEqual(film.budget, 69420)
        self.assertEqual(film.homepage, "https://www.google.com")
        self.assertEqual(film.imdb_id, "1")
        self.assertEqual(film.original_title, "Joker")
        self.assertEqual(
            film.overview,
            "During the 1980s, a failed stand-up comedian is driven insane and "
            "turns to a life of crime and chaos in Gotham City while becoming an "
            "infamous psychopathic crime figure.",
        )
        self.assertEqual(film.popularity, 9.99)
        self.assertEqual(
            film.poster_path,
            "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
        )
        self.assertEqual(film.release_date, "2019-10-01")
        self.assertEqual(film.revenue, 500000)
        self.assertEqual(film.runtime, 120)
        self.assertEqual(film.status, "Released")
        self.assertEqual(film.tagline, "A test tagline")
        self.assertEqual(film.title, "Joker")
        self.assertEqual(film.tmdb_id, 475557)
        self.assertEqual(film.vote_average, 8.152)
        self.assertEqual(film.vote_count, 25372)
        self.assertEqual(str(film), "Joker")


# Add other model tests (GenreModelTest, KeywordModelTest, etc.) following
# the same pattern


class ViewerModelTest(TestCase):
    def setUp(self):
        self.viewer = Viewer.objects.create(
            name="travis ditmanson", email="tditmans@uccs.edu"
        )

    def test_viewer_creation(self):
        self.assertEqual(self.viewer.name, "travis ditmanson")
        self.assertEqual(self.viewer.email, "tditmans@uccs.edu")
        self.assertEqual(str(self.viewer), "travis ditmanson")
