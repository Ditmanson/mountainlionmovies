from django.test import TestCase, Client
from django.contrib.auth.models import User
from filmproject.models import (
    Film,
    Genre,
    Keyword,
    Country,
    Company,
    Language,
    Person,
    Collection,
    Viewer,
    FriendRequest,
)


class SimpleTest(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)


class URLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username="admin", password="adminpass"
        )
        self.regularuser = User.objects.create_user(
            username="user", password="userpass"
        )

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_admin_authenticated(self):
        self.client.login(username="admin", password="adminpass")
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_admin_not_authenticated(self):
        self.client.login(username="user", password="userpass")
        response = self.client.get("/admin/")
        self.assertNotEqual(response.status_code, 200)

    def test_search_movies(self):
        response = self.client.get("/search_movies/")
        self.assertEqual(response.status_code, 200)


class FilmModelTest(TestCase):
    def test_film_creation(self):
        film = Film.objects.create(
            adult=False,
            backdrop_path="https://example.com/backdrop.jpg",
            belongs_to_collection=False,
            budget=1000000,
            homepage="https://example.com",
            imdb_id="tt1234567",
            original_title="Test Movie",
            overview="This is a test movie.",
            popularity=8.5,
            poster_path="https://example.com/poster.jpg",
            release_date="2022-01-01",
            revenue=5000000,
            runtime=120,
            status="Released",
            tagline="Just a test.",
            title="Test Movie",
            tmdb_id=12345,
            vote_average=7.8,
            vote_count=100,
        )
        self.assertEqual(film.title, "Test Movie")
        self.assertEqual(film.runtime, 120)
        self.assertEqual(str(film), "Test Movie")


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(tmdb_id=1, genre="Action")

    def test_genre_creation(self):
        self.assertEqual(self.genre.genre, "Action")
        self.assertEqual(self.genre.tmdb_id, 1)
        self.assertEqual(str(self.genre), "Action")


class KeywordModelTest(TestCase):
    def setUp(self):
        self.keyword = Keyword.objects.create(tmdb_id=1, keyword="Adventure")

    def test_keyword_creation(self):
        self.assertEqual(self.keyword.keyword, "Adventure")
        self.assertEqual(self.keyword.tmdb_id, 1)
        self.assertEqual(str(self.keyword), "Adventure")


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            code="US", country="United States"
        )

    def test_country_creation(self):
        self.assertEqual(self.country.country, "United States")
        self.assertEqual(self.country.code, "US")
        self.assertEqual(str(self.country), "United States")


class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(tmdb_id=1, company="Test Studio")

    def test_company_creation(self):
        self.assertEqual(self.company.company, "Test Studio")
        self.assertEqual(self.company.tmdb_id, 1)
        self.assertEqual(str(self.company), "Test Studio")


class LanguageModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(code="en", language="English")

    def test_language_creation(self):
        self.assertEqual(self.language.language, "English")
        self.assertEqual(self.language.code, "en")
        self.assertEqual(str(self.language), "English")


class PersonModelTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            adult=False,
            gender=1,
            tmdb_id=1234,
            known_for_department="Acting",
            name="John Doe",
            popularity=7.5,
            profile_path="https://example.com/profile.jpg",
        )

    def test_person_creation(self):
        self.assertEqual(self.person.name, "John Doe")
        self.assertEqual(self.person.known_for_department, "Acting")
        self.assertEqual(str(self.person), "John Doe")


class CollectionModelTest(TestCase):
    def setUp(self):
        self.collection = Collection.objects.create(
            tmdb_id=1,
            name="Test Collection",
            poster_path="https://example.com/collection_poster.jpg",
            backdrop_path="https://example.com/collection_backdrop.jpg",
        )

    def test_collection_creation(self):
        self.assertEqual(self.collection.name, "Test Collection")
        self.assertEqual(self.collection.tmdb_id, 1)
        self.assertEqual(str(self.collection), "Test Collection")


class ViewerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
        )
        self.viewer = Viewer.objects.create(
            user=self.user, name="Test Viewer", email="testuser@example.com"
        )

    def test_viewer_creation(self):
        self.assertEqual(self.viewer.name, "Test Viewer")
        self.assertEqual(self.viewer.email, "testuser@example.com")
        self.assertEqual(str(self.viewer), "Test Viewer")


class FriendRequestTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", password="password"
        )
        self.viewer1 = Viewer.objects.create(user=self.user1, name="Viewer 1")
        self.user2 = User.objects.create_user(
            username="user2", password="password"
        )
        self.viewer2 = Viewer.objects.create(user=self.user2, name="Viewer 2")

    def test_send_friend_request(self):
        friend_request = FriendRequest.objects.create(
            sender=self.viewer1, receiver=self.viewer2
        )
        self.assertEqual(friend_request.status, "pending")

    def test_accept_friend_request(self):
        friend_request = FriendRequest.objects.create(
            sender=self.viewer1, receiver=self.viewer2
        )
        friend_request.status = "accepted"
        friend_request.save()
        self.assertEqual(friend_request.status, "accepted")
